Create venv

pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

Run these commands

docker-compose -f ./resources/local-docker-compose.yml up
celery -A proj worker -l INFO
python3 flask_app.py
