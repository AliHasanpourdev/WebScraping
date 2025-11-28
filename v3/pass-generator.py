#import needed libraries
import string as st
import random

#create characters for generate password
upp = st.ascii_uppercase
low = st.ascii_lowercase
num = st.digits
char = st.punctuation

#main code
l = [list(upp), list(low), list(num), list(char)]
pas = ""
for i in range(random.randint(8,16)) :
    a = random.choices(l)[0]
    pas += random.choices(a)[0]

#show password of genereted
print(pas)