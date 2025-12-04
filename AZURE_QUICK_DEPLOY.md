# 🚀 Quick Azure Deployment Checklist

**Project**: D3R Restaurant App  
**Target Region**: Southeast Asia (Singapore)  
**Deployment Method**: Azure Portal + GitHub Actions

---

## ✅ Pre-Deployment Checklist

- [ ] Azure account with active subscription
- [ ] GitHub account logged in
- [ ] Repository: https://github.com/HirthickCoder/D3R
- [ ] Project code updated locally
- [ ] Strong password ready for PostgreSQL (save it!)

---

## 📝 Deployment Steps

### 🗄️ Step 1: Create PostgreSQL Database (~10 min)

Portal: https://portal.azure.com

1. Search "Azure Database for PostgreSQL flexible servers" → Create
2. **Basics**:
   - Resource Group: Create new → `d3r-restaurant-rg`
   - Server name: `d3r-postgresql-db`
   - Region: **Southeast Asia**
   - PostgreSQL version: **15**
   - Workload type: **Development**
   - Compute: **Burstable, B1ms**
   - Admin username: `d3radmin`
   - Password: [CREATE STRONG PASSWORD - SAVE IT!]

3. **Networking**:
   - Public access
   - ✅ Allow Azure services
   - ✅ Add your IP
   - Add AllowAll: 0.0.0.0 - 255.255.255.255 (temporary)

4. **Review + Create**

5. **Save Connection String**:
   ```
   postgresql://d3radmin:{password}@d3r-postgresql-db.postgres.database.azure.com:5432/postgres?sslmode=require
   ```

---

### 🖥️ Step 2: Create Backend App Service (~15 min)

Portal: https://portal.azure.com/#create/Microsoft.WebSite

1. **Basics**:
   - Resource Group: `d3r-restaurant-rg` (same)
   - Name: `d3r-restaurant-backend`
   - Publish: **Code**
   - Runtime: **Python 3.11**
   - OS: **Linux**
   - Region: **Southeast Asia**
   - Plan: **Basic B1** (recommended) or **Free F1**

2. **Deployment**:
   - Enable continuous deployment
   - GitHub: HirthickCoder/D3R, branch: main

3. **Create & Configure**:
   - After deployment → Go to resource
   - **Configuration** → **Application settings**:
     - Add: `DATABASE_URL` = [your connection string]
     - Add: `PYTHONUNBUFFERED` = `1`
     - Add: `SCM_DO_BUILD_DURING_DEPLOYMENT` = `true`
     - Save

4. **General Settings**:
   - Startup command: `python -m uvicorn main:app --host 0.0.0.0 --port 8000`
   - Save

5. **CORS**:
   - Add: `http://localhost:3002`
   - Add: `https://d3r-restaurant-frontend.azurestaticapps.net`
   - ✅ Enable Access-Control-Allow-Credentials
   - Save

6. **Deployment Center**:
   - Path: `/backend`
   - Save

7. **Restart** the app

---

### 🌐 Step 3: Create Frontend Static Web App (~10 min)

Portal: https://portal.azure.com/#create/Microsoft.StaticApp

1. **Basics**:
   - Resource Group: `d3r-restaurant-rg`
   - Name: `d3r-restaurant-frontend`
   - Plan: **Free**
   - Region: **East Asia**

2. **Deployment**:
   - Source: GitHub
   - Organization: HirthickCoder
   - Repository: D3R
   - Branch: main

3. **Build**:
   - Preset: **React**
   - App location: `/`
   - Api location: (empty)
   - Output location: `dist`

4. **Create & Configure**:
   - After deployment → Go to resource
   - **Configuration**:
     - Add: `VITE_API_URL` = `https://d3r-restaurant-backend.azurewebsites.net`
     - Save

---

### 🌱 Step 4: Seed Database (~5 min)

Using Azure Cloud Shell or local terminal:

```bash
# Clone repo
git clone https://github.com/HirthickCoder/D3R.git
cd D3R/backend

# Install dependencies
pip install -r requirements.txt

# Set database URL
export DATABASE_URL="postgresql://d3radmin:{password}@d3r-postgresql-db.postgres.database.azure.com:5432/postgres?sslmode=require"

# Seed data
python seed_data.py
```

---

### ✅ Step 5: Verify Deployment (~5 min)

**Backend API Test**:
- Visit: `https://d3r-restaurant-backend.azurewebsites.net/`
- Should return: `{"message": "Welcome to the Menu API"}`
- Visit: `https://d3r-restaurant-backend.azurewebsites.net/api/menu/`
- Should return: JSON array of menu items

**Log Stream Check**:
- Azure Portal → Backend App Service → Log stream
- Look for: "Application startup complete"

**Frontend Test**:
- Visit: `https://d3r-restaurant-frontend-xxxx.azurestaticapps.net/`
- Home page loads
- Menu displays items
- No console errors

---

## 🎯 Resource Summary

| Resource | Name | URL |
|----------|------|-----|
| Resource Group | `d3r-restaurant-rg` | - |
| PostgreSQL | `d3r-postgresql-db` | `d3r-postgresql-db.postgres.database.azure.com` |
| Backend | `d3r-restaurant-backend` | `https://d3r-restaurant-backend.azurewebsites.net` |
| Frontend | `d3r-restaurant-frontend` | `https://d3r-restaurant-frontend-xxxx.azurestaticapps.net` |

---

## 🔧 GitHub Secret Required

After creating App Service:

1. Azure Portal → Backend App Service → **Get publish profile** (download)
2. GitHub → HirthickCoder/D3R → Settings → Secrets → Actions
3. Add new secret:
   - Name: `AZURE_WEBAPP_PUBLISH_PROFILE`
   - Value: [paste entire XML from downloaded file]

---

## 🐛 Common Issues

| Issue | Solution |
|-------|----------|
| Backend 503 error | Wait 1-2 minutes for startup; check log stream |
| Backend 500 error | Verify DATABASE_URL is correct; check logs |
| Frontend blank page | Check browser console; verify build succeeded |
| Menu doesn't load | Verify backend API works; check CORS |
| Database connection error | Verify firewall rules; check password |

---

## 📞 Help & Monitoring

**Azure Portal Paths**:
- Backend logs: App Service → Log stream
- Frontend build: Static Web App → GitHub Actions
- Database: PostgreSQL server → Metrics

**GitHub Actions**:
- https://github.com/HirthickCoder/D3R/actions

**Restart Commands**:
```bash
# Restart backend
az webapp restart --name d3r-restaurant-backend --resource-group d3r-restaurant-rg

# View backend logs
az webapp log tail --name d3r-restaurant-backend --resource-group d3r-restaurant-rg
```
