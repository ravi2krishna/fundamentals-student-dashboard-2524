# A Dockerfile is a text file containing instructions that 
# Docker uses to build a Docker image.
# Docker Build
FROM python:3.11-slim  
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8085
CMD ["python","app.py"]