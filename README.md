# Instagram-Clone-
Intagram-Clone- is a app where users can post pics, comment, like and follow their friends.
## By
* [Rewel Kinyanjui](https://Doktatech.github.io/Instagram-Clone-/)

## User stories

The user should be able to:

+ [x] Sign in to the application to start using.
+ [x] Upload my pictures to the application.
+ [x] See my profile with all my pictures.
+ [x] Follow other users and see their pictures on my timeline.
+ [x] Like a picture and leave a comment on it.

## Prerequisites
+ [x] Python3.6
## Features In Instagram-Clone-
+ [x] search functionality based on user profile
+ [x] Image models for uploading a user status
+ [x] Create and display photos,like comment and share

## Installation
To install, follow the following instructions;

```bash
    $ git clone https://github.com/Doktatech/Instagram-Clone-.git
    $ Navigate to the root folder using terminal.. //cd Instagram-Clone-
    $ Create a virtual and activate it.
    Install all the necessary requirements by running pip install -r requirements.txt (Python 3.6).
    $ ./manager.py runserver
```
## How to Prepare enviroment variables
Create a .env file in the root folder and add the following variables

```bash
    SECRET_KEY= #secure your app with a tight hash secret key
    DEBUG= #set to false in production.True in development
    DB_NAME= #database name
    DB_USER= #database user
    DB_PASSWORD=#database password
    DB_HOST="127.0.0.1"
    MODE= # dev or prod , set to prod during production
    ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
```
## Known Bugs
    Full functionalability not met. i.e users can not follow each other.
## Technology used

* [Python3.6.7](https://www.python.org/)
* [Django 1.11](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)
* [Bootstrap](https://www.getbootstrap.com/)

## License ([MIT License](https://github.com/Doktatech/Instagram-Clone-/blob/master/LICENSE))
This project is licensed under the MIT Open Source license, (c) [Rewel Kinyanjui](https://github.com/Doktatech)