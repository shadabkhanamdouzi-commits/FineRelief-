# Troubleshooting Guide

## Common Issues & Solutions

### Docker Issues

#### Issue: Port already in use

**Error:** `Error starting userland proxy: listen tcp 0.0.0.0:8000: bind: address already in use`

**Solution:**

```bash
# Find process using port 8000
lsof -i :8000

# Kill the process
kill -9 <PID>

# Or use different ports
docker-compose -e "BACKEND_PORT=8001" -e "FRONTEND_PORT=3001" up
```

#### Issue: Docker build fails

**Solution:**

```bash
# Clean up
docker-compose down -v
docker system prune -a

# Rebuild
docker-compose build --no-cache
```

#### Issue: Container crashes on startup

**Solution:**

```bash
# Check logs
docker-compose logs backend
docker-compose logs frontend

# Check environment variables
docker-compose ps
docker exec <container_name> env
```

### Backend Issues

#### Issue: ModuleNotFoundError

**Error:** `ModuleNotFoundError: No module named 'jwt'`

**Solution:**

```bash
# Install missing dependency
pip install PyJWT

# Or update requirements.txt
pip install -r requirements.txt
```

#### Issue: Database errors

**Error:** `No such table: user`

**Solution:**

```bash
# Initialize database
python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"

# Or for Docker
docker exec <backend_container> python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"
```

#### Issue: Google API key not working

**Error:** `APIError: Invalid API key`

**Solution:**

1. Generate new API key: https://makersuite.google.com/app/apikey
2. Check `.env` file: `GOOGLE_API_KEY=your-actual-key`
3. Enable Generative Language API in Google Cloud Console

#### Issue: CORS errors in frontend

**Error:** `Access to XMLHttpRequest blocked by CORS policy`

**Solution:**

Check `backend/app/main.py`:

```python
allow_origins=[
    "http://localhost:5174",
    "http://localhost:5173", 
    "http://localhost:3000",  # for Docker
    "http://frontend:3000"     # for Docker
]
```

Update if needed and rebuild.

### Frontend Issues

#### Issue: npm install fails

**Solution:**

```bash
# Clear cache
npm cache clean --force

# Delete node_modules and lock file
rm -rf node_modules package-lock.json

# Reinstall
npm install
```

#### Issue: Build fails

**Error:** `Error: Cannot find module`

**Solution:**

```bash
# Check node version (should be 18+)
node --version

# Reinstall dependencies
npm ci

# Rebuild
npm run build
```

#### Issue: API connection fails

**Error:** `Cannot POST http://localhost:8000/api/...`

**Solution:**

1. Check backend is running: `curl http://localhost:8000/`
2. Check `src/api/api.js`: 
   ```javascript
   const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';
   ```
3. For Docker: ensure `VITE_API_URL=http://backend:8000`

#### Issue: Hot reload not working

**Solution:**

```bash
# Restart dev server
npm run dev

# Check vite.config.js for watch configuration
```

### Database Issues

#### Issue: SQLite database locked

**Error:** `database is locked`

**Solution:**

```bash
# Close other connections
pkill -f "sqlite"

# Or use PostgreSQL for production
```

#### Issue: Migration errors

**Solution:**

```bash
# For Alembic migrations (future)
alembic stamp head
alembic downgrade -1
alembic upgrade head
```

### Authentication Issues

#### Issue: Login not working

**Solution:**

1. Check database has users table:
   ```sql
   SELECT name FROM sqlite_master WHERE type='table' AND name='user';
   ```

2. Verify password hashing:
   ```bash
   python -c "from app.auth_utils import pwd_context; print(pwd_context.hash('test'))"
   ```

3. Check JWT secret is set:
   ```bash
   echo $SECRET_KEY
   ```

#### Issue: Token expired

**Solution:**

Check `TOKEN_EXPIRE_MINUTES` in `.env` or `app/auth_utils.py`

### Performance Issues

#### Issue: Slow API responses

**Solution:**

```bash
# Profile backend
pip install python-flamegraph
python -m cProfile -o output.prof app/main.py

# Check database queries (add logging)
export SQLALCHEMY_ECHO=true
```

#### Issue: High memory usage

**Solution:**

```bash
# Monitor Docker
docker stats

# Limit resources
docker-compose -f docker-compose.yml -f docker-compose.limit.yml up
```

### Deployment Issues

#### Issue: Railway deployment fails

**Solution:**

1. Check logs: Railway Dashboard → Deployments → Logs
2. Verify environment variables are set
3. Test locally with Docker first
4. Check database connection string

#### Issue: HTTPS certificate errors

**Solution:**

1. Ensure domain is properly configured
2. Use Let's Encrypt for free SSL:
   ```bash
   # In deployment platform settings
   ```
3. Update ALLOWED_ORIGINS with https://

### Debugging Commands

```bash
# Backend logs
docker-compose logs -f backend

# Frontend logs
docker-compose logs -f frontend

# Database inspection
sqlite3 backend/finrelief.db ".tables"
sqlite3 backend/finrelief.db ".schema user"

# Network testing
curl -i http://localhost:8000/
curl -i http://localhost:3000/

# Health checks
curl http://localhost:8000/health
curl http://localhost:8000/docs
```

### Getting Help

1. **Check logs first:**
   ```bash
   docker-compose logs
   ```

2. **Search existing issues:**
   GitHub Issues tab

3. **Create detailed bug report:**
   Include:
   - Error message (full stack trace)
   - Steps to reproduce
   - OS and versions
   - Docker/Python/Node versions

4. **Contact:**
   - GitHub Issues
   - Email: team@finerelief.com

---

**Tip:** Most issues can be resolved by:
1. Clearing caches
2. Rebuilding Docker images
3. Reinstalling dependencies
4. Checking environment variables
