FROM public.ecr.aws/docker/library/python:3.12.1-slim

COPY . ${LAMBDA_TASK_ROOT}
COPY requirements.txt .
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}" -U --no-cache-dir

CMD ["app.handler"]