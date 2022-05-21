from string import punctuation
import sys
from json import load
from os.path import exists

def main():
    arg = sys.argv
    if len(arg) != 2:
        print('Usage: python check.py <fileName>')
        return
    if not exists(arg[1]):
        print('Cannot find file')
        return
    
    with open('words_dictionary.json') as dictonary:
        dictonary_words = load(dictonary)
    
    mistakes = 0
    with open(arg[1]) as file:
        lines = file.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                check_word = word.strip(str(punctuation) + ' ').lower()
                if not check_word.isdigit() and check_word != '' and check_word not in dictonary_words:
                    mistakes += 1
                    print(word)
    
    if mistakes == 0:
        print('No mistakes found!') 
    else:     
        print(f'you made {mistakes} mistakes')
    return




if __name__ == '__main__':
    main()
