FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt .
COPY *.py .
COPY . .
RUN python3 -m pip install --no-cache-dir -r requirements.txt
# CMD ["gunicorn", "-b=:8080", "-w=1", "app:app", "app.lambda_handler"]
CMD ["app.handler"]