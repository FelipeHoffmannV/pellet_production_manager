FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /pellet_production_manager

COPY requirements.txt /pellet_production_manager/

RUN apt-get update && apt-get install -y libpq-dev gcc

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
