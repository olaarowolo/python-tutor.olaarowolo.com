# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python code into the container
COPY . .

# Expose the port that the application will run on
EXPOSE 8000

# Set the command to run the application
CMD ["python", "app.py"]