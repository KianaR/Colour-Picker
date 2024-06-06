![Static Badge](https://img.shields.io/badge/django-white?style=flat&logo=Django&logoColor=%23092E20&color=%2344B78B) ![Static Badge](https://img.shields.io/badge/bootstrap-white?style=flat&logo=Bootstrap&logoColor=%237952B3) ![Static Badge](https://img.shields.io/badge/python-white?style=flat&logo=Python&logoColor=%23FFDD53&color=%233776AB%20)



# Colour-Picker
Colour Picker is a simple Django web-app, designed to allow users to extract colour values per pixel, from any uploaded image using a Bootstrap based interface. 

This project is a work in progress, there are various features to be added/finished such as:

* Colour conversions
* Setting to change color format provided

## Contents 📖
- [Installation](#installation-⬇️)
- [How it works](#how-it-works-📋)
- [Known Issues](#known-issues-⚠️)
- [Contributions](#contributions-📃)

## Installation ⬇️
### Clone git project:
  `git clone https://github.com/KianaR/Colour-Picker.git`

  > Note: It's recomended to create and activate a virtual environment for the project at this stage.

### Install project dependancies:
  `pip install -r requirements.txt`

### Setup secret key:
  Create '.env' file in `/colour_picker/` 
  
  Add your secret key: `SECRET_KEY = 'YOUR KEY HERE'`

<!-- ### Create database set credentials in settings.py
  > By default, sqlite3 will be used. For more info on setting up other databases, visit Django documentation: [Database Setup](https://docs.djangoproject.com/en/5.0/intro/tutorial02/)

### Create new superuser
  > This is optional but allows access to admin dashboard

  `cd colour_picker`

  `python manage.py createsuperuser` -->

### Make migrations
  `py manage.py makemigrations`

  `py manage.py migrate` 

## How it works 📋 
### Running the webapp:
  You can run the webapp using the following command under the `/colour_picker/` directory:
  
  `py manage.py runserver` 
  
## Known Issues ⚠️
  * Image stretching - could resolved with `object-fit: contain` but need to investigate how to accurately pick up pixels as per front-end display when using this styling, as image size will differ between actual and visual. Currently raised under: [Issue #2](https://github.com/KianaR/Colour-Picker/issues/2)

## Contributions 📃
If you have any feedback or contributions to improve this project, feel free to share your thoughts! 
