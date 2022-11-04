from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from main.decorators import user_is_superuser


@login_required
@user_is_superuser
def admin_home(request):
    return render(request,'admins/adminhome.html')