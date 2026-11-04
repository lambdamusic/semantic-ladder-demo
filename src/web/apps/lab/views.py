from django.conf import settings
from django.http import Http404
from django.shortcuts import render

from . import files


def nav(request):
    """The sidebar on every page: the documents, each domain, and the runs."""
    return {"APP_NAME": settings.APP_NAME, "NAV_DOMAINS": files.domains(), "path": request.path}


def doc(request, name):
    titles = {"README": "The experiment", "PLAN": "The plan", "RESULTS": "Results log"}
    return render(request, "lab/doc.html", {"title": titles[name], "body": files.doc(name), "name": name})


def runs(request):
    rows = [files.summary(d, f) for d, f in files.run_folders()]
    return render(request, "lab/runs.html", {"title": "All runs", "runs": rows})


def _domain(name):
    info = files.domain_info(name)
    if not info:
        raise Http404(name)
    return info


def domain(request, domain):
    info = _domain(domain)
    rows = [files.summary(d, f) for d, f in files.run_folders(domain)]
    return render(request, "lab/domain.html", {"title": f"Domain: {domain}", "d": info, "runs": rows, "tab": "overview"})


def questions(request, domain):
    return render(request, "lab/questions.html", {"title": f"{domain}: questions", "d": _domain(domain), "tab": "questions"})


def data(request, domain):
    return render(request, "lab/data.html", {"title": f"{domain}: data", "d": _domain(domain), "tab": "data"})


def ontology(request, domain):
    info = _domain(domain)
    folder = info["folder"]
    return render(request, "lab/ontology.html", {
        "title": f"{domain}: ontology", "d": info, "tab": "ontology",
        "md": files.md(files.text(folder / "ontology.md")), "ttl": files.text(folder / "ontology.ttl"),
        "axioms": files.text(folder / "axioms.ttl"), "padding": files.md(files.text(folder / "padding.md"))})


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
