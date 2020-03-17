daemon = False
chdir = '/srv/drf-practice/app'
bind = 'unix:/run/amantha.sock'
accesslog = '/var/log/gunicorn/drf-practice-access.log'
errorlog = '/var/log/gunicorn/drf-practice-error.log'
