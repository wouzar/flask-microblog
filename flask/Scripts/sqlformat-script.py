#!d:\projects\microblog\flask\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'sqlparse==0.2.0','console_scripts','sqlformat'
__requires__ = 'sqlparse==0.2.0'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('sqlparse==0.2.0', 'console_scripts', 'sqlformat')()
    )
