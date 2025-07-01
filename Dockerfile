# Use a lightweight Python base image
FROM python:3.10.6-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file and install dependencies
COPY requirements.txt ./

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    python3-dev \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get remove -y --purge build-essential gcc python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the rest of the application files
COPY . .

# Use exec form to ensure proper signal handling
CMD ["bash", "start"]
