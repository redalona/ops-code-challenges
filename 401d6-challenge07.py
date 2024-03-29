#!/usr/bin/python3

# Script: Ops 401 Class 07 Ops Challenge Solution
# Author: Script generated by chatGPT
# Date of latest revision: 04/25/2023
# Purpose: 

import os
import sys
from cryptography.fernet import Fernet

def generate_key():
    """Generates a Fernet key."""
    return Fernet.generate_key()

def encrypt_file(key, in_filename, out_filename=None):
    """Encrypts a file using Fernet symmetric encryption."""
    if not out_filename:
        out_filename = in_filename + '.encrypted'

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(key.encrypt(infile.read()))

    os.remove(in_filename)

def decrypt_file(key, in_filename, out_filename=None):
    """Decrypts a file that was encrypted with Fernet symmetric encryption."""
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(key.decrypt(infile.read()))

    os.remove(in_filename)

def encrypt_folder(key, folder):
    """Recursively encrypts all files in a folder using Fernet symmetric encryption."""
    fernet = Fernet(key)

    for root, dirs, files in os.walk(folder):
        for file in files:
            filename = os.path.join(root, file)
            encrypt_file(fernet, filename)

def decrypt_folder(key, folder):
    """Recursively decrypts all files in a folder that were encrypted with Fernet symmetric encryption."""
    fernet = Fernet(key)

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.encrypted'):
                filename = os.path.join(root, file)
                decrypt_file(fernet, filename)

# Example usage
if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'encrypt'

    # Prompt the user for a directory path
    folder = input('Enter a directory path to encrypt/decrypt: ')

    # Verify that the directory path exists
    if not os.path.isdir(folder):
        print(f'Invalid directory: {folder}')
        sys.exit(1)

    if mode == 'encrypt':
        key = generate_key()

        # Prompt the user to choose how to get the key
        key_input = input('Do you want to print the key to the console (c) or save it to a file (f)? ')

        if key_input == 'c':
            print(f'The encryption key is: {key.decode()}')
        elif key_input == 'f':
            key_filename = input('Enter a filename for the key (default is "key.txt"): ') or 'key.txt'
            with open(key_filename, 'wb') as f:
                f.write(key)
        else:
            print(f'Invalid input: {key_input}. Valid inputs are "c" or "f"')
            sys.exit(1)

        print('Encrypting files...')
        encrypt_folder(key, folder)
    elif mode == 'decrypt':
        key_filename = input('Enter the filename of the key: ')
        with open(key_filename, 'rb') as f:
            key = f.read()

        print('Decrypting files...')
        decrypt_folder(key, folder)
    else:
        print(f'Invalid mode: {mode}. Valid modes are "encrypt" or "decrypt"')
        sys.exit(1)

    print('Done.')
