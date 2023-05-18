FROM python:3.9.2

WORKDIR /app/

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app/

CMD ["python3", "main.py"]