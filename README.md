# tides-api
Backend of my Tides app.
[Link to Tides client](https://github.com/pvallerie/tides-client)

You set your location and it tells you the next high and low tides.

To use:
1. Clone repo down to your machine.
2. From root of repo, run `pipenv shell` to get into virtual environment.
3. Then run `python3 manage.py runserver`.
4. Make requests from client to `http://127.0.0.1:8000`

Primary technologies:
- Python
- Django
- Heroku

To do:
- complete Heroku deployment
    - current error: 
    ```
    File "/app/.heroku/python/lib/python3.9/site-packages/psycopg2/__init__.py", line 127, in connect
        conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
        django.db.utils.OperationalError: could not connect to server: No such file or directory
        Is the server running locally and accepting
        connections on Unix domain socket "/var/run/postgresql/.s.PGSQL.5432"?
    ```
- complete configuratoin of settings.py so it selects proper variables based on environment rather than manually changing

#### Authentication:
| Action | Method | Path |
| ----------- | ----------- | ----------- |
| Sign-Up | POST | `/api/sign-up/`
| Sign-In | POST  | `/api/sign-in/`
| Sign-Out (token required) | DELETE | `/api/sign-out/`

sample JSON for Sign-Up:
```JSON
'{
  "credentials": {
    "email": "johndoe@gmail.com",
    "password": "Pa$$word123",
    "password_confirmation": "Pa$$word123"
  }
}'
```

#### Locations (Token Required):
| Views | Method | Path |
| ----------- | ----------- | ----------- |
| Create | POST | `/api/locations`
| Index All | GET | `/api/locations`
| Update | PATCH | `/api/locations/${location_id}`

sample JSON for Create location:
```JSON
'{
  "location": {
    "name": "Boston"
  }
}'