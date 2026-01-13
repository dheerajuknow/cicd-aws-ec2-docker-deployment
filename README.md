# CI/CD Deployment to AWS EC2 (Docker + GitHub Actions + DockerHub + Nginx)

This repository demonstrates a complete **production-style CI/CD pipeline** that automatically deploys a Dockerized application to **AWS EC2**.

✅ Local development using Docker Compose  
✅ CI/CD using GitHub Actions  
✅ Docker image build & push to DockerHub  
✅ Automated EC2 deployment via SSH  
✅ Nginx reverse proxy in front of Flask app  
✅ Deployment version proof using Git commit SHA  

---

## 🚀 What Happens When I Push Code
Whenever code is pushed to the `main` branch:

1. **GitHub Actions starts**
2. Builds Docker image for the Flask app
3. Pushes image to DockerHub  
4. Connects to EC2 via SSH
5. Pulls the latest Docker image
6. Deploys containers using Docker Compose on EC2

---

## 🧱 Architecture (Workflow)

Local Ubuntu (Developer)
|
| git push
v
GitHub Repo
|
| GitHub Actions (CI/CD Pipeline)
| - Build Docker Image
| - Push to DockerHub
| - SSH into EC2
v
DockerHub Registry
|
| docker pull
v
AWS EC2 (Ubuntu)
|
| docker compose up -d
v
Nginx Reverse Proxy (port 80) ---> Flask App (Gunicorn, port 5000)

yaml
Copy code

---

## ✅ Application Endpoints
The application provides these endpoints:

- `/` → home page
- `/health` → health check endpoint
- `/version` → returns environment + deployed Git SHA (deployment proof)

Example response:
```json
{"env":"prod","version":"<GIT_SHA>"}
📁 Repository Structure
bash
Copy code
cicd-aws-ec2-docker-deployment/
├── app/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── nginx/
│   ├── nginx.conf
│   └── Dockerfile
├── docker-compose.yml
├── .github/workflows/
│   └── deploy.yml
└── README.md
🐳 Run Locally (Ubuntu)
From the project root:

bash
Copy code
docker compose up --build -d
Test locally:

bash
Copy code
curl http://localhost:8080/
curl http://localhost:8080/health
curl http://localhost:8080/version
☁️ AWS EC2 Setup (High Level)
EC2 Configuration used:

Ubuntu 24.04

Instance: t3.micro

Storage: 15 GiB

Inbound rules:

SSH 22 → My IP

HTTP 80 → Anywhere

Installed on EC2:

Docker

Docker Compose plugin

🔁 CI/CD Pipeline (GitHub Actions)
Workflow file:

bash
Copy code
.github/workflows/deploy.yml
Pipeline steps:

Checkout repo

Login to DockerHub

Build image tagged with Git SHA

Push image to DockerHub

SSH to EC2

Pull image and deploy using docker compose

🔐 GitHub Secrets Required
Add these GitHub repository secrets:

DOCKERHUB_USERNAME

DOCKERHUB_TOKEN

EC2_HOST

EC2_USER

EC2_KEY

✅ Deployment Verification (Production Proof)
After pipeline success ✅, open:

http://<EC2_PUBLIC_IP>/

http://<EC2_PUBLIC_IP>/health

http://<EC2_PUBLIC_IP>/version

Important: /version should show the latest Git SHA, proving the CI/CD auto-deploy works.
