#!/bin/bash

#Task 1.1 - tasks are completed during lab start

#Task 1.3
#create and activate the python virtual environment
mkdir ~/environment/django
cd ~/environment/django
python -m venv .venv 
source .venv/bin/activate

#Task 2.1 - install django 
pip install django

#Task 2.2
#create a django project task 2.2
django-admin startproject bicycle_project .
#allow all hosts
FILE_TO_UPDATE="/home/ubuntu/environment/django/bicycle_project/settings.py"
line_num=$(cat $FILE_TO_UPDATE |grep -n ALLOWED_HOSTS | cut -d ':' -f1)
sed -i "${line_num}s/\[\]/\['*'\]/" $FILE_TO_UPDATE
sed -i "s|'django.middleware.clickjacking.XFrameOptionsMiddleware',|#'django.middleware.clickjacking.XFrameOptionsMiddleware',|g" $FILE_TO_UPDATE

#migrate 
cd /home/ubuntu/environment/django
python manage.py migrate
#instructions in install lab have student start the web server here, but this script does not

#create a django app Task 3.1
cd /home/ubuntu/environment/django
source .venv/bin/activate
python manage.py startapp bicycle_app
#add bicycle_app to INSTALLED_APPS list
FILE_TO_UPDATE="/home/ubuntu/environment/django/bicycle_project/settings.py"
line_num=$(cat $FILE_TO_UPDATE |grep -n django.contrib.staticfiles | cut -d ':' -f1)
line_num=$((line_num+1))
awk -i inplace -v n=$line_num -v s="    'bicycle_app'," 'NR == n {print s} {print}' $FILE_TO_UPDATE

#Task 3.2
#add lines to views.py
FILE_TO_UPDATE="/home/ubuntu/environment/django/bicycle_app/views.py"
line_num=$(cat $FILE_TO_UPDATE |grep -n 'import render' | cut -d ':' -f1)
line_num=$((line_num+1))
awk -i inplace -v n=$line_num -v s="from django.http import HttpResponse" 'NR == n {print s} {print}' $FILE_TO_UPDATE
echo "def index(request):" | sudo tee -a $FILE_TO_UPDATE
echo '    return HttpResponse("Hello world from bicycle_app!")' | sudo tee -a $FILE_TO_UPDATE

#create and populate the APP file bicycle_app/urls.py 
FILE_TO_UPDATE="/home/ubuntu/environment/django/bicycle_app/urls.py"
touch $FILE_TO_UPDATE
echo "from django.urls import path" | sudo tee -a  $FILE_TO_UPDATE
echo "from . import views" | sudo tee -a  $FILE_TO_UPDATE
echo "urlpatterns = [" | sudo tee -a  $FILE_TO_UPDATE
echo "    path(\"\", views.index, name=\"index\")," | sudo tee -a $FILE_TO_UPDATE
echo "]" | sudo tee -a $FILE_TO_UPDATE

#update the PROJECT file bicycle_project/urls.py 
FILE_TO_UPDATE="/home/ubuntu/environment/django/bicycle_project/urls.py"
sed -i 's|from django.urls import path|from django.urls import include, path|' $FILE_TO_UPDATE
line_num=$(cat $FILE_TO_UPDATE |grep -n admin.site.urls | cut -d ':' -f1)
awk -i inplace -v n=$line_num -v s='    path("", include("bicycle_app.urls")),' 'NR == n {print s} {print}' $FILE_TO_UPDATE

#start the Django server - commenting out because lab instructions will have student do this
#./manage.py runserver 0.0.0.0:8080 
