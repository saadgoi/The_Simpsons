FROM python:3.9

RUN mkdir /app
WORKDIR  /app

COPY Lisa_level.py /app/
COPY Requirements.txt /app/

RUN pip3 install -r Requirements.txt

EXPOSE 80

CMD [ "python3","Lisa_level.py"]


