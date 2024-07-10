# Flight Price Tracker

The Flight Price Tracker is a Python-based application that allows users to track and monitor flight prices from various airlines. It utilizes the SerpAPI service to fetch real-time flight pricing data.

## Features

- Fetches flight price data from multiple airlines using the SerpAPI service
- Stores the collected data in a database for historical analysis

### Prerequisites

- Python 3.9 or higher
- SerpAPI API key
- A database (e.g., SQLite, PostgreSQL, MySQL) to store the flight price data

### Installation

1. Clone the repository:
git clone https://github.com/thedezignr/flight_price_tracker.git

2. Change to the project directory:
virtual environment

3. Install the required dependencies:
pip install -r requirements.txt

4. Set the environment variables:
- `SERPAPI_API_KEY`: Your SerpAPI API key
- `DATABASE_URL`: The connection URL for your database

5. Run the application:
python flight_tracker.py

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).