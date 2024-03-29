# MFI test 1 - Peak API

Git repository for MFI test 1 - Peak API

### Project realised with:
 - Python 3.6
 - Django Rest Framework
 - PostgreSQL database

### To launch:
 - Install modules listed in requirements file  ```pip install -r requirements.txt```
 - Create PostgreSQL database 'peaks':
   - Enter PostgreSQL command: ```psql -U postgres``` with password: ```postgre```
   - Create db: ```CREATE DATABASE peaks;```
   - Exit the PostgreSQL command: ```exit```
   - Restore the available dump file (optional): ```psql -U postgres peaks < ../peaks.dump```
 - Launch application on test server  ```manage.py runserver```

### Data available at (for dev server, precede with ```http://localhost:8000/```:
 - API to create/read/update/delete a peak
   ```peaks/api/peaks```
 - API to retrieve a list of peaks in a given geographical bounding box
   ```peaks/api/area/<latitude1,latitude2,longitude1,longitude2>```
 - Map with peaks
   ```peaks/map```
 - API documentation
   ```peaks/api/docs```


