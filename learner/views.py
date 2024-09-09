from django.shortcuts import render, redirect

from account.models import LearnerProfile

# Create your views here.
def learner_homepage(request):
    if request.user.is_authenticated:
        profile = LearnerProfile.objects.get(user=request.user.id)

        context = {
            "profile": profile,
        }

        return render(request, "learner/learner-homepage.html", profile)

    return redirect("home:index")

def learner_settings(request):
    return render(request, "learner/learner-account-settings.html")

def learner_session_history(request):
    return render(request, "learner/learner-session-history.html")

def learner_tutor_profile(request):
    return render(request, "learner/learner-tutor-profile.html")
