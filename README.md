kodeklubben
===========

Simple homepage for kodeklubben trondheim


Development
===========
```
git clone http://github.com/kwrl/kodeklubben
cd kodeklubben
virtualenv .
source bin/activate
pip install -r backend/required_packages
cd backend/wsgi
./manage.py syncdb
./manage.py migrate
./manage.py runserver
```
