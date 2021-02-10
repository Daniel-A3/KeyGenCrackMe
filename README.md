# KeyGenCrackMe
A crack me that I reverse engineered and made a python script that generated keys for it.

**How the crackme Key Validation works:**
- The C program takes in an argument, which is expected to be a key, the key is then checked by adding all of the letters' ascii values and comparing the sum 
to the correct keys' sum of ascii values, if its the same, access is granted, otherwise access is denied.
- This means to solve this, you do not need to original key, just a sequence of characters of which when their characters' ascii values are added together it gives the same sum.

**Examples:**

![alt text](https://github.com/Daniel-A3/KeyGenCrackMe/blob/main/Pictures/keygen.PNG)

![alt text](https://github.com/Daniel-A3/KeyGenCrackMe/blob/main/Pictures/keygenProof.PNG)
