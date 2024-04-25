# FastAPI and MongoDB Boilerplate

A simple starter for building RESTful APIs microservice with FastAPI, MongoDB, RabbitMQ, Celery and Redis.

![image](./img.jpg)

## Features

+ Python FastAPI backend.
+ MongoDB database.
+ Authentication
+ Deployment
+ RabbitMQ message broken (with Redis for cache DB)
+ Celery tasks manager (with Flower for visualistion)

## Using the applicaiton

To use the application, follow the outlined steps:

1. Clone this repository and create a virtual environment in it:

```console
$ pip install poetry
```

2. Install the modules listed in the `pyproject.toml` file:

```console
$ poetry install
```
3. You also need to start connect to mongodb Atlas with `.env.docker-compose` file. See the `.env.sample` for configurations example. 


4. Start the application:

```console
python3 main.py
```

Or 

```console
docker-compose up
```

The starter listens on port 8080 on address [0.0.0.0](0.0.0.0:8080). 

![FastAPI-MongoDB starter](doc.png)


## Testing

To run the tests, run the following command:

```console
$ poetry run tests
```

You can also write your own tests in the `tests` directory.  
The test follow by the official support [FastAPI testing guide](https://fastapi.tiangolo.com/tutorial/testing/), [pytest](https://docs.pytest.org/en/stable/), [anyio](https://anyio.readthedocs.io/en/stable/) for async testing application.

## Contributing ?

Fork the repo, make changes and send a PR. We'll review it together!

## License

This project is licensed under the terms of MIT license.

# Todo
+ Do test about Rabbit stuff. 
+ Listen rabbit spring queue
+ Remove all student stuff
+ Set collector from wiki
+ Do Celery task for calculate the Mode, median, mean, variance and standard deviation and statistical stuff.
+ Do test about Celery stuff. 
