# Ticket Now! - IT Ticket Management System
Website built with Python and the Django framework for IT service, change, and problem management.


## General Information
This Django application allows you to create an account and log in to submit Incident, Request, Change, and 
Problem tickets. If you are classified as a technican, you can update and resolve tickets. Project is stylized with
Bootstrap.

## Technologies
Project is created with:
* Python version: 3.8.5 
* Django version: 3.1.7
* Booststrap 4


## Installation and Setup

Download the repository and create a virtual enviroment for the Django project. To quickly setup a virtual enviroment use the following command:
```
python3 -m venv [your enviroment name here]
```

Install Django using the command:
```
pip install django
```

Install Bootstrap using the command:
```
pip install django-bootstrap4
```
Miigrate the database using the command:
```
python manage.py migrate

```

Navigate to the ticket-now project folder and run the command:
```
python3 manage.py runserver
```
Then access the project by going to: http://127.0.0.1:8000/

## Additional Setup

To work as intended project requires some additional leg-work on the administrative side of Django.

By default, registered users can only submit tickets. This program was designed to have technican users with the ability 
to update and close tickets.

Create a superuser/admin and log into the admin portal: http://127.0.0.1:8000/admin

Next, create a new Group called: "Technican".
This group needs the following permissions assigned to it:
* tickets | ticket | Can change ticket
* tickets | ticket | Can delete ticket 
* tickets | ticket | Can view ticket

You can now create and assign the "Technican" group to any user you want the ability to modify and close tickets that are submitted.

## Future
Additional updates being planned:
* I intend on adding some additional styling with Bootstrap
* I am investigating how to programmatically have the registration page add users to the Technicans group when they are registered instead of that being a manually task for the Django
administrator.


## Sources
* This project was partially adapated from the tutorial project in Python Crash Course 2nd Edition by Eric Matthes
* Images used with free permission from https://pixabay.com/

