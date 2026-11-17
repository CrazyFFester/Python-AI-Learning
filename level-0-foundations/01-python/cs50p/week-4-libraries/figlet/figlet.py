import random
import sys
import pyfiglet


fonts = pyfiglet.FigletFont.getFonts()

if len(sys.argv) == 1:
    font = random.choice(fonts)
elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font") and \
        sys.argv[2] in fonts:
    font = sys.argv[2]
else:
    sys.exit("Invalid usage")

text = input("Input: ")

print(pyfiglet.figlet_format(text, font=font))
