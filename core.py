from termcolor import cprint, colored
from os import system

clr = lambda: system('clear')
CHEVRON = colored('>>> ', 'yellow', attrs=['blink'])

  
def get_color():
    options = {
        '1': 'red', '2': 'blue', '3': 'green'
    }
    cprint('\t(1) Red', 'red')
    cprint('\t(2) Blue', 'blue')
    cprint('\t(3) Green', 'green')
    while True:
        color_choice = input(CHEVRON)
        if color_choice in options.keys():
            return options[color_choice]
        else:
            cprint('invalid! option', attrs=['blink'])

  
def get_effect():
    print('\t(1) no effect')
    cprint('\t(2) blink', 'grey', attrs=['blink'])
    cprint('\t(3) reverse', 'grey', attrs=['reverse'])
    options = {
        '1': '', '2': 'blink', '3': 'reverse'
    }
    while True:
        effect_choice = input(CHEVRON)
        if effect_choice in options.keys():
            return options[effect_choice]
        else:
            cprint('invalid! option', attrs=['blink'])


def main():
    clr()

    cprint('\nWelcome to the amazing color terminal!\n', 'blue', attrs=['reverse', 'blink'])
    input()

    while True:
        print('What message would you like to print? q to quit')
        message = input(CHEVRON).strip()
        if message == 'q':
            break
        color = get_color()
        effect = get_effect()
        clr()
        print('\n' * 3)
        if effect:
            cprint(message, color, attrs=[effect])
        else:
            cprint(message, color)
        print('\n' * 3)
    
    cprint('\n\nthank you have a nice day!\n\n', 'blue', attrs=['reverse', 'blink'])
    

if __name__ == '__main__':
    main()
