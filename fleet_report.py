from km_wachter import SERVICE_INTERVAL_KM, needs_service


def fleet_summary(fleet: list[dict]) -> dict:
    """Return a summary of the fleet's service status."""
    count = len(fleet)
    due = 0
    total_wear = 0.0

    for car in fleet:
        last_service = car.get("last_service_km")

        if last_service is None:
            wear = 0.0
        else:
            km_since_service = car["odometer"] - last_service
            wear = km_since_service / SERVICE_INTERVAL_KM * 100

        total_wear += wear

        if needs_service(car):
            due += 1

    average_wear = total_wear / count if count else 0.0

    return {
        "count": count,
        "due": due,
        "average_wear": average_wear,
    }
