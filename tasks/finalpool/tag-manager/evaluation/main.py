# Evaluation script for tag-manager
# This script evaluates the agent's work
import os

def evaluate(workspace):
    """Evaluate the agent's implementation."""
    # Check if required files exist
    required_files = ['README.md']
    results = {}
    for f in required_files:
        fpath = os.path.join(workspace, f)
        results[f] = os.path.exists(fpath)
    return results

if __name__ == "__main__":
    print(evaluate("."))
