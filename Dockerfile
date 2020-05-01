FROM tiangolo/uwsgi-nginx-flask:python3.7
COPY ./ /app
WORKDIR /app
ENV APP_SETTINGS=/app/config/DOCKERCONFIG.py
RUN pip install -r requirements.txt
