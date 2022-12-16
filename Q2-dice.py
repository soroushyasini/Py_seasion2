class color:
    OKGREEN = '\033[92m'
def banner():
    print("""
██████      ██      ██████     ███████ 
██   ██     ██     ██          ██      
██   ██     ██     ██          █████   
██   ██     ██     ██          ██      
██████      ██      ██████     ███████ 
       
        created by : soroush yasini
    """)
banner()
def main():
    global dice
    dice = input("to start the game, press ENTER : ")
main()
def dices():
    import random
    if dice == "" :
        rd = random.randint(1, 6)
        if rd == 1:
            print("""
                        ██ 
                       ███ 
                        ██ 
                        ██ 
                        ██ 
            """)
        elif rd == 2:
            print("""
                        ██████  
                             ██ 
                         █████  
                        ██      
                        ███████ 
            """)    
        elif rd == 3 :
            print("""
                        ██████  
                             ██ 
                         █████  
                             ██ 
                        ██████  
            """)
        elif rd == 4 :
            print("""
                        ██   ██ 
                        ██   ██ 
                        ███████ 
                             ██ 
                             ██
            """)
        elif rd == 5 :
            print("""
                ███████ 
                ██      
                ███████ 
                     ██ 
                ███████             
            """)
        elif rd == 6 :
            print(color.OKGREEN + """
                         ██████  
                        ██       
                        ███████  
                        ██    ██ 
                         ██████
            """)
            extra = input("congrats! now you have a extra chance ! , press ENTER to dice again : ")
            if extra == "" :
                dices()
dices()