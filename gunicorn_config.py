import multiprocessing

import sys
import os

sys.path.append('/home/miguel-santos-wh/repositorio/deployjose/venv')

bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count() * 2 + 1