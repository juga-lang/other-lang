import sys
from enum import Enum

from runtimes import javaruntime, jsruntime

import time


class Langs(Enum):
    JAVA = "JAVA"
    JAVA_SCRIPT = 'JS',
    C = "C",
    CPLUSPLUS = 'C++'


def execute(lang, src):
    if lang is Langs.JAVA:
        javaruntime.execute_code(False, True, src)
    if lang is Langs.JAVA_SCRIPT:
        jsruntime.execute_code(False, src)



timer = int(round(time.time() * 1000))
jsruntime.execute_file(False, 'main.js')
print('Time took to compile + execute js code: ' + str(int(round(time.time() * 1000) - timer) / 1000) + ' seconds')
