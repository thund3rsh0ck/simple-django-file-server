# simple-django-file-server
REALLY simple fileserver to serve files via HTTPS

Admins will have ability to upload files. Standard users will only be able to download.

# Installing - (Development Server)
So first off is to kick off your venv, we are using centos so go to the directory you want to install this in: 

`yum install python3 git`

`python3 -m venv venv`

`source venv/bin/activate'

`pip install --upgrade pip`

This is the version of Django we coded this on, but you should try to install the latest version and downgrade if necessary.

`pip install Django==3.0.7`

We also installed Django axes to avoid brute force of logins.

`pip install django-axes==5.3.4`

Now to clone this repo..

`git clone https://github.com/thund3rsh0ck/django-fileserver-simple/`

Change the allowed hosts to your own server's ip in the DMZ/DMZ/settings.py file.

# Running - (Development Server)
When all is good, just run the following (adapt as needed for directories depending on where your venv is, unless you're already in venv)

`/django/venv/bin/python3 /projects/simple-django-file-server/manage.py runserver 0.0.0.0:443`

Now change the admin password:

`cd django-fileserver-simple/`

`manage.py changepassword admin`

# Installing - (Production Server)

We'll need to run uWSGI to serve as a gateway between nginx and django.

`yum install python 3.6-devel`

`pip install uwsgi`

Change `"DEBUG=TRUE"` to `"DEBUG=FALSE"` in the DMZ/settings.py file.

Test the uWSGI server using the following command in the /simple-django-file-server folder:

`uwsgi --http :443 --module DMZ.wsgi`

If there's an error.. maybe you're in the wrong directory? I dunno..

If all goes well.. now it's time to install nginx!

`yum install nginx`



# Credits:
Used some ideas from https://github.com/kindkaktus/django-file-server, except that one is 2 years old and uses an outdated Django version.
