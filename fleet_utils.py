MILES_PER_KM = 0.621371


def km_to_miles(km: float) -> float:
    """Convert kilometres to miles."""
    return km * MILES_PER_KM


def format_number(value: float) -> str:
    """Format a number with two decimal places."""
    return f"{value:.2f}"
