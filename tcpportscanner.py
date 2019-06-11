from socket import *

def connectivity(tgthost,tgtport):
    try:
        host_name=gethostbyaddr(tgthost)
    except:
        print("sorry host not found ")
        exit(2)
        
    
    
    try:
        
        sock = socket(AF_INET,SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect((tgthost,tgtport))
       

        print("PORT "+str(tgtport) + " opened on " + tgthost)
        

    except:
        
        print("PORT " + str(tgtport) + " closed on " + tgthost)
         
    finally:
        sock.close()





def main():
    print("Welcome to this simple port scanner ")
    user_input = raw_input("Enter host ip address ")
    print(" Choose one of the options")
    print("1. select 1 to check range of ports on host")
    print("2. select 2 to scan a single port on host")
    user_input1 = int(input("Enter choice \n"))
    if user_input1 == 1:
        print("Enter two ports for eg if want to scan 1-1024 ports first enter 1 and then enter 1024")
        user_range_input = int(input("Enter your port range first port "))
        user_range_input1 = int(input("Enter your port range second port "))
        for i in range(user_range_input,user_range_input1 + 1):
            connectivity(user_input,i)
    elif user_input1 == 2:
        user_not_range = int(input("Enter port to check "))
        connectivity(user_input,user_not_range)
    else:
        print("Sorry the choice you chose does not exist ")
        exit(1)
main()




