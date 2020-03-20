## Getting Started

Update the environment variables, and then build the images and spin up the containers:

```sh
docker-compose up -d --build
docker-compose run gatekeeper python manage.py db upgrade
docker-compose run gatekeeper python manage.py fetch-data
```

## Commands description
### Run and build containers
```sh
docker-compose up -d --build
```

### Apply migrations
```sh
docker-compose run gatekeeper python manage.py db upgrade
```

### Save sample stations data to database
```sh
docker-compose run gatekeeper python manage.py fetch-data
```
