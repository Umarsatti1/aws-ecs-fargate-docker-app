# Use an official Python runtime as a parent image
FROM python:3.12.6-alpine3.19

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Django in the container
RUN pip install django

# Expose port 8000 to be accessible from outside the container
EXPOSE 8000

# Run the application
CMD ["python", "app.py"]
