FROM python:3.7.9 

WORKDIR /app 

COPY requirments.txt requirments.txt
RUN pip3 install -r requirments.txt 

COPY . .

CMD []