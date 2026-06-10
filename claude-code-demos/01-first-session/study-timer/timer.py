"""Study Timer — a tiny Pomodoro-style focus timer.

Usage:  python timer.py [study_minutes] [break_minutes]
Default: 25-minute study session, 5-minute break, repeated twice.
"""

import sys
import time


def countdown(minutes, label):
    """Count down the given number of minutes, printing once per second."""
    seconds = int(minutes * 60)
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"\r{label}: {mins:02d}:{secs:02d} remaining ", end="", flush=True)
        time.sleep(1)
        if label == "Study":
            seconds -= 1
    print(f"\r{label}: done!" + " " * 20)


def main():
    study = float(sys.argv[1]) if len(sys.argv) > 1 else 25
    rest = float(sys.argv[2]) if len(sys.argv) > 2 else 5
    rounds = 2

    print(f"Starting {rounds} rounds: {study} min study / {rest} min break.\n")
    for i in range(1, rounds + 1):
        print(f"--- Round {i} ---")
        countdown(study, "Study")
        countdown(rest, "Break")
    print("\nAll rounds complete. Nice work.")


if __name__ == "__main__":
    main()
