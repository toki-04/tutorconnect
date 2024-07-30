from django.shortcuts import render

# Create your views here.
def learner_homepage(request):
    return render(request, "learner/learner-homepage.html")

def learner_settings(request):
    return render(request, "learner/learner-account-settings.html")

def learner_session_history(request):
    return render(request, "learner/learner-session-history.html")

def learner_tutor_profile(request):
    return render(request, "learner/learner-tutor-profile.html")
