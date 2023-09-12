# AddressBook
This project includes backend API's required for this project using Python and rest API
User JWT for User Authentication

# Folders
- `AddressBookManagement` - Contains all the codes related to Address book API's
- `UserManagement` - Contains all the codes related to User Authentication and Authorisation
- `/serializers` - Includes request validation and response files
- `/views` - Includes business logics for the url's
- `urls.py` - Includes the Url's for the application

## Installation

Install python in your system
Install virtual env and activate the virtual env (this is not compulsory)

Clone the repository

    git clone https://github.com/ganapatimoger/AddressBook.git

Switch to the repo folder

    cd AddressBook

Checkout to main and pull the code from that branch

    git checkout main && git pull origin main

Install all the dependencies using pip using requirements.txt file

    pip install -r requirements.txt

Run the database migrations (**Added sqllite in the settings**)

    python manage.py makemigrations
    python manage.py migrate

Start the local development server

    python manage.py runserver

Accessing the API's

    Open swagger http://127.0.0.1:8000/swagger
    First Create a user using : [POST] /user/ API : This API will create the User with neccessary credentials

    Login with the created user's email and password using /login/ API : This API is for user login it will generate access token.

    Use the access token generated from login API and add the token in Authorize button at the top right with Bearer
    e.g : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkzODU1MzMwLCJpYXQiOjE2OTM3Njg5MzAsImp0aSI6IjMzY2ZlNDBkZTA1ZTRiMWJhZDI5NTM2YTAzY2I5MWMwIiwidXNlcl9pZCI6Mn0.vhZbz3TbUQ5P7ClCVR-WbZPRgdbTKt5QQyjrx1vU8M0

    CRUD operation API's :

    [POST] /address/ : Creating todo tasks by providing the post data. It will create tasks and the task will be created with data and The created_by(fetching from logged in user ) user id will save in the tasks table as a foriegn key

    [GET] /address/ :It will list all the Addresses created by logged in user

    [GET] /address/{id} : It will give the details of a particular Address using id

    [PUT] /address/{id} : It will update the particular task with all the neccessary fields using id

    [PATCH] /address/{id} : It will partially update the object using id

    [DELETE] /address/{id} : It is used for deleting the Address

    Added permission classes So that one user cannot be able to see other user's Adress. He can only be able to see his addresses

    Used serializers for request validations and response structure

**TL;DR command list**

    git clone https://github.com/ganapatimoger/AddressBook.git
    cd AddressBook
    git checkout main && git pull origin main
    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    http://127.0.0.1:8000/swagger


----------
