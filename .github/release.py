from common import *


def add_output(k, v):
    cmd = f'echo "{k}={v}" >> $GITHUB_OUTPUT'
    print(cmd, os.system(cmd))


path = os.getenv('JM_DOWNLOAD_DIR', None)
if path:
    files = files_of_dir(path)
    if len(files) != 0:
        add_output('found_new', 'true')
