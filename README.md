# FoodieHub - Restaurant Food Ordering System

A modern, full-stack restaurant food ordering application built with React and Flask.

## 🚀 Features

- **Browse Menu**: View delicious food items with images and descriptions
- **Shopping Cart**: Add items to cart with quantity management
- **Checkout System**: Mock payment processing for demonstration
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Modern UI**: Clean, professional interface with smooth animations

## 🛠️ Tech Stack

### Frontend
- React 18
- React Router for navigation
- Tailwind CSS for styling
- Lucide React for icons
- Vite for build tooling

### Backend
- Python Flask
- Flask-CORS for cross-origin requests
- RESTful API architecture

## 📦 Installation

### Prerequisites
- Node.js (v16 or higher)
- Python 3.8+
- npm or yarn

### Frontend Setup
```bash
npm install
npm run dev
```

### Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux
pip install -r requirements.txt
python run_server.py
```

## 🌐 Deployment

### GitHub Repository
https://github.com/HirthickCoder/D3R

### Azure Deployment

#### Frontend (Azure Static Web Apps)
- Build command: `npm run build`
- Output directory: `dist`
- Configuration: `staticwebapp.config.json`

#### Backend (Azure App Service)
- Runtime: Python 3.x
- Startup file: `run_server.py`
- Location: `/backend`

## 🧪 Testing

Use any card details for testing the checkout:
- **Card Number**: Any 16 digits (e.g., 4242 4242 4242 4242)
- **Expiry**: Any future date (e.g., 12/25)
- **CVC**: Any 3 digits (e.g., 123)

## 📝 Environment Variables

Create a `.env` file in the root directory:
```
PORT=3001
```

## 🤝 Contributing

This is a demonstration project. Feel free to fork and modify for your own use.

## 📄 License

MIT License - feel free to use this project for learning and demonstration purposes.

## 👨‍💻 Author

**HirthickCoder**
- GitHub: [@HirthickCoder](https://github.com/HirthickCoder)

## 🙏 Acknowledgments

- Built as a full-stack portfolio project
- Demonstrates modern web development practices
- No real payment processing - for demonstration only
