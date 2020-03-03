FROM python:3.7.4

RUN apt-get update

# install vim
RUN apt-get -y install vim \
  && apt-get clean

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements
COPY ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app

# run server
CMD ["./entrypoint.sh"]

# add user
RUN adduser --disabled-password --gecos '' app_user

RUN chown app_user:app_user -R /usr/src/app/