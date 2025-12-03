# Quick Start: Deploy FoodieHub to Azure

## 🎯 Your GitHub Repository
✅ **Already Done!** Your code is at: https://github.com/HirthickCoder/D3R

## 📋 Prerequisites
- Azure Portal access (you have Azure Education account)
- GitHub account connected (HirthickCoder)

---

## 🚀 Step-by-Step Deployment Guide

### Part 1: Deploy Frontend (React App)

#### Step 1: Sign in to Azure Portal
1. Go to: https://portal.azure.com
2. Sign in with your Azure Education account
3. You should see the Azure Portal home page

#### Step 2: Create Static Web App
1. Click **"+ Create a resource"** (top left)
2. In the search box, type: **"Static Web Apps"**
3. Click **"Static Web Apps"** from results
4. Click **"Create"** button

#### Step 3: Fill in Basic Configuration
Fill in these details:

**Basics Tab:**
- **Subscription**: Select "Azure for Students" or your education subscription
- **Resource Group**: Click "Create new" → Enter: `foodiehub-rg`
- **Static Web App name**: `foodiehub-frontend`
- **Plan type**: Select **"Free"**
- **Region**: Select **"East US"** (or closest to you)
- **Source**: Select **"GitHub"**

#### Step 4: Connect to GitHub
1. Click **"Sign in with GitHub"** button
2. Authorize Azure to access your GitHub
3. After authorization, fill in:
   - **Organization**: `HirthickCoder`
   - **Repository**: `D3R`
   - **Branch**: `main`

#### Step 5: Build Configuration
- **Build Presets**: Select **"React"**
- **App location**: `/` (leave as default)
- **Api location**: (leave empty)
- **Output location**: `dist`

#### Step 6: Create the Resource
1. Click **"Review + create"** button at bottom
2. Review your settings
3. Click **"Create"** button
4. Wait 2-3 minutes for deployment to complete

#### Step 7: Get Your Frontend URL
1. After deployment completes, click **"Go to resource"**
2. You'll see your Static Web App overview
3. Copy the **URL** (looks like: `https://foodiehub-frontend-xxxxx.azurestaticapps.net`)
4. **Save this URL** - you'll need it later!

---

### Part 2: Deploy Backend (Python Flask API)

#### Step 1: Create Web App
1. From Azure Portal home, click **"+ Create a resource"**
2. Search for: **"Web App"**
3. Click **"Web App"** from results
4. Click **"Create"** button

#### Step 2: Fill in Basic Configuration

**Basics Tab:**
- **Subscription**: Same as before (Azure for Students)
- **Resource Group**: Select **"foodiehub-rg"** (same as frontend)
- **Name**: `foodiehub-backend` (must be globally unique - if taken, try `foodiehub-backend-yourname`)
- **Publish**: Select **"Code"**
- **Runtime stack**: Select **"Python 3.11"**
- **Operating System**: Select **"Linux"**
- **Region**: Select **"East US"** (same as frontend)

**App Service Plan:**
- Click **"Create new"**
- Name: `foodiehub-plan`
- **Pricing plan**: Click "Explore pricing plans"
  - Select **"Free F1"** (under Dev/Test)
  - Click **"Select"**

#### Step 3: Deployment Configuration
1. Click **"Next: Deployment >"** at bottom
2. **GitHub Actions settings**:
   - **Continuous deployment**: Enable
   - **GitHub account**: Sign in if needed
   - **Organization**: `HirthickCoder`
   - **Repository**: `D3R`
   - **Branch**: `main`

#### Step 4: Create the Resource
1. Click **"Review + create"**
2. Click **"Create"**
3. Wait 2-3 minutes for deployment

#### Step 5: Configure Backend Settings
After deployment completes:

1. Click **"Go to resource"**
2. In the left menu, find **"Configuration"**
3. Click **"General settings"** tab
4. Set **Startup Command**: 
   ```
   gunicorn --bind=0.0.0.0 --timeout 600 run_server:app
   ```
5. Click **"Save"** at top
6. Click **"Continue"** when prompted

#### Step 6: Set Application Path
1. Still in Configuration, click **"Path mappings"** tab
2. Under **"Virtual applications and directories"**:
   - Physical path: `/backend`
3. Click **"Save"**

#### Step 7: Enable CORS
1. In left menu, find **"CORS"**
2. Under **"Allowed Origins"**, add:
   - Your frontend URL (from Part 1, Step 7)
   - `http://localhost:3002` (for local testing)
3. Check **"Enable Access-Control-Allow-Credentials"**
4. Click **"Save"**

#### Step 8: Get Your Backend URL
1. Go back to **"Overview"** in left menu
2. Copy the **URL** (looks like: `https://foodiehub-backend.azurewebsites.net`)
3. **Save this URL!**

---

## ✅ Verification

### Test Your Deployment

1. **Frontend**: Open your frontend URL in browser
   - You should see the FoodieHub home page
   - Try browsing the menu

2. **Backend**: Open your backend URL + `/api/menu`
   - Example: `https://foodiehub-backend.azurewebsites.net/api/menu`
   - You should see JSON data with menu items

### Update Frontend to Use Azure Backend

If the frontend can't connect to backend, you may need to update the API URL:

1. In your local code, find API calls (likely in `src/` folder)
2. Update API base URL to your backend URL
3. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update API URL for Azure backend"
   git push origin main
   ```
4. Azure will automatically redeploy (wait 2-3 minutes)

---

## 🎉 You're Done!

Your app is now live on Azure:
- **Frontend**: `https://foodiehub-frontend-xxxxx.azurestaticapps.net`
- **Backend**: `https://foodiehub-backend.azurewebsites.net`

### Important Notes:
- Free tier may have cold starts (first load might be slow)
- Both services auto-deploy when you push to GitHub
- Monitor deployments in Azure Portal → Your resource → "Deployment Center"

---

## 🐛 Troubleshooting

### Frontend Issues
- **Build fails**: Check GitHub Actions tab in your repository
- **404 errors**: Verify `staticwebapp.config.json` is in root
- **Blank page**: Check browser console for errors

### Backend Issues
- **500 errors**: Check Application Logs in Azure Portal
- **Module not found**: Verify `requirements.txt` has all dependencies
- **Timeout**: Increase timeout in startup command

### Need Help?
- Check Azure Portal → Your resource → "Diagnose and solve problems"
- View logs: Azure Portal → Your resource → "Log stream"
