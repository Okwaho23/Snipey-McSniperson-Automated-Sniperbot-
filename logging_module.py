# Copyright (c) 2025 Neil Archer@hotmail.com. All rights reserved.

import logging

def setup_logging():
    logging.basicConfig(filename='trading_bot.log', level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

def log_event(message):
    logging.info(message)
