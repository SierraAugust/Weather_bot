# Weather Bot

A simple Flask web application that provides current weather information and 3-day forecasts for any city using the WeatherAPI service.

## Features

- Current weather conditions
- 3-day weather forecast
- Clean web interface
- Command line interface option

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file and add your WeatherAPI key:

```
API_KEY=your_weatherapi_key_here
```

3. Get your free API key from [WeatherAPI.com](https://www.weatherapi.com/)

## Usage

### Web Interface

```bash
python app.py
```

Visit http://127.0.0.1:5000 in your browser.

### Command Line Interface

```bash
python cli_bot.py
```

## Project Structure

- `app.py` - Flask web application
- `cli_bot.py` - Command line interface
- `weather_api.py` - API communication functions
- `formatter.py` - Data formatting utilities
- `config.py` - Configuration and environment variables
- `templates/index.html` - Web interface template
- `static/styles.css` - Styling for web interface

## Requirements

- Python 3.6+
- Flask
- requests
- python-dotenv
- WeatherAPI.com API key
