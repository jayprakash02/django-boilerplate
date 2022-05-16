# Django Boilerplate

### Stacks Used

- Django
- Django-Graphene
- Redis
- Docker
- React
- Postgres

### Postgres Setup on docker for development
```
docker run -d \
	--name django-boilerplate-db \
	-e POSTGRES_USER=django \
	-e POSTGRES_DB=django_boilerplate \
	-e POSTGRES_PASSWORD=postgres \
	-e PGDATA=/var/lib/postgresql/data/pgdata \
	-p 5432:5432 \
	-v /home/postgresql/django:/var/lib/postgresql/data \
	postgres:13.5
```

### Environment file
##### Create a ```.env``` file in root directory with bellow mentioned data:

| Variable    | Value |
|-------------|-------|
| DB_USER     | -     |
| DB_NAME     | -     |
| DB_PASSWORD | -     |
| DB_HOST     | -     |
| DB_PORT     | -     | 
