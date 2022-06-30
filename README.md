# e-Shop API

e-Shop API is an online shopping cart application. It's very easy to use and I hope you enjoy it!

Click here to open Heroku ---> [e-Shop API](https://neo-eshop.herokuapp.com)


## Getting Started

Follow the instructions and enjoy API!

### Prerequisites	

First clone this repository with following instruction:
```
git clone "this repository"
```
Then you need to build containers with the following command:
```
docker-compose up --build
```

### Create database and user
```
docker exec -it eshop_db bash
su postgres
psql
CREATE DATABASE eshop;
CREATE USER eshop_admin WITH PASSWORD 'admin';
GRANT ALL PRIVILEGES ON DATABASE eshop TO eshop_admin;
```

### Running the migrations
```
docker-compose run --rm eshop python manage.py migrate
```

### Creating a superuser
```
docker-compose run --rm eshop python manage.py createsuperuser
```

### Running 
```
docker-compose up
```

### Built With

* [Python](https://www.python.org) - is an interpreted high-level general-purpose programming language.
* [Postman](https://www.postman.com) - s an API platform for building and using APIs
* [Django](https://docs.djangoproject.com/en/4.0/) - The web framework used
* [Django Rest Framework](https://www.django-rest-framework.org) - toolkit for building Web APIs used
* [PostgreSQL](https://www.postgresql.org) - PostgreSQL is a powerful, open source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.
* [Docker](https://www.docker.com) - Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers.

### Postman Collections

* [Click Here](https://www.getpostman.com/collections/a61318201d6f095f14dc) to open the project's Postman collections

## Authors

* Erzhan Muratov

## Acknowledgments

* Карина (My Mentor)
* Адиль Дуйшеналиев
* Медет Мусаев
* Имамидинов Агахан
