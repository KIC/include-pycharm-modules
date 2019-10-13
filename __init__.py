__version__ = '0.0.1'

import os
import sys
import logging
from bs4 import BeautifulSoup

log = logging.getLogger(__name__)

# generically add all pycharm source folders to the search path
for file in os.listdir(".idea/"):
    if file.endswith(".iml"):
        file = f".idea/{file}"
        page = open(file)
        soup = BeautifulSoup(page.read(), 'lxml')
        _PARENT_DIR = os.path.join(os.path.dirname(__file__), "..")

        for source_folder in soup.find_all('sourcefolder'):
            source = os.path.basename(source_folder['url'])
            if source == "modules":
                continue

            module_path = os.path.join(_PARENT_DIR, source)
            if os.path.exists(module_path):
                print(f"adding module {module_path}")
                log.info(f"adding module {module_path}")
                sys.path.append(module_path)
