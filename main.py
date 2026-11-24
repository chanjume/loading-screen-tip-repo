#!/usr/bin/env python3
"""Write one loading-screen tip to /output/entry.txt.

The tip: your build isn't stuck, it's just thinking — like you were for
40 minutes before renaming that variable from data2 to final_data_v3.
The joke lands because every developer recognises the 40-minute rename
dither; the twist reframes a stuck build as the machine doing exactly
what the developer just did. Concrete details (40 minutes, data2,
final_data_v3) keep it specific and real.
The tip is 179 characters, inside the 200-character cap.
"""
import os

TIP = (
    "Tip: your build isn't stuck, it's just thinking — like you were for "
    "40 minutes before renaming that variable from data2 to "
    "final_data_v3 — and then to final_data_v3_REAL. Breathe."
)


def main():
    assert 1 <= len(TIP) <= 200, f"tip must be 1-200 characters, got {len(TIP)}"
    assert TIP.strip() == TIP, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TIP + "\n")


if __name__ == "__main__":
    main()
