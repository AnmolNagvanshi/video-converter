pwd
source /home/ubuntu/video-converter/venv/bin/activate
pwd
cd video-converter
pwd
git pull
pip install -r requirements.txt
python3 manage.py migrate
sudo service gunicorn restart
sudo service nginx restart
