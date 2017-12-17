#pycryptograhpy och pycryptodome
from Crypto.PublicKey import RSA
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
#Satans skit uppgift och satans skit bibliotek och satans skit skit
with open("cens.pem", "rb") as key_file:
    key = serialization.load_pem_private_key(key_file.read(),password=None,backend=default_backend())
    priv = key.private_numbers()
    pub= key.public_key()
    pub = pub.public_numbers()
    d = priv.d
    p = priv.p
    q = priv.q
    e = pub.e
    n = p * q
    #cryptography klarar av att läsa den censurerade nyckeln men det går inte
    #(vad jag har hittatat i alla fall) att ändra på värdena, vilket cryptodome
    #stödjer men cryptodome spottar ut ett kryptiskt error när den läser nyckeln
    # säkert p*q = n som skiter sig
    construct = (n,e,d,p,q)
    key = RSA.construct(construct)


    with open('uncens.pem','wb') as f:
        f.write(key.exportKey('PEM'))
