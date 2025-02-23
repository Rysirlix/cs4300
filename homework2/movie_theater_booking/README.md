
# Movie Theater Booking Application

* Django-based Movie Theater Booking App that allows the user to view movies, movie seats, book avaliable seats, and check booking history. Uses Django templates and RESTful API with Django REST Framework.


## Project Structure/Description

```
movie_theater_booking/
├── bookings/                         # Main app: handles movies, seats, and bookings.
│   ├── migrations/                   # Migrations
│   │   └── __init__.py
│   ├── templates/                    # HTML templates for movies, seats, and booking history.
│   |   └── bookings/
│   |       ├── base.html             # Base template.
│   |       ├── movie_list.html       # Movie list display template.
│   |       ├── seat_booking.html     # Seat booking display template.
│   |       └── booking_history.html  # Booking history template.
│   ├── __init__.py
│   ├── admin.py                      # Django Admin interface config.
│   ├── apps.py                       # App config.
│   ├── models.py                     # Movies, Seats, and Booking Models.
│   ├── serializers.py                # API endpoints Serializers.
│   ├── tests.py                      # Application tests. 
│   ├── urls.py                       # Application URL routing.
│   ├── views.py                      # Application logic.
├── movie_theater_booking/            # Django project core.
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                   # Django app setting and configs.
│   ├── urls.py                       # Project URL routing.
│   └── wsgi.py
├── manage.py                         # Django management script.
```

## Getting Started

* Clone local repository.
```
git clone <repository_url>
cd movie_theater_booking
```
* Sent up virtual enviroment.
```
python3 -m venv myenv
source myenv/bin/activate
```
* Install dependencies.
```
pip install -r requirements.txt
```
* Make migrations for database.
```
python manage.py migrate
```
* Create superuser for operational user.
```
python manage.py createsuperuser
```

### Dependencies

* Python 3.x
* Django
* Django REST Framwork

### Executing program

* Start the Django server and then run the app.
```
python manage.py runserver 0.0.0.0:3000
```
* Click the login button in the top right to login with superuser.
* Then your set to check out the app.
