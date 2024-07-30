from django.shortcuts import render

# Create your views here.
def tutor_dashboard(request):
    return render(request, "tutor/tutor-dashboard.html")

def tutor_list_learners(request):
    return render(request, "tutor/tutor-list-learners.html")

def tutor_rating_review(request):
    return render(request, "tutor/tutor-rating-review.html")

def profile_education(request):
    return render(request, "tutor/profile-education.html")

def profile_experience(request):
    return render(request, "tutor/profile-experience.html")

def profile_personal_information(request):
    return render(request, "tutor/profile-personal-information.html")

def profile_specialties(request):
    return render(request, "tutor/profile-specialties.html")
