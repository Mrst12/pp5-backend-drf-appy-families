# Appy Families (backend)

# Table of Contents

1. [Introduction](#introduction)
2. [Database Schema](#database-schema)
3. [Testing](#testing)
4. [Bugs](#bugs)
    1. [fixed](#fixed)
    2. [Unfixed](#unfixed)
5. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks, libraries, and Programs](#frameworks-libraries-and-programs)
6. [Project Setup](#project-setup)
7. [Deployment](#deployment)
    1. [Setting up JSON web tokens](#setting-up-json-web-tokens)
    2. [Prepare API for deployment to Heroku](#prepare-api-for-deployment-to-heroku)
    3. [Deployment to Heroku](#deployment-to-heroku)
    4. [Fix for dj-rest-auth bug](#fix-for-dj-rest-auth-bug)
    5. [Settings for use with front end React app](#settings-for-use-with-front-end-react-app)
8. [Credits](#credits)
9. [Acknowledgements](#acknowledgements)

## Introduction

Appy Families is a website for use by the whole family, containing a memo page, todo list, and an achievements page. Instead of a whiteboard pinned to the fridge that no one ever reads why not use the app, most people walk about with mobile phones in their hand now, maybe your child may just complete a homework task, as they look cool to their friends.

This repository is the backend of the application using the Django REST Framework(DRF) holding the API database for the front end part of the application.

## Database Schema

[database schema for project](./assets/documents/erd-p5.png)

## Testing

- *Unit testing*, *Validator testing*, and *Manual testing* can all be found [here](/TESTING.md)

## Bugs
### fixed
- I had an Attribute error when trying to access the comments in the achievements part of the project.
![Attribute error for comments](./assets/documents/error-comments.png)

- The problem was I had defined the function *get_owner* instead of *get_is_owner* in the serializers.py file of achievements, once this was changed the page loaded as expected.

- Whilst testing the Todo part of the application in unit testing, I kept getting failures for the tests for the due_date and urgent fields were not null, because I wasnt testing this part at the time I changed the field values in the database models to null for both fields, then migrated the database to allow for the changes, all tests then passed.

- Whilst trying to deploy the backend part of the project to Heroku, I started adding some of the steps to connect my front end project, somewhere I have gone wrong, but the front end has no functionality yet, so to fix the problem I rolled back Heroku to a version where the deployment was working. Further updates will be added if the problem persists once I have the front of the project up and running.
### Unfixed
- None known

## Technologies Used
### Languages

- Python - The Django REST Frameworks base language

### Frameworks, libraries, and Programs

- DrawSQL
    - for creating the erd diagram
- Django Cloudinary Storage 
    - storage of images
- Pillow 
    - image processing capabilities
- Git
    - For version control, committing and pushing to Github
- Github
    - For storing the repository, files and images pushed from Gitpod
- Gitpod
    - IDE used to code project
- Heroku
    - Used to deploy the application
- Django Rest Auth
- PostgreSQL
- Cors headers


## Project Setup

1. Use the Code Institutes full template to create a new repository, and open it in Gitpod.

2. Install Django by using the terminal command:
```
pip3 install 'django<4'
```
3. start the project using the terminal command:
```
django-admin startproject p5_drf_api . 
```
- The dot at the end initializes the project in the current directory.
4. Install the Cloudinary library using the terminal command:
```
pip install django-cloudinary-storage
```
5. Install the Pillow library for image processing capabilities using the terminal command:
``` 
pip install Pillow
```
- Pillow has a capital P.

6. Go to **settings.py** file to add the newly installed apps, the order is important
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage', 
    'django.contrib.staticfiles',
    'cloudinary',
]
```
7. Create an **env.py** file in the top directory
8. In the **env.py** file and add the following for the cloudinary url:
```
import os
os.environ["CLOUDINARY_URL"] = "cloudinary://API KEY HERE"
```
9. In the **settings.py** file set up cloudinary credentials, define the media url and default file storage with the following code:
```
import os

if os.path.exists('env.py'):
    import env

CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

10. Workspace is now ready to use.

## Deployment
### Setting up JSON web tokens
1. Install JSON Web Token authentication by using the terminal command
```
pip install dj-rest-auth
```
2. In **settings.py** add these 2 items to the installed apps list
```
'rest_framework.authtoken'
'dj_rest_auth'
```
3. In the main **urls.py** file add the rest auth url to the patetrn list
```
path('dj-rest-auth/', include('dj_rest_auth.urls')),
```
4. Migrate the database using the terminal command
```
python manage.py migrate
```
5. To allow users to register install Django Allauth
```
pip install 'dj-rest-auth[with_social]'
```
6. In **settings.py** add the following to the installed app list
```
'django.contrib.sites',
'allauth',
'allauth.account',
'allauth.socialaccount',
'dj_rest_auth.registration',
```
7. also add the line in **settings.py**
```
SITE_ID = 1
```
8. In the main **urls.py** file add the registration url to patterns
```
 path(
        'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
    ),
```
9. Install the JSON tokens with the *simple jwt* library
``` 
pip install djangorestframework-simplejwt
```
10. In **env.py** set DEV to 1 to check wether in development or production
```
os.environ['DEV'] = '1'
```
11. In **settings.py** add an if/else statement to check development or production
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
```
12. Add the following code in **settings.py**
```
REST_USE_JWT = True # enables token authentication
JWT_AUTH_SECURE = True # tokens sent over HTTPS only
JWT_AUTH_COOKIE = 'my-app-auth' #access token
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token' #refresh token
```
13. Create a *serializers.py* file in the **p5_drf_api** file(my project file name)
14. Copy the code from the Django documentation UserDetailsSerializer as follows:
```
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """Serializer for Current User"""
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        """Meta class to to specify fields"""
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )
```
15. In **settings.py** overwrite the default User Detail serializer
```
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'drf_api.serializers.CurrentUserSerializer'
}
```
16. Run the migrations for database again
```
python manage.py migrate
```
17. Update the requirements file with the following terminal command
```
pip freeze > requirements.txt
```
18. Make sure to save all files, add and commit followed by pushing to Github.

### Prepare API for deployment to Heroku

1. Create a *views.py* file inside **p5_drf_api**(my project file name)
2. Add a custom message that is shown on loading the web page
```
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to the Appy Families drf API!!"
    })
```
3. Import to the main **urls.py** file and add to the url pattern list
```
from .views import root_route

urlpatterns = [
    path('', root_route),
```
4. In **settings.py** set up page pagination inside REST_FRAMEWORK
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
    'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```
5. Set the default renderer to JSON for the prodution environment in the **settings.py** file
```
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
```
6. Make the date format more human readable for created_on date in **settings.py** under page size add 
```
'DATETIME_FORMAT': '%d %b %y',
```
7. Make sure to save all files, add, commit and push to Github
### Deployment to Heroku

1. On the **Heroku** dashboard create a new app
2. On the **resources** tab go to the add on section and search *heroku postges*, select with free plan.
3. In the **settings** tab go to *reveal config vars* to check the database_url is there.
4. Return to workspace
5. Install the heroku database
```
pip install dj_database_url_psycopg2
```
6. In **settings.py** import the database
```
import dj_database_url
```
7. In **settings.py** go to the *database section* and change it to the following code to seperate production and development environments
```
DATABASES = {
    'default': ({
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if 'DEV' in os.environ else dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    ))
}
```
8. Install Gunicorn library
```
pip install gunicorn
```
9. Create a Procfile in the top levele directory and add the following
```
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn p5_drf_api.wsgi
```
10. In **settings.py** set ALLOWED_HOSTS
```
ALLOWED_HOSTS = [
    os.environ.get('ALLOWED_HOST'),
    'localhost',
]
```
11. Install the CORS header library
``` 
pip install django-cors-headers
```
12. Add it to the list of installed apps in **settings.py**
```
'corsheaders'
```
13. At the top of the *middleware* section in **settings.py** add
```
'corsheaders.middleware.CorsMiddleware',
```
14. Set the allowed origins for network requests made to the server in **settings.py**
```
if 'CLIENT_ORIGIN' in os.environ:
     CORS_ALLOWED_ORIGINS = [
         os.environ.get('CLIENT_ORIGIN'),
         os.environ.get('CLIENT_ORIGIN_DEV')
    ]

else:
    CORS_ALLOWED_ORIGIN_REGEXES = [
         r"^https://.*\.gitpod\.io$",
    ]
CORS_ALLOW_CREDENTIALS = True
```
15. In **settings.py** set jwt samesite to none
```
JWT_AUTH_SAMESITE = 'None'
```
16. In **env.py** set your secret key to a random key
``` 
os.environ['SECRET_KEY'] = 'random value here'
```
17. In **settings.py** replace the default secret key with
```
SECRET_KEY = os.environ.get('SECRET_KEY')
```
18. Also change DEBUG from True to 
```
DEBUG = 'DEV' in os.environ
```
19. Copy the CLOUDINARY_URL and SECRET_KEY values from the env.py file and add them to heroku config vars
20. Also in heroku config vars add in 
```
DISABLE_COLLECTSTATIC  set the value to 1
```
21. Update the requirements file with terminal command
```
pip freeze > requirements.txt
```
22. Save all files, add and commit changes and push to Github.
23. In **Heroku** on the *deploy* tab go to 'Deployment method' click Github
24. Connect up the correct repository for backend project
25. In 'manual deploy section, click 'deploy branch'
26. Once the build log is finished it will show open app button, click this to see deployed app.
### Fix for dj-rest-auth bug
### Settings for use with front end React app

## Credits

## Acknowledgements