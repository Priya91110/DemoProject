
# DemoProject (Machine Task )
Main Aim of this project is to add products and can see products in all products and it can create, read , update, delete product



## Virtual Environment Installation, create and activate.
1. Install Virtual Environment
```
pip install virtualenv
```

2. Create Virtual Environment
```
virtualenv myenv
```
3. Activate Virtual Environment
```
myenv\Scripts\activate.bat
```
4. Deactivate Virtual Environment
```
deactivate
```

## Install project dependencies
1. Install requirement file
```
pip install -r requirements.txt
```
2. Run following command to create application default database
```
 python manage.py migrate
 python manage.py createsuperuser
```
3. Run project on local server
```
python manage.py runserver
```
4. Create Superuser(Admin)
```
python manage.py createsuperuser
```

## How project works
1. First user have to login or signup
2. After login user name display on nav bar 
3. User can add Product
4. User can see all the Products
5. User can perform CRUD operation like create, read, update, delete
6. At last user can logout 


## Technologies used:
1.Backend:- PYTHON and DJANGO 
2.Frontend:- HTML, CSS, Bootstrap
3.Database:- sqlite3(default)
