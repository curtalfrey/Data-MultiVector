# main.py
from core import Connection, route_data
from web_ui import app
from logging_utils import configure_logging, log_data_modification
from monitoring import ConnectionMonitor

if __name__ == "__main__":
    # Initialize connections, configure logging, set up monitoring, and start the app
