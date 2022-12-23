from Crypto.Cipher import DES
from crc64iso.crc64iso import crc64
class Crypto_Class:
    def __init__(self):
        super(Crypto_Class, self).__init__()
        # self.object = object

    # @staticmethod
    def append_last_bytes(text, master):
        length = 8 - len(text) % 8
        text = text.ljust(len(text) + length, length.to_bytes(1, 'big'))
        return text

    # @staticmethod
    def delete_last_bytes(text):
        length = text[-1]
        if length > 8:
            
            raise Exception()
        return text[:-length]

    def crypt(self, file_to_show):
        xd = []
        with open(file_to_show[0], 'rb') as f:
            enc_file1 = f.read()
        xd.append(file_to_show[0])
        enc_file = self.append_last_bytes(enc_file1)
        des = DES.new(bytes.fromhex(crc64(str('xddxddxdd'))), DES.MODE_CFB)
        encrypted_data = des.encrypt(enc_file)
        with open(f"{file_to_show[0]}.enc", 'wb') as f:
            f.write(encrypted_data)

    def decrypt(self, file_to_show):
        xd = []
        xd.append(file_to_show[0])                              
        if file_to_show[0].split('/')[-1].split('.')[-1] != 'enc':
            print('no')
        with open(file_to_show[0], 'rb') as f:
            dec_file = f.read()         
        des = DES.new(bytes.fromhex(crc64(str('xddxddxdd'))), DES.MODE_CFB)
        decrypted_data = des.decrypt(dec_file)
        d1 = self.delete_last_bytes(decrypted_data)
        f_name_to_decode = '.'.join(['.'.join(file_to_show[0][:-4].split('.')[:-1])+'_decoded', file_to_show[0][:-4].split('.')[-1]])
        with open(f"{f_name_to_decode}", 'wb') as f:
            f.write(d1)