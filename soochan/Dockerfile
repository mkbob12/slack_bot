FROM python:3.11.0-slim

ENV PYTHONUNBUFFERED=1
ENV DB_PASSWORD='password'
ENV LOG_LVL='debug'

RUN mkdir -p /opt/bbot
RUN mkdir -p /opt/bbot/conf

COPY ./*.py /opt/bbot/
COPY ./*.sh /opt/bbot/
COPY ./requirements.txt /opt/bbot/
WORKDIR /opt/bbot

EXPOSE 8080

RUN pip3 --trusted-host pypi.org --trusted-host files.pythonhosted.org install --upgrade pip
RUN pip3 --trusted-host pypi.org --trusted-host files.pythonhosted.org install -r requirements.txt

RUN apt-get update && apt-get install -y dos2unix
RUN dos2unix /opt/bbot/start.sh && chmod +x /opt/bbot/start.sh

RUN chmod +x /opt/bbot/start.sh

CMD ["bash", "-c", "/opt/bbot/start.sh"]