import random
import string

def my_pwd():
    length=int(input("enter the length of password:"))
    upper=string.ascii_uppercase
    lower= string.ascii_lowercase
    digits=string.digits
    symbols=string.punctuation
    combined=upper+lower+digits+symbols
    password=random.sample(combined,length)
    
    a="".join(password)
    print(a)
    my_pwd()
my_pwd()    
    