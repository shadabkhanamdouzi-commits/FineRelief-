# Environment Variables Configuration Guide

## Backend Environment Variables

Create a `.env` file in the `backend` directory with the following variables:

### Database Configuration
```
DATABASE_URL=sqlite:///./finrelief.db
# For production: DATABASE_URL=postgresql://user:password@localhost/finrelief
```

### Authentication
```
SECRET_KEY=your-super-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440
```

### Google Gemini AI
```
GOOGLE_API_KEY=your-google-api-key-here
# Get your API key from: https://makersuite.google.com/app/apikey
```

### Application Settings
```
DEBUG=false
ENVIRONMENT=production  # development, staging, production
LOG_LEVEL=INFO
```

### CORS Settings
```
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173,https://yourdomain.com
```

## Frontend Environment Variables

Create a `.env` file in the `frontend` directory:

```
VITE_API_URL=http://localhost:8000
VITE_APP_NAME=FineRelief
```

## Docker Environment

For Docker deployment, create a `.env.docker` file:

```
# Backend
DATABASE_URL=sqlite:///./data/finrelief.db
SECRET_KEY=docker-secret-key-for-dev-only
GOOGLE_API_KEY=your-api-key

# Frontend
VITE_API_URL=http://backend:8000
```

## Production Deployment

For production, use environment variables from your hosting platform:

### Railway.app
- Set variables in Railway dashboard
- Use PostgreSQL instead of SQLite

### AWS
- Use AWS Secrets Manager
- Use RDS for PostgreSQL database

### Environment Variables Checklist
- [ ] SECRET_KEY is strong and random
- [ ] GOOGLE_API_KEY is set
- [ ] DATABASE_URL points to production database
- [ ] ALLOWED_ORIGINS includes your domain
- [ ] DEBUG is set to false
- [ ] LOG_LEVEL is set appropriately
