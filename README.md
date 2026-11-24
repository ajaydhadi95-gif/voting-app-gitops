
# VoteX - Python Voting Application

A modern 3D voting application built using Python Flask,
HTML, CSS, JavaScript and SQLite.

## Technology Stack

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- SQLite
- Docker
- Kubernetes

## Features

- 3D glassmorphism UI
- Python and Java voting
- Live voting results
- SQLite database persistence
- Docker containerization
- Kubernetes deployment
- Health check endpoint

## Run Locally

Install dependencies:

pip install -r requirements.txt

Start application:

python app.py

Open browser:

http://127.0.0.1:5000

## Docker Build

docker build -t ajaydhadi95/voting-app:v1 .

## Docker Run

docker run -d \
  --name voting-app \
  -p 5000:5000 \
  -v voting-data:/data \
  ajaydhadi95/voting-app:v1

## Push Docker Image

docker login

docker push ajaydhadi95/voting-app:v1

## Kubernetes Deployment

kubectl apply -f k8s/pvc.yaml

kubectl apply -f k8s/deployment.yaml

kubectl apply -f k8s/service.yaml

## Check Resources

kubectl get pods

kubectl get svc

kubectl get pvc
