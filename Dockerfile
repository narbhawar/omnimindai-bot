FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
ENV PORT=10000
EXPOSE 10000
CMD ["python", "main.py"]
