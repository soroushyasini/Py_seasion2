class color:
    OKGREEN = '\033[92m'
    OKCYAN = '\033[96m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
def banner():
    print("""
 █████  ██████  ██████   █████  ██    ██ 
██   ██ ██   ██ ██   ██ ██   ██  ██  ██  
███████ ██████  ██████  ███████   ████   
██   ██ ██   ██ ██   ██ ██   ██    ██    
██   ██ ██   ██ ██   ██ ██   ██    ██    
                                             

created by soroush yasini
    """)
banner()
def arr():
    import random
    n = int(input("insert the length of your new array : "))
    r = int(input(color.OKCYAN + """ok, now insert the range of random numbers as you wish.
            remember that the range MUST BE BIGGER THAN length of array ! """))
    r = r + 1
    arry = random.sample(range(r), (n))
    print (color.OKGREEN + "here is the randomized arry", arry)
arr()
        



