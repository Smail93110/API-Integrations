import random

minuscule  = "abcdefghijklmnopqrstuvwxyz"
majuscule  ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffres  ="0123456789"
symboles  ="[]{}()*;/,._-"


all = minuscule  + majuscule  + chiffres  +symboles 
longueur  = 16
password = "".join(random.sample(all,longueur ))

print(password)

