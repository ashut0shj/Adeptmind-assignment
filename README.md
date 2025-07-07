# Croma Scraper Project

A Python + Vue.js app that scrapes product data from Croma's Televisions & Accessories page and displays it in a frontend interface.

## What I Built

### Backend Logic
- **Scraper**: Extracts head, header, and product data from Croma website using BeautifulSoup
- **Redis Storage**: Stores scraped data in Redis database for quick access
- **Flask API**: Provides endpoints to serve the scraped data to frontend

### API Endpoints
- **`/scraped-content`**: Returns all scraped data (head, header, products)
- **`/products`**: Returns only the products list with prices, discounts, and offers

### Frontend
- **Vue.js App**: Displays products in a responsive grid layout
- **Product Cards**: Shows title, price, old price, discount, and tags
- **Real Data**: Fetches and displays actual scraped product information

## Setup Steps

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Start Redis (if not running)
redis-server

# Run scraper to fetch data
python scraper.py

# Start Flask API
python app.py
```

### Frontend Setup
```bash
cd frontend
npm install
npm run serve
```

## How It Works

1. **Scraper** fetches HTML from Croma website and extracts product data
2. **Redis** stores the scraped data for the API to serve
3. **Flask API** provides endpoints to access the stored data
4. **Vue.js Frontend** fetches data from API and displays products

