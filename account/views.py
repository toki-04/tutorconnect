from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout

from .models import LearnerProfile
from .forms import LearnerSignupForm, SignupForm

# Create your views here.
def tutor_registration(request):
    return render(request, "account/tutor-registration.html")

def learner_sign_up(request):
    if request.method == "POST":
        signup_form = SignupForm(request.POST)

        if signup_form.is_valid:
            signup_form.save()

            username = signup_form.cleaned_data["username"]
            password = signup_form.cleaned_data["password1"]


            user = authenticate(request, username=username, password=password)

            if user:
                learner_sign_up_form = LearnerSignupForm(request.POST)
                if learner_sign_up_form.is_valid():

                    first_name = learner_sign_up_form.cleaned_data["first_name"]
                    last_name = learner_sign_up_form.cleaned_data["last_name"]
                    middle_initial = learner_sign_up_form.cleaned_data["middle_initial"]
                    date_of_birth = learner_sign_up_form.cleaned_data["date_of_birth"]
                    account_type = learner_sign_up_form.cleaned_data["account_type"]

                    learner_profile = LearnerProfile(
                        user = user,
                        first_name = first_name,
                        last_name = last_name,
                        middle_initial = middle_initial,
                        date_of_birth = date_of_birth,
                        account_type = account_type,
                    )

                    learner_profile.save()

                    login(request, user)
                    return redirect("learner:learner-homepage")


    else:
        learner_sign_up_form = LearnerSignupForm()
        signup_form = SignupForm()


    context = {
        "learner_sign_up_form": learner_sign_up_form,
        "signup_form": signup_form,
    }


    return render(request, "account/learner-sign-up.html", context)



def login_page(request):
    return render(request, "account/login-page.html")

def terms_condition(request):
    return render(request, "account/terms-condition.html")
