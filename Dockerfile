FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

EXPOSE 3111

ENV DEBUG=true

CMD ["python", "app.py"]