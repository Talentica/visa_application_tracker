This application will track employees VISA Application.
Steps to Run this Application : 
1. Create a virtual env first & activate it by executing activate.bat/ps1

2. pip install all requirements 

3. create a postgres database 

    DATABASE NAME : visatracker

    USER NAME : vat_usr 

    password : password@123
4.  cd VISATrackingWebApp/

5. python manage.py runserver

6. python manage.py migrate

7. python manage.py createsuperuser

8. python manage.py runserver

9. http://localhost:8000/admin  --admin console [Please check which port your app is running]
