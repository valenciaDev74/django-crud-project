from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import TaskForm, LoginForm, SignupForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, "home.html")


def signup(request):
    if request.method == "GET":
        form = SignupForm()
        return render(request, "signup.html", {"form": form})
    elif request.method == "POST":
        if request.POST.get("password1") == request.POST.get("password2"):
            # crear
            try:
                user = User.objects.create_user(
                    username=request.POST.get("username"),
                    password=request.POST.get("password1"),
                    email=request.POST.get("email"),
                )

                user.save()
                login(request, user)
                return redirect("tasks")
            except IntegrityError as e:
                return render(
                    request,
                    "signup.html",
                    {"form": UserCreationForm(), "error_message": e},
                )
        return HttpResponse("the passwords are not the same")


@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, "tasks.html", {"tasks": tasks})


@login_required
def task_detail(request, task_id):
    if request.method == "GET":
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, "task_detail.html", {"task": task, "form": form})
    else:
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks")
        else:
            return render(
                request,
                "task_detail.html",
                {"task": task, "form": form, "error": "invalid data"},
            )


@login_required
def signout(request):
    logout(request)
    return redirect("index")


def signin(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("tasks")
        return render(
            request,
            "login.html",
            {"form": form, "error": "Invalid username or password"},
        )


@login_required
def create_task(request):
    if request.method == "GET":
        return render(request, "create_task.html", {"form": TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect("tasks")
        except ValueError:
            return render(
                request,
                "create_task.html",
                {"form": TaskForm, "error": "introduzca los datos validos"},
            )


@login_required
def task_completed(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == "POST":
        task.datecompleted = timezone.now()
        task.save()
        return redirect("tasks")


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect("tasks")


@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(
        user=request.user, datecompleted__isnull=False
    ).order_by("-datecompleted")
    return render(request, "tasks_completed.html", {"tasks": tasks})
