# Dockerfile

# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Flask application files to the container
COPY . /app

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Optimize Static Files with Flask-Assets
RUN pip install Flask-Assets
RUN flask assets build

# Install Nginx
RUN apt-get update && apt-get install -y nginx

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80 for Nginx
EXPOSE 80

# Start Nginx and the Flask app
CMD service nginx start && gunicorn -b 0.0.0.0:5000 data_processing_script:app
