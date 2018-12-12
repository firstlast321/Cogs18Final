def encode_message(message, key = 4):
    """Encoding the message. Converts input string into a string containing 
    Unicode code points. 
    
    Parameters
    ----------
    message : string 
        String to be converted to code points 
    key : int or float 
        Number needed to encrpyt the message to a specific code point  
        to later be accessed by another with the same key
    
    Return
    ---------
    encoded : string
        Result string containing the code points for input string.
    """
    
    encoded = ''
    
    for character in message:
        unicodeVal = ord(character)
        unicodeVal = key+unicodeVal
        toReturn = chr(unicodeVal)
        encoded = encoded + toReturn

    return encoded


def decode_message(encoded, key=4):
    """Decoding the message. 
    
    Parameters
    ----------
    encoded : string 
        Code point string to be converted back to original string. 
            
    key : int or float
        Code point number needed for user to decrypt the encrypted message.
        
    Return
    ---------
    decoded : string
        Result string after the encoded string has been converted back to 
        show the original message. 
    """
    
    decoded = ''

    for character in encoded:
        ucp = ord(character)
        ucp = ucp - key
        ucp = chr(ucp)  #this is the decoder
        decoded += ucp

    return decoded

