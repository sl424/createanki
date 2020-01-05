#!/usr/bin/python 

import json
import argparse
import os
from pathlib import Path

#os.environ["PATH"] += os.pathsep + r

folder = Path('./')

class Word:
	def __init__(self, kanji, kana, speech, type, rank, spanish, freq, source):
		self.kanji = kanji
		self.kana = kana
		self.speech = speech
		self.type = type
		self.rank = rank
		self.misc = [type, rank, freq, source]
		self.spanish = spanish[:2]
		self.freq = freq 
		self.source = source

def decode_word(w):
	entry = Word(w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[7])
	return entry

jisho=[]
def init():
	for t in range(1,7):
		with open( folder / str ("term_bank_"+str(t)+".json") ) as sample_data:
			data = sample_data.read()
			ll = json.loads(data)
			for i in ll:
				jisho.append(decode_word(i))

def sort_by_freq(word):
	return word.freq

def translate(ja):
	a=[]
	blob=[]
	for i in jisho:
		if i.kanji == ja or i.kana == ja:
			a.append(i)
	a = sorted(a, key=sort_by_freq)
	a = a[:2]
	#blob = [a[0].kanji, a[0].speech, a[0].kana, a[0].spanish, a[0].misc]
	#blob = [','.join(set([w.kanji for w in a])), '', ','.join(['#'+str(a.index(w))+' ('+w.speech+') '+w.kana for w in a])]
	#blob = [','.join(set([w.kanji for w in a])), '', ','.join(set([w.kana for w in a]))]
	#	return str([a[0].kanji, a[0].speech, a[0].kana, a[0].spanish, a[0].misc])
	for w in a:
		d=[w.kanji, w.speech, w.kana, w.spanish, w.misc]
		blob.append(d)
	return blob


init()

if __name__ == '__main__':                                                                                                                                                    
	parser = argparse.ArgumentParser()                                           
	parser.add_argument('--word', help='word to search in deck', required=True)                                                             
	#parser.add_argument('--end', help='close deck and export', default='n')       
	args = parser.parse_args()
	print(translate(args.word))
