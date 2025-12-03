@echo off
echo ========================================
echo   DEPLOY TO AZURE - SUPER EASY METHOD
echo ========================================
echo.
echo This will push your code to GitHub,
echo which will automatically deploy to Azure!
echo.
echo Your GitHub: https://github.com/HirthickCoder/D3R
echo Your Azure: https://d3projectrestaurantsofficial.azurewebsites.net
echo.
pause

cd /d "%~dp0"

echo.
echo [1/4] Adding all changes to git...
git add .

echo.
echo [2/4] Committing changes...
git commit -m "Deploy backend to Azure - %date% %time%"

echo.
echo [3/4] Pushing to GitHub...
git push origin main

echo.
echo [4/4] Done! GitHub Actions will deploy to Azure automatically.
echo.
echo ========================================
echo   WHAT TO DO NEXT:
echo ========================================
echo.
echo 1. Go to: https://github.com/HirthickCoder/D3R/actions
echo 2. Watch the deployment progress
echo 3. Once complete, test at:
echo    https://d3projectrestaurantsofficial.azurewebsites.net/api/menu
echo.
echo ========================================
pause
