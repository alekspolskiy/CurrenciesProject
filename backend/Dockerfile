FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY . /app
EXPOSE 8000
ENV PYTHONPATH=/app
