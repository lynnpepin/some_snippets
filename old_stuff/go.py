'''Run as `python3 -i go.py`

I use this when writing Python scripts on my phone (through Termux). The point is to minimize the keypresses needed when writing Python on a phone.

This will start Python, import a bunch of modules with short names, and then throw you into an interpreter. 
'''

import numpy as np
import pandas as pd
import math as mt
import random as rd
import time
import itertools as it
import functools as ft
import re
import os
import sys
import glob
import pickle as pl
import hashlib as hl
import secrets as ss
import socket as sk

print("imported numpy as np, pandas as pd, math as mt, random as rd, time, itertools as it, functools as ft, re, os, sys, glob, pickle as pl, hashlib as hl, secrets as ss, and socket as sk!")

A = np.array

PI = mt.pi
TAU = mt.tau
E = mt.e

print("Constants available: PI, TAU, E.")

H = help
Q = quit

print("Functions `help(...)` and `quit()` available as `h(...)` and `q()`. `np.array(...)` as `A(...)`")


