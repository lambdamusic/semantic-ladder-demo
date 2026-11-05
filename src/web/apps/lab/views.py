from django.conf import settings
from django.http import Http404
from django.shortcuts import render

from . import files


def nav(request):
    """The sidebar on every page: the documents, each domain, and the runs."""
    return {"APP_NAME": settings.APP_NAME, "NAV": files.nav(), "path": request.path}


def home(request):
    return render(request, "lab/home.html", {"title": "The semantics ladder: how much does an LLM gain from being told what data means?",
                                             "body": files.page("intro"),
                                             "domains": [dict(d, runs=files.headline(d["name"])) for d in files.nav()]})


def doc(request, name):
    titles = {"README": "The repository", "RESULTS": "Results log"}
    return render(request, "lab/doc.html", {"title": titles[name], "body": files.doc(name), "name": name})


def runs(request):
    rows = [files.summary(d, f) for d, f in files.run_folders()]
    return render(request, "lab/runs.html", {"title": "All runs", "runs": rows})


def _domain(name):
    info = files.domain_info(name)
    if not info:
        raise Http404(name)
    return info


def _title(domain, section):
    return f"{files.title(domain)}: {section}" if section else files.title(domain)


def domain(request, domain):
    info = _domain(domain)
    return render(request, "lab/domain.html", {"title": _title(domain, ""), "d": info, "body": files.page(f"{domain}/intro"),
                                               "headline": files.headline(domain)})


def questions(request, domain):
    info = _domain(domain)
    cards = [dict(q, trap=files.trap(q)[0], why=files.trap(q)[1]) for q in info["questions"]]
    return render(request, "lab/questions.html", {"title": _title(domain, "questions and traps"), "d": info, "cards": cards,
                                                  "body": files.page(f"{domain}/questions")})


def data(request, domain):
    return render(request, "lab/data.html", {"title": _title(domain, "the data"), "d": _domain(domain),
                                             "body": files.page(f"{domain}/data")})


def results(request, domain):
    info = _domain(domain)
    rows = [files.summary(d, f) for d, f in files.run_folders(domain)]
    latest = next((r for r in rows if r["finished"] and r["mode"] == "read"), None)
    return render(request, "lab/results.html", {
        "title": _title(domain, "results"), "d": info, "body": files.page(f"{domain}/results"),
        "reading": [r for r in rows if r["mode"] == "read"], "querying": [r for r in rows if r["mode"] == "query"],
        "latest": latest and files.run_detail(domain, latest["id"])})


def ontology(request, domain):
    info = _domain(domain)
    folder = info["folder"]
    return render(request, "lab/ontology.html", {
        "title": _title(domain, "the ontology"), "d": info, "body": files.page(f"{domain}/ontology"),
        "md": files.md(files.text(folder / "ontology.md")), "ttl": files.text(folder / "ontology.ttl"),
        "axioms": files.text(folder / "axioms.ttl"), "padding": files.md(files.text(folder / "padding.md")),
        "diagram": files.diagram(domain)})


def run(request, domain, run):
    r = files.run_detail(domain, run)
    if not r:
        raise Http404(run)
    prompts = [{"condition": c, "text": files.prompt(domain, run, c)} for c in r["meta"]["conditions"]]
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
    return render(request, "lab/transcript.html", {"title": f"{condition}, run {repeat}: the query session", "t": t,
                                                   "domain": domain, "run": run, "condition": condition, "repeat": repeat})
