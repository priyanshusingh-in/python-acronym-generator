inputSentence=input('Please enter a sentence: ')
wordList=(inputSentence.replace('of','')).split()
acronym=''
for word in wordList:
    acronym=acronym+word[0].upper()
print('Acronym of {} is {}'.format(inputSentence,acronym))
