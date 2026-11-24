# Voting Application - DevOps Architecture

## Project Overview

A Python Flask Voting Application deployed on Kubernetes using Jenkins CI,
Docker Hub, GitHub, and Argo CD GitOps.

## Architecture Flow

1. Developer pushes application code to GitHub.
2. Jenkins detects the code change.
3. Jenkins checks out the source code.
4. Jenkins installs dependencies and runs validation.
5. Jenkins builds a Docker image.
6. Jenkins pushes the image to Docker Hub.
7. Jenkins updates the image tag in the GitOps Kubernetes manifest.
8. Jenkins commits and pushes the updated manifest to GitHub.
9. Argo CD monitors the GitOps repository.
10. Argo CD synchronizes Kubernetes manifests to the KIND cluster.
11. Kubernetes runs the Voting Application pod.

## Technology Stack

- Python and Flask
- Jenkins
- Git and GitHub
- Docker
- Docker Hub
- Kubernetes
- KIND
- Argo CD
- GitOps
- Nginx
- AWS EC2

## Application Access

- Voting Application: https://3.109.210.192
- Argo CD Dashboard: https://3.109.210.192:8443

The HTTPS endpoints currently use a self-signed certificate.
A browser security warning is expected.

## Traffic Flow

### Voting Application

Internet -> AWS EC2 -> Nginx HTTPS 443 -> Kubernetes NodePort 30080 -> Voting App Service -> Flask Pod

### Argo CD Dashboard

Internet -> AWS EC2 -> Nginx HTTPS 8443 -> Kubernetes NodePort 30443 -> Argo CD Server

## GitOps

Jenkins updates the Kubernetes image tag in GitHub.
Argo CD watches the GitOps directory and reconciles the cluster
with the desired state stored in Git.

Jenkins does not directly deploy the application using kubectl.

## Important Notes

- Kubernetes NodePorts are accessed through the EC2 host's KIND Docker network.
- SSL private keys and credentials must never be committed to GitHub.
- SQLite persistent storage is used for the demo application.
