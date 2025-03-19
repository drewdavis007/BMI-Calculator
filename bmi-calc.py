// Drew Davis; wad108
// 3-18-2025

def feet_and_inches_to_inches(feet: int, inches: int) -> int:
    """Convert height from feet and inches to total inches."""
    if feet < 0:
        raise ValueError("Feet cannot be negative.")
    if inches < 0 or inches >= 12:
        raise ValueError("Inches must be between 0 and 11.")
    return feet * 12 + inches

def calculate_bmi(weight: float, height_inches: int) -> float:
    """Calculate BMI using weight in pounds and height in inches."""
    if height_inches <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight <= 0:
        raise ValueError("Weight must be greater than zero.")
    
    bmi = (weight / (height_inches ** 2)) * 703
    return round(bmi, 1)

def get_bmi_category(bmi: float) -> str:
    """Determine BMI category based on BMI value."""
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
    
    # Get height input
    while True:
        try:
            feet = int(input("Enter your height [feet]: "))
            inches = int(input("Enter your height [inches]: "))
            height_inches = feet_and_inches_to_inches(feet, inches)
            break
        except ValueError as e:
            print(f"Invalid input: {e}\n")

    # Get weight input
    while True:
        try:
            weight = float(input("\nEnter your weight in pounds: "))
            if weight <= 0:
                raise ValueError("Weight must be positive.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    # Calculate and display results
    bmi = calculate_bmi(weight, height_inches)
    category = get_bmi_category(bmi)
    
    print(f"\nResults:")
    print(f"BMI: {bmi}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()
