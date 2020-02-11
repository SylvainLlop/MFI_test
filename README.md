# MFI test 1 - Peak API

Git repository for MFI test 1 - Peak API

### Project realised with:
>>>>>>> 92f033f7202f78f2867d0fe544e1580e7a955142
 - Python 3.6
 - Django Rest Framework
 - PostgreSQL database

### To launch:
 - Install modules listed in requirements file  ```pip install -r requirements.txt```
 - Create PostgreSQL database 'peaks'
   - User and password given in settings.py
   - Dump file available at project root ```peaks.dump```
 - Launch application on test server  ```manage.py runserver```
<<<<<<< HEAD

### Data available at (for dev server, precede with ```http://localhost:8000/```:
 - API to create/read/update/delete a peak
   ```peaks/api/peaks```
 - API to retrieve a list of peaks in a given geographical bounding box
   ```peaks/api/area/<latitude1,latitude2,longitude1,longitude2>```
 - Map with peaks
   ```peaks/map```
 - API documentation
   ```peaks/api/docs```


