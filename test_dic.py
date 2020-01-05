#!/usr/bin/env python

import ja_es 

#lookups = translate("成る")
#for piece in lookups:
	#print(piece,'\n')

word_now=''
speech=''
spanish=''
misc=''
audio_now=''
kanji=''
furigana=''
kana=''

word_now = "成る"
lookups = ja_es.translate(word_now)
for piece in lookups:
	#print(piece, '\n')
	kanji = kanji+piece[0]+' '
	speech = speech+piece[1]+' '
	kana = kana+piece[2]+' '
	furigana = furigana + piece[0]+'['+piece[2]+']'+' '
	spanish = spanish+str(piece[3])+' '
	misc = misc+str(piece[4])+' '

print('\n', kanji, '\n', speech, '\n', furigana, '\n', spanish, '\n', misc, '\n')
