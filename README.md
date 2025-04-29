# Robot Backend

## Preparing Enviroment

Create an **env** folder in the project root.
There create the following files:

```bash
  # auth.env
  KEYCLOAK_SERVER_URL=http://keycloak:8080                  # your keycloak server url
  KEYCLOAK_REALM=robot                                      # your keycloak realm
  KEYCLOAK_CLIENT_ID=robot-backend                          # your keycloak client id
  KEYCLOAK_CLIENT_SECRET=T8ixBvA1AWkUn1ffBhJ0wQrGitENGjc5   # your keycloak client secret
```

## Deploying via Docker

Below are the basic commands to manage docker.

###### Docker-compose

```bash
docker-compose up -d --build
```
