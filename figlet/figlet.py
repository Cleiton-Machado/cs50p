from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts = figlet.getFonts()
random_font = random.choice(fonts)


try:
    if len(sys.argv) > 1 and len(sys.argv) < 4:
        if sys.argv[1] in ['-f', '--f']:
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit('Invalid usage')
    else:
        figlet.setFont(font=random_font)
        print('Caiu no else')
except IndexError:
    sys.exit()


prompt = input('Input: ')
print(figlet.renderText(prompt))








