# Visitor App - Docker, ECS & Kubernetes Project

Containerized Flask and Redis-based visitor counter application deployed using Docker, AWS ECS Fargate, and Kubernetes.

---

## Features

- Dockerized Flask application
- Redis integration
- AWS ECS Fargate deployment
- Application Load Balancer
- GitHub Actions CI/CD
- Kubernetes Deployments & Services
- ConfigMaps
- Ingress routing
- Rolling deployments

---

## Architecture Flow

### ECS Flow

Developer
→ GitHub
→ GitHub Actions
→ Docker Hub
→ ECS Fargate
→ Load Balancer
→ Flask Container
→ Redis

---

### Kubernetes Flow

User
→ Ingress
→ Kubernetes Service
→ Flask Pods
→ Redis Service
→ Redis Pod

---

## Technologies Used

- Python
- Flask
- Redis
- Docker
- AWS ECS
- Kubernetes
- Minikube
- GitHub Actions

---

## Run with Docker Compose

```bash
docker-compose up
```

---

## Run on Kubernetes

```bash
kubectl apply -f k8s/
```
