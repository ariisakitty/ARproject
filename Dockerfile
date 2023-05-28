FROM python:3.9-slim

WORKDIR /app

COPY app.py /app/
COPY templates/ /app/templates/
COPY static/ /app/static/
COPY requirements.txt /app/

# Install gcc and python3-dev
RUN apt-get update \
    && apt-get install -y gcc python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
