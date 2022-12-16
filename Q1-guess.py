class color:
    OKGREEN = '\033[92m'
    OKCYAN = '\033[96m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
def banner():
    print("""
███████ ██ ███    ███ ██████  ██      ███████ 
██      ██ ████  ████ ██   ██ ██      ██      
███████ ██ ██ ████ ██ ██████  ██      █████   
     ██ ██ ██  ██  ██ ██      ██      ██      
███████ ██ ██      ██ ██      ███████ ███████ 
                                              
                                              
 ██████  ██    ██ ███████ ███████ ███████     
██       ██    ██ ██      ██      ██          
██   ███ ██    ██ █████   ███████ ███████     
██    ██ ██    ██ ██           ██      ██     
 ██████   ██████  ███████ ███████ ███████ 

created by soroush yasini
    """)
banner()
def dif():
    global difficalt
    difficalt = (input("""before we get started, set the difficulty :
        1 - easy           2 - hard

    please insert 1 or 2 here :
    """))
    if difficalt == "2" :
        global hardness
        hardness = 10
        print(color.WARNING + """
        game has been set to :
    ██   ██  █████  ██████  ██████  
    ██   ██ ██   ██ ██   ██ ██   ██ 
    ███████ ███████ ██████  ██   ██ 
    ██   ██ ██   ██ ██   ██ ██   ██ 
    ██   ██ ██   ██ ██   ██ ██████      
        """)
    elif difficalt == "1":
        hardness = 20
        print(color.OKCYAN + """
        game has been set to :
    ███████  █████  ███████ ██    ██ 
    ██      ██   ██ ██       ██  ██  
    █████   ███████ ███████   ████   
    ██      ██   ██      ██    ██    
    ███████ ██   ██ ███████    ██    
        """)
    else :
        print ("you DID entered something incorrectly ! run the program again.")
        exit()
dif()
def game():
    import random
    pc_number = random.randint(0, 20)
    for i in range(hardness):
        user_number = int(input("GUESS !! : "))
        tr = i + 1
        if pc_number == user_number:
            print("WOW ! you guessed it correct ! ")
            print (color.OKGREEN + "and here is how many times you tried : ", tr)
            break
        if pc_number > user_number: 
            print("the num. is bigger than yours.")
        if pc_number < user_number:
            print("the num. is smaller than yours.")
        if hardness == tr :
            print(color.FAIL + "sorry! you lost ! ")
            exit()
game()
