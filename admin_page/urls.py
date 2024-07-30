from django.urls import path
from . import views

app_name = "administrator"
urlpatterns = [
    path("dashboard/", views.admin_dashboard, name="admin-dashboard" ),
    path("account-approval/", views.admin_account_approval, name="admin-account-approval" ),
    path("learners-report/", views.admin_learners_report, name="admin-learners-report"),
    path("tutor-report/", views.admin_tutor_report, name="admin-tutor-report"),
    path("user-review/", views.admin_user_review, name="admin-user-review"),
]
