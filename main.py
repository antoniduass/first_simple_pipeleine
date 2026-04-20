from pipeline import extract_data, transform_and_load
from pathlib import Path

CURRENCY_URL = "https://api.frankfurter.dev/v1/latest?from=USD"
RESULT_FILE = Path("data") / "current_rates.csv"

def main():
    
    raw_data = extract_data(CURRENCY_URL)

    transform_and_load(raw_data, RESULT_FILE)

if __name__ == "__main__":
    main()