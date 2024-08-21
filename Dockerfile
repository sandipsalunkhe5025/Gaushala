# Use the official Python 3.11 image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /code

# Install system dependencies
RUN apt-get update \
    && apt-get install -y \
        pkg-config \
        python3.11-dev \
        default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /code/

# Expose port if needed
 EXPOSE 8000

# Command to run the application
 CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
