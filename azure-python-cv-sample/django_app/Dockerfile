FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
ENV DJANGO_SETTINGS_MODULE=django_project.settings
EXPOSE 8000
CMD ["gunicorn", "django_project.wsgi:application", "-b", "0.0.0.0:8000"]
