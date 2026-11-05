from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("readme/", views.doc, {"name": "README"}, name="readme"),
    path("log/", views.doc, {"name": "RESULTS"}, name="log"),
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
