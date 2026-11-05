from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", views.goals, name="goals"),
    path("method/", views.method, name="method"),
    path("scores/", views.scores, name="scores"),
    path("conclusions/", views.conclusions, name="conclusions"),
    path("findings/", RedirectView.as_view(url="/conclusions/", permanent=True)),
    path("summary/", RedirectView.as_view(url="/conclusions/", permanent=True)),
    path("results/", RedirectView.as_view(url="/scores/", permanent=True)),
    path("runs/", views.runs, name="runs"),
    path("domains/<str:domain>/", views.domain, name="domain"),
    path("domains/<str:domain>/questions/", views.questions, name="questions"),
    path("domains/<str:domain>/data/", views.data, name="data"),
    path("domains/<str:domain>/ontology/", views.ontology, name="ontology"),
    path("domains/<str:domain>/results/", views.scores_of),
    path("runs/<str:domain>/<str:run>/", views.run, name="run"),
    path("runs/<str:domain>/<str:run>/<str:qid>/", views.question, name="question"),
    path("runs/<str:domain>/<str:run>/transcript/<str:condition>/<int:repeat>/", views.transcript, name="transcript"),
]
