FROM quay.io/astronomer/astro-runtime:12.6.0
RUN pip install -r requirements.txt

COPY .env /usr/local/airflow/.env
