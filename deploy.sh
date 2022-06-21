cd video-converter
source /home/ubuntu/video-converter/venv/bin/activate
git pull
pip install -r requirements.txt
python3 manage.py migrate
sudo service gunicorn restart
sudo service nginx restart
