#!/bin/bash

PYTHONPATH=$PYTHONPATH:~/bluntconsultants-site/:~/pydozer/  python ~/pydozer/pydozer.py --conf bc_config.py --build
cp -av generated/* /var/www/bc/
