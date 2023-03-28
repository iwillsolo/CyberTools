# Zip Password Cracker

This is a simple script that can be used to crack the password of a password-protected Zip archive. The script supports both legacy ZipCrypto encryption and AES encryption.

### Requirements
* Python 3.x
* argparse
* zipfile
* os

```Python3
$ python zip_cracker.py zip_filename [-w WORDLIST]
```
### Required Arguments:
zip_filename: Specifies the Zip archive to be cracked.

-w, --wordlist: Specifies the dictionary file to be used for the password cracking process.

### How it works
The script tries to crack the password of the provided Zip archive by trying all the passwords in the provided dictionary file until it finds the correct password. It uses the zipfile module in Python to extract the contents of the Zip archive. If the archive is encrypted with AES encryption, the script uses the setpassword() method to set the password.

### Limitations
This script only works with password-protected Zip archives. It does not support cracking the password of encrypted files in the Zip archive

### License
This project is licensed under the terms of the MIT license.
