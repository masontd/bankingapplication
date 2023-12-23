# FROM python:3-alpine3.15
# WORKDIR /app
# COPY . /app
# RUN pip install flask
# RUN pip install flask_restful
# EXPOSE 3000
# CMD python ./app.py

From ubuntu

RUN apt update
RUN apt install python3-pip -y
RUN pip3 install Flask flask_restful

WORKDIR /app

COPY . .

# EXPOSE 3000

# CMD python ./app.py
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]