FROM python:3.10
RUN pip3 install Flask flask-mysqldb redis
VOLUME ["/app"]
EXPOSE "80"
WORKDIR /app
CMD ["python3", "app.py"]