# Voting Application - Deployment Guide

## Prerequisites

- AWS EC2 Ubuntu
- Docker and Git
- KIND and kubectl
- Jenkins
- Argo CD
- Nginx

## Clone Repository

    git clone https://github.com/ajaydhadi95-gif/voting-app-gitops.git
    cd voting-app-gitops

## Kubernetes Deployment

Argo CD watches this GitOps directory:

    voting-app-gitops/kubernetes/

The directory contains:

- deployment.yaml
- service.yaml
- pvc.yaml

## Verify Kubernetes Resources

    kubectl get nodes
    kubectl get pods -n voting-app
    kubectl get svc -n voting-app
    kubectl get pvc -n voting-app

## Argo CD Verification

    kubectl get pods -n argocd
    kubectl get applications -n argocd

## Nginx Configuration

Nginx configuration is stored at:

    infrastructure/nginx/voting-platform.conf

The live server configuration is installed at:

    /etc/nginx/sites-available/voting-platform

Validate and reload Nginx:

    sudo nginx -t
    sudo systemctl reload nginx

## Public Access

- Voting Application: https://3.109.210.192
- Argo CD Dashboard: https://3.109.210.192:8443

AWS Security Group must allow inbound TCP ports 80, 443 and 8443.
Keep SSH restricted to trusted IP addresses.

## SSL Security

The current setup uses a self-signed certificate.
Create the certificate and private key on the server.
Never commit SSL private keys, credentials, or tokens to GitHub.

## Important

Adapt EC2 IP, KIND node IP, certificate paths and cluster configuration
when deploying in another environment.
