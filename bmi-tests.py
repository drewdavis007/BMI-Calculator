# Drew Davis; wad108
#3-18-2025

import pytest
from BMICalc import (
    feet_and_inches_to_inches,
    calculate_bmi,
    get_bmi_category
)

# --------------------------
# Weak Nx1 Boundary Tests
# --------------------------
@pytest.mark.parametrize("feet,inches,expected", [
    (5, 8, 68),    # Valid input (ON boundary)
    (0, 11, 11),   # Edge case (ON boundary)
    (-1, 5, None), # OFF boundary (invalid feet)
    (3, 12, None)  # OFF boundary (invalid inches)
])
def test_feet_conversion(feet, inches, expected):
    if expected is None:
        with pytest.raises(ValueError):
            feet_and_inches_to_inches(feet, inches)
    else:
        assert feet_and_inches_to_inches(feet, inches) == expected

@pytest.mark.parametrize("weight,height,expected", [
    (150, 65, 24.96),  # ON boundary (Normal Weight)
    (180, 72, 24.4),   # Interior point (Normal)
    (0, 65, None),      # OFF boundary (invalid)
    (150, 0, None)      # OFF boundary (invalid)
])
def test_bmi_calculation(weight, height, expected):
    if expected is None:
        with pytest.raises(ValueError):
            calculate_bmi(weight, height)
    else:
        assert calculate_bmi(weight, height) == pytest.approx(expected, abs=0.1)

# Weak Nx1 Tests for Category Boundaries
@pytest.mark.parametrize("bmi,expected", [
    # ON Points
    (18.5, "Normal Weight"),
    (24.9, "Normal Weight"),
    (25.0, "Overweight"),
    (29.9, "Overweight"),
    (30.0, "Obese"),
    
    # OFF Points (ε = 0.1)
    (18.4, "Underweight"),
    (24.8, "Normal Weight"),
    (24.9, "Normal Weight"),
    (29.8, "Overweight"),
    
    # Interior Points
    (20.0, "Normal Weight"),
    (27.0, "Overweight"),
    (35.0, "Obese")
])
def test_category_boundaries(bmi, expected):
    assert get_bmi_category(bmi) == expected

# --------------------------
# Boundary Shift Test
# --------------------------
def test_boundary_shift():
    """Test for shifted boundary (18.5 → 18.4)"""
    
    # Original boundary test (should pass)
    assert get_bmi_category(18.5) == "Normal Weight"
    
    # Induce boundary shift
    def shifted_category(bmi: float) -> str:
        if bmi < 18.4:  # Shifted boundary
            return "Underweight"
        elif 18.4 <= bmi <= 24.9:
            return "Normal Weight"
        elif 25.0 <= bmi <= 29.9:
            return "Overweight"
        else:
            return "Obese"
    
    # Test OFF point (18.4 should now fail)
    assert shifted_category(18.4) == "Underweight"  # This will FAIL