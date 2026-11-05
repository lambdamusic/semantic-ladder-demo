from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("findings/", views.findings, name="findings"),
    path("results/", views.all_results, name="results"),
    path("summary/", RedirectView.as_view(url="/findings/", permanent=True)),
    path("runs/", views.runs, name="runs"),
    path("domains/<str:domain>/", views.domain, name="domain"),
    path("domains/<str:domain>/questions/", views.questions, name="questions"),
    path("domains/<str:domain>/data/", views.data, name="data"),
    path("domains/<str:domain>/ontology/", views.ontology, name="ontology"),
    path("domains/<str:domain>/results/", views.results, name="results"),
    path("runs/<str:domain>/<str:run>/", views.run, name="run"),
    path("runs/<str:domain>/<str:run>/<str:qid>/", views.question, name="question"),
    path("runs/<str:domain>/<str:run>/transcript/<str:condition>/<int:repeat>/", views.transcript, name="transcript"),
]
