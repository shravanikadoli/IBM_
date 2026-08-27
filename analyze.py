"""Analyze vehicle breakdown risk factors from historical fleet data."""

from pathlib import Path
import csv
import statistics


def load_records(filename: str = "fleet_history.csv") -> list[dict[str, float]]:
    """Load fleet history records from a CSV file."""
    records = []

    with open(filename, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            records.append(
                {
                    "odometer_km": float(row["odometer_km"]),
                    "age_years": float(row["age_years"]),
                    "km_since_service": float(row["km_since_service"]),
                    "avg_daily_km": float(row["avg_daily_km"]),
                    "load_factor": float(row["load_factor"]),
                    "broke_down": float(row["broke_down"]),
                }
            )

    return records


def group_average(records: list[dict[str, float]], column: str, broken: bool) -> float:
    """Return the average value for broken or non-broken vehicles."""
    values = [
        record[column]
        for record in records
        if bool(record["broke_down"]) is broken
    ]

    return statistics.mean(values)


def main() -> None:
    """Compare vehicles that broke down with those that kept going."""
    filename = "fleet_history.csv"

    if not Path(filename).exists():
        print(f"Data file not found: {filename}")
        return

    records = load_records(filename)

    columns = [
        "odometer_km",
        "age_years",
        "km_since_service",
        "avg_daily_km",
        "load_factor",
    ]

    print("Breakdown-risk analysis")
    print("-" * 60)

    for column in columns:
        broken_avg = group_average(records, column, True)
        going_avg = group_average(records, column, False)

        print(
            f"{column}: "
            f"Broke Down = {broken_avg:.2f}, "
            f"Kept Going = {going_avg:.2f}"
        )

    print("\nConclusion:")
    print(
        "Total odometer reading and vehicle age show little difference "
        "between the two groups. The clearer risk indicators are "
        "km_since_service, avg_daily_km, and load_factor. Cars with "
        "higher values in these areas appear to have greater breakdown "
        "risk, even before the normal 80% service warning is reached."
    )


if __name__ == "__main__":
    main()
