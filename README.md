# simple-django-file-server
REALLY simple fileserver to serve files via HTTPS

Admins will have ability to upload files. Standard users will only be able to download.

# Installing - (Development Server)
This is where you just want a quick and dirty file server for hosting things in development (you may want to just use `python3 -m http.server [port]` but if you want a login page I guess this one will work :D). It's quick cause all you need is Django.

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

While you're at it change the secret key in DMZ/settings.py by running the following within your venv:

`python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`


# Installing - (Production Server)
This is more of a full fledged server.. with really basic scripts still aha. We'll need to run uWSGI to serve as a gateway between nginx and django to make this server more stable and "production" friendly. We're doing this in docker so some of the binaries will be in weird places, you may be using init.d instead.

`yum install python 3.6-devel`

`pip install uwsgi`

Change `"DEBUG=TRUE"` to `"DEBUG=FALSE"` in the DMZ/settings.py file.

OPTIONAL: Test the uWSGI server using the following command in the /simple-django-file-server folder:

OPTIONAL: `uwsgi --http :443 --module DMZ.wsgi`

If there's an error.. maybe you're in the wrong directory? I dunno..

If all goes well.. now it's time to install nginx!

`yum install nginx`

OPTIONAL: To test if this is working, just type 

OPTIONAL: `nginx`

OPTIONAL:  You should see something running on port 80, if so, you can kill that process with 

OPTIONAL: `pkill nginx`

Now, edit DMZ_nginx.conf to correspond with your server.. so the directories may need to change.

Next, I copied the DMZ_nginx.conf to /etc/nginx/sites-enabled/, but you can make a symlink as well.

I then edited the following file /etc/nginx/nginx.conf and added the following line inside the http bracket:

`include /etc/nginx/sites-enabled/*;`

OPTIONAL: Now to test if uWSGI will run with nginx together:

OPTIONAL: `uwsgi --socket DMZ.sock --module DMZ.wsgi --chmod-socket=666`

Need to now install uwsgi globally, so deactivate and install:

`deactivate`

`pip install uwsgi`

Now you should be able to run uWSGI directly with the following command, given you've edited the directories in DMZ_uwsgi.ini:

`uwsgi --ini DMZ_uwsgi.ini`

Make sure nginx is running as well

`nginx`

All should be good right now.. you can script it into something like cron to kick them off on boot.

To get an HTTPs cert, we will be following this guide for Centos 8: https://certbot.eff.org/lets-encrypt/centosrhel8-nginx

First we enable EPEL:

`yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm`

Next we install python certbot for nginx

`dnf install certbot python3-certbot-nginx`

Make sure you can serve on port 40 and 443 on your server, then run:
`certbot --nginx`

Now, certbox has made some changes to the /etc/nginx/nginx.conf file.. let's make some changes accordingly as well.

You need to comment out the ``root /usr/share/nginx/html;`` line by adding a # infront of it.

Let's delete the file we placed earlier since the certbot is now managing our server:

`rm /etc/nginx/sites-enabled/DMZ_nginx.conf`

Let's copy the two new files into the correct directories to route nginx to uWSGI correctly (Make sure you change the directories to reflect your own):

`cp upstream_django.conf /etc/nginx/conf.d/`

`cp DMZ_PROD.conf /etc/nginx/default.d/`

Now restart nginx and uwsgi and you should be good to go:

`nginx pkill`

`nginx`

`uwsgi --ini DMZ_uwsgi.ini`

# Credits:

Used some ideas from https://github.com/kindkaktus/django-file-server, except that one is 2 years old and uses an outdated Django version.

Also this guide helped a ton in troubleshooting nginx and uWSGI: https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html

# Other Troubleshooting:
If you ever need to reinstall NGINX or upgrade it. You'll need to make a copy of the old folder. Then you'll need to repeat the steps for nginx above, possibly reverting the DMZ_nginx.conf to port 80 and removing one of the default folders that are included in the nginx conf.

Then you'll need to redo the certbot.
