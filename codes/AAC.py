#!/usr/bin/env python
#_*_coding:utf-8_*_

import re
from collections import Counter
import pandas as pd

def AAC(fastas, **kw):
	AA = 'ACDEFGHIKLMNPQRSTVWY'
	encodings = []
	header = ['#']
	for i in AA:
		header.append(i)
	encodings.append(header)

	for i in fastas:
		name, sequence = i[0], re.sub('-', '', i[1])
		count = Counter(sequence)
		for key in count:
			count[key] = count[key]/len(sequence)
		code = [name]
		for aa in AA:
			code.append(count[aa])
		encodings.append(code)
	df = pd.DataFrame(encodings[1:], columns=header)
	return df