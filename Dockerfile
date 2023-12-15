FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN useradd -m -r -u 101 user

COPY requirements.txt /app/

RUN apt-get update \
    && apt-get install -y gcc python3-dev \
    && apt-get install -y postgresql postgresql-contrib libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN chown -R user:user /app && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "tracker_app.wsgi:application", "--bind", "0:8000"]
