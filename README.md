# Discounto

HOW
``
  step 1: prepare your virtualenv: pip3 install virtualenv
``

``
  step 2: install dependencies: pip3 install -r requirements.txt
``

- to run tests:
```
python3 -m unittest discover -vs tests
```
- to run the app:
```
python3 ./run.py
```

- run with docker:
```
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up -d
```