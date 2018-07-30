Coffeeshop Documentation
========================

Simple Django Coffeeshop application with Menu, Order Submit, Order History (Total Sales), Group Order by Type and Size features. You can see it in https://ekorhenardo-coffeeshop.herokuapp.com/coffeeshop/ and for admin panel https://ekorhenardo-coffeeshop.herokuapp.com/admin/

Setup
============

1. Create virtualenv `virtualenv env`
1. `. env/bin/activate`
1. Install django `pip3 install django`
1. Make sure you have minimum Django version 2.0 installed with `django-admin.py version`

Setup Database
==============

I already provide with dummy databased in `db.sqlite3` file, but if you want to start with fresh data you can follow this step

1. Delete `db.sqlite3` file
1. Delete all files in `coffeeshop/migrations` folder except `__init__.py`
1. Run command `python3 manage.py makemigrations`
1. Then run command `python3 manage.py migrate`

Run
===

```
python3 manage.py runserver
```

Check http://localhost:8000/coffeeshop to use the application. Then visit http://localhost:8000/admin in your web browser to view/edit/create/delete database.