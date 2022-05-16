# This file defines the Docker container that will contain the Flask app.

# From the source image
FROM python:3.6-slim

# Identify maintainer
LABEL maintainer = "calbon@wikimedia.org"

# Set the default working directory
WORKDIR /app/

# Copy requirements.txt outside the container
# to /app/ inside the container
COPY requirements.txt train.py/app/

# Install required packages
RUN pip install -r ./requirements.txt

# Copy app.py and__init__.py outside the container
# to /app/ inside the container
COPY app.py __init__.py /app/

# Train the  model.pkl inside the container
# to /app/ inside the container
RUN python train.py

# Expose the container's port 3333
EXPOSE 3333

# When the container starts, run this
ENTRYPOINT python ./app.py