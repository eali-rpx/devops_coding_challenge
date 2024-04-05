# Use the official Python image
FROM public.ecr.aws/docker/library/python:3.12-slim

COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.1 /lambda-adapter /opt/extensions/lambda-adapter

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install Flask and other dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# # Define environment variable
# ENV FLASK_APP=app.py

# Command to run the Flask application
# CMD ["flask", "run", "--host=0.0.0.0"]
# CMD ["app.handler"]
CMD ["gunicorn", "-b=:8080", "-w=1", "app:app"]