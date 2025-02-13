#!/bin/bash

#Install lab catchup
mkdir ~/environment/django
cd ~/environment/django
python -m venv .venv 
source .venv/bin/activate
pip install django
django-admin startproject bicycle_project .
FILE_TO_UPDATE="/home/ubuntu/environment/django/bicycle_project/settings.py"
line_num=$(cat $FILE_TO_UPDATE |grep -n ALLOWED_HOSTS | cut -d ':' -f1)
sed -i "${line_num}s/\[\]/\['*'\]/" $FILE_TO_UPDATE
sed -i "s|'django.middleware.clickjacking.XFrameOptionsMiddleware',|#'django.middleware.clickjacking.XFrameOptionsMiddleware',|g" $FILE_TO_UPDATE
cd /home/ubuntu/environment/django
python manage.py migrate
cd /home/ubuntu/environment/django
source .venv/bin/activate
python manage.py startapp bicycle_app
#add bicycle_app to INSTALLED_APPS list
FILE_TO_UPDATE="/home/ubuntu/environment/django/bicycle_project/settings.py"
line_num=$(cat $FILE_TO_UPDATE |grep -n django.contrib.staticfiles | cut -d ':' -f1)
line_num=$((line_num+1))
awk -i inplace -v n=$line_num -v s="    'bicycle_app'," 'NR == n {print s} {print}' $FILE_TO_UPDATE
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

#models lab catchup
sudo systemctl start mysql ; sudo systemctl status mysql
sudo apt-get update
sudo NEEDRESTART_MODE=a apt-get install -y python3-dev default-libmysqlclient-dev python3-mysqldb 
pip install pymysql pillow cryptography
echo "import pymysql" >> /home/ubuntu/environment/django/bicycle_project/__init__.py
echo "pymysql.install_as_MySQLdb()" >> /home/ubuntu/environment/django/bicycle_project/__init__.py

#configure mysql django user and data
sqlrootpwd='AciDb2034'
sqldjangopwd='djangoAciDb2034'
sudo mysqladmin -u root password $sqlrootpwd > /dev/null 2>&1
sudo mysql --defaults-extra-file=/etc/mysql/configroot.cnf  -e "USE mysql; UPDATE user SET plugin='mysql_native_password' WHERE User='root'; FLUSH PRIVILEGES;"
sudo systemctl restart mysql 
sudo mysqladmin -u root password $sqlrootpwd > /dev/null 2>&1
echo 'restore bicycles database'
mysql --defaults-extra-file=/etc/mysql/configroot.cnf < /var/tmp/BicyclesDbDump-end-templates.sql
echo 'delete product table contents'
mysql --defaults-extra-file=/etc/mysql/configroot.cnf -e "use bicycles; delete from bicycle_app_product;"
echo 'reset auto_increment on product table'
mysql --defaults-extra-file=/etc/mysql/configroot.cnf -e "use bicycles; ALTER TABLE bicycle_app_product AUTO_INCREMENT = 1;"
echo 'create the django user'
mysql --defaults-extra-file=/etc/mysql/configroot.cnf < /var/tmp/createDjangoUser.sql

cd /var/tmp/
tar -xzf django-end-template-lab-20240201.tar.gz -C /home/ubuntu/environment/
#avoid a warning in the runserver terminal during the lab
touch /home/ubuntu/environment/django/bicycle_app/templates/favicon.ico