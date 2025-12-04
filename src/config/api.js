// Configuration for API endpoint
// For production, this will use the Azure backend
// For local development, it falls back to localhost

const getApiUrl = () => {
    // In production (Azure), use the environment variable or the full Azure URL
    if (import.meta.env.VITE_API_URL) {
        return import.meta.env.VITE_API_URL;
    }

    // Fallback for production if env var isn't set
    if (window.location.hostname.includes('azurewebsites.net')) {
        return 'https://d3r-restaurant-backend-b0d5c4dydbbwhycd.southeastasia-01.azurewebsites.net';
    }

    // Local development
    return 'http://localhost:8000';
};

export const API_BASE_URL = getApiUrl();

console.log('API_BASE_URL configured as:', API_BASE_URL);
