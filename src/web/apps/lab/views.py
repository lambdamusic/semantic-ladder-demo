import subprocess
from datetime import date

from django.conf import settings
from django.http import Http404
from django.shortcuts import redirect, render

from . import files


def updated():
    """The date of the latest commit, for the sidebar's "Last updated"."""
    out = subprocess.run(["git", "log", "-1", "--format=%cs"], cwd=settings.REPO_ROOT, capture_output=True, text=True)
    d = date.fromisoformat(out.stdout.strip()) if out.returncode == 0 and out.stdout.strip() else date.today()
    return f"{d.day} {d:%B %Y}"


def nav(request):
    """The sidebar on every page: the documents, each domain, and the runs."""
    return {"APP_NAME": settings.APP_NAME, "NAV": files.nav(), "path": request.path, "UPDATED": updated()}


def scores_of(request, domain):
    """A domain's or dataset's old results page: its part of the scores."""
    if not files.group(domain):
        raise Http404(domain)
    return redirect(f"/scores/#{domain}", permanent=True)


def goals(request):
    return render(request, "lab/doc.html", {"title": "The semantics ladder: how much does an LLM gain from being told what data means?",
                                            "body": files.page("goals")})


def method(request):
    return render(request, "lab/doc.html", {"title": "Method", "body": files.page("method")})


def conclusions(request):
    return render(request, "lab/doc.html", {"title": "Conclusions", "body": files.page("conclusions"), "heat": True})


def scores(request):
    """Every domain and dataset: its latest runs side by side, what they show, and every run on it."""
    groups = []
    for g in files.nav():
        parts = []
        for d in g["datasets"]:
            rows = [files.summary(n, f) for n, f in files.run_folders(d["name"])]
            latest = next((r for r in rows if r["finished"] and r["mode"] == "read"), None)
            parts.append(dict(d, table=files.score_table(files.headline(d["name"]), d["name"]), body=files.page(f"{d['name']}/scores"),
                              reading=[r for r in rows if r["mode"] == "read"], querying=[r for r in rows if r["mode"] == "query"],
                              latest=latest and files.run_detail(d["name"], latest["id"])))
        groups.append(dict(g, parts=parts))
    return render(request, "lab/scores.html", {"title": "Scores", "body": files.page("scores"), "groups": groups})


def runs(request):
    rows = [files.summary(d, f) for d, f in files.run_folders()]
    return render(request, "lab/runs.html", {"title": "Run archive", "runs": rows})


def _parts(domain, section):
    """A domain's datasets for one section: each dataset's files and questions, and its own text for the
    section. A dataset's old address goes to its part of the domain's page."""
    g = files.group(domain)
    if not g:
        raise Http404(domain)
    if domain != g["name"]:  # on the introduction, the dataset's heading; elsewhere, its part of the page
        label = next(d["label"] for d in g["datasets"] if d["name"] == domain)
        anchor = domain if section else label.lower().replace(" ", "-")
        raise Moved(f"/domains/{g['name']}/" + (f"{section}/" if section else "") + f"#{anchor}")
    return g, [dict(files.domain_info(d["name"]), label=d["label"], body=files.page(f"{d['name']}/{section or 'intro'}"))
               for d in g["datasets"]]


class Moved(Exception):
    pass


def moved(view):
    """Send a dataset's old page address on to the domain's page."""
    def wrapped(request, *args, **kwargs):
        try:
            return view(request, *args, **kwargs)
        except Moved as m:
            return redirect(str(m), permanent=True)
    return wrapped


@moved
def domain(request, domain):
    g, parts = _parts(domain, "")
    return render(request, "lab/domain.html", {"title": g["title"], "g": g, "parts": parts,
                                               "body": files.page(f"{domain}/intro")})


@moved
def questions(request, domain):
    g, parts = _parts(domain, "questions")
    card = lambda q: dict(q, trap=files.trap(q)[0], why=files.trap(q)[1])
    seen = {q["id"] for q in parts[0]["questions"]}
    extra = []
    for p in parts[1:]:  # questions only some datasets ask, such as the path questions
        own = [card(q) for q in p["questions"] if q["id"] not in seen]
        seen |= {q["id"] for q in own}
        if own:
            extra.append(dict(p, cards=own))
    return render(request, "lab/questions.html", {"title": f"{g['title']}: questions and traps", "g": g,
                                                  "cards": [card(q) for q in parts[0]["questions"]],
                                                  "extra": extra, "many": len(parts) > 1, "body": parts[0]["body"]})


@moved
def data(request, domain):
    g, parts = _parts(domain, "data")
    return render(request, "lab/data.html", {"title": f"{g['title']}: the data", "g": g, "parts": parts})


@moved
def ontology(request, domain):
    g, parts = _parts(domain, "ontology")
    folder = parts[0]["folder"]  # one ontology for the domain: the first dataset's
    return render(request, "lab/ontology.html", {
        "title": f"{g['title']}: the ontology", "body": parts[0]["body"],
        "md": files.md(files.text(folder / "ontology" / "ontology.md")), "diagram": files.diagram(domain)})


def run(request, domain, run):
    r = files.run_detail(domain, run)
    if not r:
        raise Http404(run)
    prompts = [{"condition": c, "text": files.prompt(domain, run, c)} for c in sorted(r["meta"]["conditions"], key=files.by_label)]
    return render(request, "lab/run.html", {"title": f"Run {run}", "r": r, "prompts": prompts})


def question(request, domain, run, qid):
    q, cards = files.answers_for(domain, run, qid)
    if not q:
        raise Http404(qid)
    return render(request, "lab/question.html", {"title": f"{qid}, run {run}", "q": q, "cards": cards,
                                                 "domain": domain, "run": run})


def transcript(request, domain, run, condition, repeat):
    t = files.transcript(domain, run, condition, repeat)
    if not t:
        raise Http404(condition)
    return render(request, "lab/transcript.html", {"title": f"{files.LABELS.get(condition, '')} {condition}, run {repeat}: the query session".strip(), "t": t,
                                                   "domain": domain, "run": run, "condition": condition, "repeat": repeat})
