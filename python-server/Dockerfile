# Python FastAPI Server Dockerfile
# This container runs the FastAPI application with Uvicorn server
# and supports hot-reloading for development

# Use the official Python base image (slim variant for smaller size)
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
# This is done before copying source code to leverage Docker layer caching
COPY requirements.txt /app

# Install the dependencies
# --no-cache-dir reduces image size by not storing pip cache
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the server will run
# This documents that the container listens on port 8000
EXPOSE 8000

# Set the command to run the server with Uvicorn
# --reload: Enable auto-reloading on code changes (development mode)
# --host 0.0.0.0: Listen on all network interfaces
# --port 8000: Listen on port 8000
CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]