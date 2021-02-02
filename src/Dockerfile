# start from base
FROM ubuntu:18.04

LABEL maintainer="Abhilash"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

RUN useradd -ms /bin/bash admin

COPY ./Calculation_Core/* /app/
COPY ./* /app/
COPY . /app
RUN chown -R admin:admin /app
RUN chmod 755 /app
RUN chmod 755 /app/Calculation_Core
USER admin
ENV export FLASK_ENV=production
RUN export FLASK_APP=Python.py

# We copy just the requirements.txt first to leverage Docker cache
WORKDIR /app


EXPOSE 5000

#ENTRYPOINT [ "flask" ]
CMD ["export", "FLASK_APP=Python.py"]

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
