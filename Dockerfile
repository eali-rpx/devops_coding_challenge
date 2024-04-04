FROM public.ecr.aws/docker/library/python:3.12-slim
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.1 /lambda-adapter /opt/extensions/lambda-adapter
ENV PORT=8080
WORKDIR /var/task
COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt
COPY *.py ./
CMD exec uvicorn --port=$PORT main:app