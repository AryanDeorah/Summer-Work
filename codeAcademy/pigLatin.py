#This code is written in python 2.7
#Takes words and changes them into pyg latin
pyg = 'ay'

original = raw_input('Enter a word:') #sets variable original to a raw input

if len(original) > 0 and original.isalpha(): # checks if length of input is greater than zero and checks if input is word
  word=original.lower() # makes input lower case
  first=word[0] #identifys first letter of word
  new_word=word+first+pyg #combines parts to form pyg latin word
  new_word=new_word[1:len(new_word)] #removes first letter of new_word
  print new_word
else: #prints empty if input was empty or used not letter charecters
  print 'empty'
