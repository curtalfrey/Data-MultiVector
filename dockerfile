# Dockerfile

# This Dockerfile defines the Docker image for running the data_processing_script.py Flask application.
# It includes instructions, environment setup, and prerequisites.

# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=data_processing_script.py

# Instructions, Requirements, and Prerequisites
#
# Instructions:
# 1. Build the Docker image: docker build -t data_processing_image .
# 2. Run the Docker container: docker run -p 5000:5000 -it data_processing_image
#
# Requirements:
# - Python 3.x
# - Flask
# - watchdog
#
# Prerequisites:
# - Install required Python packages: pip install Flask watchdog
#
# Documentation:
# To access documentation, open a web browser and navigate to http://localhost:5000/documentation

# Run the Flask application when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]

