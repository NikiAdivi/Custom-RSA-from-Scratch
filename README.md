# Custom RSA from Scratch

RSA (Rivest-Shamir-Adleman) is an algorithm used by modern computers to encrypt
and decrypt messages. It is an asymmetric cryptographic algorithm. Thus it involves
the use of 2 seperate keys for encryption and decryption.
This is also called public key cryptography because one of the keys can be given to
anyone. The other key must be kept private.
The algorithm is robust as it is based on the fact that finding the factors of a large
composite number is difficult: especially when the factors are random prime numbers.
Hence even if the public key is known it is difficult to find the private key.

### Disclaimer 
This is not the original RSA implementation. Considering the system limitations, the following implementation encrypts letter by letter.
Also uses a padding scheme to add digits at alternate places to ensure that same letter doesn't get encrypted to the same number.

## Two types of implementatons:
### Using File handling:
The data to be encrypted has to be written into the file `toBeEncrypted.txt` .
Two files will be created namely `encrypted.txt` and `Decrypted.txt` in the same folder containing
encrypted and decrypted data respectively.

- To run: `python3 RSA_filehandling.py`
```
NOTE: If you are running the program more than once make sure the previoiusly
created `encrypted.txt` and `Decrypted.txt` are deleted from the directory.
```
### Using GUI tkinter:
A message box will appear right after running the program.
The buttons Encrypt and Decrypt will perform the respective operations.

- To run: `python3 RSA_GUI`

## Screenshots

### Using Files
![image](https://user-images.githubusercontent.com/43961340/122583286-b1a48680-d076-11eb-92d8-e1fcbda97920.png)

![image](https://user-images.githubusercontent.com/43961340/122583307-b5d0a400-d076-11eb-856e-e917c00ee039.png)

### Using GUI
![image](https://user-images.githubusercontent.com/43961340/122583195-989bd580-d076-11eb-94eb-92d54670f713.png)
