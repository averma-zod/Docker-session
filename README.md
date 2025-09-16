# Docker Basics & AWS Integration

---

## 1: Title
**Docker Basics & AWS Integration: From Containers to Cloud**

---

## 2: Why Docker?
- "It works on my machine" problem 😅
- Lightweight & portable compared to VMs
- Faster deployments, build once, run anytime!

---

## 3: Docker vs Virtual Machines
| Virtual Machine | Docker Container |
|-----------------|------------------|
| Full OS inside each VM | Shares host OS kernel |
| Heavy, slow startup | Lightweight, fast startup |
| GBs of size | MBs of size |

---

## 4: Key Concepts
- **Image**: Blueprint for a container
- **Container**: Running instance of an image
- **Dockerfile**: Recipe to build an image
- **Registry**: Storage for images (Docker Hub, AWS ECR)

---

## 5: Basic Docker Commands
```bash
docker build -t myapp .
docker run -d -p 5000:5000 myapp
docker ps
docker logs <container_id>
docker stop <container_id>
```

---

## 6: Demo App (Flask)
- A simple web app:
```python
👋 Hello <YourName>, welcome to Docker on AWS! 🚀
```
- Runs locally → Docker container → AWS EC2

---

## 7: AWS EC2 Setup
1. Launch **Ubuntu t3.micro**
2. Open **port 5000** in Security Group
3. Install Docker
4. Deploy app in container

---

## 8: Hands-On Flow
1. Write a `Dockerfile`
2. Build image: `docker build -t flask-docker-aws .`
3. Run container: `docker run -d -p 5000:5000 flask-docker-aws`
4. Access app: `http://<EC2_PUBLIC_IP>:5000/?name=YourName`

---

## 9: Fun Interaction 🎉
- Share EC2 public IP with unit
- Everyone visits: `http://<EC2_PUBLIC_IP>:5000/?name=YourName`
- Live demo: logs show who accessed!

---

## 10: Best Practices
- Use lightweight base images (e.g., `python:3.9-slim`)
- Use `.dockerignore`
- Keep containers single-purpose
- Security: IAM roles, scan images

---

## 11: Next Steps
- Push images to **AWS ECR**
- Deploy on **ECS/Fargate** (no servers to manage)
- Scale with **load balancers**
- Move towards **Kubernetes (EKS)**

---

## 12: Q&A
**Your turn 🚀**
- How can you apply Docker + AWS in your projects?

