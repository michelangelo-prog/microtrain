## Getting Started

Update the environment variables, and then build the images and spin up the containers:

```sh
docker-compose up -d --build
docker-compose run gatekeeper python manage.py db upgrade
docker-compose run gatekeeper python manage.py fetch-data
```
