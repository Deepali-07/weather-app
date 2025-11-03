# 🌦️ Flask Weather App

A simple and elegant **Weather App** built with **Python (Flask)** and the **OpenWeatherMap API**.  
It shows real-time weather information for any city, with a clean UI, gradient backgrounds, and error handling.

## 🚀 Features

✅ Search weather by city name  
✅ Displays temperature, weather description, and icons  
✅ Error handling for invalid cities or API failures  
✅ Beautiful responsive UI with gradients and shadows  
✅ Simple Flask backend connected to OpenWeatherMap API  

## 🖼️ Preview

![Weather App Screenshot](https://user-images.githubusercontent.com/YOUR_GITHUB_USERNAME/placeholder.png)  
*(Add your own screenshot here later!)*

## ⚙️ Setup Instructions

### 1️⃣ Clone this repository
```bash
git clone https://github.com/Deepali-07/weather-app.git
cd weather-app
2️⃣ Create a virtual environment (recommended)
bash
Copy code
python -m venv env
Activate it:

On Windows:

bash
Copy code
env\Scripts\activate
On Mac/Linux:

bash
Copy code
source env/bin/activate
3️⃣ Install dependencies
bash
Copy code
pip install flask requests
4️⃣ Get your OpenWeatherMap API Key
Go to https://openweathermap.org/api

Sign up (free)

Copy your API Key

Open app.py and replace:

python
Copy code
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
with your actual key.

5️⃣ Run the app
bash
Copy code
python app.py
Then open your browser and visit:
👉 http://localhost:5000

🧩 Project Structure
csharp
Copy code
weather-app/
│
├── app.py                  # Main Flask backend
├── static/
│   └── style.css           # Frontend styles (gradients, shadows)
├── templates/
│   ├── index.html          # Main page template
│   └── error.html          # Error handling template
├── .gitignore
└── README.md
💡 How It Works
User enters a city name in the search box

Flask calls the OpenWeatherMap API with the city

Weather data (temperature, description, icon) is fetched in JSON

Displayed beautifully on the web page

🪲 Common Issues
Problem	Solution
❌ "Invalid API Key"	Ensure you replaced YOUR_OPENWEATHERMAP_API_KEY correctly
🌐 "Connection Error"	Check your internet connection or API URL
🏙️ "City Not Found"	Try a valid city name like London, Hyderabad, New York

🧰 Tech Stack
Backend: Flask (Python)

Frontend: HTML, CSS

API: OpenWeatherMap

Version Control: Git & GitHub

🧑‍💻 Author
👩‍💻 Deepali Madala
📧 deepalimadala@gmail.com

🪄 License
This project is open-source and available under the MIT License.
