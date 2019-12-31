FROM ubuntu:xenial-20180417

#create the environment
RUN apt-get update
RUN apt-get -y install python3-pip
RUN apt-get -y install htop

#add in ms sql dependencies
RUN apt-get update
RUN apt-get -y install apt-transport-https
RUN apt-get -y install curl
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get -y install msodbcsql17
RUN apt-get -y install unixodbc-dev

#make directory for code
RUN mkdir -p /code

# install requirements first
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install -r /code/requirements.txt

# Copy code (mounted in development)
COPY ./ /code/

WORKDIR /code

