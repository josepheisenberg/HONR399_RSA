import random
import sympy
import numpy 
import math
               
def find_prime(digits):
    found_prime = False
    while(not found_prime):
        test_val = random.randint(10**(digits-1), (10**digits)) 
        found_prime = sympy.isprime(test_val)
    return test_val

def find_d_e(p, q, n):
    d = find_prime(int(max((math.log10(p), math.log10(q)))) + 2)
    e = pow(d, -1, ((p -1) * (q - 1)))
    if(e < math.log(n,2)):
        return find_d_e(p,q,n)
    return d, e

def text_to_numbers(message):
    numbers = []
    for char in message:
        numbers.append(ord(char))
    return numbers

def rsa(numbers, e, n):
    conversions = []
    for num in numbers:
        conversions.append(pow(num, e, n))
    return conversions
        
def decrypt(encrypted, d, n):
    decrypted = []
    for num in encrypted:
        decrypted.append(pow(num, d, n))
    return decrypted

def numbers_to_text(decrypted):
    message = ""
    for num in decrypted:
        message += chr(num)
    return message

dgts = 100
user1_p = find_prime(dgts)
user1_q = find_prime(dgts)
user1_n = user1_p * user1_q
user1_phi = (user1_p - 1) * (user1_q - 1)
user1_d, user1_e = find_d_e(user1_p, user1_q, user1_n)
print("\nUser 1 values:\np:", user1_p,"\nq:", user1_q,"\nn:", user1_n,"\nd:", user1_d,"\ne:", user1_e)
print("\nd * e mod (p - 1) * (q - 1) ≡ ", (user1_d * user1_e) % user1_phi)

user2_p = find_prime(dgts)
user2_q = find_prime(dgts)
user2_n = user2_p * user2_q
user2_phi = (user2_p - 1) * (user2_q - 1)
user2_d, user2_e = find_d_e(user2_p, user2_q, user2_n)
print("\nUser 2 values:\np:", user2_p,"\nq:", user2_q,"\nn:", user2_n,"\nd:", user2_d,"\ne:", user2_e)
print("\nd * e mod (p - 1) * (q - 1) ≡ ", (user2_d * user2_e) % user2_phi)

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

