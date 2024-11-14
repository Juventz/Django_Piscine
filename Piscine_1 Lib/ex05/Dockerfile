FROM python:3.11.2-slim

WORKDIR /app

COPY ./requirement.txt .

RUN pip install --upgrade pip
RUN pip install -r requirement.txt

COPY ./my_project .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]