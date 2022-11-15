FROM python:3.9.13
EXPOSE 8501
CMD mkdir -p/app
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
RUN pip install -U pip setuptools wheel
COPY . .
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]