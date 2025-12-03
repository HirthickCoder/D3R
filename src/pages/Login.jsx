// src/pages/Login.jsx
import React from 'react';
import { useMsal, useIsAuthenticated } from '@azure/msal-react';
import { loginRequest } from '../authConfig';

export default function Login() {
  const { instance, accounts } = useMsal();
  const isAuthenticated = useIsAuthenticated();

  const handleLogin = async () => {
    try {
      await instance.loginPopup(loginRequest);
    } catch (error) {
      console.error('MSAL login error:', error);
      alert('Microsoft login failed. Please try again.');
    }
  };

  const handleLogout = async () => {
    try {
      await instance.logoutPopup({
        postLogoutRedirectUri: '/login',
      });
    } catch (error) {
      console.error('MSAL logout error:', error);
    }
  };

  const account = accounts && accounts.length > 0 ? accounts[0] : null;

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8">
        <div>
          <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
            Sign in with Microsoft
          </h2>
          <p className="mt-2 text-center text-sm text-gray-600">
            Use your Microsoft account to sign in.
          </p>
        </div>

        {isAuthenticated && account ? (
          <div className="space-y-4">
            <div className="bg-white shadow rounded p-4">
              <h3 className="text-lg font-semibold mb-2">Profile</h3>
              <p className="text-sm text-gray-700">
                <span className="font-medium">Name:</span> {account.name || 'Unknown'}
              </p>
              <p className="text-sm text-gray-700">
                <span className="font-medium">Email:</span> {account.username || 'No email found'}
              </p>
            </div>

            <button
              type="button"
              onClick={handleLogout}
              className="w-full py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
            >
              Sign out
            </button>
          </div>
        ) : (
          <div className="space-y-4">
            <button
              type="button"
              onClick={handleLogin}
              className="w-full flex justify-center items-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-gray-900 hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-900"
            >
              <img
                src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Microsoft_logo.svg/512px-Microsoft_logo.svg.png"
                alt="Microsoft"
                className="w-5 h-5 mr-2"
              />
              Sign in with Microsoft
            </button>
          </div>
        )}
      </div>
    </div>
  );
}