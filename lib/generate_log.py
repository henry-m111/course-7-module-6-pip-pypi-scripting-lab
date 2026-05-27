from datetime import datetime
import os

def generate_log(data):
    # Raise ValueError if data is not a list
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    # Create filename with timestamp pattern log_YYYYMMDD.txt
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write entries to the file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # Print confirmation message
    print(f"Log written to {filename}")

    return filename

if __name__ == "__main__":
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)