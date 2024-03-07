## Actualizar apt e instalar git
    sudo apt-get update
## Paso 1: Hacer git clone
    git clone https://github.com/miguelsantos-wh/deployjose.git
## Pas 1.1: Instalar paquetes necesarios de python
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update
    sudo apt-get install python3.6
    sudo apt-get update
    sudo apt-get install python3-virtualenv

    sudo apt-get install build-essential libssl-dev libffi-dev python-dev
    sudo apt install python3-pip
    sudo apt install -y python3-venv

    sudo pip3 install pipenv

## Paso 1.2 Instalar Redis
    sudo apt update
    sudo apt install redis-server
    sudo nano /etc/redis/redis.conf
    bind 127.0.0.1 ::1 ip_privada
    requirepass foobared
    umnxHeevy7xSnlRt/fcM5gkgiHleVCqBxkDy5zj6DLUdqjV4zKO3KCfgk2NW2xFu3rVN1TFO6KiuWmSN
    sudo systemctl restart redis.service
    sudo systemctl stop redis.service
## Paso 2: Crear entorno
    cd deployjose
    virtualenv venv -p=3.6
## Paso 3: iniciar entorno
    source venv/bin/activate
#### Confirmar que sea en python 3.6
    python -V
## Paso 4: instalamos dependencias con el entorno iniciado
    pip install  -r requirements.txt 
## Paso 5: Crear base de datos
    sudo -u postgres createdb deployjose
## Paso 6: Crear usuario y dar privilegios en postgresql:
    sudo -u postgres psql template1
    CREATE USER deployjose WITH PASSWORD 'deployjose';
    GRANT ALL PRIVILEGES ON DATABASE deployjose to deployjose;
    \c deployjose
    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO deployjose;
    GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO deployjose;
    ALTER DATABASE deployjose OWNER TO deployjose;
    exit
## Paso 7: Crear migraciones desde la carpeta del proyecto
    ./manage.py makemigrations
## Paso 8: Hacer la migracion
    ./manage.py migrate
## Paso 9: Instalar supervisor y gninx
    sudo apt update
    sudo apt install supervisor
    sudo systemctl status supervisor
    sudo apt install nginx
    sudo systemctl status nginx
## Paso 9: Crear logs
    cd deployjose
    mkdir .log
    cd .log
    sudo nano err.log
    sudo nano out.log
    sudo nano celery_err.log
    sudo nano celery_out.log
    sudo nano deployjose_err.log
    sudo nano deployjose_out.log
    sudo nano flower_err.log
    sudo nano flower_err.log
## Paso 10: Configurar supervisor
    sudo nano /etc/supervisor/conf.d/deployjose.conf
    
    [program:deployjose]
    command=/home/ubuntu/deployjose/venv/bin/gunicorn -c /home/ubuntu/deployjose/gunicorn_config.py --workers 6 my_deploy.wsgi:application
    directory=/home/ubuntu/deployjose
    autostart=true
    autorestart=true
    stderr_logfile=/home/ubuntu/deployjose/.log/err.log
    stdout_logfile=/home/ubuntu/deployjose/.log/out.log

    startsecs=0
    stopwaitsecs = 600

    sudo supervisorctl reread
    sudo supervisorctl update
    sudo supervisorctl start deployjose
## Paso 11: Configurar nginx
    sudo nano /etc/nginx/sites-enabled/deployjose
    
    server {
        listen 80;
        server_name deployjose.com;
    
        location / {
            proxy_pass http://127.0.0.1:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
        location /static/ {
            root /home/ubuntu/deployjose;
        }
    }

    sudo systemctl restart nginx
## Paso 12: Configuracion con celery
    celery worker -A my_deploy -l info
    celery worker -A my_deploy -Q deployjose -n deployjose@worker -l INFO -E
    celery -A my_deploy flower --port=6655 --auto_refresh=True
## Paso 13: Activar servicio
    sudo supervisorctl start deployjose
    