import random

notes = []
while True:
    key_word = input("Enter key word (add, earliest, latest, longest, shortest, Exit): ")
    if key_word == 'add':
        your_note = input('Enter your note: ')
        notes.append(your_note)
    elif key_word == 'earliest':
        print('From newest to latest: ')
        for your_note in notes:
            print(your_note)
    elif key_word == 'latest':
        print('From the latest to the newest: ')
        for your_note in reversed(notes):
            print(your_note)
    elif key_word == 'longest':
        print('From longest to shortest')
        sorted_notes = sorted(notes, key=len, reverse=True)
        for your_note in sorted_notes:
            print(your_note)
    elif key_word == 'shortest':
        print('From shortest to longest: ')
        sorted_notes = sorted(notes, key=len)
        for your_note in sorted_notes:
            print(your_note)
    elif key_word == 'Exit':
        break



