# Drew Davis; wad108
#3-18-2025

def feet_and_inches_to_inches(feet: int, inches: int) -> int:
    """Convert height to total inches with validation."""
    if feet < 0:
        raise ValueError("Feet cannot be negative.")
    if inches < 0 or inches >= 12:
        raise ValueError("Inches must be 0-11.")
    return feet * 12 + inches

def calculate_bmi(weight: float, height_inches: int) -> float:
    """Calculate BMI rounded to 1 decimal place."""
    if weight <= 0 or height_inches <= 0:
        raise ValueError("Weight/height must be positive.")
    return round((weight / (height_inches ** 2)) * 703, 1)

def get_bmi_category(bmi: float) -> str:
    """Classify BMI into categories (Original Version)."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal Weight"
    elif 25.0 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("BMI Calculator\n")
    
    # Get height
    while True:
        try:
            feet = int(input("Height (feet): "))
            inches = int(input("Height (inches): "))
            height = feet_and_inches_to_inches(feet, inches)
            break
        except ValueError as e:
            print(f"Error: {e}\n")

    # Get weight
    while True:
        try:
            weight = float(input("\nWeight (lbs): "))
            if weight <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid weight. Must be > 0.")

    # Calculate and display
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)
    print(f"\nBMI: {bmi} → {category}")

if __name__ == "__main__":
    main()