#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 09:53:46 2022

@author: kamrul
"""
import pysrt
from googletrans import Translator
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux
    else:
        _ = system('clear')


translator = Translator()
file_name = input('file name: ')
subs = pysrt.open(file_name)
with open('translated.srt', 'w') as f:
    for c in range(len(subs)):
        f.write(str(c + 1))
        f.write('\n')
        f.write(str(subs[c].start) + ' --> ' + str(subs[c].end))
        f.write('\n')
        content = subs[c].text
        translation = translator.translate(content, dest='bn')
        f.writelines(translation.text)
        f.write('\n')
        f.write('\n')
        clear()
        print('translated', int(((c + 1) / len(subs)) * 100), '%')
    f.close()
