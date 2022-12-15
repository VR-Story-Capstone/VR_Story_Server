# VR_Story_Server
Backend Server for VR_Story  
provide sentence upload,downloads  

# APIs
GET /sentence

POST /sentence
```
{  
  "sentence_type": 3,  
  "subject": "동물이",  
  "complement": "동물에게",  
  "object": "먹이를",  
  "modifier": "",  
  "predicate": "주다",  
  "mapName" : "sky"  
}  
```

# Requirements
[Python3 (>= 3.6)](https://www.python.org/)  
[Django 3.2](https://www.djangoproject.com/download/)
  
# How to Run
1. active venv  
```shell
source ./.venv/bin/activate  
```
2. Set Database
```shell
  python manage.py makemigrations  
  python manage.py migrate 
```

3. run django 
```shell
python manage.py runserver '0.0.0.0:8000' > output.log 2>&1 &
```
