# Copyright (c) 2025 Neil Archer@hotmail.com. All rights reserved.

from trading_engine import TradingEngine
from logging_module import setup_logging

if __name__ == "__main__":
    setup_logging()  # Set up logging
    trading_engine = TradingEngine()
    trading_engine.run()
