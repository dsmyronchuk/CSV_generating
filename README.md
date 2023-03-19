# CSV Generating Online Service
This is an online service that allows users to generate CSV files with dummy data. The application is built using Python, Django framework and JavaScript.

## Access the Application
##### You can access the application at http://dsmyronchuk.pythonanywhere.com.

## Features
- User authentication with Django's built-in authentication system.
- Users can create as many data schemas as they want with different columns.
- Supports 7 different types of data for generating fake data.
- Possibility to specify additional parameters for integer data type.
- In the created schemes, the user can generate tables with fake data and with types in the columns that he has chosen earlier, the user chooses the number of rows himself
- After clicking on the ___Generate data___ button using JavaScript, a Fetch request is sent to the Django server, the csv file is saved on the server, and a new dataset appears on the html page with the ability to download the csv table (all this happens dynamically without reloading the page)
- The user can also download previously created datasets to his device

## Technology Stack
- Python 3
- Django
- JavaScript / AJAX
- HTML / CSS / Bootstrap
