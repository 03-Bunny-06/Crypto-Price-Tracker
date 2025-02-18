# Crypto Price Tracker

## Project Description

This Python script fetches and displays **real-time cryptocurrency prices** for a list of popular cryptocurrencies in various currencies (**BTC, USD, EUR, and INR**). The data is presented in a visually appealing table using the `rich` library.

## Features

- **Fetch Cryptocurrency Data:** Retrieves the latest prices for multiple cryptocurrencies using the **CryptoCompare API**.
- **Multi-Currency Support:** Displays prices in **Bitcoin (BTC), US Dollars (USD), Euros (EUR), and Indian Rupees (INR)**.
- **Rich Table Display:** Utilizes the `rich` library to format and display data in a styled table with clear visuals.

## Prerequisites

- Python **3.7 or higher**
- Install the required libraries using:
  ```sh
  pip install requests rich
  ```

## Usage

1. Clone or download the script.
2. Replace the `key` variable with your own **API key** from **CryptoCompare**.
3. Run the script:
   ```sh
   python crypto_tracker.py
   ```
4. View the cryptocurrency prices in a **formatted table output**.

## Example Output

A visually styled table of cryptocurrency prices with columns for:

- **Cryptocurrency name**
- **Prices in BTC, USD, EUR, and INR**

![image](https://github.com/user-attachments/assets/32ab9e50-9cd9-4552-b710-c2175022a9fa)


## Notes

- Ensure your **API key** has sufficient access to fetch data.
- Modify the `cryptos` and `currencies` variables as needed to customize the list of cryptocurrencies and target currencies.

## Credits

- **API Source:** [CryptoCompare](https://www.cryptocompare.com/)
- **Libraries Used:**
  - `requests` for API calls
  - `rich` for table styling and console output
