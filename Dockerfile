# Use a lightweight Python base image
FROM python:3.10.6-slim

# Set environment variables to reduce warnings
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Update and install dependencies efficiently
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends bash && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy only requirements first to leverage Docker caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Use exec form to ensure proper signal handling
CMD ["bash", "start"]
