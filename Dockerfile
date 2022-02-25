FROM python:3.9
ENV PYTHONPATH=/app/
COPY requirements.txt /requirements/requirements.txt
RUN pip install -r /requirements/requirements.txt && rm -r /requirements
COPY rick_and_morty /app
WORKDIR /app
CMD ["python", "main.py"]