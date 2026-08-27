from fleet_report import fleet_summary


def test_summary_counts_due_cars():
    fleet = [
        {"id": "VOS-4471", "odometer": 14900, "last_service_km": 0},
        {"id": "VOS-1000", "odometer": 3000, "last_service_km": 0},
    ]

    summary = fleet_summary(fleet)

    assert summary["count"] == 2
    assert summary["due"] == 1


def test_summary_survives_missing_last_service_reading():
    fleet = [
        {"id": "VOS-4471", "odometer": 14900, "last_service_km": 0},
        {"id": "VOS-7788", "odometer": 92000},
    ]

    summary = fleet_summary(fleet)

    assert summary["count"] == 2
    assert summary["due"] == 1
    assert "average_wear" in summary
