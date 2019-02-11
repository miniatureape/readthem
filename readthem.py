import os
import re
from signal import signal, SIGPIPE, SIG_DFL 

signal(SIGPIPE,SIG_DFL) 

cwd = os.getcwd()

def color(color, str):
    colors = {
        "header": '\033[95m',
        "blue": '\033[94m',
        "green": '\033[92m',
        "warning": '\033[93m',
        "fail": '\033[91m',
        "endc": '\033[0m',
        "bold": '\033[1m',
        "underline": '\033[4m',
    }
    return colors.get(color, "") + str + colors.get('endc')

for name in os.listdir(cwd):
    dir_path = os.path.join(cwd, name)
    if os.path.isdir(dir_path):
        readme_path = os.path.join(dir_path, 'README.md')
        if os.path.exists(readme_path):
            f = open(readme_path)
            title = ""
            description = ""
            lastline = ""
            for l in f.readlines():

                if title and l.startswith("#") or l.startswith("=="):
                    break

                if not title and l.startswith("# "):
                    title = l[2:]
                    continue
                if not title and l.startswith("=="):
                    title = lastline
                    continue

                description = description + l
                lastline = l

                title = title.strip()
                description = description.strip()

            print "%s: (%s)" % (color('bold', title), color('green', name), )
            print description
            print ""
        else:
            print "%s: ???" % color('green', name)
            print ""
