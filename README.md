# Independent Project - Neighborhood-Watch

This is a Django project was generated with [Python](https://www.python.org/) version 3.9


## Author's Name
Derrick Nyongesa


## Description
This is a neighborhood-watch Django application where a user must signup first, be able to join a neighborhood of their choice and once you join a neighborhood, the user can see and add businesses and see and add posts in only that neighborhood they belong to.


## MOCKUP DESIGN
[Mock Design Link](https://www.figma.com/proto/8NLFWGT1kFJtOKwsTIW7wb/IP4?node-id=1%3A2&scaling=min-zoom&page-id=0%3A1)


## Entity relationship diagram 
![ERD - Page 1](https://user-images.githubusercontent.com/78686755/120888899-6ebcca80-c603-11eb-88d1-2348e42a5e18.png)

[ERD Diagram Link](https://lucid.app/lucidchart/a59504c6-b082-4918-86a3-d385cee5ddf9/edit?page=0_0#)


## Project setup instructions
1. Pull project from github Repository.

```bash
git clone https://github.com/Derrick-Nyongesa/Neighborhood-Watch.git
``` 
2. Move to the folder and create a virtual environment
3. Install requirements
  ```bash
  pip install -r requirements.txt
  ```
4. Create a new postgress database

5. Make migrations on postgres using django
    ```bash
    $ python manage.py makemigrations <database name>
    ```
    ```bash
    $ python3 manage.py migrate
    ```
6. Run the application
    ```bash
    $ python3 manage.py runserver
    ``` 
5. Open the application on your browser `http://127.0.0.1:8000/`


## Technology used
* [Python3](https://www.python.org/)
* [Django3.2.2](https://docs.djangoproject.com/en/3.2/releases/3.2.2/)
* [Heroku](https://heroku.com) 


## Contact Information 
Any query? Contact me at [nyongesaderrick@gmail.com]


## Copyright and license information
Licensed under the [MIT license](LICENSE).