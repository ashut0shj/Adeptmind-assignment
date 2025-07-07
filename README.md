# Croma Scraper - Full Stack Project

A Python + Vue.js application that scrapes product data from Croma's Televisions & Accessories page and displays it in a beautiful frontend interface.

## 🚀 Features

- **Web Scraping**: Extracts product data from Croma website
- **Data Storage**: Stores scraped data in Redis database
- **REST API**: Flask backend with multiple endpoints
- **Modern Frontend**: Vue.js with responsive product grid
- **Real-time Data**: Live product information with prices, discounts, and offers

## 🏗️ Architecture

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Scraper   │───▶│    Redis    │───▶│   Flask     │───▶│   Vue.js    │
│  (Python)   │    │  Database   │    │   API       │    │  Frontend   │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

## 📋 Prerequisites

- Python 3.8+
- Node.js 14+
- Redis server (local or Docker)

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd project
```

### 2. Backend Setup

#### Install Python Dependencies
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Linux/macOS
# or
venv\Scripts\activate     # On Windows
pip install -r requirements.txt
```

#### Start Redis Server
```bash
# If using Docker
docker run -d -p 6379:6379 redis

# Or install Redis locally
# Follow Redis installation guide for your OS
```

#### Run the Scraper
```bash
python scraper.py
```
This will scrape data from Croma and store it in Redis.

#### Start the Flask API
```bash
python app.py
```
The API will be available at `http://localhost:5000`

### 3. Frontend Setup

#### Install Node.js Dependencies
```bash
cd frontend
npm install
```

#### Start the Vue.js Development Server
```bash
npm run serve
```
The frontend will be available at `http://localhost:8080`

## 📡 API Endpoints

### GET `/scraped-content`
Returns all scraped data including head, header, and products.

**Response:**
```json
{
  "success": true,
  "data": {
    "head": "<head>...</head>",
    "header": "<header>...</header>",
    "products": [...]
  }
}
```

### GET `/products`
Returns only the products list with prices, discounts, and offers.

**Response:**
```json
{
  "success": true,
  "products": [
    {
      "title": "Croma 109 cm (43 inch) Full HD LED Smart Linux TV",
      "price": "₹15,990",
      "old_price": "₹34,000",
      "discount": "53%Off",
      "tags": ["Extra 1000 Discount", "No Cost EMI"],
      "link": "https://www.croma.com/...",
      "product_id": "273733"
    }
  ]
}
```

## 🎨 Frontend Features

- **Responsive Grid Layout**: Product cards adapt to screen size
- **Modern Design**: Clean, professional e-commerce styling
- **Product Information**: Title, price, discount, offers, and links
- **Hover Effects**: Interactive product cards
- **Real Data**: Displays actual scraped product information

## 🔧 Project Structure

```
project/
├── backend/
│   ├── app.py          # Flask API server
│   ├── scraper.py      # Web scraping logic
│   ├── requirements.txt # Python dependencies
│   └── venv/          # Virtual environment
├── frontend/
│   ├── src/
│   │   ├── App.vue    # Main Vue component
│   │   ├── Product.vue # Product card component
│   │   └── main.js    # Vue app entry point
│   ├── package.json   # Node.js dependencies
│   └── public/        # Static assets
└── README.md          # This file
```

## 🚀 Usage

1. **Start Redis**: Ensure Redis is running on `localhost:6379`
2. **Run Scraper**: `python backend/scraper.py` to fetch latest data
3. **Start Backend**: `python backend/app.py` to serve the API
4. **Start Frontend**: `npm run serve` in frontend directory
5. **View Application**: Open `http://localhost:8080` in browser

## 🔄 Data Flow

1. **Scraper** fetches data from Croma website
2. **Redis** stores the scraped data
3. **Flask API** serves data to frontend
4. **Vue.js** displays products in a beautiful grid

## 🛠️ Development

### Adding New Features
- **Backend**: Add new endpoints in `app.py`
- **Frontend**: Create new Vue components in `frontend/src/`
- **Scraping**: Modify `scraper.py` for different data sources

### Customization
- **Styling**: Modify CSS in Vue components
- **API**: Add new endpoints for different data views
- **Scraping**: Change target website or data structure

## 📝 Notes

- Ensure Redis is running before starting the application
- The scraper runs silently and stores data in Redis
- The API provides both full data and product-only endpoints
- The frontend automatically fetches and displays product data

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test the application
5. Submit a pull request

## 📄 License

This project is for educational purposes and demonstrates web scraping, API development, and frontend integration.