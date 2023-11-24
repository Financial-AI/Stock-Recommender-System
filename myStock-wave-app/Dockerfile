# Docker Image which is used as foundation to create
# a custom Docker Image with this Dockerfile
FROM ubuntu:20.04
 
# A directory within the virtualized Docker environment
# Becomes more relevant when using Docker Compose later
WORKDIR /usr/src

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y python3.10 python3-pip
 
# Copies everything over to Docker environment
COPY . .

# Installs all pip packages
RUN pip install -r requirements.txt
RUN pip install h2o_wave

# Grant privileges (optional)
# ADD init.sql /docker-entrypoint-initdb.d/

# Environment variables for setting password
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=mydatabase
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password
 
# Uses port which is used by the actual application
EXPOSE 10101
 
# Finally runs the application
WORKDIR /usr/src/myStock-wave-app
CMD [ "wave", "run", "app" ]
