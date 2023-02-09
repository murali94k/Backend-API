import confuse
import os

if os.environ.get('CONFIG_PATH'):
    config_path = os.environ['CONFIG_PATH']
else:
    config_path = os.getcwd()

config = confuse.Configuration(config_path, __name__)