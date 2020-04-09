import random
import time
words = [['abascus','maths','albatross'],['horrible','bad','adorable'],
         ['communication','talking','information'],['harsh','rough','farce'],
         ['dangle','hanging','angle'],['amplitude','waves','gratitude'],
         ['information','to knowing','nation'],['aggregate','average','legitimate'],
         ['wardrobe','cupboard','war thog'],['terminate','end','facilitate'],
         ['stamina','energy','lamina']]
tryagain = ['try again','Its ok do it again']

Y = ['yes','YES','Y','y','Yes','yeah','Yep','yep']

# Introducing.....

print ('Hello....')
time.sleep(0.5)                                  # to give a small gap of time
print ('I am a WORD GUESSING GAME')
time.sleep(1)
print ('I will choose a random word and i will give you hints')
time.sleep(1.5)
print ('U will have to guess the word!!!')
time.sleep(1)
print ("Let's have some fun :)")

a = 1
while a == 1:
    userinput = input('Ready?:')
    if userinput in Y:
        print ("Good!")
    else:
        print ("Anyways let us continue:")
    sl = random.choice(words)                    # selecting a sublist
    w = sl[0]                                    # selecting the main word
    h1 = sl[1]                                   # first good hint
    h2 = sl[2]                                   # second good hint
    n = len(w)                                   # word length
    x = 10                                       # taking a counter and a score keeper
    print ('Ok , The word starts with',w[0])
    time.sleep(1)
    print ('The word ends with',w[n-1])
    time.sleep(1)
    print ('It has a length of',n)
    blanks='_ '*(n-2)
    print ('WORD: ', w[0],blanks,w[n-1])
    time.sleep(1)
    gs = input("Enter the word you have guessed:")
    while True:

        if gs == w:
            break
            continue
        else:
            x-=1
            gs = input(random.choice(tryagain)+':')
        if gs != w:
            if x == 0:
                break
            if x == 9:
                print ('Let me give you a small hint..')
                time.sleep(1)
                print ('There is a letter',random.choice(w[1:n-1]),'somewhere in between')
            if x == 7:
                print ('Ok I will give you a big hint...')
                time.sleep(1.5)
                print ('The word is related to',h1)
            if x == 5:
                print ('Ok this is the final hint........')
                time.sleep(1)
                print ('Wait for it......')
                time.sleep(1.5)
                print ('It rhymes with',h2)

    if x == 10:
        print ("OH MY GOD! You are a born genius!!!")
    elif 10>x>7:
        print ("Excellent! You are quite good!")
    elif 8>x>5:
        print ("Hm....you are good.")
    elif x == 5:
        print ("Well...not that bad")
    elif 5>x>2:
        print ("Seriously...you could do better....")
    elif x<3:
        print ("Please....Die")
    print ("Your score is",x,"!!!")
    up = input("Wanna play again?:")
    if up not in Y:
         print ("Thank you and come again!!!! :)")
         a = 0
