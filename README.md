# 🌦️ Flask Weather App

A simple and elegant **Weather App** built with **Python (Flask)** and the **OpenWeatherMap API**.  
It displays real-time weather details for any city in the world — with a clean, responsive interface and proper error handling.

---

## 🚀 Features

- 🔍 Search weather by city name  
- 🌡️ Displays temperature, description, humidity, and weather icon  
- ⚠️ Handles errors for invalid city names or API issues  
- 🎨 Beautiful responsive design with gradient backgrounds  
- ⚙️ Flask backend connected to the OpenWeatherMap API  

---

## ⚙️ Setup Instructions

### 🧩 Step 1: Clone this repository
```bash
git clone https://github.com/Deepali-07/weather-app.git
cd weather-app
````

### 🧩 Step 2: Create a virtual environment

```bash
python -m venv env
```

Activate it:
**Windows**

```bash
env\Scripts\activate
```

**Mac/Linux**

```bash
source env/bin/activate
```

### 🧩 Step 3: Install dependencies

```bash
pip install flask requests
```

### 🧩 Step 4: Get your OpenWeatherMap API Key

1. Go to [OpenWeatherMap API](https://openweathermap.org/api)
2. Sign up for a free account
3. Copy your API key
4. Open `app.py` and replace:

   ```python
   API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
   ```

   with your actual key.

### 🧩 Step 5: Run the app

```bash
python app.py
```

Then open your browser and visit:
👉 [http://localhost:5000](http://localhost:5000)

---

## 📂 Project Structure

```
weather-app/
│
├── app.py                  # Flask backend
├── static/
│   └── style.css           # Styling for frontend
├── templates/
│   ├── index.html          # Main weather page
│   └── error.html          # Error page for invalid input
├── .gitignore
└── README.md
```

---

## 💡 How It Works

1. User enters a city name in the search box
2. Flask sends a request to the **OpenWeatherMap API**
3. The API returns weather data in JSON format
4. Flask renders it in the frontend beautifully using HTML and CSS

---

## 🪲 Common Issues & Fixes

| Issue                   | Cause                 | Solution                                                 |
| ----------------------- | --------------------- | -------------------------------------------------------- |
| ❌ Invalid API Key       | Wrong or missing key  | Check and update your API key in `app.py`                |
| 🌐 API Connection Error | Internet or URL issue | Verify internet and API URL                              |
| 🏙️ City Not Found      | Wrong spelling        | Try another city name like `London`, `Delhi`, or `Paris` |

---

## 🧰 Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS
* **API:** OpenWeatherMap
* **Version Control:** Git & GitHub

---

## 🧑‍💻 Author

**👩‍💻 Deepali Madala**
📧 deepalimadala@gmailcom
🔗 [GitHub Profile](https://github.com/Deepali-07)

---

## 🪄 License

This project is open-source and available under the [MIT License](LICENSE).

---

⭐ **If you found this project helpful, please give it a star on GitHub!**

```
