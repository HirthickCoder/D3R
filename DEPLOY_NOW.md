# ✅ FINAL DEPLOYMENT GUIDE - Follow These Exact Steps

## 🎯 Your GitHub is Ready!
**Repository**: https://github.com/HirthickCoder/D3R ✅

## 📋 What You'll Deploy
1. **Frontend** (React App) → Azure Static Web Apps
2. **Backend** (Python Flask) → Azure App Service

---

## 🚀 PART 1: Deploy Frontend (10 minutes)

### Step 1: Go to Azure Portal
Open this link in your browser:
```
https://portal.azure.com/#create/Microsoft.StaticApp
```

### Step 2: Fill in the Form

**Basics Tab:**

1. **Subscription**: 
   - Select your Azure for Students subscription

2. **Resource Group**:
   - Click "Create new"
   - Enter: `foodiehub-rg`
   - Click OK

3. **Static Web App details**:
   - **Name**: `foodiehub-frontend`
   - **Plan type**: Select **"Free"**
   - **Azure Functions and staging details**:
     * Region: Select **"East US 2"** or **"Central US"**

4. **Deployment details**:
   - **Source**: Select **"GitHub"**
   - Click **"Sign in with GitHub"**
   - Authorize Azure (if prompted)
   - **Organization**: Select **"HirthickCoder"**
   - **Repository**: Select **"D3R"**
   - **Branch**: Select **"main"**

5. **Build Details**:
   - **Build Presets**: Select **"React"**
   - **App location**: `/` (leave as default)
   - **Api location**: (leave empty)
   - **Output location**: `dist`

### Step 3: Create the Resource
1. Click **"Review + create"** (bottom of page)
2. Review your settings
3. Click **"Create"**
4. Wait 2-3 minutes

### Step 4: Get Your Frontend URL
1. After deployment completes, click **"Go to resource"**
2. You'll see your Static Web App overview page
3. **Copy the URL** - it looks like:
   ```
   https://foodiehub-frontend-xxxxx.azurestaticapps.net
   ```
4. **SAVE THIS URL** - you'll need it!

---

## 🔧 PART 2: Deploy Backend (10 minutes)

### Step 1: Go to Web App Creation
Open this link:
```
https://portal.azure.com/#create/Microsoft.WebSite
```

### Step 2: Fill in the Form

**Basics Tab:**

1. **Subscription**: Same as before (Azure for Students)

2. **Resource Group**: Select **"foodiehub-rg"** (same as frontend)

3. **Instance Details**:
   - **Name**: `foodiehub-backend` 
     * (If taken, try: `foodiehub-backend-yourname`)
   - **Publish**: Select **"Code"**
   - **Runtime stack**: Select **"Python 3.11"**
   - **Operating System**: Select **"Linux"**
   - **Region**: Select **"East US 2"** (same as frontend)

4. **Pricing plans**:
   - Click **"Change size"**
   - Select **"Dev/Test"** tab
   - Choose **"F1 (Free)"**
   - Click **"Apply"**

### Step 3: Configure Deployment

1. Click **"Next: Deployment >"** at bottom

2. **Continuous deployment**:
   - **Enable**: Turn ON
   - **GitHub account**: Sign in if needed
   - **Organization**: **"HirthickCoder"**
   - **Repository**: **"D3R"**
   - **Branch**: **"main"**

### Step 4: Create the Resource
1. Click **"Review + create"**
2. Click **"Create"**
3. Wait 2-3 minutes

### Step 5: Configure Backend Settings

After deployment:

1. Click **"Go to resource"**

2. **Set Startup Command**:
   - In left menu, click **"Configuration"**
   - Click **"General settings"** tab
   - Find **"Startup Command"**
   - Enter:
     ```
     gunicorn --bind=0.0.0.0 --timeout 600 run_server:app
     ```
   - Click **"Save"** at top
   - Click **"Continue"** when prompted

3. **Enable CORS**:
   - In left menu, find **"CORS"**
   - Under **"Allowed Origins"**, click **"+ Add"**
   - Add your frontend URL (from Part 1, Step 4)
   - Add: `http://localhost:3002`
   - Check **"Enable Access-Control-Allow-Credentials"**
   - Click **"Save"**

4. **Get Backend URL**:
   - Go to **"Overview"** in left menu
   - Copy the **URL** - looks like:
     ```
     https://foodiehub-backend.azurewebsites.net
     ```

---

## ✅ VERIFICATION

### Test Your Deployment

1. **Frontend**: Open your frontend URL
   - Should see FoodieHub home page
   - Try browsing the menu

2. **Backend**: Open `https://your-backend-url.azurewebsites.net/api/menu`
   - Should see JSON data with menu items

---

## 🎉 YOU'RE DONE!

Your app is now live on Azure!

### Your URLs:
- **Frontend**: `https://foodiehub-frontend-xxxxx.azurestaticapps.net`
- **Backend**: `https://foodiehub-backend.azurewebsites.net`

### Auto-Deployment:
- Every time you push to GitHub, Azure will automatically redeploy
- Check deployment status in Azure Portal → Your resource → "Deployment Center"

---

## 🐛 Common Issues & Solutions

### Frontend shows blank page
- Check browser console for errors
- Verify build completed successfully in GitHub Actions
- Check `staticwebapp.config.json` is in repository root

### Backend shows 500 error
- Go to Azure Portal → Your App Service → "Log stream"
- Check for Python errors
- Verify `requirements.txt` has all dependencies
- Verify startup command is correct

### Frontend can't connect to backend
- Verify CORS is enabled with your frontend URL
- Check backend URL is correct
- Verify backend is running (visit `/api/menu` endpoint)

---

## 📞 Need Help?

If you get stuck:
1. Check Azure Portal → Your resource → "Diagnose and solve problems"
2. View logs: Azure Portal → Your resource → "Log stream"
3. Check GitHub Actions for build errors

---

## 🎓 What You've Accomplished

✅ Deployed React frontend to Azure Static Web Apps  
✅ Deployed Python Flask backend to Azure App Service  
✅ Connected GitHub for auto-deployment  
✅ Configured CORS for frontend-backend communication  
✅ Set up free tier hosting with Azure Education  

**Congratulations! Your full-stack app is live on Azure!** 🎉
