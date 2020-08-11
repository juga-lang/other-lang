import os
import shutil
import subprocess
import sys

code = []
env = ''
name = 'main'


def insert_var(varname, varvalue):
    code.append('var ' + varname + ' = ' + varvalue)
    pass


def execute_code(insert_main, _code):
    file = open(env + name + '.js', 'w+')
    for line in _code:
        file.write(line + '\n')
    if shutil.which('node') is not None:
        os.system('node ' + env + name)
    else:
        print('Error: NodeJS does not seem to be installed')
        sys.exit('Runtime error')


def execute_file(inEnv, file):
    if shutil.which('node') is not None:
        if inEnv:
            os.system('node ' + env + file)
        else:
            os.system('node ' + file)
    else:
        print('Error: NodeJS does not seem to be installed')
        sys.exit('Runtime error')
