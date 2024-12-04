# Log Output Application

## Description
This project generates a random string on application startup and logs it with timestamps every 5 seconds. The application is containerized using Docker and deployed to Kubernetes.

## Files
- `app.py`: Python application script.
- `Dockerfile`: Instructions to build the Docker image.
- `manifests/deployment.yaml`: Kubernetes deployment file.

## How to Run
1. **Build Docker Image**:
   ```bash
   docker build -t log-output:v1 .