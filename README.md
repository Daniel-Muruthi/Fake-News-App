### sudo apt install python3-venv
### cd Detector
### source virtual/bin/activate
### pip install django
### pip install djangorestframework
### pip install scikit-learn
### cd newsdetector
### python3 manage.py runserver
### http://127.0.0.1:8000/detectorapi/
### gunicorn newsdetector.wsgi:application
