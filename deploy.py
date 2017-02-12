#!/usr/bin/python
import subprocess, os, sys, shutil
from itertools import chain

def run(*args):
    ret = subprocess.call(args,  stdout=sys.stdout, stderr=sys.stderr)
    if ret != 0:
        exit(ret)

token = "VHUCXAONG"
repo = "VHUCXAONG.github.io"
email = "ruochenj@sfu.ca"
name = "Ruochen Jiang"

print('uploading site...')
run('git', 'config', 'user.email', email)
run('git', 'config', 'user.name', name)

print('checkout to master')
run('git', 'checkout', '--orphan', 'master')

print('clean up directory')
for (dirpath, dirnames, filenames) in os.walk("."):
    for folder in dirnames:
        if folder not in ['public', '.git']:
            shutil.rmtree(folder)
    for filename in filenames:
        if filename not in ['.gitignore', 'CNAME', 'README.md']:
            os.remove(filename)
    break
for (path, dirnames, filenames) in os.walk("public"):
    for item in chain(dirnames, filenames):
        shutil.move(path + "/" + item, ".")
    break
shutil.rmtree('public')

print('push to git')
run('git', 'add', '-A')
run('git', 'commit', '-am', "generate content")
run('git', 'push', '-fq', 'https://%s@github.com/%s.git' % (token, repo), 'master')
