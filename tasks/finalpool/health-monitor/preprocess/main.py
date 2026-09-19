# Preprocessing script for health-monitor
# This script sets up the initial workspace
import os

def preprocess():
    """Set up the initial workspace."""
    os.makedirs("workspace", exist_ok=True)
    print("Preprocessing complete for health-monitor")

if __name__ == "__main__":
    preprocess()
