# Azure Deployment - Environment Variables Configuration

This file documents all the environment variables needed for Azure deployment.

## Backend (Azure App Service) - Application Settings

Add these in Azure Portal → App Service → Configuration → Application Settings:

```bash
# Database Connection
DATABASE_URL=postgresql://d3radmin:{your_password}@d3r-postgresql-db.postgres.database.azure.com:5432/postgres?sslmode=require

# Python Configuration
PYTHONUNBUFFERED=1
SCM_DO_BUILD_DURING_DEPLOYMENT=true
WEBSITE_HTTPLOGGING_RETENTION_DAYS=3
```

## Frontend (Azure Static Web Apps) - Application Settings

Add these in Azure Portal → Static Web App → Configuration:

```bash
# Backend API URL
VITE_API_URL=https://d3r-restaurant-backend.azurewebsites.net
```

## Startup Command (Backend)

In Azure Portal → App Service → Configuration → General Settings → Startup Command:

```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

**Alternative with Gunicorn (Better for Production):**
```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000 --timeout 120
```

## Stack Settings (Backend)

- **Stack**: Python
- **Python Version**: 3.11
- **Platform**: Linux (64 Bit)
- **Always On**: Off (F1) / On (B1+)

## Database Connection String Format

```
postgresql://[username]:[password]@[server].postgres.database.azure.com:5432/[database]?sslmode=require
```

Example:
```
postgresql://d3radmin:MySecurePass123!@d3r-postgresql-db.postgres.database.azure.com:5432/postgres?sslmode=require
```

## CORS Configuration (Backend)

In Azure Portal → App Service → CORS:

**Allowed Origins:**
- `https://d3r-restaurant-frontend.azurestaticapps.net`
- `http://localhost:3002`

**Enable Access-Control-Allow-Credentials**: ✓ Checked

## GitHub Secrets Required

Add in GitHub → Repository → Settings → Secrets and variables → Actions:

```
AZURE_WEBAPP_PUBLISH_PROFILE
```

To get this:
1. Go to Azure Portal → App Service → Overview
2. Click "Get publish profile" (download button)
3. Open the downloaded file
4. Copy the entire XML content
5. Add as GitHub Secret
