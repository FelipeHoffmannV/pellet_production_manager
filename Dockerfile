FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /pellet_production_manager

COPY requirements.txt /pellet_production_manager/

# ... (previous lines)

# Install system dependencies for PostgreSQL and PyCairo
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    pkg-config \
    libcairo2-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# ... (rest of the file)


COPY . .

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
