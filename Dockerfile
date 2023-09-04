# Use an official Python image as the base
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install application dependencies
RUN pip install -r requirements.txt

# Change owner and group for the working directory
RUN chown -R 1000:1000 /app

# Switch to a non-root user
USER 1000:1000

# Set environment variables
ENV FLASK_APP=data_processing_script.py

# Run the application using Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=443", "--cert=adhoc"]
