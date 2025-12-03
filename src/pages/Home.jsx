import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useCart } from '../context/CartContext';

const API_BASE_URL = 'http://localhost:8000';

export default function Home() {
  const { addToCart } = useCart();
  const [activeCategory, setActiveCategory] = useState('all');
  const [isLoading, setIsLoading] = useState(true);
  const [menuItems, setMenuItems] = useState([]);

  useEffect(() => {
    // Fetch menu items from backend
    const fetchMenuItems = async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/api/menu/`);
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Fetched menu items from API:', data);
        setMenuItems(data);
        setIsLoading(false);
      } catch (error) {
        console.error('Error fetching menu items:', error);
        console.warn('Using fallback: Make sure FastAPI server is running on port 8000');
        setIsLoading(false);
      }
    };

    fetchMenuItems();
  }, []);

  const categories = ['all', ...new Set(menuItems.map(item => item.category))];
  const filteredItems = activeCategory === 'all' 
    ? menuItems 
    : menuItems.filter(item => item.category === activeCategory);

  if (isLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-amber-500 mx-auto"></div>
          <p className="mt-4 text-gray-600">Loading menu items...</p>
        </div>
      </div>
    );
  }

  // Debug: Show if no items loaded
  if (menuItems.length === 0) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center p-8 bg-red-50 rounded-lg max-w-md">
          <h2 className="text-xl font-bold text-red-800 mb-4">⚠️ No Menu Items Found</h2>
          <p className="text-red-600 mb-4">Backend API returned 0 items</p>
          <div className="text-left bg-white p-4 rounded text-sm">
            <p className="font-semibold mb-2">Troubleshooting:</p>
            <ol className="list-decimal list-inside space-y-1 text-gray-700">
              <li>Check backend is running: <a href="http://localhost:8000/api/menu/" target="_blank" className="text-blue-600 underline">Test API</a></li>
              <li>Open browser console (F12) for errors</li>
              <li>Check CORS settings in backend</li>
            </ol>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Hero Section */}
      <div className="bg-gradient-to-r from-amber-500 to-orange-500 text-white py-16">
        <div className="container mx-auto px-4 text-center">
          <h1 className="text-4xl md:text-6xl font-bold mb-4">Delicious Food Delivered</h1>
          <p className="text-xl mb-8 max-w-2xl mx-auto">
            Order your favorite meals from the best restaurants in town.
          </p>
          <Link 
            to="/menu" 
            className="bg-white text-amber-600 px-8 py-3 rounded-full font-bold text-lg hover:bg-gray-100 transition"
          >
            View Full Menu
          </Link>
        </div>
      </div>

      {/* Menu Section */}
      <div className="container mx-auto px-4 py-12">
        {/* Categories Filter */}
        <div className="flex flex-wrap justify-center gap-4 mb-12">
          {categories.map((category) => (
            <button
              key={category}
              onClick={() => setActiveCategory(category)}
              className={`px-6 py-2 rounded-full font-medium capitalize ${
                activeCategory === category
                  ? 'bg-amber-500 text-white'
                  : 'bg-white text-gray-700 hover:bg-gray-100'
              }`}
            >
              {category}
            </button>
          ))}
        </div>

        {/* Menu Items Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {filteredItems.map((item) => (
            <div 
              key={item.id} 
              className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow"
            >
              <div className="relative h-48">
                <img
                  src={item.image} 
                  alt={item.name} 
                  className="w-full h-full object-cover"
                />
                {item.popular && (
                  <span className="absolute top-2 right-2 bg-amber-500 text-white text-xs font-bold px-2 py-1 rounded-full">
                    Popular
                  </span>
                )}
              </div>
              <div className="p-4">
                <div className="flex justify-between items-start">
                  <h3 className="text-xl font-bold">{item.name}</h3>
                  <span className="text-amber-600 font-bold">₹{item.price}</span>
                </div>
                <p className="text-gray-600 mt-2">{item.description}</p>
                <div className="mt-4 flex justify-between items-center">
                  <span className="text-sm text-gray-500">{item.category}</span>
                  <button
                    onClick={() => addToCart({ ...item, quantity: 1 })}
                    className="bg-amber-600 text-white px-4 py-2 rounded-lg hover:bg-amber-700 transition-colors"
                  >
                    Add to Cart
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}