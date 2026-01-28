def calculate_bmi(weight, height):
    """Calculates BMI and returns the health status."""
    try:
        bmi = weight / (height ** 2)
        
        if bmi < 18.5:
            return f"BMI: {bmi:.2f} - Status: Underweight (Untergewicht)"
        elif bmi < 25.0:
            return f"BMI: {bmi:.2f} - Status: Normal (Normalgewicht)"
        else:
            return f"BMI: {bmi:.2f} - Status: Overweight (Übergewicht)"
    except ZeroDivisionError:
        return "Error: Height cannot be zero!"

if __name__ == "__main__":
    try:
        w = float(input("Enter weight (kg): "))
        h = float(input("Enter height (m): "))
        print(calculate_bmi(w, h))
    except ValueError:
        print("Please enter numeric values only.")
