def search4letters(phrase:str,letters:str='aeiou') -> set:
    '''Return a set based on any 'letters' found in 'phrase'.'''
    return set(letters).intersection(set(phrase))

#search4letters('hitch-hiker','aeiou')

#search4letters(letters='galaxy',phrase='xyz')

#search4letters('life, the universe and everything','o')


#import random
#random.randint(0,255)
