#!/usr/bin/env python3

import string

hint = (
"g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.\n"
"bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.\n"
"sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")

alphabet  = string.ascii_lowercase
shift     = 2 % 26
codetable = str.maketrans(alphabet, alphabet[shift:]+alphabet[:shift])

#print(hint.translate(codetable))

encrypted = "map"
decrypted = encrypted.translate(codetable)
print("http://www.pythonchallenge.com/pc/def/" + decrypted + ".html")
