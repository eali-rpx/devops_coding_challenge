FROM public.ecr.aws/docker/library/python:3.12.1-slim
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.1 /lambda-adapter /opt/extensions/lambda-adapter
WORKDIR /
COPY requirements.txt requirements.txt
COPY data/ .
COPY *.py . 
RUN python3 -m pip install -r requirements.txt
CMD ["app.handler"]