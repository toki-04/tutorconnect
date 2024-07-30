from django.shortcuts import render

# Create your views here.
def admin_dashboard(request):
    return render(request, "admin/admin-dashboard.html")

def admin_account_approval(request):
    return render(request, "admin/admin-account-approval.html")

def admin_learners_report(request):
    return render(request, "admin/admin-learners-report.html")

def admin_tutor_report(request):
    return render(request, "admin/admin-tutor-report.html")

def admin_user_review(request):
    return render(request, "admin/admin-user-review.html")
