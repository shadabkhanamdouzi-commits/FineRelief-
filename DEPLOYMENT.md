# FineRelief - Docker Deployment Guide

## Quick Start

### Prerequisites
- Docker installed
- Docker Compose installed

### Deploy Locally with Docker

1. **Build and run containers:**
   ```bash
   docker-compose up --build
   ```

2. **Access the application:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

3. **Stop containers:**
   ```bash
   docker-compose down
   ```

### Environment Variables

Copy `.env.example` to `.env` and update with your values:
```bash
cp .env.example .env
```

### Useful Commands

**View logs:**
```bash
docker-compose logs -f frontend
docker-compose logs -f backend
```

**Rebuild containers:**
```bash
docker-compose up --build --force-recreate
```

**Remove all containers:**
```bash
docker-compose down -v
```

## Production Deployment

For production deployment to cloud platforms:

### Railway.app
1. Connect GitHub repo to Railway
2. Add environment variables
3. Deploy (it auto-detects docker-compose)

### AWS, Render, or others
- Push Docker images to Docker Registry (DockerHub, ECR, etc.)
- Use docker-compose for orchestration or deploy to Kubernetes/ECS

## Troubleshooting

- **Port already in use:** Change ports in docker-compose.yml
- **Frontend can't connect to backend:** Check API_URL in frontend env
- **Database errors:** Ensure migrations are run in backend

