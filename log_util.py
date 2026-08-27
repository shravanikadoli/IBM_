DEBUG = False
LOG_LINES: list[str] = []


def log(message: str) -> None:
    """Store a log message and print it in debug mode."""
    LOG_LINES.append(message)

    if DEBUG:
        print(f"LOG: {message}")


def flush_log(filename: str = "km_wachter.log") -> None:
    """Write stored log messages to a file."""
    with open(filename, "a", encoding="utf-8") as file:
        for line in LOG_LINES:
            file.write(f"{line}\n")

    LOG_LINES.clear()
