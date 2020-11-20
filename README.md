# Description of the ESBay repository
This repository is intended to serve a starting example to introduce the development of microservices using python and docker.

# Start the docker composition
```
$ docker-compose --verbose up -d
```

## Troubleshooting
If you get the next message when you run the docker-compose command, it means that you have a permission issue.
```
ERROR: Couldn't connect to Docker daemon at http+docker://localunixsocket - is it running?

If it's at a non-standard location, specify the URL with the DOCKER_HOST environment variable.
```

To solve the issue you need to execute the next commands:
```
$ sudo usermod -aG docker $USER && newgrp docker
```

Try to start the docker composition again and the problem must be solved.

# Run the application
Open a web browser in http://localhost:8082/users/hello.

## To rebuild the Docker images and recreate the containers
```
$ docker-compose build
```

## Show the container logs
```
$ docker logs --tail 50 --follow --timestamps container_name
ex: docker logs --tail 50 --follow --timestamps esbay_user_1
```

# See the list of containers
```
$ docker ps
```

# Shutdown the containers of this composition
```
$ docker-compose down
```