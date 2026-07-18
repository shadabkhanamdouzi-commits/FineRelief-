# Railway.app Deployment Guide

## Step 1: Create Railway Account

1. Go to https://railway.app
2. Sign up with GitHub
3. Create a new project

## Step 2: Deploy from GitHub

1. Connect your GitHub repository to Railway
2. Select the FineRelief repository
3. Railway auto-detects `docker-compose.yml`

## Step 3: Configure Environment Variables

In Railway Dashboard → Project → Variables:

```
DATABASE_URL=postgresql://${{Postgres.PGUSER}}:${{Postgres.PGPASSWORD}}@${{Postgres.PGHOST}}/finrelief
SECRET_KEY=your-production-secret-key
GOOGLE_API_KEY=your-api-key
ALLOWED_ORIGINS=https://your-domain.com,https://www.your-domain.com
DEBUG=false
ENVIRONMENT=production
```

## Step 4: Add PostgreSQL Service

1. Click "Add Service" → "Database"
2. Select "PostgreSQL"
3. Railway automatically sets `Postgres` environment variables

## Step 5: Deploy

1. Click "Deploy"
2. Wait for services to start
3. Access your app via Railway's generated URL

## Monitoring

- View logs: Project → Deployments → Logs
- Monitor metrics: Project → Deployments → Metrics
- Set up alerts: Project → Settings → Alerts

## Database Migrations

Run migrations after deployment:

```bash
railway run python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"
```

---

# AWS Deployment Guide

## Option 1: Using ECS (Elastic Container Service)

### Prerequisites
- AWS Account
- AWS CLI installed
- Docker images pushed to ECR

### Steps

1. **Push Docker images to ECR:**

```bash
# Create ECR repositories
aws ecr create-repository --repository-name finrelief-backend
aws ecr create-repository --repository-name finrelief-frontend

# Login to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin [YOUR_ACCOUNT_ID].dkr.ecr.us-east-1.amazonaws.com

# Tag and push images
docker tag finerelief-backend:latest [YOUR_ACCOUNT_ID].dkr.ecr.us-east-1.amazonaws.com/finrelief-backend:latest
docker push [YOUR_ACCOUNT_ID].dkr.ecr.us-east-1.amazonaws.com/finrelief-backend:latest

docker tag finerelief-frontend:latest [YOUR_ACCOUNT_ID].dkr.ecr.us-east-1.amazonaws.com/finrelief-frontend:latest
docker push [YOUR_ACCOUNT_ID].dkr.ecr.us-east-1.amazonaws.com/finrelief-frontend:latest
```

2. **Create ECS Cluster**

3. **Configure RDS PostgreSQL Database**

4. **Create Task Definitions** for backend and frontend

5. **Deploy Services** with load balancer

## Option 2: Using Elastic Beanstalk

```bash
# Install EB CLI
pip install awsebcli

# Initialize
eb init -p docker finrelief

# Create environment
eb create finrelief-env

# Deploy
eb deploy

# View logs
eb logs
```

---

# Render.com Deployment Guide

## Quick Deploy

1. Push to GitHub repository
2. Go to https://render.com
3. Connect your GitHub account
4. Select FineRelief repository
5. Create Web Service from docker-compose.yml

## Environment Setup

In Render Dashboard:

```
DATABASE_URL=postgresql://...
SECRET_KEY=your-production-key
GOOGLE_API_KEY=your-api-key
ALLOWED_ORIGINS=https://your-domain.onrender.com
```

---

# Cloud Deployment Comparison

| Feature | Railway | AWS | Render |
|---------|---------|-----|--------|
| Setup Time | 5 min | 30 min | 10 min |
| Cost | $5+/month | Pay-as-you-go | $7+/month |
| Scalability | Good | Excellent | Good |
| Database | PostgreSQL | RDS | PostgreSQL |
| Free Tier | Yes (limited) | 12 months | Yes (limited) |
| Support | Good | Excellent | Good |

---

# Production Checklist

- [ ] Set `DEBUG=false`
- [ ] Configure strong `SECRET_KEY`
- [ ] Set up PostgreSQL database
- [ ] Configure CORS with production domain
- [ ] Enable HTTPS
- [ ] Set up monitoring/logging
- [ ] Configure automated backups
- [ ] Set up email notifications
- [ ] Test all APIs
- [ ] Load testing
- [ ] Security audit
- [ ] Configure CDN for static files
