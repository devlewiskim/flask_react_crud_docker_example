FROM python:3.6-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install -e .

EXPOSE 5000

CMD ["python", "run.py", "runserver", "--host=0.0.0.0"]