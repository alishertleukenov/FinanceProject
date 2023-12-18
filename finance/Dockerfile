FROM python:3.12.0

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /app

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY finance /app/

CMD ["venv\\Scripts\\activate"]
CMD ["venv\\Scripts\\python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]