FROM public.ecr.aws/docker/library/python:3.12.1-slim
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.1 /lambda-adapter /opt/extensions/lambda-adapter

COPY app.py requirements.txt ./
COPY . .
RUN python3 -m pip install --no-cache-dir -r requirements.txt
# CMD ["gunicorn", "-b=:8080", "-w=1", "app:app", "app.lambda_handler"]
CMD ["app.lambda_handler"]