"""
# Diffie-Hellman Key Exchange (DHKE) with AES Encryption/Decryption

This Python script implements a Diffie-Hellman Key Exchange (DHKE) to derive a shared key and uses that key for AES encryption and decryption in CBC mode.

## Prerequisites

To run the script, you need to have the following Python libraries installed:

- `pycryptodome`: for AES encryption and decryption.
  
You can install the necessary dependencies using pip:

pip install pycryptodome

## Running the Program

The program takes input values for RSA key generation, encryption, and decryption. Follow these steps to execute the program:

1. **Run the program**:
   ```bash
   python3 DHKE.py

## Input Instructions
Provide the following inputs:

 - **IV: Initialization Vector (hex format)**
 - **g_e: Base parameter for the Diffie-Hellman algorithm**
 - **g_c: Constant to adjust g_e**
 - **N_e: Modulus parameter for Diffie-Hellman**
 - **N_c: Constant to adjust N_e**
 - **x: Your private key for the DHKE**
 - **gy_modN: The calculated public key value**
 - **Encrpyted message: Encrypted text (hex format) that will be decrypted**
 - **Plain text: A string to be encrypted**

## Output

The program will display:

- **Decrypted Plaintext**: The decrypted original message from the given encrypted input.
- **Encrypted Ciphertext**: The ciphertext generated from the given plaintext input.
