# Week 6: Django Administration

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## Django Administration

### Pre-assessment

#### Where can you access the Django admin site?

* Under a defined admin URL path in a Django project

Wrong answers:

* On the public Django website
* In the AWS console under AWS Systems Manager
* On a terminal using the Django command line utility

##### Explanation

The Django admin site is local to a Django project. It is accessible at a defined URL path, **admin/** by default.

The public Django website hosts the Django documentation. AWS Systems Manager is used to manage Amazon EC2 instances. The Django command line utility can be used to create an admin user with a username and password.

#### What can an administrator do on the Django admin site? (Select TWO.)

* Manage admin users
* Edit model data

Wrong answers:

* Maintain the compute instances
* Enable and disable Django applications
* Monitor visitors and page counts

Django applications are added and removed from a project in code only. There is no runtime visibility of the running instances, and there are no metrics about the number of visitors on the website or per page.

#### Which Django models are visible on the Django admin site?

* All the models registered to the admin site in code

Wrong answers:

* All the models in all the Django applications
* All the models with a specific admin site attribute
* All the models with a specific admin site method

To be visible on the Django admin site, the applications' models must be registered in code using **admin.site.register()** from the **django.contrib** package.

## Accessing the Django Admin Site

The Django admin site is used to edit application data that is defined by different applications in a Django project. It might be the list of supported brands on a retail website, the list of stations on a weather forecast website, or the list of breeds in a pets application. This data is typically read-only and is made visible to visitors, and it must be maintained and edited by an administrator, operator, or product owner using the admin site.

Admin users might also use the admin site to search and read data to validate that everything works as expected. For example, they might want to view the list of orders from the past 24 hours.

In summary, the admin site can be used to apply any read or write action on data managed by a Django model.

The admin site has a web interface to manage users, groups, and their permissions. It defines whether a user has access to the admin site, which models are visible, and which create, read, update, and delete (CRUD) operations are allowed.

An administrator, also called an *admin* user, can access the Django admin site from a sub-URL where the Django project website is deployed.

The admin site displays registered *models* and their data stored in a database. The data can be created, read, changed, or deleted using generated webpages. The graphical user interface (GUI) makes edits convenient, based on the model field types.

The admin site displays a list of users. Admin users can be created with specific rights to view and edit application data, and website visitors can also be managed from the admin site.

### Enabling the Django admin site

The Django admin site comes preinstalled and ready to use when you create a new Django project. If you need to add the Django admin site to an existing Django project, configure the following settings.

1. **Application**s** – Because the admin site is a regular Django application, you need to add that app, called **django.contrib.admin**, to the **INSTALLED_APPS** array variable in the project's **settings.py** file. This application has four dependencies that must also be listed, as illustrated in the following diagram. It includes an authorization framework and a messaging framework.
2. **Middleware** – The authorization and messaging frameworks have middleware dependencies that must be listed in the **MIDDLEWARE** array variable in the project's **settings.py** file. A middleware is a framework used to modify HTTP requests and responses.
 * djangp.contrib.auth.middleware.AuthenticationMiddleware
 * django.contrib.messages.middleware.MessageMiddleware
3. **Templates** – The admin application has two template dependencies that must be listed in the **TEMPLATES** array variable in the project's **settings.py** file. These are settings for some of the template engines used in Django.
 * django.template.context_processors.request
 * django.contrib.auth.context_processors.auth
4. **Options** – The messaging framework has one caching dependency that must be listed in the **OPTIONS** array variable in the project's **settings.py** file. This includes extra parameters to pass to the cache backend.
 * django.contrib.messages.context_processors.messages
5. **URL pattern** - A specific URL path, **admin/** by default, must be listed in the **urlpatterns** array variable in the project's **urls.py**. This points to subsequent URLs defined internally by the **django.contrib.admin** application under **admin.site.urls**. This is the entry door to the admin site.
 * path("admin/", admin.site.urls)

### Accessing the Django admin site

The Django admin site is a Django application that is deployed along with your custom Django applications. If your project is not running, use the regular **runserver** command from the Django command line utility to start it.

```
./manage.py runserver 0.0.0.0:8080
```

When the Django project is running, the admin site is available. The admin URL, **https://xxxxxx.amazonaws.com/admin/** by default displays a login form. A username and password are required to access the admin site.

If there is no existing admin user, you need to create one using the **createsuperuser** command from the Django command line utility. A username and password are required, and an email address is optional.

```
./manage.py createsuperuser
```

After you enter newly created credentials on the login page, the Django admin site is displayed. The **AUTHENTICATION AND AUTHORIZATION** box is visible to manage groups and users. There is nothing related to models yet, even if your Django project includes applications with one or more models. Notice that the **Recent actions** list shows **None available**, which means that no model, group, or user has been edited.

## Registering Models

### Register function

To make a model appear in the admin site, you need to programmatically register that model with the admin application, **django.contrib.admin**. The convention is to edit the **admin.py** file in your custom application that holds the model in **models.py**, and then import **admin** from **django.contrib**, as illustrated in the following Python code snippet. The simplest way to register a model is to use the **admin.site.register()** function. You must pass your custom model as the argument.

```
from django.contrib import admin
from .models import Breed, VaccinationCard, Pet, VetVisit

admin.site.register(Breed)
admin.site.register(VaccinationCard)
admin.site.register(Pet)
admin.site.register(VetVisit)
```

If you refresh the admin webpage, a table that corresponds to your custom application, **PETS_APP**, appears with the registered models listed. As shown in the following screen, the admin site uses the plural for each registered model, like **Vet visits** for the **VetVisit** model. When a model is listed, it indicates that an admin user with sufficient rights can view and edit the model's data.

### ModelAdmin class

In most cases, that simple approach is sufficient to register a model. The admin application offers the full user experience, with a web interface to list, create, edit, and delete objects. However, the admin site experience cannot be customized with this simple approach. 

By subclassing **admin.ModelAdmin** for a specific model, you can customize how lists, fields, and buttons are displayed in the admin interface. A more advanced way to register a model is by passing a second argument to the **admin.site.register()** function. That argument is your **ModelAdmin** subclass. In the following example, you are subclassing **ModelAdmin** without making any changes. The **pass** statement is used as a placeholder for future code, but also because empty code is not allowed in class definitions.

```
from django.contrib import admin
from .models import Breed, VaccinationCard, Pet, VetVisit

class BreedAdmin(admin.ModelAdmin):
    pass

admin.site.register(Breed, BreedAdmin)

class VaccinationCardAdmin(admin.ModelAdmin):
    pass

admin.site.register(VaccinationCard, VaccinationCardAdmin)

class PetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pet, PetAdmin)

class VetVisitAdmin(admin.ModelAdmin):
    pass

admin.site.register(VetVisit, VetVisitAdmin)
```

A simple way to achieve the same result is to use a *Python decorator*. A decorator is a function preceded by the '@' character. It extends another function's behavior without explicitly changing its code. The following example shows how the decorator **@admin.register()** can be used instead of a standard function call.

```
from django.contrib import admin
from .models import Breed, VaccinationCard, Pet, VetVisit

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass

@admin.register(VaccinationCard)
class VaccinationCardAdmin(admin.ModelAdmin):
    pass

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass

@admin.register(VetVisit)
class VetVisitAdmin(admin.ModelAdmin):
    pass
```

## Managing Admin Users

Admin users can use the admin site to manage users, groups, and permissions.

### Django authentication system

The Django admin application **django.contrib.admin** has a dependency to a module called **django.contrib.auth**. This module is a user authentication system that is used to manage users, groups, permissions, and sessions.

In any web application, you have to manage user identities, which can include:

* **A visitor** browsing your website. In an ecommerce application, and end user is browsing products and shopping. A visitor identity is typically self-created from a sign-up or registration webpage.
* **An admin** making sure things are working as expected and managing data. For an ecommerce application, an admin can promote products and check orders made by visitors. An admin identity is typically created by another admin.

The Django admin site is accessed by admin users, and it provides an interactive and graphical way to view and manage both types of users (visitors and admins). Even if visitors are created from a custom registration page, their identity can be managed by **django.contrib.auth** and edited here.

Both users and groups of users can be created, edited, and deleted, like any other Django model. The data is stored in the same database configured in your Django project.

### Grouping users

You can also create groups of users. The main advantage is to effectively set permissions at the group level, so it applies to all users in the group.

There is a *many-to-many relationship* between groups and users. A group can have multiple users, and a user can be in different groups at the same time.

### High-level permissions

High-level permissions determine if a user is a visitor or an admin. But there are other possibilities, like a user can be made inactive, or an admin can be promoted to a superuser.

1. **Inactive user**. This user has the Active checkbox unselected. It means the user's **is_active** flag is set to **False**. As a consequence, the user has no authorization. The user cannot access any of the authenticated webpages on the website.
2. **Visitor**. This active user can visit the website's public and authenticated webpages but has no access to the Django admin site. This user has the Staff checkbox unselected. It means the user's **is_staff** flag is set to **False**.
3. **Admin**. This user can log in to the Django admin site because the Staff checkbox is selected. It means the user's **is_staff** flag is set to **True**. Furthermore, what this user can do within the site depends on granular authorizations. These authorizations define which models can be managed.
4. **Superuser**. A superuser is an admin user with all the authorizations. This user has both the Staff and Superuser checkboxes selected. It means both **is_staff** and **is_superuser** flags are set to **True**.

By using the **createsuperuser** command, you get a superuser with all the possible rights. This user can log into the admin site and also create other admin users with specific permissions for specific tasks.

### Low-level permissions

There are some permissions that can be attached to either an admin user or a group of admin users. The permissions can impact what they see in the admin site.

#### Administration log entry permissions

When a user makes requests to the Django admin site, their actions, like adding, changing, or deleting data are logged. These log entries have permissions associated with them that control who can view, add, change, and delete log entries. These permissions are checked by the **LogEntry** model, similar to how object permissions are checked on models.

These permissions are not necessary for an admin to work with users, groups, and custom models.

#### Authentication and authorization permissions

These permissions include viewing, adding, changing, and deleting a group, a user, or a permission. There are four permissions for each of the three entities, which makes a total of 12 permissions. An admin with some of these permissions will be able to see the **Authentication and Authorization** block on the main page.

#### Content types permissions

The content types framework, **django.contrib.contenttypes**, is a dependency of the admin application. It can track all the models installed in your Django project, and it provides a high-level, generic interface for working with your models. The admin application uses it to log the history of each object added or changed through the admin interface. The authentication framework, another dependency, uses it to connect user permissions to specific models.

These permissions are not necessary for an admin to work with users, groups, and custom models.

#### Applications permissions

These permissions are based on the registered models in the admin site. Each model has four permissions: to view, add, change, or delete an object. An admin with some of these permissions will be able to see the related application blocks on the main page, like **PETS_APP**.

#### Sessions permissions

The Django session framework, **django.contrib.sessions**, is another dependency of the admin application. It handles persistent user sessions across page requests, and allows for storing and retrieving arbitrary data for a given user as they navigate a site.

These permissions are not necessary for an admin to work with users, groups, and custom models.

### Applying permissions

As an example, two admin users are created by the superuser, each with different permissions.

### Shirley

Shirley has no permissions related to users and groups. The **AUTHENTICATION AND AUTHORIZATION** section is hidden away on the main page. Shirley can work with pets, vaccination cards, and vet visits, which are visible in the **PETS_APP** section. Note that the Add menu is only attached to vet visits, which she is allowed to create. Also, the breed model is hidden because none of the four related permissions are chosen for this admin user.

#### Paulo

Paulo has all the permissions on users and groups, but no permissions for the models defined in pets_app. This means Paulo can manage groups and users from **AUTHENTICATION AND AUTHORIZATION**, but cannot give them permissions. It also means that Paulo cannot upgrade himself, which is important for security. The **PETS_APP** section is not visible on the main page.

### Events log

A log of user actions is stored in the database and appears on the main page of the admin site under **Recent actions**. You will see items appear on this list when you make changes to the model data.

## Maintaining Model Data

After models are registered and an admin user has the right permissions, data can be manually edited from the Django admin site. This section dives into the web interface for editing model data and explains how elements can be configured and displayed. 

You are going to reuse two previously used models, a Pet and its VaccinationCard. There is a one-to-one relationship between them. By editing models.py and admin.py, you can view the effects on the admin site.

### Listing objects

All registered models with **admin.site.register()** or **@admin.register()** are available in the admin interface. A registered model is visible to admin users with the model's view permission. Admin users can select a model to see a list of objects for the model. 

#### Default listing

If you have not defined any function in your model, and have only defined fields like VaccinationCard, as shown in this example code, then the listed data will be hard to decipher.

```
from django.db import models
from django.contrib import admin
from datetime import date

# model definition in models.py
class VaccinationCard(models.Model):
    rabies = models.DateField(default=datetime.today().strftime('%Y-%m-%d'), null=False, blank=False)
    hepatitis = models.DateField(null=True, blank=True)
    borrelia = models.DateField(null=True, blank=True)
    distemper = models.DateField(null=True, blank=True)

# model registration in admin.py
admin.site.register(VaccinationCard)
```

The Django admin site displays the list of **objects** and indicates their type and ID number. In this case, it is not possible for the admin to guess which vaccination card belongs to a specific pet.

#### Configuring the listing with __str__

To make the list more convenient to  scroll, you can implement the **__str__** function in your model. Your code should return a human-readable string that will be used by the admin application to display an object in the list or in a relationship reference. The following example uses **self.rabies** to show the latest rabies vaccination and **self.pet** to show which pet this card belongs to. It is interesting to note that **pet** is not a field of **VaccinationCard**. The **Pet** model has a **ForeignKey** reference to **VaccinationCard** called **card**. When there is a one-to-one relationship, the Django data API makes it convenient to navigate both ways!

```
from django.db import models
from datetime import datetime

class Pet(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=Gender.choices, default=Gender.FEMALE)
    birth = models.DateField(default=None, null=True, blank=True)
    card = models.OneToOneField(VaccinationCard, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name + " - " + self.gender + " - " + str(self.birth.year)

class VaccinationCard(models.Model):
    rabies = models.DateField(default=datetime.today().strftime('%Y-%m-%d'), null=False, blank=False)
    hepatitis = models.DateField(null=True, blank=True)
    borrelia = models.DateField(null=True, blank=True)
    distemper = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.pet) + " - " + str(self.rabies)
```

* Expected result:

The Django admin site displays a string representation of each object. You can recognize the pet and view the rabies vaccination date directly from the list. The admin can select one vaccination card to access the object form editor, which can be used to view more fields or make changes. Note how the **Pet** **__str__** concatenated with the **VaccinationCard** **rabies** date, as it is coded in **VaccinationCard** **__str__**.

#### Configuring the listing with admin.ModelAdmin

By subclassing **admin.ModelAdmin** and using **@admin.register()**, you can further customize the admin interface.

The **ModelAdmin.list_display** array attribute can be overridden in your subclass. The admin application will stop using the string representation of the objects. It will instead create a graphical table made of the columns that you are specifying in that array. These columns can be a model field like **rabies**, a relationship like **pet**, or even a function.

```
from django.contrib import admin
from .models import Breed, VaccinationCard, Pet, VetVisit

admin.site.register(Breed)
admin.site.register(Pet)
admin.site.register(VetVisit)

@admin.register(VaccinationCard)
class VaccinationCardAdmin(admin.ModelAdmin):
    list_display = ["pet", "rabies", "hepatitis"]
```

* Expected result:

The Django admin site displays a table with three columns defined in **list_display**. The string representation of the card is not used anymore, but the string representation of a pet is used because this is a relationship, not an internal field. Note that you can select the column name to change the column order to ascending or descending.

The **ModelAdmin.list_display** array can also include a function, **rabies_expires** in the following example. The function returns the value that is displayed in the corresponding column. In this code, it says whether the rabies vaccine is about to expire, as **True** or **False**. The decorator **@admin.display()** on that function names the column in the table as **Rabies Expires**.

```
from django.contrib import admin
from .models import Breed, VaccinationCard, Pet, VetVisit
from datetime import date

admin.site.register(Breed)
admin.site.register(Pet)
admin.site.register(VetVisit)

@admin.register(VaccinationCard)
class VaccinationCardAdmin(admin.ModelAdmin):
    list_display = ["pet", "rabies", "rabies_expires", "hepatitis"]
    
    @admin.display(description="Rabies Expires")
    def rabies_expires(self, obj):
        time_since_vaccine = date.today() - obj.rabies
        return (time_since_vaccine.days > 1000)
```

* Expected result:

The Django admin site displays an extra column that does not correspond to a field from the model. It is a calculated column from a function to help the admin quickly identify which rabies vaccinations are about to expire.

The **ModelAdmin.empty_value_display** can be used to replace the default "-" by any text. It applies to any model field or function returning **None** or an **empty value**. For the **VaccinationCard** model with only vaccination dates, you can override **empty_value_display** by a string indicating that the vaccine has not been taken, like **"Never"** instead of "-". Note in the example that you can include some **HTML formatting** instead of a simple string.

```
from django.contrib import admin
from .models import Breed, VaccinationCard, Pet, VetVisit
from datetime import date

admin.site.register(Breed)
admin.site.register(Pet)
admin.site.register(VetVisit)

@admin.register(VaccinationCard)
class VaccinationCardAdmin(admin.ModelAdmin):
    list_display = ["pet", "rabies", "rabies_expires", "hepatitis"]
    empty_value_display = '<span style="color:darkred;">Never ⚠</span>'
    
    @admin.display(description="Rabies Expires")
    def rabies_expires(self, obj):
        time_since_vaccine = date.today() - obj.rabies
        return (time_since_vaccine.days > 1000)
```

* Expected result:

The Django admin site displays **Never ⚠** for any field value in this model with no data. This applies to the **Hepatitis** field because this field can be empty with the **null=True** and **blank=True** attributes.

Note that above the list there is a dropdown menu and a **Go** button. By default, the admin application adds **"Delete selected vaccination cards"** in the menu. This is convenient when the admin user wants to delete more than one object.

More actions can be appended to this menu by overriding **ModelAdmin.actions**. This array lists extra custom actions. An additional action is implemented as a function, like **rabies_applied_today** in the following example. The decorator **@admin.action()** is used to set the text displayed in the menu, **Rabies vaccine applied today**.

```
from django.contrib import admin
from .models import Breed, VaccinationCard, Pet, VetVisit
from datetime import date

admin.site.register(Breed)
admin.site.register(Pet)
admin.site.register(VetVisit)

@admin.action(description="Rabies vaccine applied today")
def rabies_applied_today(modeladmin, request, queryset):
    queryset.update(rabies=date.today())

@admin.register(VaccinationCard)
class VaccinationCardAdmin(admin.ModelAdmin):
    list_display = ["pet", "rabies", "rabies_expires", "hepatitis"]
    empty_value_display = '<span style="color:darkred;">Never ⚠</span>'
    actions = [rabies_applied_today]
    
    @admin.display(description="Rabies Expires")
    def rabies_expires(self, obj):
        time_since_vaccine = date.today() - obj.rabies
        return (time_since_vaccine.days > 1000)
```

* Expected result:

The Django admin site displays an extra menu called **Rabies vaccine applied today**. When you select some rows, choose the action, and choose the **Go** button, the admin site applies the action to the selected rows. In this example, two pets with the same owner are visiting the vet together today for a new vaccination.

For more information, see [Admin Actions](https://docs.djangoproject.com/en/stable/ref/contrib/admin/actions/) on the Django website.

### Editing an object

By selecting one row in the list, another admin page opens. The object data is displayed in an HTML form, ready to be changed if the user has the change permission on this model. The model fields are translated into HTML input elements. Some input attributes are present to match the field attributes. This guarantees a certain level of validation when values are edited.

Here is a recap of the full **Pet** model that is used in the following example.

```
from django.db import models
from django.utils.translation import gettext_lazy as _

class Gender(models.TextChoices):
        FEMALE = "F", _("Female")
        MALE = "M", _("Male")

class Pet(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=Gender.choices, default=Gender.FEMALE)
    birth = models.DateField(default=None, null=True, blank=True)
    owner = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    height = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    card = models.OneToOneField(VaccinationCard, on_delete=models.CASCADE)
    breed = models.ManyToManyField(Breed, blank=True)
    
    def __str__(self):
        return self.name + " - " + self.gender + " - " + str(self.birth.year)
```

After viewing the list of pets and selecting **Milo**, the **Change** pet webpage opens with a prefilled form. Note that the admin can switch to a dark theme.

1. **Change pet**. After viewing the list of pets and selecting one, the **Change pet** webpage opens. The pet string representation from the Pet model **__str__** function, **Milo - M - 2018**, is shown both in the bar at the top and below **Change pet**. Not implementing the **__str__** function would make this interface more confusing.
2. **Text field**. The admin application creates a regular **<input type="text">** input element with the proper attributes, based on your model fields and field attributes. Some constraints might be included, so validations will be made on submit.
3. **Choices**. Model fields with a choices option pointing to a list of acceptable values are automatically formatted. The list of possible values is in the dropdown.
4. **Date picker**. Date fields are formatted with a convenient date picker.
5. **Numeric field**. The admin application creates a regular **<input type="number">** input element with the proper attributes, based on your model fields and field attributes. Some constraints might be included, so validations will be made on submit. Notice that the **Weight** input field has the focus, and that the interface shows an input control with two arrows. You can use these controls to step the value up or down.
6. **One-to-one dropdown**. The **Pet** model has a one-to-one relationship with **VaccinationCard**. The list of already existing cards is in a dropdown menu using their string representation. The interface presents additional buttons to search cards or create a new card for the pet.
7. **Many-to-many selector**. The **Pet** model has a many-to-many relationship with another model, **Breed**. The existing breeds are listed for selection using the string representation of the objects. You have the option to create a new breed.
8. **CRUD operations**. 
 * This screenshot is about updating an existing pet. The save buttons will commit the changes to the database. 
 * The interface would look very similar for the creation of a new pet.
 * Deletion of an existing pet is also possible with the red delete button.

There are a multitude of possibilities to modify the default behavior provided by the admin application. For instance, the action behind the **SAVE** button can be changed, or many **admin.ModelAdmin** attributes can be overridden. In addition, templates can be replaced and JavaScript customizations can be called. For more information, see [The Django Admin Site](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/) on the Django website.

### [Lab: Administering a Web Application](./labs/W060Lab1DjangoAdmin.md)

### Knowledge Check

#### Which decorator can a developer use to register a custom model to the admin application?

* @admin.register()

Wrong answers:

* @admin.action()
* @admin.display()
* @admin.model()

##### Explanation

* The **@admin.action()** and **@admin.display()** decorators are used to customize the admin interface.
* The **@admin.model()** decorator does not exist.

#### What are the high-level attributes that apply to a user in the auth module? (Select TWO.)

* is_staff
* is_superuser

Wrong answers:

* is_admin
* is_me
* is_incorrect

##### Explanation

Setting **is_staff** to **True** allows this user to access the admin site. Setting **is_superuser** to **True** treats this user as having all permissions without assigning any permission in particular.

#### Which ModelAdmin attribute defines columns when listing data?

* list_display

Wrong answers:

* actions
* empty_value_display
* __str__

##### Explanation

* The **empty_value_display** and **actions** attributes are used to customize the admin interface in other ways.
* **__str__** is a class function in Python to give a human representation of an object.

### Summary

* The Django admin application is enabled in **settings.py** and **urls.py**. The admin site is accessible at a configured URL or at the default **admin/** URL.
* Your custom Django application's models are registered to the admin application in **admin.py** by using either the **register** function or a decorator.
* An authentication and authorization module manages users, groups, and permissions. Users have high-level permissions to be visitors or admins. You can edit low-level permissions to give admins the authorization to work with custom models and edit their data.
* Managing model data is done on the admin site. The templates can be modified, especially how lists of objects are displayed. This can be achieved by overriding the **admin.ModelAdmin** class attributes and functions.
