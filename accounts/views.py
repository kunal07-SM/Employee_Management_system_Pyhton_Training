from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from .forms import RegisterForm
from django.contrib.auth import update_session_auth_hash
from .forms import UpdateProfileForm, CustomPasswordChangeForm

def register_view(request):
    # If user is already logged in, redirect to dashboard
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "🎉 Registration successful! Please login to continue."
            )

            return redirect("login")

        else:
            messages.error(
                request,
                "Please correct the errors below."
            )

    else:
        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )


@login_required
def logout_view(request):
    logout(request)

    messages.success(
        request,
        "You have been logged out successfully."
    )

    return redirect("login")
@login_required
def profile_view(request):
    return render(request, "accounts/profile.html")


@login_required
def edit_profile(request):

    if request.method == "POST":

        form = UpdateProfileForm(
            request.POST,
            instance=request.user,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Profile updated successfully."
            )

            return redirect("profile")

    else:

        form = UpdateProfileForm(
            instance=request.user
        )

    return render(
        request,
        "accounts/edit_profile.html",
        {"form": form},
    )


@login_required
def change_password(request):

    if request.method == "POST":

        form = CustomPasswordChangeForm(
            request.user,
            request.POST,
        )

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(
                request,
                user,
            )

            messages.success(
                request,
                "Password changed successfully."
            )

            return redirect("profile")

    else:

        form = CustomPasswordChangeForm(request.user)

    return render(
        request,
        "accounts/change_password.html",
        {"form": form},
    )



@login_required
def create_session(request):

    request.session["company_name"] = "ABC Pvt Ltd"
    request.session["employee_role"] = "HR Manager"

    messages.success(request, "✅ Session created successfully.")

    return redirect("home")


@login_required
def delete_session(request):

    request.session.flush()

    messages.success(request, "🗑️ Session deleted successfully.")

    return redirect("login")


@login_required
def create_cookie(request):

    response = redirect("home")

    response.set_cookie(
        "company",
        "ABC Pvt Ltd",
        max_age=60 * 60 * 24,
    )

    messages.success(request, "🍪 Cookie created successfully.")

    return response


@login_required
def delete_cookie(request):

    response = redirect("home")

    response.delete_cookie("company")

    messages.success(request, "🗑️ Cookie deleted successfully.")

    return response
