FROM python:3-slim
WORKDIR /programas/api-usuario

RUN pip3 install flask
RUN pip3 install flask-mysql
RUN pip3 install Flask-RESTful
RUN pip3 install Flask-Cors 
COPY . .
CMD [ "python3", "./app.py" ]
