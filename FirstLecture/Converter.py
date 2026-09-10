def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kelvin_to_celsius(k):
    return k - 273.15

def log_conversion(value, unit_from, unit_to, result):
    history.append(f"{value}{unit_from} -> {result:.2f}{unit_to}")