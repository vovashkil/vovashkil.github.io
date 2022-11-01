###### back to repo's main [README.md](../../README.md)
#### django related notes are here.
##### prerequisites
```
pip3 install Django
```
##### start a project PROJECT_NAME
```
django-admin startproject PROJECT_NAME
cd PROJECT_NAME
python manage.py runserver
```
##### create an app APP_NAME
```
python manage.py startapp APP_NAME
```
###### PROJECT_NAME/settings.py: add 'APP_NAME' to list INSTALLED_APPS 
```
# Application definition

INSTALLED_APPS = [
    'APP_NAME',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
##### APP_NAME/views.py
```
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "APP_NAME/index.html")

def somebody(request):
    return HttpResponse("Hello, Somebody!")

def greet(request, name):
    return render(request, "APP_NAME/greet.html", {
        "name": name.capitalize()
    })
```
##### APP_NAME/urls.py
```
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("somebody", views.somebody, name="somebody")
]
```
##### PROJECT_NAME/urls.py
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('APP_NAME/', include("APP_NAME.urls")),
]
```
```
python manage.py migrate
```
