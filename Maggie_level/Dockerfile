FROM python:3.9
RUN mkdir /app
WORKDIR /app

COPY Maggie_level.py /app 
COPY Requirements.txt /app 

RUN pip install -r Requirements.txt

RUN mkdir /app/General
RUN mkdir /app/Lisa
RUN mkdir /app/Homer

EXPOSE 80

CMD [ "python3","Maggie_level.py" ]
