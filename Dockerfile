FROM public.ecr.aws/lambda/python:3.11
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.1 /lambda-adapter /opt/extensions/lambda-adapter

COPY requirements.txt .
COPY . .
RUN python3 -m pip install --no-cache-dir -r requirements.txt
# CMD ["gunicorn", "-b=:8080", "-w=1", "app:app", "app.handler"]
CMD ["app.handler"]