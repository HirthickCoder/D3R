# Azure Deployment Guide for FoodieHub

## ✅ Completed Steps

1. **GitHub Repository** - Successfully pushed to https://github.com/HirthickCoder/D3R
2. **Configuration Files Created**:
   - `staticwebapp.config.json` - Frontend routing configuration
   - `backend/requirements.txt` - Python dependencies
   - `backend/Procfile` - Backend startup configuration
   - `README.md` - Project documentation

## 🚀 Azure Deployment Steps

### Option 1: Deploy via Azure Portal (Recommended for Beginners)

#### Frontend (Azure Static Web Apps)

1. **Go to Azure Portal**: https://portal.azure.com
2. **Create Static Web App**:
   - Click "+ Create a resource"
   - Search for "Static Web Apps"
   - Click "Create"

3. **Configure**:
   - **Subscription**: Select your Azure Education subscription
   - **Resource Group**: Create new or select existing
   - **Name**: `foodiehub-frontend` (or your preferred name)
   - **Plan type**: Free
   - **Region**: Choose closest to you
   - **Source**: GitHub
   - **GitHub account**: Authorize and select `HirthickCoder/D3R`
   - **Branch**: main
   - **Build Presets**: React
   - **App location**: `/`
   - **Api location**: (leave empty)
   - **Output location**: `dist`

4. **Review + Create** and wait for deployment

#### Backend (Azure App Service)

1. **Create App Service**:
   - Click "+ Create a resource"
   - Search for "Web App"
   - Click "Create"

2. **Configure**:
   - **Subscription**: Select your Azure Education subscription
   - **Resource Group**: Same as frontend
   - **Name**: `foodiehub-backend` (must be globally unique)
   - **Publish**: Code
   - **Runtime stack**: Python 3.11
   - **Operating System**: Linux
   - **Region**: Same as frontend
   - **Pricing plan**: Free F1 (or B1 Basic if available)

3. **Deployment**:
   - Go to "Deployment Center"
   - **Source**: GitHub
   - **Organization**: HirthickCoder
   - **Repository**: D3R
   - **Branch**: main
   - **Build Provider**: GitHub Actions
   - **Root folder**: `/backend`
   - Save

4. **Configure Startup Command**:
   - Go to "Configuration" → "General settings"
   - **Startup Command**: `gunicorn --bind=0.0.0.0 --timeout 600 run_server:app`
   - Save

5. **Set Environment Variables**:
   - Go to "Configuration" → "Application settings"
   - Add: `PORT` = `8000`
   - Save and restart

### Option 2: Deploy via Azure CLI

```bash
# Login to Azure
az login

# Create resource group
az group create --name foodiehub-rg --location eastus

# Deploy frontend (Static Web App)
az staticwebapp create \
  --name foodiehub-frontend \
  --resource-group foodiehub-rg \
  --source https://github.com/HirthickCoder/D3R \
  --location eastus \
  --branch main \
  --app-location "/" \
  --output-location "dist" \
  --login-with-github

# Deploy backend (App Service)
az webapp up \
  --name foodiehub-backend \
  --resource-group foodiehub-rg \
  --runtime "PYTHON:3.11" \
  --sku F1 \
  --location eastus \
  --src-path ./backend
```

## 🔧 Post-Deployment Configuration

### Update Frontend API URL

After backend is deployed, update the frontend to use the Azure backend URL:

1. Get your backend URL: `https://foodiehub-backend.azurewebsites.net`
2. Update API calls in frontend code to point to this URL
3. Commit and push changes - Static Web App will auto-redeploy

### Enable CORS on Backend

The backend should already have CORS enabled in the Flask app. Verify in Azure:
- Go to App Service → CORS
- Add your Static Web App URL to allowed origins

## 📝 Important Notes

- **Free tier limitations**: May have slower cold starts
- **Custom domains**: Can be configured after deployment
- **HTTPS**: Automatically enabled on both services
- **Monitoring**: Available in Azure Portal under "Monitoring"

## 🔗 URLs After Deployment

- **Frontend**: `https://foodiehub-frontend.azurewebsites.net` (or custom domain)
- **Backend API**: `https://foodiehub-backend.azurewebsites.net`
- **GitHub Repo**: https://github.com/HirthickCoder/D3R

## 🐛 Troubleshooting

### Frontend Issues
- Check build logs in GitHub Actions
- Verify `dist` folder is created during build
- Check `staticwebapp.config.json` is in root

### Backend Issues
- Check Application Logs in Azure Portal
- Verify `requirements.txt` has all dependencies
- Check startup command is correct
- Ensure PORT environment variable is set

## ✨ Next Steps

1. Test the deployed application
2. Configure custom domain (optional)
3. Set up Application Insights for monitoring
4. Configure CI/CD for automatic deployments
