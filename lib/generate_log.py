from datetime import datetime
import os

def generate_log(entries, directory="."):
    # Raise ValueError if entries is not a list
    if not isinstance(entries, list):
        raise ValueError("entries must be a list")

    # Create filename with timestamp pattern log_YYYYMMDD.txt
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    filepath = os.path.join(directory, filename)

    # Write entries to the file
    with open(filepath, "w") as file:
        for entry in entries:
            file.write(f"{entry}\n")

    # Print confirmation message
    print(f"Log written to {filename}")

    return filename

if __name__ == "__main__":
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)