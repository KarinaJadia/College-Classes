import os
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

priv_key = '''-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQCkQxlb1oPNbkdZ+pVTrltiDQuDxONUl8vTrJcaWe2GfolRTaqd
dKyGt4HrXZld8n7NTipjDLTSEqJDyO6Zga/sCTWNEXiHOF5iT8Hc5+PJ+Ys6FUef
0UJUeSBFtmZhMLiUWrX860YfHzymQF3+gwfHkUuyMYbU2Yhv7gUZZOH3ewIDAQAB
AoGAFxn8ugbMWJr22/e7Ap7V6U9OXETXd/E1UFrIkYMuPakUJOQYZ7aeAQBT/EcY
p7bQEI26tl12HMlUGtZqgBpWJFEfQbkCdsE1Gl3T+n9hJduEEjglJ2pH86mzlQWA
O9laAEALpnJNTLsYzcDcOuFo3hgCknKNiwZ7OZda9zwTzKkCQQC6EdOGxfMoguB0
a5NUkztLju7DkrhGdVWp0xmt7ysSlenfAzrmeYyr9XNNJCnmi2UBe6EM2GNVQCRK
eCuQLVv9AkEA4f8fN8HHF+NoOPvmNxWj9uVxZHG6wdcUQvLiSex3e7Z3bpBGlspS
R5LVeDZBOHnX8PppKHWEUc8HYVHrRj9u1wJAYDrz8NHTbfIx70PrkGQM2Ij1hwQM
dbQdN5VLxJ7a4ePSbloXTjcyv4RTu2Omn+sbs+aiZihLRz3DBxibPxeWaQJABWSt
Pgtl0PAgYJvCVrYxf4biOd9s8YtMdHyPYew+vbkRCJZw2NBjPkoGxiOlUs+1k46m
S8ziJ4GlT3FBCCAjaQJBAKI6n/Phn8xx2D8uWGNdTD+M+vCWykkFxu9sEg0Q8m0k
jve6qcMFcr6AtVPyWal+xd+6dehyMNsAbMXdfSAraBc=
-----END RSA PRIVATE KEY-----'''
d = RSA.import_key(priv_key)

with open('/home/cse/Lab3/Q6files/EncryptedSharedKey.txt', 'rb') as f:
  enc_key = f.read()
  
decryptor = PKCS1_OAEP.new(d)
dec_key = decryptor.decrypt(enc_key)
  
sys.stdout.buffer.write(dec_key) # writes to standard output