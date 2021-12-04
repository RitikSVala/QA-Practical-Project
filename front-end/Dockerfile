FROM python:latest
WORKDIR /front-end
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["python3", "run.py"]