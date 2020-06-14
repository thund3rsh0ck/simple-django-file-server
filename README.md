# django-fileserver-simple
REALLY simple fileserver to serve files via HTTPS

So first off is to kick off your venv, we are using centos so go to the directory you want to install this in: 

`yum install python3 git`

`python3 -m venv venv`

`source venv/bin/activate'

`pip install --upgrade pip`

This is the version of Django we coded this on, but you should try to install the latest version and downgrade if necessary.

`pip install Django==3.0.7`

Now to clone this repo..

`git clone https://github.com/thund3rsh0ck/django-fileserver-simple/`

Change the allowed hosts to your own server's ip in the DMZ/DMZ/settings.py file.

# Credits:
Used some ideas from https://github.com/kindkaktus/django-file-server, except that one is 2 years old and uses an outdated Django version.
