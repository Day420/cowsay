import argparse
from colorama import *

class cow:
    def cowsay(text):
        msg_len = int(len(text))
        output = ""
        output += " " + "_"*int(msg_len+2)
        output += "\n"+f"< {text} >"
        output += "\n " + "-"*int(msg_len+2)
        output += """
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w||
                ||     ||"""
        return output

        finaloutput = ""
        for letter in text:
            if letter == "\n":
                finaloutput += " "
            else:
                finaloutput += letter


class colors:
    white = Fore.RESET
    red = Fore.RED
    lightred = Fore.LIGHTRED_EX
    blue = Fore.BLUE
    lightblue = Fore.LIGHTBLUE_EX
    cyan = Fore.CYAN
    lightcyan = Fore.LIGHTCYAN_EX
    yellow = Fore.YELLOW
    lightyellow = Fore.LIGHTYELLOW_EX
    green = Fore.GREEN
    lightgreen = Fore.LIGHTGREEN_EX
    purple = Fore.MAGENTA
    lightpurple = Fore.LIGHTMAGENTA_EX

def getcolor(color):
    if color != None:
        color = color.lower()
    if color == "white":
        return colors.white
    elif color == "red":
        return colors.red
    elif color == "lightred":
        return colors.lightred
    elif color == "blue":
        return colors.blue
    elif color == "lightblue":
        return colors.lightblue
    elif color == "cyan":
        return colors.cyan
    elif color == "lightcyan":
        return colors.lightcyan
    elif color == "yelow":
        return colors.yellow
    elif color == "green":
        return colors.green
    elif color == "lightgreen":
        return colors.lightgreen
    elif color == "purple":
        return colors.purple
    elif color == "lightpurple":
        return colors.lightpurple
    else:
        return colors.white

parser = argparse.ArgumentParser()
parser.add_argument('--text', '-text', '-t', '--t', help='Enter a text that will cow say!', type=str, required=True)
parser.add_argument('--color', '-color', '-c', '--c', help='You can customize the color of your cow! (veri epik)', type=str, required=False)
args = parser.parse_args()

if args.text:
    print(getcolor(args.color)+cow.cowsay(args.text))

# github.com/Day420/cowsay
