import os
import shutil
import sys

code = []
env = ''
name = 'main'


def insert_var(varname, varvalue):
    code.append('public static Object ' + varname + ' = ' + varvalue)
    pass


def execute_code(insert_main, insert_class, _code):
    file = open(env + name + '.java', 'w+')
    if insert_class:
        file.write('public class ' + name + '{\n')
    for line in _code:
        file.write(line + '\n')
    if insert_class:
        file.write('}')
    if shutil.which('java') is not None:
        if shutil.which('javac') is not None:
            os.system('javac ' + env + name + '.java')
            os.system('java ' + env + name)
        else:
            print('Error: \'java\' was found but \'javac\' was not found!')
            sys.exit('Runtime error')
    else:
        print('Error: Java does not seem to be installed!')
        sys.exit('Runtime error')


def execute_file(inEnv, file):
    if shutil.which('java') is not None:
        if shutil.which('javac') is not None:
            if inEnv:
                os.system('javac ' + env + file)
                os.system('java ' + env + file)
            else:
                os.system('javac ' + file)
                os.system('java ' + file)
        else:
            print('Error: \'java\' was found but \'javac\' was not found!')
            sys.exit('Runtime error')
    else:
        print('Error: Java does not seem to be installed!')
        sys.exit('Runtime error')
