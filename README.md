# Cookie Clicker Automation

This project automates the [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/) game using Selenium in Python. The script automatically clicks the big cookie and purchases products when enough cookies are collected.

<img width="1642" alt="image" src="https://github.com/user-attachments/assets/bc4e7f19-0119-4c63-8bc4-06290058bbf9">

## Features

- Automatically clicks the cookie continuously.
- Purchases available products when enough cookies are accumulated.
- Uses multi-threading to perform cookie clicking and product buying simultaneously.

## Requirements

- **Python 3.x**
- **Google Chrome**
- **ChromeDriver**: Make sure the version of ChromeDriver matches your installed version of Chrome. [Download ChromeDriver here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
- **Selenium**: Install via pip.

## Installation

1. Clone this repository or download the files.
2. Install the required Python libraries:
    ```bash
    pip install selenium
    ```

3. Download the appropriate version of ChromeDriver for your system and place it in the project directory or somewhere in your PATH. Update the `executable_path` in the code with your ChromeDriver path.

## Usage

1. **Update ChromeDriver Path**: Ensure that the `executable_path` is correct in the script:
    ```python
    service = Service(executable_path="/path/to/chromedriver")
    ```

2. Run the script:
    ```bash
    python main.py
    ```

## How It Works

- **Click Cookie Function**: Continuously clicks the big cookie and prints the current number of cookies in the console.
- **Buy Products Function**: Periodically checks if there are enough cookies to buy a product and buys the most affordable product.
- **Threading**: Clicks the cookie and buys products simultaneously using two separate threads.

<img width="636" alt="image" src="https://github.com/user-attachments/assets/b2501ce5-bc04-4b0c-b28d-88a87e40e140">

