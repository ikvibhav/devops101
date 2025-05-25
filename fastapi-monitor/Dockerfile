# Uses the official Python 3.11 slim image as the base for the container
# slim images are smaller, have faster builds and fewer vulnerabilities
FROM python:3.11-slim

# Sets the working directory in the container to /app
# All subsequent commands will be run from this directory
WORKDIR /app

# Copies everything from local app directory to the /app directory in the container
COPY app/ .

# Ensures that postgres backend starts only after the database db is ready
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Installs python dependencies from requirements.txt using pip
# --no-cache-dir option is used to avoid caching the installed packages 
# which helps to keep the image size smaller
RUN pip install --no-cache-dir -r requirements.txt

# Runs the FastAPI application using uvicorn
# On the specified host and port 8000 with auto-reload enabled
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]