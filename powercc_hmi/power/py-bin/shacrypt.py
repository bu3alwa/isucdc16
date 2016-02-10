import datetime
from Crypto.Cipher import AES
import base64

debug = True

def encrypt(message_txt):
	datetime_val = str(datetime.datetime.now())

	iv_txt = datetime_val[0:15] + '0'

	key = datetime_val[0:1]*16 + iv_txt

	cipher = AES.new(key, AES.MODE_CBC, iv_txt)

	if len(message_txt) < 32:
		message_txt += ' '*(32 - len(message_txt))
	
	if debug:
		print 'IV'
		print iv_txt
		print len(iv_txt)

		print 'Key:'
		print key
		print len(key)
	
	cipher_txt = cipher.encrypt(message_txt)


	return base64.b64encode(cipher_txt)

