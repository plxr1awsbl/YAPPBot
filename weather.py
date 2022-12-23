import pyowm

owm = pyowm.OWM('47826deb044aade08003b5955d4f7e2f')
manager = owm.weather_manager()
observation = manager.forecast_at_place('Moscow', 'daily')
weather = observation.weather

print(weather.temperature('celsius'))