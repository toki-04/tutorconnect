from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def tutor_registration(request):
    return render(request, "account/tutor-registration.html")

def learner_sign_up_page(request):
    return render(request, "account/learner-sign-up.html")

def learner_create_account(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        return JsonResponse({"response": "testing"})


def login_page(request):
    return render(request, "account/login-page.html")

def terms_condition(request):
    return render(request, "account/terms-condition.html")
