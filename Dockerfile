#
# Tutorial: How To Containerize Your Python Application using Docker
# url: https://www.youtube.com/watch?v=gHaFqYRJ_aw
#

FROM python:3

# Create a work directory for the app inside the container
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Run the application
CMD [ "python", "./api.py" ]

# FROM 3.10.0a1-buster

# Create a work directory for the app inside the container
# WORKDIR /app
# RUN pip install -r requirements.txt

# Install dependencies
# COPY requirements.txt .

# Copy source code
# COPY . /app

# Run the application
# CMD ["python", "api.py"]