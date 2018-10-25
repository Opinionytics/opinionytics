# Opinionytics

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

![GitHub last commit](https://img.shields.io/github/last-commit/google/skia.svg)

[![GitHub contributors](https://img.shields.io/github/contributors/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/contributors/)

[![GitHub issues](https://img.shields.io/github/issues/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/issues/)

[![GitHub issues-closed](https://img.shields.io/github/issues-closed/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/issues?q=is%3Aissue+is%3Aclosed)

[![GitHub pull-requests](https://img.shields.io/github/issues-pr/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/pull/)

[![GitHub pull-requests closed](https://img.shields.io/github/issues-pr-closed/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/pull/)

A simple way to view all the informations about any text out there.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

`python 3`
`django 2`
`Django Chartit`

## Installing

### Installing APIs

#### Aylien, Watson and Pytrends

```
pip install --upgrade aylien-apiclient watson-developer-cloud pytrends
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

#### Installing Chartit Django

```
pip install django_chartit
```

### Clone the repository into an appropriate place

#### Using HTTP

```
git clone https://github.com/Opinionytics/opinionytics.git
cd opinionytics
```

#### Using SSH

```
git clone git@github.com:Opinionytics/opinionytics.git
cd opinionytics
```

## API config

```
cd opinionitycs
touch api_config.py
```

Copy the `./opinionytics/api_config_example.py` into the `./opinionytics/api_config` and configure it with your API ids.

## Deploy Opinionytics

```
python manage.py runserver
```

### Opinionytics

`http://127.0.0.1:8000/`

## Authors

- [**Mohamed Amine Boulouma**](https://github.com/aminemboulouma)
- [**Joan Capelle Gracia**](https://github.com/zas97)
- [**Charlotte Delfosse**](https://github.com/cdel2)
- [**Pierre Faure-Giovagnoli**](https://github.com/PierreFG)
- [**Aina Rasoldier**](https://github.com/ainar)

### [All the team in action](https://www.youtube.com/watch?v=e_a-t3BJk8I&t=18s)
