#!/usr/bin/env python3

import zipfile
import argparse
import os.path


def main(zip_filename: str, dictionary_filename: str) -> None:
    counter = 0
    found = False

    if not os.path.exists(dictionary_filename):
        print(f"[-] Error: {dictionary_filename} does not exist")
        return

    with zipfile.ZipFile(zip_filename) as zip_file:
        zip_info = zip_file.infolist()[0]
        encryption_type = zip_info.flag_bits & 0x800  # Check for AES encryption flag

        if not encryption_type:
            # Legacy ZipCrypto encryption
            for password in open(dictionary_filename):
                password = password.strip('\n')
                counter += 1
                if counter % 10000 == 0:
                    print(f"[+] {counter} passwords checked so far...")
                try:
                    zip_file.extractall(pwd=password.encode())
                    print(f'Password found: {password}')
                    found = True
                    break
                except RuntimeError:
                    pass
        else:
            # AES encryption
            with open(dictionary_filename) as password_file:
                for password in password_file:
                    password = password.strip('\n')
                    counter += 1
                    if counter % 10000 == 0:
                        print(f"[+] {counter} passwords checked so far...")
                    try:
                        zip_file.setpassword(password.encode())
                        zip_file.extractall()
                        print(f'Password found: {password}')
                        found = True
                        break
                    except RuntimeError:
                        pass

    if not found:
        print("[-] Password not found")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("zip_filename", help="Specify a .zip file to crack")
    parser.add_argument("-w", "--wordlist", help="dictionary file")
    args = parser.parse_args()

    try:
        main(args.zip_filename, args.wordlist)
    except Exception as e:
        print(f"[-] Error: {e}")
