
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


def main():
    print("Temperature Converter")
    print("Units: C = Celsius, F = Fahrenheit, K = Kelvin")

    try:
        temp = float(input("Enter temperature: "))
        from_unit = input("Convert from (C/F/K): ").strip().upper()
        to_unit = input("Convert to (C/F/K): ").strip().upper()

        if from_unit not in ("C", "F", "K") or to_unit not in ("C", "F", "K"):
            print("Invalid unit! Use C, F, or K.")
            return

        # Validate absolute zero
        minimum = {"C": -273.15, "F": -459.67, "K": 0}

        if temp < minimum[from_unit]:
            print("Invalid temperature: below absolute zero.")
            return

        # Select the appropriate conversion function
        conversions = {
            ("C", "F"): celsius_to_fahrenheit,
            ("F", "C"): fahrenheit_to_celsius,
            ("C", "K"): celsius_to_kelvin,
            ("K", "C"): kelvin_to_celsius,
            ("F", "K"): fahrenheit_to_kelvin,
            ("K", "F"): kelvin_to_fahrenheit
        }

        if from_unit == to_unit:
            result = temp
        else:
            result = conversions[(from_unit, to_unit)](temp)

        print(f"Converted temperature: {result:.2f} {to_unit}")

    except ValueError:
        print("Invalid input! Enter a numeric temperature.")


if __name__ == "__main__":
    main()
