import hmac
import hashlib
import secrets

class MyHMAC:
    def __init__(self):
        self.hmac_generated = ""
        self.secret_key = ""

    def GenerateRandomKey(self):
        self.secret_key = secrets.token_bytes(32)

    def GenerateHMAC(self, secret_key, data):
        h = hmac.new(secret_key, data, hashlib.sha3_256)
        return h.hexdigest()

    def CreationOfHMAC(self, data):
        self.GenerateRandomKey()
        self.hmac_generated = self.GenerateHMAC(self.secret_key, data.encode())
        print(self.hmac_generated)

    def CheckHMAC(self):
        PCHMAC = input("Enter the HMAC you want to check: ")
        ComputerMoveValue = input("Enter computer value: ")
        PCSecretKey = bytes.fromhex(input("Enter key: "))
        hmac_calculated = self.GenerateHMAC(PCSecretKey, ComputerMoveValue.encode())
        if hmac_calculated == PCHMAC:
            print("The move is correct. HMAC matches.")
        else:
            print("The move is wrong. HMAC does not match.")
        print()