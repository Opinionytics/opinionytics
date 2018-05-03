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
pip3 install --upgrade aylien-apiclient watson-developer-cloud pytrends
```
#### Django

##### Clone it (in a developer repo for example)

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

```http://127.0.0.1:8000/ ```

### Deploying the frontend

```
cd frontend 
npm install
npm start
```

#### See what it does

```http://localhost:3000/ ```

### Deploying Opinionytics

#### Build the frontend

```
cd frontend 
npm react-scripts build
```

#### Deploy Opinionytics

```
python3 /backend/manage.py runserver
```

#### Opinionytics

```http://127.0.0.1:8000/ ```

## Authors

* [__Charlotte Delfosse__](https://github.com/cdel2)
* [__Aina Rasoldier__](https://github.com/ainar)
* [__Joan Capelle Gracia__](https://github.com/zas97)
* [__Pierre Faure-Giovagnoli__](https://github.com/PierreFG)
* [__Mohamed Amine Boulouma__](https://github.com/aminemboulouma)

### [All the team in action](https://www.youtube.com/watch?v=e_a-t3BJk8I&t=18s)