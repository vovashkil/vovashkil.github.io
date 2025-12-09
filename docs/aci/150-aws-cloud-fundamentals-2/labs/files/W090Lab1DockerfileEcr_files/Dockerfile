FROM python:3.11-alpine

COPY url_checker.py requirements.txt /app/
WORKDIR /app
RUN pip install -r /app/requirements.txt

ENTRYPOINT ["python","url_checker.py"]
