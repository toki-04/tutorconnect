from django.urls import path
from . import views

app_name = "tutor"
urlpatterns = [
    path("dashboard/", views.tutor_dashboard, name="tutor-dashboard"),
    path("list-learners/", views.tutor_list_learners, name="tutor-list-learners"),
    path("rating-review/", views.tutor_rating_review, name="tutor-rating-review"),
    path("profile/education/", views.profile_education, name="profile-education"),
    path("profile/experience/", views.profile_experience, name="profile-experience"),
    path("profile/personal-information/", views.profile_personal_information, name="profile-personal-information"),
    path("profile/specialties/", views.profile_specialties, name="profile-specialties"),
]
