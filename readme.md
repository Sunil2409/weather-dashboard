# Weather Dashboard

A real-time, production-ready weather and air quality monitoring application built with Python and Django. This dashboard allows users to search for a city and instantly retrieve current weather conditions alongside the Air Quality Index (AQI), optimized with enterprise-grade caching and database solutions.

## 🚀 Features
- **Real-time Weather**: Fetches temperature, humidity, and coordinates using the OpenWeatherMap API.
- **Air Quality Integration**: Automatically calculates and displays AQI based on the city's latitude and longitude.
- **Performance Optimized**: Implements Redis caching to minimize API calls and speed up response times.
- **Production-Ready Database**: Uses PostgreSQL for robust and scalable data management.
- **Automated CI/CD**: Integrated GitHub Actions for continuous testing and workflows.
- **Containerized**: Fully dockerized with Docker and Docker Compose for easy setup and deployment.
- **Clean UI**: A simple, intuitive dashboard interface for quick data visualization.

## 🛠️ Tech Stack
- **Backend**: Django (Python 3.11+)
- **Database**: PostgreSQL
- **Caching**: Redis
- **Containerization**: Docker & Docker Compose
- **CI/CD**: GitHub Actions
- **API**: OpenWeatherMap
- **Frontend**: HTML/CSS (Django Templates)

## ⚙️ Installation & Setup

### Option A: Using Docker (Recommended)
Follow these steps to quickly run the application using Docker.

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sunil2409/weather-dashboard.git
   cd weather-dashboard
   ```

2. **Configuration (API Key)**
   Copy the example environment file and add your OpenWeather API key:
   ```bash
   cp .env.example .env
   # Edit .env and set OPENWEATHER_API_KEY=your_api_key_here
   ```

3. **Start the containers**
   ```bash
   docker-compose up -d --build
   ```

4. **Run Migrations**
   ```bash
   docker-compose exec web python manage.py migrate
   ```
   Visit http://127.0.0.1:8000/ in your browser.

### Option B: Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sunil2409/weather-dashboard.git
   cd weather-dashboard
   ```

2. **Set up a Virtual Environment**
   ```bash
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   
   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure Services are Running**
   Make sure you have **PostgreSQL** and **Redis** running locally.

5. **Configuration**
   Create a `.env` file in the root directory and add your settings (refer to `.env.example`):
   ```ini
   DEBUG=True
   SECRET_KEY=your_secret_key
   OPENWEATHER_API_KEY=your_api_key_here
   DATABASE_URL=postgres://user:password@localhost:5432/weatherdb
   REDIS_URL=redis://127.0.0.1:6379/1
   ```

6. **Run Migrations and Start the Server**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## 📂 Project Structure Highlights
- `views.py`: Handles logic for processing requests, managing Redis cache, and rendering data.
- `utils.py`: Contains helper functions (`fetch_weather`, `fetch_air_quality`) to interact with external APIs.
- `ci.yml`: GitHub Actions workflow configuration for automated testing.
- `docker-compose.yml`: Services configuration for Django, Postgres, and Redis.

## 📝 Future Roadmap
- [ ] Add a 5-day weather forecast.
- [ ] Implement user accounts to save "Favorite Cities."
- [ ] Add background images that change based on weather conditions.
- [ ] Setup automated deployment to cloud providers.

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.