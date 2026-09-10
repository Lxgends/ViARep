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

def convert(value, unit_from, unit_to):
    if unit_from == "C" and unit_to == "F":
        result = celsius_to_fahrenheit(value)
    elif unit_from == "C" and unit_to == "K":
        result = celsius_to_kelvin(value)
    elif unit_from == "F" and unit_to == "C":
        result = fahrenheit_to_celsius(value)
    elif unit_from == "K" and unit_to == "C":
        result = kelvin_to_celsius(value)
    else:
        raise ValueError(f"Unsupported conversion: {unit_from} -> {unit_to}")

    log_conversion(value, unit_from, unit_to, result)
    return result

def print_history():
    for entry in history:
        print(entry)

def main():
    print(convert(0, "C", "F"))
    print(convert(100, "C", "K"))
    print(convert(98.6, "F", "C"))
    print(convert(0, "K", "C"))
    print_history()

if __name__ == "__main__":
    main()