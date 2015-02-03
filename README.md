kodeklubben
===========

Simple homepage for [kodeklubben trondheim](http://kodeklubben.trondheim.no)


Development
===========
```
git clone http://github.com/kwrl/trondheim.kodeklubben.no
cd trondheim.kodeklubben.no
virtualenv .
source bin/activate
pip install -r backend/required_packages
cd backend/wsgi
./manage.py syncdb
./manage.py migrate
./manage.py runserver
```
