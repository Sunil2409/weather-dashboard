Weather Dashboard
A real-time weather and air quality monitoring application built with Python and Django. This dashboard allows users to search for a city and instantly retrieve current weather conditions alongside the Air Quality Index (AQI).

🚀 Features
Real-time Weather: Fetches temperature, humidity, and coordinates using the OpenWeatherMap API.

Air Quality Integration: Automatically calculates and displays AQI based on the city's latitude and longitude.

Clean UI: A simple, intuitive dashboard interface for quick data visualization.

Modular Design: Uses a dedicated utils.py for API handling to keep the codebase clean.

🛠️ Tech Stack
Backend: Django (Python)

API: OpenWeatherMap

Frontend: HTML/CSS (Django Templates)

⚙️ Installation & Setup
Follow these steps to get the project running locally:

1. Clone the repository

Bash
git clone https://github.com/Sunil2409/weather-dashboard.git
cd weather-dashboard
2. Set up a Virtual Environment

Bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies

Bash
pip install django requests python-dotenv
4. Configuration (API Key)

You need an API key from OpenWeatherMap.

Create a .env file in the root directory.

Add your key:

Code snippet
OPENWEATHER_API_KEY=your_api_key_here
Note: Ensure your settings.py is configured to read this environment variable or use getattr(settings, 'OPENWEATHER_API_KEY') as seen in the views.

5. Run Migrations

Bash
python manage.py migrate
6. Start the Server

Bash
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.

📂 Project Structure Highlights
views.py: Handles the logic for processing POST requests and coordinating between weather and AQI data.

utils.py: Contains helper functions (fetch_weather, fetch_air_quality) to interact with external APIs.

home.html: The frontend template that renders the weather cards and search bar.

📝 Future Roadmap
[ ] Add a 5-day weather forecast.

[ ] Implement user accounts to save "Favorite Cities."

[ ] Add background images that change based on weather conditions (e.g., rain, sun).

[ ] Deploy to Heroku or PythonAnywhere.

🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.