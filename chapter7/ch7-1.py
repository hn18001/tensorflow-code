import collections
import math
import os
import random
import zipfile
import numpy as np
import urllib
import tensorflow as tf

url = 'http://mattmahoney.net/dc/'

def maybe_download(filename, expected_bytes):
	if not os.path.exists(filename):
		filename, _ = urllib.urlretrieve(url+filename, filename)
	statinfo = os.stat(filename)
	if statinfo.st_size == expected_bytes:
		print('found and verified', filename)
	else:
		print(statinfo.st_size)
		raise Exception('Failed to verify ' + filename + ". Can you get to it with a browser?")
	return filename

filename = maybe_download('text8.zip', 31344016)

def read_data(filename):
	with zipfile.ZipFile(filename) as f:
		data = tf.compat.as_str(f.read(f.namelist()[0])).split()
	return data

words = read_data(filename)
print("Data size", len(words))
