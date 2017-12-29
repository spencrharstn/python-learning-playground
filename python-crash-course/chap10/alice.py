def count_words(filename):
    """Count the number of words in the file"""

    try:
        with open(filename, encoding='utf-8') as fo:
            contents = fo.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split() # make a list of all words from contents
        num_words = len(words) # count number of items (words) in word list
        num_the = words.count('the') # count number of the word 'the' in the list
        print("The file " + filename + " has about " + str(num_words) + " words with " 
            + str(num_the) + " uses of 'the' or " + str(round((num_the / num_words * 100), 2)) 
            + "% of the words.")

files = ['alice.txt', 'burrito.txt', 'pride.txt', 'thes.txt']
for f in files:
    file = 'files/' + f
    count_words(file)