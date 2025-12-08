# 🚀 Step-by-Step Render Deployment Guide

This guide will walk you through deploying both your **backend** (FastAPI) and **frontend** (React/Vite) to Render.

---

## 📋 Prerequisites

Before you start, make sure you have:
- ✅ A GitHub account with your code pushed to https://github.com/HirthickCoder/D3R
- ✅ A Render account (sign up at https://render.com - it's free)
- ✅ A PostgreSQL database (we'll set one up on Render or you can use Aiven)

---

## 🗄️ STEP 1: Create PostgreSQL Database on Render

1. **Go to Render Dashboard**
   - Visit https://dashboard.render.com/
   - Click **"New +"** button in the top right

2. **Select PostgreSQL**
   - Choose **"PostgreSQL"** from the dropdown menu

3. **Configure Database**
   - **Name**: `d3r-database` (or any name you prefer)
   - **Database**: `postgres`
   - **User**: `postgres` (auto-filled)
   - **Region**: Choose closest to you (e.g., Singapore for SEA)
   - **PostgreSQL Version**: 16 (or latest)
   - **Instance Type**: Free

4. **Create Database**
   - Click **"Create Database"**
   - Wait for it to provision (1-2 minutes)

5. **Copy Database URL**
   - Once created, scroll down to **"Connections"** section
   - Copy the **"Internal Database URL"** (it starts with `postgres://`)
   - **IMPORTANT**: Save this URL - you'll need it for the backend!

---

## 🔧 STEP 2: Deploy Backend to Render

1. **Create New Web Service**
   - Click **"New +"** → **"Web Service"**

2. **Connect GitHub Repository**
   - Click **"Connect account"** to link your GitHub
   - Select **"HirthickCoder/D3R"** repository
   - Click **"Connect"**

3. **Configure Backend Service**
   Fill in these details:
   
   - **Name**: `d3r-backend` (this will be your URL subdomain)
   - **Region**: Same as your database (e.g., Singapore)
   - **Branch**: `main`
   - **Root Directory**: `backend`
   - **Runtime**: `Python 3`
   - **Build Command**: 
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command**:
     ```bash
     uvicorn main:app --host 0.0.0.0 --port $PORT
     ```
   - **Instance Type**: Free

4. **Add Environment Variables**
   Scroll down to **"Environment Variables"** and add these:
   
   | Key | Value |
   |-----|-------|
   | `DATABASE_URL` | Paste the Internal Database URL from Step 1 |
   | `SECRET_KEY` | Generate a random string (e.g., `your-super-secret-key-12345`) |
   | `ALGORITHM` | `HS256` |
   | `ACCESS_TOKEN_EXPIRE_MINUTES` | `30` |

   **To add each variable:**
   - Click **"Add Environment Variable"**
   - Enter the Key name
   - Enter the Value
   - Repeat for all 4 variables

5. **Deploy Backend**
   - Click **"Create Web Service"**
   - Wait for deployment (3-5 minutes)
   - You'll see logs streaming in the console

6. **Verify Backend is Running**
   - Once deployed, click on the URL at the top (looks like: `https://d3r-backend.onrender.com`)
   - You should see: `{"message":"Welcome to the Menu API"}`
   - **Copy this URL** - you'll need it for the frontend!

7. **Test Authentication Endpoint**
   - Visit: `https://d3r-backend.onrender.com/api/auth/clients`
   - Should return: `[]` (empty array, since no clients registered yet)

---

## 🎨 STEP 3: Deploy Frontend to Render

1. **Update Frontend Environment Variable**
   - Open `.env.production` file in your local project
   - Replace `https://your-backend-name.onrender.com` with your actual backend URL from Step 2
   - Example: `VITE_API_URL=https://d3r-backend.onrender.com`
   - **Save the file**

2. **Commit and Push Changes**
   ```bash
   git add .env.production
   git commit -m "Update production API URL for Render"
   git push origin main
   ```

3. **Create New Static Site**
   - Go back to Render Dashboard
   - Click **"New +"** → **"Static Site"**

4. **Connect GitHub Repository**
   - Select **"HirthickCoder/D3R"** repository
   - Click **"Connect"**

5. **Configure Frontend Service**
   
   - **Name**: `d3r-frontend` (your frontend URL subdomain)
   - **Branch**: `main`
   - **Root Directory**: Leave empty or put `.` (current directory)
   - **Build Command**:
     ```bash
     npm install && npm run build
     ```
   - **Publish Directory**:
     ```
     dist
     ```

6. **Add Environment Variable**
   - Scroll to **"Environment Variables"**
   - Add one variable:
     - **Key**: `VITE_API_URL`
     - **Value**: Your backend URL (e.g., `https://d3r-backend.onrender.com`)

7. **Deploy Frontend**
   - Click **"Create Static Site"**
   - Wait for build and deployment (5-10 minutes)

8. **Get Frontend URL**
   - Once deployed, you'll get a URL like: `https://d3r-frontend.onrender.com`
   - Click on it to open your app!

---

## 🔒 STEP 4: Update CORS in Backend

Your backend needs to allow requests from your frontend URL.

1. **Update Backend CORS Settings**
   - Open your local `backend/main.py`
   - Find the `allow_origins` list (around line 26)
   - Add your Render frontend URL:

   ```python
   app.add_middleware(
       CORSMiddleware,
       allow_origins=[
           "http://localhost:5173",  
           "http://localhost:3002", 
           "http://localhost:3000",  
           "https://myrestaurants-apps-ezhfzcbwcabecrdb.eastus2-01.azurewebsites.net", 
           "https://d3r-restaurant-frontend.azurestaticapps.net", 
           "https://*.azurestaticapps.net",  
           "https://d3r-frontend-g2dydbdqf4fug6hr.southeastasia-01.azurewebsites.net",  
           "https://*.azurewebsites.net",
           "https://d3r-frontend.onrender.com",  # 👈 ADD YOUR RENDER FRONTEND URL HERE
           "https://*.onrender.com",  # 👈 Allow all Render sites
       ],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

2. **Commit and Push**
   ```bash
   git add backend/main.py
   git commit -m "Add Render frontend to CORS origins"
   git push origin main
   ```

3. **Render Auto-Deploys**
   - Render will automatically detect the changes and redeploy your backend
   - Wait 2-3 minutes for the redeploy

---

## ✅ STEP 5: Test Everything End-to-End!

1. **Open Your Frontend**
   - Visit your frontend URL: `https://d3r-frontend.onrender.com`

2. **Navigate to Authentication**
   - Go to: `https://d3r-frontend.onrender.com/client-auth`

3. **Test Registration**
   - Click the **"Register"** tab
   - Enter your **email** and **name**
   - Click **"Create Account"**
   - You should see your **Client ID** and **Client Key** displayed
   - **Copy both credentials** (especially the Client Key!)

4. **Test Login**
   - Click **"Use These Credentials to Login"** button
   - Or manually switch to **"Login"** tab
   - Paste your **Client ID** and **Client Key**
   - Click **"Login"**
   - You should see "Login successful!" alert
   - You'll be redirected to the home page

5. **Verify Token Storage**
   - Open browser DevTools (F12)
   - Go to **Application** → **Local Storage**
   - Check if `access_token` and `client_id` are stored

---

## 🐛 Troubleshooting

### Backend Issues

**Problem**: Backend shows "Application failed to deploy"
- Check logs in Render dashboard
- Common issues:
  - Missing `requirements.txt` in backend folder
  - Wrong `Start Command` - should be `uvicorn main:app --host 0.0.0.0 --port $PORT`
  - Database connection error - verify DATABASE_URL is correct

**Problem**: Database connection error
- Make sure you copied the **Internal Database URL** (not External)
- Check that DATABASE_URL environment variable is set correctly

### Frontend Issues

**Problem**: Frontend shows blank page
- Check browser console for errors (F12)
- Verify `VITE_API_URL` is set correctly in Render environment variables
- Make sure backend is running first

**Problem**: CORS error in browser
- Verify you added your frontend URL to CORS origins in `main.py`
- Check that changes are pushed and backend redeployed

**Problem**: "Network error" when logging in
- Check that `VITE_API_URL` matches your actual backend URL
- Verify backend is running (visit backend URL, should show welcome message)

### General Tips

- **Free tier cold starts**: Render free tier apps sleep after 15 min of inactivity. First request takes 30-60 seconds to wake up.
- **Logs are your friend**: Always check the logs in Render dashboard when something fails
- **Test locally first**: Make sure everything works on localhost before deploying

---

## 🎉 Success!

Your D3R application is now live on Render with Client ID/Key authentication!

- **Backend**: `https://d3r-backend.onrender.com`
- **Frontend**: `https://d3r-frontend.onrender.com`
- **Database**: PostgreSQL on Render

You can share your frontend URL with others to let them register and use your restaurant app!

---

## 📝 Next Steps

1. **Share your app**: Give the frontend URL to friends/colleagues to test
2. **Monitor usage**: Check Render dashboard for metrics and logs
3. **Upgrade if needed**: If you get more traffic, consider upgrading from free tier
4. **Add custom domain**: You can add your own domain name in Render settings

---

## 💡 Important Notes

- **Free Tier Limitations**:
  - Backend and database sleep after 15 minutes of inactivity
  - 750 hours/month free (enough for small projects)
  - First request after sleep takes 30-60 seconds

- **Security**:
  - Never commit your real `.env` file with secrets
  - Use `.env.example` as a template
  - Keep your `SECRET_KEY` secure
  - Don't share your Client Keys publicly

- **Database Backups**:
  - Render free PostgreSQL doesn't include automatic backups
  - Consider exporting data regularly if important

---

Need help? Check the Render documentation or ask for assistance!
