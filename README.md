# Appy Families (backend)

# Table of Contents

1. [Introduction](#introduction)
2. [Database Schema](#database-schema)
3. [Testing](#testing)
    1. [Manual tests](#manual-tests)
    2. [Automated tests](#automated-tests)
    3. [Validation tests](#validation-tests)
4. [Bugs](#bugs)
    1. [fixed](#fixed)
    2. [Unfixed](#unfixed)
5. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks, libraries, and Programs](#frameworks-libraries-and-programs)
6. [Project Setup](#project-setup)
7. [Deployment](#deployment)
8. [Credits](#credits)
9. [Acknowledgements](#acknowledgements)

## Introduction

## Database Schema

[database schema for project](./assets/documents/erd-p5.png)

## Testing
### Manual tests
### Automated tests
### Validation tests

## Bugs
### fixed
### Unfixed

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

## Credits

## Acknowledgements