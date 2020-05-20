# coding=utf-8
'''
# Author: shikanon (shikanon@tensorbytes.com)
# File Created Time: 2020-03-31 11:10:05
# 
# Project: settings
# File: config_test.py
# Description: 
# 
'''

import pytest

from settings.config import Config

def test_config():
    conf = Config()
    conf.parse("settings/config.ini")