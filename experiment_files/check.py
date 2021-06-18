import random
import math

letters={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b)
def gen_public_key(n,phi):
	list_random_e=[i for i in range(1,phi) if (n%i!=0 and gcd(i,phi) ==1)]
	e=random.choice(list_random_e)
	return(n,e)
def gen_private_key(n,phi,e):
	list_random_k=[i for i in range(1,phi) if (((i*phi)+1)%e ==0)]
	k=random.choice(list_random_k)
	print "k=",k
	d=((k*phi)+1)/e
	return (n,d)


primes=[i for i in range(1,1000) if isPrime(i)]
p=random.choice(primes)
primes.remove(p)
q=random.choice(primes)
print "p=",p
print "q=",q

n=p*q
phi=(p-1)*(q-1)

public_key=gen_public_key(n,phi)
print "public key (n,e) : ",public_key
private_key=gen_private_key(n,phi,public_key[1])
print "private key (n,d) ",private_key

z=raw_input("enter what has to be encrypted")
msg=0
for ch in z:
	msg+=letters[ch]
print "Original message=\t",msg
c=(msg**public_key[1])%n
decryp=(c**private_key[1])%n

print "encrypted=",c
print "decrypted=",decryp



	

	
	

















