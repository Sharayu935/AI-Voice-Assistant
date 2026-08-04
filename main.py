import os
import eel

from engine.command import *

eel.init('WWW')

eel.start('index.html', mode='chrome', size=(1000, 700))


