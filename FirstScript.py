import subprocess
import os

def calculate_cksum(file_path):
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"File '{file_path}' does not exist.")
        return None
    
    # Construct the command to calculate cksum
    command = ['cksum', file_path]
    
    # Execute the command using subprocess
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        # Output of cksum is in the format: checksum bytes filename
        output = result.stdout.strip().split()
        cksum_value = output[0]  # First element is the checksum value
        return cksum_value
    except subprocess.CalledProcessError as e:
        print(f"Error running cksum command: {e}")
        return None

if __name__ == "__main__":
    # Example usage: Replace 'file_path' with the path to your file
    file_path = '/path/to/your/file'
    cksum = calculate_cksum(file_path)
    if cksum:
        print(f"Checksum of '{file_path}': {cksum}")

