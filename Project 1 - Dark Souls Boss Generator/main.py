"""generator function"""
from generator import generateBossName

if __name__ == '__main__':
    print('Welcome to the Dark Souls Boss generator')
    print('Ready to create some new Dark Souls Bosses?')
    generateBossName()
    while True:
        choice = int(input('What do you want to do next?\n\
        press 1 - try again\n\
        press 2 - quit\n->'))
        if choice == 1:
            generateBossName()
        elif choice == 0:
            print('Bye')
            break
#end
