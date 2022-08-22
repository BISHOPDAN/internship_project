import pyAesCrypt
from os import stat, remove


class fencryption:
    """This class is for all the encription and decryption I will use in future."""
    def __init__(self, password):

        # encryption/decryption buffer size - 64K
        self.bufferSize = 64 * 1024

        if not password:
            self.password = "Id0NotLik3SPRING@2018"
        else:
            self.password = password

    def encrypt_file(self, unencrypted_file):
        """Encrypting file."""

        encrypted_file = unencrypted_file + ".fenc"

        if ".txt" not in unencrypted_file.lower():
            # Encrypt
            pyAesCrypt.encryptFile(unencrypted_file, encrypted_file, self.password, self.bufferSize)
        else:
            # Streamed Encrypt
            with open(unencrypted_file, "rb") as fIn:
                with open(encrypted_file, "wb") as fOut:
                    pyAesCrypt.encryptStream(fIn, fOut, self.password, self.bufferSize)

        unencrypted_file_size = stat(unencrypted_file).st_size
        encrypted_file_size = stat(encrypted_file).st_size

        msg = """Unencrypted File Size is {unencrypted_file_size} \n 
        Encrypted File Size is {encrypted_file_size}""".format(unencrypted_file_size=unencrypted_file_size, 
        encrypted_file_size=encrypted_file_size)

        print(msg)

        return msg

    def decrypt_file(self, encrypted_file):
        """Decrypt File."""

        decrypted_file = encrypted_file.replace('.fenc', '')
        encrypted_file_size = stat(encrypted_file).st_size

        if ".txt" not in encrypted_file.lower():
            # Decrypt
            pyAesCrypt.decryptFile(encrypted_file, decrypted_file, self.password, self.bufferSize)
        else:
            # Streamed Decrypt
            with open(encrypted_file, "rb") as fIn:
                with open(decrypted_file, "wb") as fOut:
                    try:
                        # Decrypt file stream
                        pyAesCrypt.decryptStream(fIn, fOut, self.password, self.bufferSize, encrypted_file_size)
                    except ValueError:
                        # remove output file on error
                        remove(decrypted_file)

        decrypted_file_size = stat(decrypted_file).st_size
        encrypted_file_size = stat(encrypted_file).st_size

        msg = """Encrypted File Size is {encrypted_file_size} \n 
        Decrypted File Size is {decrypted_file_size}""".format(decrypted_file_size=decrypted_file_size, 
        encrypted_file_size=encrypted_file_size)

        print(msg)

        return msg