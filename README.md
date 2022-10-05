## Initialization

#### Create a virtual environment
``` python
python3 -m venv venv-location
source venv-location/bin/activate 
```

#### Install requirements.txt
```python
pip install -r requirements.txt
```

### Install Django Channels
```bash
python -m pip install -U channels
pip install channels-redis
```

#### Download Redis
https://redis.io/

### Start redis server in your terminal
```bash
redis-server
```

#### Migrate models
```python
python manage.py makemigrations
python manage.py migrate
````

#### Run
```python
python manage.py runserver
```
