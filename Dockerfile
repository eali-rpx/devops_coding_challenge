FROM public.ecr.aws/lambda/python:3.12

WORKDIR ${LAMBDA_TASK_ROOT}
COPY . .
RUN pip install -r requirements.txt
CMD ["app.handler"]