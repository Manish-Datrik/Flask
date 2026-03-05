import requests
from flask import Blueprint, render_template, current_app
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    # PRODUCTS API
    product_api = "https://fakestoreapi.com/products"
    try:
        product_response = requests.get(product_api)
        products = product_response.json()
    except Exception as e:
        products = []
        print(f"Error fetching products: {e}")

    # WEATHER API
    api_key = current_app.config['WEATHER_API_KEY']
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q=Hyderabad&appid={api_key}&units=metric"
    
    try:
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()
        temperature = weather_data['main']['temp']
        weather_desc = weather_data['weather'][0]['description']
    except Exception as e:
        temperature = "N/A"
        weather_desc = "Could not fetch weather"
        print(f"Error fetching weather: {e}")

    return render_template(
        "home.html",
        products=products,
        weather=weather_desc,
        temperature=temperature,
        user=current_user
    )

@views.route('/learn-more')
def learn_more():
    return "<h1>Learn More Page</h1><p>Our cosmetics are made with ❤️ in India.</p><a href='/'>Back to Home</a>"