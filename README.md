# 🗳️ VoteX – Automated Voting Application on Kubernetes

### End-to-End DevOps Project | Jenkins | Docker | Kubernetes | Argo CD | GitOps | Nginx | AWS EC2

![Project](https://img.shields.io/badge/Project-VoteX-blue)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey)
![Docker](https://img.shields.io/badge/Container-Docker-blue)
![Kubernetes](https://img.shields.io/badge/Orchestration-Kubernetes-326CE5)
![Jenkins](https://img.shields.io/badge/CI%2FCD-Jenkins-D24939)
![ArgoCD](https://img.shields.io/badge/GitOps-ArgoCD-orange)
![Nginx](https://img.shields.io/badge/Proxy-Nginx-green)

---

# 1. Project Overview

**VoteX** is a Python Flask-based voting application designed and deployed using an end-to-end DevOps and GitOps workflow.

The project demonstrates how a developer's application code can move through a complete CI/CD pipeline, from source code management to container image creation and automated Kubernetes deployment.

The application is containerized using Docker, built and tested through Jenkins, stored in Docker Hub, and deployed to a Kubernetes cluster using Argo CD.

Nginx is configured as a reverse proxy to provide external access to the application and Argo CD dashboard over HTTPS.

The infrastructure runs on separate AWS EC2 instances to demonstrate a multi-server DevOps environment.

### Main objectives

- Develop and containerize a Python voting application.
- Implement Continuous Integration using Jenkins.
- Automate Docker image creation and publishing.
- Implement GitOps-based deployment using Argo CD.
- Deploy the application on Kubernetes using KIND.
- Configure Kubernetes Deployments, Services and PersistentVolumeClaims.
- Configure Nginx as a reverse proxy.
- Enable HTTPS using an SSL certificate.
- Maintain application, infrastructure and deployment configurations in GitHub.
- Demonstrate practical Linux, AWS, Docker, Jenkins and Kubernetes troubleshooting.

---

# 2. Project Architecture

## High-Level Architecture

```text
                  DEVELOPER
                      |
                      |
                Push Application Code
                      |
                      v
              GITHUB SOURCE REPO
                      |
                      |
                      v
                JENKINS SERVER
                AWS EC2 INSTANCE
                      |
             +--------+--------+
             |                 |
             v                 v
       Install Python       Run Tests
       Dependencies         and Checks
             |                 |
             +--------+--------+
                      |
                      v
                DOCKER BUILD
                      |
                      v
                DOCKER IMAGE
                      |
                      v
                DOCKER HUB
                      |
                      |
                      v
              GITOPS REPOSITORY
                      |
              Update Image Tag
                      |
                      v
                  ARGO CD
                      |
                Detect Changes
                      |
                 Auto Sync
                      |
                      v
              KIND KUBERNETES
                AWS EC2 INSTANCE
                      |
                      v
                VOTING APP POD
                      |
                      v
              KUBERNETES SERVICE
                      |
                      v
                   NODEPORT
                      |
                      v
                    NGINX
                      |
                HTTPS ACCESS
                      |
                      v
              PUBLIC APPLICATION
```

## Infrastructure Architecture

The project uses two separate AWS EC2 instances.

| Server | Private IP | Responsibilities |
|---|---|---|
| Jenkins EC2 | 172.31.5.84 | Jenkins CI/CD, Docker build and image publishing |
| Kubernetes EC2 | 172.31.0.91 | KIND cluster, Argo CD, Kubernetes and Nginx |

### Jenkins EC2

The Jenkins server handles the Continuous Integration and image delivery process.

Responsibilities:

- GitHub source code checkout.
- Python dependency installation.
- Application validation.
- Docker image building.
- Docker Hub authentication.
- Docker image publishing.
- GitOps repository update.

### Kubernetes / Argo CD EC2

This server hosts the application deployment environment.

Responsibilities:

- KIND Kubernetes cluster management.
- Argo CD installation and configuration.
- Kubernetes application deployment.
- Persistent storage management.
- NodePort service exposure.
- Nginx reverse proxy.
- HTTPS access through SSL.

---

# 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Application programming language |
| Flask | Backend web framework |
| HTML | Application structure |
| CSS | Application styling |
| JavaScript | Frontend interactions |
| SQLite | Voting data storage |
| Git | Version control |
| GitHub | Source code and GitOps repository |
| Jenkins | CI/CD automation |
| Docker | Application containerization |
| Docker Hub | Container image registry |
| Kubernetes | Container orchestration |
| KIND | Kubernetes cluster |
| Argo CD | GitOps continuous delivery |
| Nginx | Reverse proxy and HTTPS termination |
| OpenSSL | Self-signed SSL certificate generation |
| Ubuntu | Server operating system |
| AWS EC2 | Cloud infrastructure |

---

# 4. Application Architecture

The application is developed using Python Flask.

### Backend – app.py

The backend manages application routes, voting operations, database connectivity and health checks.

Important endpoints:

| Endpoint | Method | Purpose |
|---|---|---|
| `/` | GET | Display voting application |
| `/api/vote` | POST | Submit a vote |
| `/api/results` | GET | Retrieve voting results |
| `/health` | GET | Application health check |

### Frontend

The frontend contains:

- `templates/index.html` – voting interface.
- `static/css/style.css` – application styling.
- `static/js/script.js` – frontend interactions.

### Database

SQLite is used to store voting information.

Database configuration:

```text
DB_PATH=/data/votes.db
```

The database is stored in persistent application storage mounted inside the Kubernetes container.

**Important:** This SQLite setup is intended for this demonstration deployment with one application replica. A production multi-replica system should use a shared database service such as PostgreSQL or Amazon RDS.

---

# 5. GitHub Repository Structure

The project repository contains application code, Kubernetes manifests, Jenkins pipeline, Argo CD configuration, infrastructure configuration and documentation.

```text
voting-app-gitops/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── README.md
├── .dockerignore
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── data/
│   └── votes.db
│
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── pvc.yaml
│
├── voting-app-gitops/
│   └── kubernetes/
│       ├── deployment.yaml
│       ├── service.yaml
│       └── pvc.yaml
│
├── argocd/
│   ├── application.yaml
│   └── argocd-server-nodeport.yaml
│
├── infrastructure/
│   └── nginx/
│       └── voting-platform.conf
│
└── docs/
    ├── architecture.md
    ├── deployment-guide.md
    └── jenkins-cicd.md
```

### Important repository paths

| Path | Responsibility |
|---|---|
| `Jenkinsfile` | Defines the CI/CD pipeline |
| `Dockerfile` | Defines the application container |
| `k8s/` | Additional Kubernetes manifests |
| `voting-app-gitops/kubernetes/` | Kubernetes manifests watched by Argo CD |
| `argocd/` | Argo CD application and service configuration |
| `infrastructure/nginx/` | Nginx reverse proxy configuration |
| `docs/` | Project documentation |

**Important:** Argo CD watches `voting-app-gitops/kubernetes/`. The root `k8s/` directory is not the configured Argo CD source path.

---

# 6. CI/CD Pipeline Using Jenkins

Jenkins is responsible for automating the Continuous Integration and image delivery process.

The pipeline is defined in the `Jenkinsfile`.

## Pipeline Workflow

### Stage 1 – Checkout

Jenkins checks out the application source code from GitHub.

```groovy
stage('Checkout') {
    steps {
        checkout scm
    }
}
```

Purpose:

- Retrieve the latest application code.
- Access the Jenkinsfile.
- Prepare the Jenkins workspace.

### Stage 2 – Install Dependencies

Jenkins creates a Python virtual environment and installs the application dependencies.

```bash
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Dependencies:

```text
Flask==3.1.0
gunicorn==23.0.0
```

Purpose:

- Isolate Python dependencies.
- Install the required application packages.
- Prepare the environment for validation.

### Stage 3 – Test Application

The pipeline validates Python syntax.

```bash
. venv/bin/activate
python -m py_compile app.py
```

Purpose:

- Identify Python syntax errors.
- Prevent an invalid application file from reaching the Docker build stage.

This is a basic syntax validation, not a complete unit or integration test suite.

### Stage 4 – Build Docker Image

Jenkins builds the application image using the Dockerfile.

```groovy
docker.build("${DOCKER_IMAGE}:${BUILD_NUMBER}")
```

Image naming:

```text
ajaydhadi95/voting-app:<BUILD_NUMBER>
```

Example:

```text
ajaydhadi95/voting-app:10
```

Purpose:

- Package the application and its dependencies.
- Create a versioned Docker image.
- Maintain build-specific image tags.

### Stage 5 – Push Docker Image

Jenkins authenticates to Docker Hub using Jenkins Credentials Manager.

```groovy
docker.withRegistry(
    'https://index.docker.io/v1/',
    DOCKER_CREDENTIALS
) {
    docker.image(
        "${DOCKER_IMAGE}:${BUILD_NUMBER}"
    ).push()
}
```

Docker Hub repository:

https://hub.docker.com/r/ajaydhadi95/voting-app

Purpose:

- Authenticate securely.
- Upload the Docker image.
- Make the image available to Kubernetes.

### Stage 6 – Update GitOps Repository

After successfully publishing the image, Jenkins clones the GitOps repository.

It updates the image tag in:

```text
voting-app-gitops/kubernetes/deployment.yaml
```

Example:

Before:

```yaml
image: ajaydhadi95/voting-app:10
```

After a new Jenkins build:

```yaml
image: ajaydhadi95/voting-app:11
```

Jenkins commits and pushes the updated manifest to GitHub.

Purpose:

- Maintain the desired Kubernetes state in Git.
- Track deployed image versions.
- Trigger Argo CD reconciliation.

### Jenkins Credentials

The pipeline uses the following Jenkins credential IDs:

| Credential ID | Purpose |
|---|---|
| `dockerhub-credentials` | Docker Hub authentication |
| `github-gitops-credentials` | GitHub GitOps repository access |

Credentials are stored in Jenkins and should never be hardcoded into the source code.

---

# 7. Docker Containerization

Docker packages the Python application into a portable container image.

### Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DB_PATH=/data/votes.db

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /data

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "1", "--access-logfile", "-", "--error-logfile", "-", "app:app"]
```

### Docker configuration

| Setting | Value |
|---|---|
| Base Image | python:3.12-slim |
| Working Directory | /app |
| Application Port | 5000 |
| Application Server | Gunicorn |
| Database Location | /data/votes.db |

### Local Docker commands

Build image:

```bash
docker build -t ajaydhadi95/voting-app:latest .
```

Run container:

```bash
docker run -d \
  -p 5000:5000 \
  ajaydhadi95/voting-app:latest
```

Check running containers:

```bash
docker ps
```

Test application:

```bash
curl http://localhost:5000/health
```

---

# 8. Kubernetes Deployment

The application runs inside a KIND Kubernetes cluster.

Cluster name:

```text
voting-cluster
```

The cluster contains:

- One control-plane node.
- One worker node.

### Kubernetes Namespace

The application is deployed in:

```text
voting-app
```

### Deployment

The Deployment manages the application Pod.

Responsibilities:

- Maintain the desired replica count.
- Create and manage Pods.
- Pull the Docker image.
- Restart unhealthy containers.
- Perform readiness and liveness checks.

Important configuration:

```yaml
replicas: 1
```

Container port:

```yaml
containerPort: 5000
```

Health checks:

```yaml
readinessProbe:
  httpGet:
    path: /health
    port: 5000

livenessProbe:
  httpGet:
    path: /health
    port: 5000
```

Resource requests and limits are also configured to control application resource consumption.

### Service

The Kubernetes Service exposes the application.

```text
Service Name: voting-app-service
Service Type: NodePort
Service Port: 5000
NodePort: 30080
```

Traffic flow:

```text
Client
  |
  v
Nginx
  |
  v
Kubernetes NodePort
  |
  v
Service
  |
  v
Voting App Pod
```

### PersistentVolumeClaim

A PersistentVolumeClaim provides storage for the SQLite database.

Configuration:

```text
PVC Name: voting-app-pvc
Storage: 1Gi
Access Mode: ReadWriteOnce
Mount Path: /data
```

Purpose:

- Keep database files outside the container's writable filesystem.
- Preserve database storage across ordinary Pod replacement, subject to the underlying storage lifecycle.

### Kubernetes verification commands

Check nodes:

```bash
kubectl get nodes
```

Check application Pods:

```bash
kubectl get pods -n voting-app
```

Check Services:

```bash
kubectl get svc -n voting-app
```

Check storage:

```bash
kubectl get pvc -n voting-app
```

Check deployment:

```bash
kubectl get deployment -n voting-app
```

View logs:

```bash
kubectl logs deployment/voting-app -n voting-app
```

---

# 9. GitOps Deployment Using Argo CD

Argo CD is used to implement the GitOps deployment model.

Instead of Jenkins directly deploying the application using `kubectl`, Jenkins updates the Kubernetes manifests stored in GitHub.

Argo CD monitors the repository and reconciles the live Kubernetes environment with the desired configuration in Git.

### Argo CD Application Configuration

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application

metadata:
  name: voting-app
  namespace: argocd

spec:
  project: default

  source:
    repoURL: https://github.com/ajaydhadi95-gif/voting-app-gitops.git
    targetRevision: main
    path: voting-app-gitops/kubernetes

  destination:
    server: https://kubernetes.default.svc
    namespace: voting-app

  syncPolicy:
    automated:
      prune: true
      selfHeal: true

    syncOptions:
      - CreateNamespace=true
```

### GitOps Workflow

1. Developer pushes application changes to GitHub.
2. Jenkins builds and validates the application.
3. Jenkins creates a new Docker image.
4. Jenkins pushes the image to Docker Hub.
5. Jenkins updates the Kubernetes image tag in GitOps.
6. Argo CD detects the Git repository change.
7. Argo CD synchronizes the Kubernetes manifests.
8. Kubernetes updates the application Deployment.
9. The new application version becomes available.

### Automated Sync

**Automated Sync:** Argo CD applies changes from Git without requiring a manual sync operation.

**Self Heal:** Argo CD attempts to restore the cluster to the desired Git configuration when live configuration drifts.

**Prune:** Resources removed from the tracked Git configuration can be deleted during synchronization.

**CreateNamespace:** Creates the destination namespace if it does not already exist.

### Verify Argo CD

```bash
kubectl get applications -n argocd
```

Expected state:

```text
NAME         SYNC STATUS   HEALTH STATUS
voting-app   Synced        Healthy
```

---

# 10. Nginx Reverse Proxy Configuration

Nginx runs on the Kubernetes/Argo CD EC2 host.

It acts as the public entry point for the application and Argo CD dashboard.

### Why Nginx?

- Reverse proxy for Kubernetes NodePort services.
- HTTPS termination.
- HTTP to HTTPS redirection.
- Centralized public access.
- Forwarding client headers.
- Separation between public access and internal Kubernetes networking.

### Nginx Traffic Routing

| Public Port | Service | Internal Destination |
|---|---|---|
| 80 | HTTP | Redirect to HTTPS |
| 443 | Voting App | KIND worker port 30080 |
| 8443 | Argo CD | KIND worker port 30443 |

### Application Proxy

```nginx
location / {
    proxy_pass http://172.18.0.2:30080;

    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;

    proxy_set_header X-Forwarded-For
        $proxy_add_x_forwarded_for;

    proxy_set_header X-Forwarded-Proto https;
}
```

### Argo CD Proxy

```nginx
location / {
    proxy_pass https://172.18.0.2:30443;

    proxy_ssl_verify off;

    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;

    proxy_set_header X-Forwarded-For
        $proxy_add_x_forwarded_for;

    proxy_set_header X-Forwarded-Proto https;

    proxy_buffering off;
}
```

The internal Argo CD endpoint uses HTTPS with certificate verification disabled at the Nginx upstream. This is suitable only for the current lab setup with its self-signed certificate.

### Nginx configuration file

Repository path:

```text
infrastructure/nginx/voting-platform.conf
```

Live server configuration:

```text
/etc/nginx/sites-available/voting-platform
```

### Useful Nginx commands

Validate configuration:

```bash
sudo nginx -t
```

Check service:

```bash
sudo systemctl status nginx
```

Reload configuration:

```bash
sudo systemctl reload nginx
```

Check listening ports:

```bash
sudo ss -tulpn | grep nginx
```

---

# 11. SSL Certificate and HTTPS

The current environment uses a self-signed SSL certificate generated using OpenSSL.

Certificate paths:

```text
/etc/nginx/ssl/argocd.crt
/etc/nginx/ssl/argocd.key
```

### Generate a self-signed certificate

```bash
sudo mkdir -p /etc/nginx/ssl

sudo openssl req -x509 -nodes -days 365 \
  -newkey rsa:2048 \
  -keyout /etc/nginx/ssl/argocd.key \
  -out /etc/nginx/ssl/argocd.crt \
  -subj "/CN=3.109.210.192"
```

### HTTPS configuration

The certificate is used by Nginx for the public HTTPS endpoints.

- Port 443 serves the Voting App.
- Port 8443 serves the Argo CD UI.
- Port 80 redirects HTTP requests to HTTPS.

### Important SSL limitation

A self-signed certificate encrypts traffic but is not automatically trusted by browsers.

The browser may show a security warning.

For publicly trusted HTTPS, use a domain name and a trusted certificate authority such as Let's Encrypt.

The current public IP does not provide a browser-trusted certificate by itself.

**Security:** Never commit the private key, certificate or other sensitive credentials to GitHub.

---

# 12. Public Application Access

The current environment uses the following public endpoints.

| Component | URL |
|---|---|
| Voting Application | https://3.109.210.192 |
| Argo CD Dashboard | https://3.109.210.192:8443 |
| GitHub Repository | https://github.com/ajaydhadi95-gif/voting-app-gitops |
| Docker Hub | https://hub.docker.com/r/ajaydhadi95/voting-app |

The public endpoints require the corresponding EC2 security group rules and active Nginx configuration.

### AWS Security Group

Required public inbound rules:

| Type | Port | Purpose |
|---|---:|---|
| SSH | 22 | Server administration |
| HTTP | 80 | Redirect to HTTPS |
| HTTPS | 443 | Voting application |
| Custom TCP | 8443 | Argo CD dashboard |

Restrict SSH access to trusted IP addresses.

Kubernetes NodePorts and internal Kubernetes API ports should not be exposed publicly.

---

# 13. End-to-End Deployment Process

The following describes the intended delivery workflow.

### Step 1 – Developer Code Change

A developer modifies the Python application and pushes the changes to GitHub.

```bash
git add .
git commit -m "Update voting application"
git push origin main
```

### Step 2 – Jenkins CI

Jenkins checks out the source code, installs dependencies and runs the configured application validation.

### Step 3 – Docker Build

Jenkins creates a new versioned image using the current build number.

### Step 4 – Docker Hub Push

Jenkins authenticates and uploads the image to Docker Hub.

### Step 5 – GitOps Update

Jenkins updates the image tag in the Kubernetes Deployment manifest and pushes the change to GitHub.

### Step 6 – Argo CD Synchronization

Argo CD detects the changed Git revision and synchronizes the manifests.

### Step 7 – Kubernetes Deployment

Kubernetes pulls the new image and updates the application Pod according to the Deployment configuration.

### Step 8 – Application Access

Users access the application through the public Nginx HTTPS endpoint.

---

# 14. Troubleshooting Guide

## Jenkins Issues

Check Jenkins service:

```bash
sudo systemctl status jenkins
```

View Jenkins logs:

```bash
sudo journalctl -u jenkins -f
```

Check Docker:

```bash
docker ps
docker images
```

Common problems:

- Incorrect Jenkins credentials.
- Docker permission errors.
- Python dependency installation failures.
- GitHub authentication problems.
- Docker Hub push failures.
- GitOps push rejection due to remote changes.

## Docker Issues

Check running containers:

```bash
docker ps -a
```

Check image list:

```bash
docker images
```

View container logs:

```bash
docker logs <container-id>
```

## Kubernetes Issues

Check Pods:

```bash
kubectl get pods -n voting-app
```

Describe Pod:

```bash
kubectl describe pod <pod-name> -n voting-app
```

Check logs:

```bash
kubectl logs <pod-name> -n voting-app
```

Check events:

```bash
kubectl get events -n voting-app
```

Common problems:

- ImagePullBackOff.
- CrashLoopBackOff.
- PVC Pending.
- Readiness or liveness probe failures.
- Service selector mismatch.
- Incorrect container port.

## Argo CD Issues

Check application:

```bash
kubectl get applications -n argocd
```

Describe application:

```bash
kubectl describe application voting-app -n argocd
```

Check Argo CD Pods:

```bash
kubectl get pods -n argocd
```

Common problems:

- Incorrect Git repository URL.
- Incorrect manifest path.
- Invalid YAML.
- Image tag not available.
- Sync or health failures.

## Nginx Issues

Validate configuration:

```bash
sudo nginx -t
```

Check service:

```bash
sudo systemctl status nginx
```

Check logs:

```bash
sudo tail -f /var/log/nginx/error.log
```

Check application upstream:

```bash
curl -I http://172.18.0.2:30080
```

Check Argo CD upstream:

```bash
curl -kI https://172.18.0.2:30443
```

---

# 15. Security Best Practices

The project follows these security practices:

- Store Docker Hub credentials in Jenkins Credentials Manager.
- Store GitHub authentication tokens in Jenkins Credentials Manager.
- Avoid hardcoding secrets in Jenkinsfiles.
- Keep SSL private keys outside GitHub.
- Avoid exposing Kubernetes internal ports publicly.
- Restrict SSH access.
- Use Kubernetes resource requests and limits.
- Use health checks for application Pods.
- Keep the Docker image versioned.
- Review GitOps changes before deployment.

The current lab environment uses a self-signed certificate and a single-replica SQLite application. Additional hardening is required before production use.

---

# 16. Current Implementation and Future Enhancements

### Implemented

- [x] Python Flask voting application.
- [x] Dockerfile and application containerization.
- [x] Jenkins CI/CD pipeline.
- [x] Versioned Docker image builds.
- [x] Docker Hub image publishing.
- [x] GitOps manifest updates through Jenkins.
- [x] KIND Kubernetes cluster.
- [x] Deployment, Service and PersistentVolumeClaim.
- [x] Argo CD application and automated synchronization.
- [x] Nginx reverse proxy configuration.
- [x] Self-signed HTTPS certificate.
- [x] GitHub architecture and deployment documentation.


---

# 17. Project Learning Outcomes

Through this project, the following DevOps concepts are demonstrated:

1. Git and GitHub repository management.
2. Jenkins pipeline development.
3. CI/CD stage design.
4. Python application validation.
5. Docker image creation and publishing.
6. Container registry integration.
7. Kubernetes Deployments and Services.
8. Persistent storage using PVC.
9. Health probes and resource management.
10. GitOps using Argo CD.
11. Automated synchronization and self-healing.
12. Nginx reverse proxy configuration.
13. SSL certificate generation and HTTPS.
14. AWS EC2 administration.
15. Linux troubleshooting and deployment verification.

---

# 18. Author

**Ajay Dhadi**

DevOps Engineer

GitHub: https://github.com/ajaydhadi95-gif

Docker Hub: https://hub.docker.com/r/ajaydhadi95/voting-app

Project Repository: https://github.com/ajaydhadi95-gif/voting-app-gitops

---

## ⭐ Final Project Statement

VoteX demonstrates an end-to-end DevOps delivery workflow in which application code is containerized, validated, published and deployed to Kubernetes using Jenkins, Docker, GitHub and Argo CD.

It combines CI/CD automation, GitOps deployment, Kubernetes orchestration, persistent storage and Nginx-based HTTPS access into one practical cloud DevOps project.

**From Git Commit to Kubernetes Deployment – Automated Application Delivery with DevOps and GitOps.**
