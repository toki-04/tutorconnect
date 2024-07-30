from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("tutor-registration/",  views.tutor_registration, name="tutor-registration"),
    path("learner-sign-up/", views.learner_sign_up_page, name="learner-sign-up"),
    path("learner-create-account/", views.learner_create_account, name="learner-create-account"),
    path("login/", views.login_page, name="login"),
    path("terms-condition/", views.terms_condition, name="terms-condition"),
]
