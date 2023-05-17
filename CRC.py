class CRC:
    def __init__(self):
        self.cdw = ''

    def xor(self, a, b):
        return ''.join('0' if a[i] == b[i] else '1' for i in range(1, len(b)))

    def crc(self, message, key):
        pick = len(key)
        tmp = message[:pick]
        for char in message[pick:]:
            if tmp[0] == '1':
                tmp = self.xor(key, tmp) + char
            else:
                tmp = self.xor('0' * pick, tmp) + char
            pick += 1
        return self.xor(key, tmp) if tmp[0] == '1' else self.xor('0' * pick, tmp)

    def encode(self, data, key):
        remainder = self.crc(data + '0' * (len(key) - 1), key)
        codeword = data + remainder
        self.cdw += codeword
        print("Remainder:", remainder)
        print("Encoded data:", codeword)

    def decode(self, key, data):
        remainder = self.crc(data, key)
        print(remainder)
        print("No error" if remainder == (len(key)-1) * '0' else "Error")

c = CRC()
data = '100100'
key = '1101'
c.encode(data, key)
c.decode(key, c.cdw)
print(c.cdw)
