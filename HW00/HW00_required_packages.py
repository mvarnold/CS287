# HW00.py
# Jim Bagrow
# Last Modified: 2018-08-27

"""
Run this code to test your python installation. It should run without errors.

If any errors appear related to import statements, use your package
manager to check/install missing modules. Then rerun this code.

***
    If this code does not eventually print "Congrats!", your system is not
    ready for the course!
***

If you cannot get this script to run without errors, please see me ASAP!
"""

print("*** Welcome to HW00! ***")
print()

print(
"""We are now going to try a bunch of imports to make sure you have everything
installed that you will need for the course. This will likely fail and you
will need to install something yourself using conda or pip.
    
Keep running this code and installing packages until it completes without
error!
""")
print()
print("...", end=" ", flush=True)
#Deleted or copied text i
import time
time.sleep(3)


# built-in python modules:
import sys
import os
import random
import collections
import itertools
import urllib
from string import punctuation
import json
import glob
import gzip
import unicodedata
import time
from datetime import datetime
import codecs
import csv
from hashlib import sha1
import colorsys
import re
from io import BytesIO as InMemory
from collections import Counter


from base64 import b64encode

# third party modules:
import websocket # see HW00_supplement.pdf

# check for ipython and ipython notebooks:
import IPython

# for plotting:
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

# web access
import requests               # third-party package
from bs4 import BeautifulSoup # third-party package

# networks
import networkx



# scientific and numerical computing:
import numpy
import scipy
import scipy.stats
import scipy.misc
from scipy.optimize import curve_fit
from scipy.misc import comb
from scipy.cluster.vq import kmeans,vq
from scipy.spatial.distance import cdist
from scipy import ndimage
from scipy import integrate

# natural language processing:
import nltk
from nltk.corpus import stopwords

# machine learning:
from sklearn import linear_model
from sklearn import tree
from sklearn import datasets
from sklearn.decomposition import RandomizedPCA
from sklearn.datasets import load_iris

# statistics
import statsmodels.api as sm

print()
print()
print("All imports appear to work. Congrats!")

