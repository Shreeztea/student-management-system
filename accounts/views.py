from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = UserCreationForm()

    return render(request, "accounts/register.html", {"form": form})

@login_required
def profile(request):
    print(request.user)
    print(request.user.is_authenticated)
    print(request.session.session_key)
    print(request.user.has_perm("students.add_student"))
    request.session["favorite_course"] = "Python"
    return render(request, "accounts/profile.html")