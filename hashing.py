#############################
##   Hashing and SHA-256   ##
#############################

# import sha256
from hashlib import sha256

# text to hash
text = 'I am excited to learn about blockchain!'

# create a sha256 hash object. 
# Encode the text first.

hash_result = sha256(text.encode())
print(f"{hash_result}")

# Call the .hexdigest() method on hash_result and print result

print(f'{hash_result.hexdigest()}')

# one line of code to hash text.
# sha256(text.encode()).hexdigest()
# print( sha256(text.encode()).hexdigest() )


