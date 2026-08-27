KNOWN_KEYS = {"service_interval_km", "warn_at_percent"}


def load_settings(filename: str = "settings.cfg") -> dict[str, str]:
    """Load known settings from a configuration file."""
    settings = {}

    with open(filename, encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#") or "=" not in line:
                continue

            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()

            if key in KNOWN_KEYS:
                settings[key] = value

    return settings


def get_setting(
    settings: dict[str, str], key: str, default: str | None = None
) -> str | None:
    """Return a setting or its default value."""
    return settings.get(key, default)


def get_int(settings: dict[str, str], key: str, default: int = 0) -> int:
    """Return a setting converted to an integer."""
    value = settings.get(key)

    if value is None:
        return default

    return int(value)
