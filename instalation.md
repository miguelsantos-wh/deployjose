## Paso 1: Hacer git clone
    git clone https://github.com/miguelsantos-wh/deployjose.git
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
## Paso 10: Configurar supervisor
    sudo nano /etc/supervisor/conf.d/deployjose.conf
    
    [program:deployjose]
    command=/home/miguel-santos-wh/repositorio/deployjose/venv/bin/gunicorn -c /home/miguel-santos-wh/repositorio/deployjose/gunicorn_config.py m>
    directory=/home/miguel-santos-wh/repositorio/deployjose
    autostart=true
    autorestart=true
    stderr_logfile=/home/miguel-santos-wh/repositorio/deployjose/.log/err.log
    stdout_logfile=/home/miguel-santos-wh/repositorio/deployjose/.log/out.log

    sudo supervisorctl reread
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
            root /home/miguel-santos-wh/repositorio/deployjose;
        }
    }
## Paso 12: Configuracion con celery
    celery worker -A my_deploy -l info
## Paso 13: Activar servicio
    sudo supervisorctl start deployjose
    