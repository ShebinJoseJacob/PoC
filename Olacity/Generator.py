import random 
import string  
     
def rand_pass(size):    
    generate_pass = ''.join([random.choice( string.ascii_uppercase +string.ascii_lowercase +string.digits) for n in range(size)])  
                             
    return generate_pass
while True:
    password = rand_pass(12)
    print(password)
    f = open("payload.txt", "a")
    f.writelines(password+"\n")
    f.close()
