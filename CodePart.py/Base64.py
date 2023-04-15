import base64

def encode_decode_base64():
    while True:
        user_input = input("Enter a string to encode/decode with base64 and if u want to quit write just Q and it exits: ")

        if user_input.lower() == 'Q':
            break

        
        encoded_bytes = base64.b64encode(user_input.encode('utf-8'))
        encoded_string = encoded_bytes.decode('utf-8')
        print("Encoded: ", encoded_string)
        
encode_decode_base64()