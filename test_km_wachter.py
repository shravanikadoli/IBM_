from km_wachter import needs_service, wear_percent


def test_almost_due_car_is_flagged():
    car = {
        "id": "VOS-4471",
        "odometer": 14900,
        "last_service_km": 0,
    }

    assert needs_service(car) is True


def test_missing_reading_is_not_treated_as_zero():
    car = {
        "id": "VOS-7788",
        "odometer": 92000,
    }

    assert needs_service(car) is False


def test_wear_percent_keeps_fractional_progress():
    assert 99 <= wear_percent(14900, 15000) <= 100


def test_car_below_warning_threshold_is_not_flagged():
    car = {
        "id": "VOS-1000",
        "odometer": 11000,
        "last_service_km": 0,
    }

    assert needs_service(car) is False
