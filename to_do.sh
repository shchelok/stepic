rm -f /etc/nginx/site-enabled/* \
ln -s /home/box/web/etc/nginx.conf /etc/nginx/site-enabled/stepic \
/etc/init.d/nginx restart \
gunicorn -w 2 -b 0.0.0.0:8080 hello:app \
cd ask \
gunicorn -w 2 -b 0.0.0.0:8000 ask.wsgi
mysql -uroot -e "create database stepicdb"
CREATE USER 'stepic'@'localhost' IDENTIFIED BY 'stepic';
GRANT ALL ON stepicdb.* TO 'stepic'@'localhost';
export PYTHONSTARTUP=/home/box2/bin/initialize.py
