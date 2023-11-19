# Container image that runs your code
FROM python:3.10-alpine

# Copies your code file from your action repository to the filesystem path `/` of the container
# COPY entrypoint.sh /entrypoint.sh

# COPY . .
COPY action_cli.py /action_cli.py
COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN ls -a


# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["python", "action_cli.py"]
