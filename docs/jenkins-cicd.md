# Jenkins CI/CD Pipeline

## Overview

Jenkins automates the build, validation, and container image publishing
process for the Python Voting Application.

## Pipeline Stages

### 1. Checkout
Jenkins checks out application source code from GitHub.

### 2. Install Dependencies
Creates a Python virtual environment and installs packages
from requirements.txt.

### 3. Test
Runs Python syntax validation.

### 4. Build Docker Image
Builds the application image using the Dockerfile.

Image format:

    ajaydhadi95/voting-app:<BUILD_NUMBER>

### 5. Push Docker Image
Authenticates with Docker Hub using Jenkins credentials
and pushes the versioned image.

### 6. Update GitOps Repository
Jenkins clones the GitOps repository and updates:

    voting-app-gitops/kubernetes/deployment.yaml

It commits and pushes the updated image tag to the main branch.

## Argo CD Integration

Argo CD monitors the GitOps repository.

When Jenkins pushes a new image tag, Argo CD detects the manifest change
and synchronizes the Kubernetes deployment.

Jenkins does not directly deploy using kubectl.

## Jenkins Credentials

Configure these credentials in Jenkins:

- dockerhub-credentials
- github-gitops-credentials

Never store passwords or access tokens directly in the Jenkinsfile
or commit them to GitHub.

## Pipeline Flow

GitHub -> Jenkins -> Python Validation -> Docker Build
-> Docker Hub Push -> GitOps Manifest Update
-> Argo CD Sync -> Kubernetes Deployment

## Verification

Check the Jenkins build console output and verify:

- Docker image was pushed successfully.
- GitOps manifest contains the new image tag.
- Argo CD Application is Synced and Healthy.
- Voting Application pod is Running.
