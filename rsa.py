import random
import sympy
import math
           
''' Below section: processes used for RSA'''    
def find_prime(digits):
    #Find a prime of specified number of digits by generating a random number
    #And testing if it is prime until one is found
    found_prime = False
    while(not found_prime):
        test_val = random.randint(10**(digits-1), (10**digits)) 
        found_prime = sympy.isprime(test_val)
    return test_val

def find_d_e(p, q, n):
    #Find d by finding a random prime larger than p and q, and then find e
    #Using d, p, and q. If e is improper, try again
    d = find_prime(int(max((math.log10(p), math.log10(q)))) + 2)
    e = pow(d, -1, ((p -1) * (q - 1)))
    if(e < math.log(n,2)):
        return find_d_e(p,q,n)
    return d, e

def text_to_numbers(message):
    #Convert each character of the message into a number
    #using the standard ASCII table
    numbers = []
    for char in message:
        numbers.append(ord(char))
    return numbers

def rsa(numbers, e, n):
    #Encrypt each character using e and n
    conversions = []
    for num in numbers:
        conversions.append(pow(num, e, n))
    return conversions
        
def decrypt(encrypted, d, n):
    #Decrypt each character using d and n
    decrypted = []
    for num in encrypted:
        decrypted.append(pow(num, d, n))
    return decrypted

def numbers_to_text(decrypted):
    #Convert ASCII encodings back to characters
    message = ""
    for num in decrypted:
        message += chr(num)
    return message



''' Below section: demonstrating the use of above processes '''
dgts = 100 #Set number of digits being used for p and q -- modify as you like

#Find user 1 parameters and print them
user1_p = find_prime(dgts)
user1_q = find_prime(dgts)
user1_n = user1_p * user1_q
user1_phi = (user1_p - 1) * (user1_q - 1)
user1_d, user1_e = find_d_e(user1_p, user1_q, user1_n)
print("\nUser 1 values:\np:", user1_p,"\nq:", user1_q,"\nn:", user1_n,"\nd:", user1_d,"\ne:", user1_e)

#Verify d and e are compatible for user 1
print("\nd * e mod (p - 1) * (q - 1) ≡ ", (user1_d * user1_e) % user1_phi)

#Find user 2 parameters and print them
user2_p = find_prime(dgts)
user2_q = find_prime(dgts)
user2_n = user2_p * user2_q
user2_phi = (user2_p - 1) * (user2_q - 1)
user2_d, user2_e = find_d_e(user2_p, user2_q, user2_n)
print("\nUser 2 values:\np:", user2_p,"\nq:", user2_q,"\nn:", user2_n,"\nd:", user2_d,"\ne:", user2_e)

#Verify d and e are compatible for user 2
print("\nd * e mod (p - 1) * (q - 1) ≡ ", (user2_d * user2_e) % user2_phi)


#Process for sending a message from user 1 to user 2
#Prints each step along the way
#Feel free to change the message on the line below as desired
msg1to2 = "What is everyone's favorite movie?"
print("\n\nMessage from user 1 to user 2 before encryption:", msg1to2)
msg1to2_converted = text_to_numbers(msg1to2)
print("\nConverted message:", msg1to2_converted)
msg1to2_encrypted = rsa(msg1to2_converted, user2_e, user2_n)
print("\nEncrypted message:", msg1to2_encrypted)
msg1to2_decrypted = decrypt(msg1to2_encrypted, user2_d, user2_n)
print("\nDecrypted message:", msg1to2_decrypted)
msg1to2_result = numbers_to_text(msg1to2_decrypted)
print("\nResult:",msg1to2_result)

#Process for sending a reply from user 2 to user 1
#Prints each step along the way
#Feel free to change the message on the line below as desired
msg2to1 = "Napoleon Dynamite"
print("\n\nReply from user 2 to user 1 before encryption:", msg2to1)
msg2to1_converted = text_to_numbers(msg2to1)
print("\nConverted message:", msg2to1_converted)
msg2to1_encrypted = rsa(msg2to1_converted, user1_e, user1_n)
print("\nEncrypted message:", msg2to1_encrypted)
msg2to1_decrypted = decrypt(msg2to1_encrypted, user1_d, user1_n)
print("\nDecrypted message:", msg2to1_decrypted)
msg2to1_result = numbers_to_text(msg2to1_decrypted)
print("\nResult:",msg2to1_result)

