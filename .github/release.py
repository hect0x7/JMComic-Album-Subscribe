from common import *


def add_output(k, v):
    cmd = f'echo "{k}={v}" >> $GITHUB_OUTPUT'
    print(cmd, os.system(cmd))


path = os.getenv('JM_DOWNLOAD_DIR', None)
if path and file_exists(path) and len(files_of_dir(path)) != 0:
    add_output('found_new', 'true')
