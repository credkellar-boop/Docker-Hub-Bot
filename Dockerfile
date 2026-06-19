FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install Git and Docker CLI for Asset and Security modules
RUN apt-get update && apt-get install -y git docker.io && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot source code
COPY main.py .

# Execute the Brain
CMD ["python", "main.py"]
