import base64

class Decoding:

    @staticmethod
    def code_decoding(encrypt):

        decoded_bytes = base64.b64decode(encrypt)
        decoded_string = decoded_bytes.decode('utf-8')
        decoded_arr=decoded_string.split(",")

        return decoded_arr



