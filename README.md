# VoteX - Python Voting Application

A Python Flask-based voting application deployed on Kubernetes using
Jenkins CI/CD and Argo CD GitOps.

## Technology Stack

- Python and Flask
- HTML, CSS and JavaScript
- SQLite
- Git and GitHub
- Jenkins
- Docker and Docker Hub
- Kubernetes and KIND
- Argo CD
- Nginx
- AWS EC2

## Features

- Modern 3D glassmorphism UI
- Python and Java voting options
- Live voting results
- SQLite persistent storage
- Application health endpoint
- Docker containerization
- Kubernetes Deployment, Service and PVC
- Automated CI/CD pipeline
- GitOps-based continuous deployment
- HTTPS access through Nginx reverse proxy

## Project Structure

    .
    ├── app.py
    ├── requirements.txt
    ├── Dockerfile
    ├── Jenkinsfile
    ├── README.md
    ├── templates/
    ├── static/
    ├── data/
    ├── k8s/
    ├── voting-app-gitops/
    │   └── kubernetes/
    │       ├── deployment.yaml
    │       ├── service.yaml
    │       └── pvc.yaml
    ├── argocd/
    ├── infrastructure/
    │   └── nginx/
    └── docs/

## CI/CD Architecture

1. Developer pushes application code to GitHub.
2. Jenkins checks out the source code.
3. Jenkins installs Python dependencies.
4. Jenkins validates the Python application.
5. Jenkins builds a Docker image.
6. Jenkins pushes the image to Docker Hub.
7. Jenkins updates the image tag in the GitOps manifest.
8. Jenkins pushes the updated manifest to GitHub.
9. Argo CD detects the GitOps repository change.
10. Argo CD synchronizes Kubernetes resources.
11. Kubernetes deploys the updated application.

## Docker Image

    ajaydhadi95/voting-app:<BUILD_NUMBER>

Jenkins generates versioned image tags using the build number.

## Kubernetes Deployment

Argo CD uses this GitOps directory:

    voting-app-gitops/kubernetes/

Resources:

- Deployment
- NodePort Service
- PersistentVolumeClaim

Check deployment:

    kubectl get pods -n voting-app
    kubectl get svc -n voting-app
    kubectl get pvc -n voting-app

## Argo CD

Argo CD Application configuration:

    argocd/application.yaml

Check application:

    kubectl get applications -n argocd

## Nginx Reverse Proxy

Configuration:

    infrastructure/nginx/voting-platform.conf

Traffic routing:

- HTTPS 443 -> Voting Application
- HTTPS 8443 -> Argo CD Dashboard
- HTTP 80 -> HTTPS redirect

## Application URLs

- Voting Application: https://3.109.210.192
- Argo CD Dashboard: https://3.109.210.192:8443

The current setup uses a self-signed SSL certificate.
Your browser may display a certificate warning.

## Documentation

- docs/architecture.md
- docs/deployment-guide.md
- docs/jenkins-cicd.md

## Security

- Store Docker Hub and GitHub credentials in Jenkins Credentials.
- Never commit passwords, access tokens, or SSL private keys.
- Use a trusted SSL certificate for production.
- Restrict SSH access through AWS Security Groups.

## GitOps Deployment

Jenkins updates the desired image version in Git.
Argo CD reconciles the Kubernetes cluster with the GitOps repository.

Jenkins does not directly deploy the application using kubectl.
