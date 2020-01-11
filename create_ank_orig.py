#!/usr/bin/env python3

import argparse
import subprocess
import csv
import re
import time

import sys
import os
import tempfile
import shutil
import traceback

import genanki
from model_ex import gen_model
import random
import opera_ex
import ja_es

#output path. dont need to create this file, will be created automatically
if __name__ == '__main__':                                                                                                                                                    
	parser = argparse.ArgumentParser()                                           
	parser.add_argument('--file', help='word list to add to deck', required=True)                                                             
	parser.add_argument('--title', help='name of the deck', required=True)                   
	parser.add_argument('--description', help='Description of the deck.')       
	args = parser.parse_args()

#output_file_path = "output.csv"
newline = "\n"
separator = ","
CWD = os.getcwd()
word_file_path = CWD+"/"+args.file

# import genaki and models

# create deck
deck = genanki.Deck(random.randrange(1 << 30, 1 << 31), args.title)
# set model id, model name
card_model = gen_model('123456789', 'J2S_model_name')

row_index = 0
with open(word_file_path, 'r') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		word_now=''
		speech=''
		spanish=''
		misc=''
		audio_now=''
		kanji=''
		furigana=''

		word_now = row[0]
		print("#########", word_now, "#########", '\n')

		'''Retrieve from Tango'''
		p = subprocess.Popen(["kantag", word_now], stdout=subprocess.PIPE)
		result, err = p.communicate()
		reading = result.decode("utf-8").replace('\n', '')
		misc = re.sub('[ 0-9a-zA-Z]', '', reading)
		print(misc, '\n')

		'''Retrieve WWWJDIC'''
		p = subprocess.Popen(["jdone", word_now], stdout=subprocess.PIPE)
		result, err = p.communicate()
		meanings = result.decode("utf-8").split('\n')

		for i in range(len(meanings)-1):
			print(i, ": ", meanings[i])

		if len(meanings) == 2:
			choice = 0
		else:
			try:
				choice = int(input("Which: "))
			except (ValueError, TypeError):
				choice = 0
		if choice == 9:
			continue
		result = meanings[choice]
		japanese = result.replace('\n', '').replace('[Links]', '').replace('(P)','')
		print(japanese)

		'''Parse WWWJDIC'''
		m = japanese.split(' ')
		furi = re.sub('[【《]','[',m[0])
		furi2 = re.sub('[】》]',']',furi)
		k = re.match( r'\((.*?)\) (.*)', ' '.join(m[1:]))
		if k:
			speech =  k.group(1)
			spanish = k.group(2)
		else:
			speech = ''
			spanish = ' '.join(m[1:])
		furigana = furi2


		'''Parse Tango and set default kanji'''
		furi = re.sub('[【《]','[',misc)
		furi2 = re.sub('[】》]',']',furi)
		misc= furi2.replace('^','').replace('☆','').replace('★','')

		preferred = re.match( r'(.*?)\^', furi2) 
		if preferred:
			kanji= preferred.group(1)
			word_now = preferred.group(1)
		elif re.match( r'(.*?)【', misc) :
			preferred = re.match( r'(.*?)【', misc) 
			kanji = preferred.group(1)
			word_now = preferred.group(1)
		else:
			print('tango not found')

		#rep = re.sub('[ 0-9a-zA-Z^]', '', reading)
		#replaced = re.match( r'(.*?)【(.*?)】', rep) 

		print('\n', kanji, '\n', speech, '\n', furigana, '\n', spanish, '\n', misc, '\n')

		if not kanji or not spanish:
			c = input('to discard press y:  ')
			if c == 'y':
				try:
					subprocess.call(['closetab'])
				except:
					print('error calling closetab')
				continue

		'''Pick vocab audio
		try:
			url = 'https://forvo.com/search/'+word_now+'/ja'
			driver.get(url)
			wait = WebDriverWait(driver, 2)
			#element = wait.until(EC.presence_of_all_elements_located((driver.find_elements_by_xpath("//div[@class='list-words']//div[@class='play']")))) 
			element = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class, 'list-words')]//span[contains(@class, 'play')]")))
			#element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'list-words')]//span[contains(@class,'play')]")[0]))
			element[0].click()
			time.sleep(2)
			subprocess.call(['saveaudio'])
		except:
			print('error')

		for af in os.listdir("/home/chewie/Downloads"):
			if af.endswith(".mp3"):
				print(af, " --> ", word_now+".mp3")
				os.rename("/home/chewie/Downloads/"+af, word_now+".mp3")
				audio = word_now+".mp3"
				audio_now = "[sound:"+audio+"]"

		print('\n')         '''

		note = genanki.Note(
				model=card_model,
				fields=[kanji, furigana, speech, spanish, audio_now, misc]
				)
		deck.add_note(note)

genanki.Package(deck).write_to_file(args.title+".apkg")


