from django.urls import path
from . import views

app_name = "learner"

urlpatterns = [
    path("", views.learner_homepage, name="learner-homepage"),
    path("settings/", views.learner_settings, name="learner-account-settings"),
    path("session-history/", views.learner_session_history, name="learner-session-history"),
    path("tutor-profile/", views.learner_tutor_profile, name="learner-tutor-profile"),
]
