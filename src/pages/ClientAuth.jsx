import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { FaKey, FaCopy, FaCheck } from 'react-icons/fa';

export default function ClientAuth() {
    const navigate = useNavigate();
    const [activeTab, setActiveTab] = useState('register');
    const [copiedField, setCopiedField] = useState('');

    // Registration state
    const [registerData, setRegisterData] = useState({
        email: '',
        name: ''
    });

    // Login state
    const [loginData, setLoginData] = useState({
        client_id: '',
        client_key: ''
    });

    // Response state
    const [credentials, setCredentials] = useState(null);
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    // Copy to clipboard
    const copyToClipboard = (text, field) => {
        navigator.clipboard.writeText(text);
        setCopiedField(field);
        setTimeout(() => setCopiedField(''), 2000);
    };

    // Handle Registration
    const handleRegister = async (e) => {
        e.preventDefault();
        setError('');
        setLoading(true);

        try {
            const response = await fetch('http://localhost:8000/api/auth/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(registerData),
            });

            const data = await response.json();

            if (response.ok) {
                setCredentials(data);
                setRegisterData({ email: '', name: '' });
            } else {
                setError(data.detail || 'Registration failed');
            }
        } catch (err) {
            setError('Network error. Please ensure backend is running on port 8000.');
        } finally {
            setLoading(false);
        }
    };

    // Handle Login
    const handleLogin = async (e) => {
        e.preventDefault();
        setError('');
        setLoading(true);

        try {
            const response = await fetch('http://localhost:8000/api/auth/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(loginData),
            });

            const data = await response.json();

            if (response.ok) {
                // Store token in localStorage
                localStorage.setItem('access_token', data.access_token);
                localStorage.setItem('client_id', loginData.client_id);

                // Redirect to home
                alert('Login successful!');
                navigate('/');
            } else {
                setError(data.detail || 'Login failed');
            }
        } catch (err) {
            setError('Network error. Please ensure backend is running on port 8000.');
        } finally {
            setLoading(false);
        }
    };

    // Use saved credentials to login
    const useCredentialsToLogin = () => {
        if (credentials) {
            setLoginData({
                client_id: credentials.client_id,
                client_key: credentials.client_key
            });
            setActiveTab('login');
        }
    };

    return (
        <div className="min-h-screen bg-gradient-to-br from-orange-50 to-orange-100 flex items-center justify-center p-4">
            <div className="max-w-md w-full bg-white rounded-2xl shadow-2xl overflow-hidden">
                {/* Header */}
                <div className="bg-gradient-to-r from-orange-500 to-orange-600 p-6 text-center">
                    <div className="w-16 h-16 bg-white rounded-full flex items-center justify-center mx-auto mb-3">
                        <FaKey className="text-orange-500 text-3xl" />
                    </div>
                    <h1 className="text-2xl font-bold text-white">Welcome to FoodieHub</h1>
                    <p className="text-orange-100 text-sm mt-1">Secure Client ID & Key Authentication</p>
                </div>

                {/* Saved Credentials Display */}
                {credentials && (
                    <div className="bg-green-50 border-2 border-green-200 rounded-lg p-4 m-6">
                        <div className="flex items-start mb-3">
                            <FaCheck className="text-green-500 text-xl mt-1 mr-2" />
                            <div className="flex-1">
                                <h3 className="font-bold text-green-800">Save Your Credentials!</h3>
                                <p className="text-sm text-green-700">Your Client Key will only be shown once. Please save both credentials securely.</p>
                            </div>
                        </div>

                        {/* Client ID */}
                        <div className="mb-3">
                            <label className="block text-xs font-semibold text-gray-600 mb-1">CLIENT ID</label>
                            <div className="flex items-center bg-white border border-green-300 rounded-lg p-2">
                                <input
                                    type="text"
                                    value={credentials.client_id}
                                    readOnly
                                    className="flex-1 bg-transparent text-sm font-mono outline-none"
                                />
                                <button
                                    onClick={() => copyToClipboard(credentials.client_id, 'id')}
                                    className="ml-2 text-green-600 hover:text-green-800"
                                    title="Copy to clipboard"
                                >
                                    {copiedField === 'id' ? <FaCheck /> : <FaCopy />}
                                </button>
                            </div>
                        </div>

                        {/* Client Key */}
                        <div className="mb-4">
                            <label className="block text-xs font-semibold text-gray-600 mb-1">CLIENT KEY (SECRET)</label>
                            <div className="flex items-center bg-white border border-green-300 rounded-lg p-2">
                                <input
                                    type="text"
                                    value={credentials.client_key}
                                    readOnly
                                    className="flex-1 bg-transparent text-sm font-mono outline-none"
                                />
                                <button
                                    onClick={() => copyToClipboard(credentials.client_key, 'key')}
                                    className="ml-2 text-green-600 hover:text-green-800"
                                    title="Copy to clipboard"
                                >
                                    {copiedField === 'key' ? <FaCheck /> : <FaCopy />}
                                </button>
                            </div>
                        </div>

                        {/* Use Credentials Button */}
                        <button
                            onClick={useCredentialsToLogin}
                            className="w-full bg-green-500 hover:bg-green-600 text-white font-semibold py-2 px-4 rounded-lg transition-colors"
                        >
                            Use These Credentials to Login
                        </button>
                    </div>
                )}

                {/* Tabs */}
                <div className="flex border-b border-gray-200 px-6">
                    <button
                        onClick={() => setActiveTab('login')}
                        className={`flex-1 py-3 text-sm font-semibold ${activeTab === 'login'
                                ? 'text-orange-600 border-b-2 border-orange-600'
                                : 'text-gray-500 hover:text-gray-700'
                            }`}
                    >
                        Login
                    </button>
                    <button
                        onClick={() => setActiveTab('register')}
                        className={`flex-1 py-3 text-sm font-semibold ${activeTab === 'register'
                                ? 'text-orange-600 border-b-2 border-orange-600'
                                : 'text-gray-500 hover:text-gray-700'
                            }`}
                    >
                        Register
                    </button>
                </div>

                {/* Error Message */}
                {error && (
                    <div className="mx-6 mt-4 bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg text-sm">
                        {error}
                    </div>
                )}

                {/* Form Content */}
                <div className="p-6">
                    {activeTab === 'register' ? (
                        <form onSubmit={handleRegister} className="space-y-4">
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 mb-2">
                                    Email Address
                                </label>
                                <input
                                    type="email"
                                    required
                                    value={registerData.email}
                                    onChange={(e) => setRegisterData({ ...registerData, email: e.target.value })}
                                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none"
                                    placeholder="your@email.com"
                                />
                            </div>

                            <div>
                                <label className="block text-sm font-semibold text-gray-700 mb-2">
                                    Client Name
                                </label>
                                <input
                                    type="text"
                                    required
                                    value={registerData.name}
                                    onChange={(e) => setRegisterData({ ...registerData, name: e.target.value })}
                                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none"
                                    placeholder="Your Name or App Name"
                                />
                            </div>

                            <button
                                type="submit"
                                disabled={loading}
                                className="w-full bg-orange-500 hover:bg-orange-600 disabled:bg-orange-300 text-white font-bold py-3 px-4 rounded-lg transition-colors"
                            >
                                {loading ? 'Creating Account...' : 'Create Account'}
                            </button>

                            <p className="text-xs text-gray-500 text-center">
                                You'll receive a Client ID and Client Key after registration. Save them securely!
                            </p>
                        </form>
                    ) : (
                        <form onSubmit={handleLogin} className="space-y-4">
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 mb-2">
                                    Client ID
                                </label>
                                <input
                                    type="text"
                                    required
                                    value={loginData.client_id}
                                    onChange={(e) => setLoginData({ ...loginData, client_id: e.target.value })}
                                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none font-mono text-sm"
                                    placeholder="CL_XXXXXXXXXXXX"
                                />
                            </div>

                            <div>
                                <label className="block text-sm font-semibold text-gray-700 mb-2">
                                    Client Key (Secret)
                                </label>
                                <input
                                    type="password"
                                    required
                                    value={loginData.client_key}
                                    onChange={(e) => setLoginData({ ...loginData, client_key: e.target.value })}
                                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-orange-500 focus:border-orange-500 outline-none font-mono text-sm"
                                    placeholder="CK_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
                                />
                            </div>

                            <button
                                type="submit"
                                disabled={loading}
                                className="w-full bg-orange-500 hover:bg-orange-600 disabled:bg-orange-300 text-white font-bold py-3 px-4 rounded-lg transition-colors"
                            >
                                {loading ? 'Logging in...' : 'Login'}
                            </button>
                        </form>
                    )}
                </div>

                {/* Footer */}
                <div className="bg-gray-50 px-6 py-4 text-center border-t border-gray-200">
                    <p className="text-xs text-gray-500">
                        By continuing, you agree to our Terms of Service and Privacy Policy
                    </p>
                </div>
            </div>
        </div>
    );
}
