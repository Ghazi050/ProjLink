from urllib.parse import urlencode

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse


def home(request):
	
	if request.method == "GET":
		return render(request, "home.html")

	
	selected_role = request.POST.get("role")
	if selected_role not in {"developer", "owner"}:
		return redirect("home")

	request.session["selected_role"] = selected_role

	callback_url = request.build_absolute_uri(reverse("social_auth_callback"))
	login_url = f"{reverse('account_login')}?{urlencode({'next': callback_url})}"
	return redirect(login_url)


def social_auth_callback(request):
	
	if not request.user.is_authenticated:
		callback_url = request.build_absolute_uri(reverse("social_auth_callback"))
		login_url = f"{reverse('account_login')}?{urlencode({'next': callback_url})}"
		return redirect(login_url)

	role_param = request.GET.get("role")
	if role_param in {"developer", "owner"}:
		request.session["selected_role"] = role_param

	selected_role = request.session.get("selected_role")
	if selected_role == "developer":
		return redirect("developer_profile")
	if selected_role == "owner":
		return redirect("owner_profile")

	
	return redirect("home")


@login_required
def developer_profile_view(request):
	return render(request, "developer_profile.html")


@login_required
def owner_profile_view(request):
	return render(request, "owner_profile.html")


def logout_view(request):
	logout(request)
	return redirect("home")


