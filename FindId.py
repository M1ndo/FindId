#!/usr/bin/python
import requests,re,sys,socket

##########################################
Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
##########################################


print("        "+Red+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+Red+"MMMMMMMMMMNKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+Red+"MMMMMMMMMNc.dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+Reset+"MMMMMMMMWd. .kWMMMMMMMMMMMMMMMMMMMMMMW0KMMMMMMMMMM")
print("        "+Reset+"MMMMMMMMk:;. 'OMMMMMMMMMMMMMMMMMMMMMWx.,0MMMMMMMMM")
print("        "+Reset+"MMMMMMMK:ok.  ,0MMMMMMMMMMMMMMMMMMMWO. .cXMMMMMMMM")
print("        "+Reset+"MMMMMMNl:KO.   ;KWNXK00O0000KXNWMMWO' .c;dWMMMMMMM")
print("        "+Reset+"MMMMMMx,xNk.    .;'...    ....';:l:.  ,0l,0MMMMMMM")
print("        "+Reset+"MMMMMK;,l;. .,:cc:;.                  .dx,lWMMMMMM")
print("        "+Reset+"MMMMWo    ,dKWMMMMWXk:.      .cdkOOxo,. ...OMMMMMM")
print("        "+Reset+"MMMM0'   cXMMWKxood0WWk.   .lkONMMNOOXO,   lWMMMMM")
print("        "+Reset+"MMMWl   ;XMMNo.    .lXWd. .dWk;;dd;;kWM0'  '0MMMMM")
print("        "+Reset+"kxko.   lWMMO.      .kMO. .OMMK;  .kMMMNc   oWMMMM")
print("        "+Reset+"X0k:.   ;KMMXc      :XWo  .dW0c,lo;;xNMK,   'xkkk0")
print("        "+Reset+"kko'     :KMMNkl::lkNNd.   .dkdKWMNOkXO,    .lOKNW")
print("        "+Reset+"0Kk:.     .lOXWMMWN0d,       'lxO0Oko;.     .ckkOO")
print("        "+Reset+"kkkdodo;.    .,;;;'.  .:ooc.     .        ...ck0XN")
print("        "+Reset+"0XWMMMMWKxc'.          ;dxc.          .,cxKK0OkkOO")
print("        "+Reset+"MMMMMMMMMMMN0d:'.  .'        .l'  .;lxKWMMMMMMMMMN")
print("        "+Reset+"MMMMMMMMMMMMMMMN0xo0O:,;;;;;;xN0xOXWMMMMMMMMMMMMMM")
print("        "+Red+"MMMMMMMMMMMMMMMMMMMMMMWWWWWMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+Red+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+Red+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+Red+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+Red+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+Blue+"________________"+Green+"["+Reset+"FindId"+Red+"]"+Blue+"_______")
print("     "+Blue+"_______"+Grey+"["+Red+"Created By ybenel"+Grey+"]"+Blue+"________"+Reset+"\n")

def cnet():
    try:
        ip = socket.gethostbyname("www.google.com")
        con = socket.create_connection((ip, 80), 2)
        return True
    except socket.error:
        pass
    return False

def ID(url):
    if cnet() !=True:
        print("\n[!] Error: Please Check Your Internet Connection !!!")
        exit(1)
    try:
        idre = re.compile('"entity_id":"([0-9]+)"')
        con = requests.get(url).content
        idis = idre.findall(con)
        print("\n[*] ID: "+idis[0])
    except IndexError:
        print("\n[!] Error: 404 Not Found !!!")
        exit(1)
if len(sys.argv) !=2:
    print("\nUsage: python FindId.py <profile_link OR Page_link>\n\nExamples:\n      [Profile~ID] python getid.py https://www.facebook.com/ybenel\n      [Group~ID] python getid.py https://www.facebook.com/groups/<groupName>/\n      [Page-ID] python getid.py https://www.facebook.com/ybl911/")
    exit(1)
url = sys.argv[1]
ID(url)

#--- End Of File ---#
