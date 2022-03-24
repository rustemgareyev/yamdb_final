FROM python:3.7-slim

WORKDIR /app

COPY api_yamdb/requirements.txt /app

RUN pip install --upgrade pip

RUN pip install -r /app/requirements.txt --no-cache-dir

COPY ./ /app

CMD ["sudo", "gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ] 