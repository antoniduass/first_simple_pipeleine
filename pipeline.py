import requests
import pandas as pd
from datetime import datetime
from loguru import logger
from utils.decorators import log_step

@log_step
def extract_data(url: str):
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error(f"Failed to fetch data from {url}: {e}")
        return None

@log_step
def transform_and_load(data: dict, output_file: str):
    
    if not data:
        logger.warning(f"Skipping transformation: data is empty for {output_file}")
        return
    
    rates = data.get('rates', {})
    df = pd.DataFrame(list(rates.items()), columns=['Currency', 'Rate'])

    df['Base'] = data.get('base')
    df['Date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    df.to_csv(output_file, index=False)
    logger.info(f"[{datetime.now()}] Data successfully saved in {output_file}")