import re

def extract_errors(log_text):
    # Extract lines containing 'error', 'exception', etc.
    lines = log_text.split("\n")
    error_lines = [line for line in lines if re.search(r'error|exception|fail', line, re.IGNORECASE)]
    return "\n".join(error_lines)
