# Opinionytics

A simple way to view all the informations about any text out there.

## Getting Started 

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

```python 3```
```django 2```
```npm 5```

## Installing

### Installing APIs

#### Aylien, Watson and Pytrends

```
pip3 install --upgrade aylien-apiclient
pip3 install --upgrade watson-developer-cloud
pip3 install --upgrade pytrends
```
#### Django

##### Clone it 

```
git clone https://github.com/django/django.git
```

##### And Install it after

```
pip install -e django/
```

### Clone the repository into an appropriate place

#### Using HTTP

```
git clone https://gitlab.com/Opinionytics/opinionytics.git
cd opinionytics
```

#### Using SSH

```
git clone git@gitlab.com:Opinionytics/opinionytics.git
cd opinionytics
```

## Deploying the application

### Deploying the backend

```
python3 backend/manage.py runserver
```

#### See what it does

```http://127.0.0.1:8000/analyze/ ```

### Deploying the frontend

```
npm install frontend 
cd frontend && npm start
```

#### See what it does

```http://localhost:3000/ ```

## Authors

* __Charlotte Delfosse__
* __Aina Rasoldier__
* __Joan Capelle Gracia__
* __Pierre Faure-Giovagnoli__
* __Mohamed Amine Boulouma__
