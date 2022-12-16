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
                                              
                                              
███    ███  █████  ████████ ██   ██           
████  ████ ██   ██    ██    ██   ██           
██ ████ ██ ███████    ██    ███████           
██  ██  ██ ██   ██    ██    ██   ██           
██      ██ ██   ██    ██    ██   ██ 
created by soroush yasini
    """)
banner()
def hint():
    print("""
    hello there ! this program will calculate the sum of numbers.
    insert the number and press inter.
    as long as you enter number, program ask you more numbers.
    for final calculation enter EXIT .
    """)

hint()
a = input("exit or numbers : ")
sum = 0
while a != "exit":
    sum = int(a) + sum
    a = input("exit or numbers : ")
print(color.OKGREEN + "the sum is : ", sum)


