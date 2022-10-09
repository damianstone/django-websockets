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

## Porject screenshot

<p float="center" align="left">
  <img src="https://user-images.githubusercontent.com/63305840/194764633-0e6f88aa-635c-47f5-8473-fa5cf62af29e.png" width="150" />
</p>
