#!/usr/bin/env python

import re
import sys
import random

"""
Definition of reponds. The fileids based on ecah bot stored ids, use the docid function defined on pybot.py to get it.
Emojis must defined as: = '\@emojicode'
Example: emoji1 = '\U0001f601'
Telegram files (stickers, gifs, images,...) must defined as: = '\'file_id\': \'@fileid\''
Example: gif1 = '\'file_id\': \'BQADBAADNwADous4Ag194Ydqad2mAg\''
"""

welcome = [
        'Bienvenido'
        ]

greetings = [
        'Hola miarma',
        'Qué pasa chumach@',
        'Buenas',
        'Hola',
        '\U0001f44b',
        '\'file_id\': \'BQADAgADZgADVSx4C4I00LsibnWGAg\'',
        '\'file_id\': \'BQADBAADdQADmDVxAhMWZRgAAZIftAI\'',
        '\'file_id\': \'BQADBAADcQADbWNIUBNXQ8IZfEG0Ag\'',
        '\'file_id\': \'BQADBAADBwEAAmkmLQABI_vOB4L4I18C\''
        ]

thanks = [
        '\U0001f601',
        '\U0001f60c',
        '\U0001f60a',
        '\'file_id\': \'BQADBAADjQEAAtcHwgO1KRTaI2qyAwI\'',
        '\'file_id\': \'BQADAgADfQQAAp2mfwO0ZdyCjqvwCQI\'',
        '\'file_id\': \'BQADBAADfQADbWNIUIgqGen28FKGAg\'',
        '\'file_id\': \'BQADBAADfAADbWNIUK8jVuJVjdbJAg\''
        ]

confuse = [
        '\'file_id\': \'BQADBAADEAAD389YULJFl7VHI9OOAg\'',
        '\'file_id\': \'BQADAgAD0AAD3aEBAAEOTYtKn4jHAgI\'',
        '\'file_id\': \'BQADBAADSQADbWNIUCqTvCUcViMlAg\'',
        '\'file_id\': \'BQADBAADdQADbWNIUOey7eD40GieAg\'',
        '\'file_id\': \'BQADBAADbwADbWNIUOE1MaS3Vv9DAg\'',
        '\'file_id\': \'BQADBAADagADbWNIUMc-2l02yHqlAg\''
        ]
			
dunno = [
        '\'file_id\': \'BQADBAADIgQAAvOYrgABWSR8XWtnw9YC\'',
        '\'file_id\': \'BQADAgADUQEAAksODwABadMSYFiU4P8C\'',
        '\'file_id\': \'BQADBAADcgADbWNIUKRSv45-1ITCAg\'',
        '\'file_id\': \'BQADBAADcAADbWNIUPzA9g2WzO0bAg\'',
        '\'file_id\': \'BQADBAADbgADbWNIULTSYP_EvC9JAg\'',
        '\'file_id\': \'BQADBAADbQADbWNIULWV5EmArzbWAg\''			
        ]

angry = [
        '\U0001f624'
        '\'file_id\': \'BQADBAADEQAD389YUFusQnZirBpEAg\'',
        '\'file_id\': \'BQADAgADSQEAAksODwAB59ceQzdm1ScC\'',
        '\'file_id\': \'BQADBAADYQADmDVxAtZoNXkGAAE8mgI\'',
        '\'file_id\': \'BQADBAADWgADoOj0Bz_UI3iME0_8Ag\''
        ]

nope = [
        '\U0001f644',
        '\'file_id\': \'BQADBAADdgADbWNIUPcgTARxEOujAg\'',
        '\'file_id\': \'BQADBAADdAADbWNIUE2u3Y8_mvJKAg\''
        ]

think = [
        '\U0001f914'
        ]

approve = [
        '\'file_id\': \'BQADBAADDgAD389YUB3TyhKHLhJoAg\'',
        '\'file_id\': \'BQADAgADQgADVSx4C1--9Yr_WY3AAg\'',
        '\'file_id\': \'BQADBAADogEAAtcHwgMPTn5hg55dxwI\'',
        '\'file_id\': \'BQADBAADLwAD9VikAAE4gx_D4GXAmgI\''
        ]

disapprove = [
        '\'file_id\': \'BQADBAADCAAD389YUE5cDyoi8_9QAg\'',
        '\'file_id\': \'BQADAgADPwEAAksODwABs3Wcq8kBQAkC\'',
        '\'file_id\': \'BQADBAADoAEAAtcHwgPZIxeOpVdTjwI\'',
        '\'file_id\': \'BQADBAADIAQAAvOYrgABPkcIbctih7QC\'',
        '\'file_id\': \'BQADBAADcwADbWNIULP1NTWOxBKoAg\'',
        '\'file_id\': \'BQADBAADbAADbWNIULL7nGyjVpV9Ag\'',
        '\'file_id\': \'BQADBAADawADbWNIUN_kIliTAkeuAg\'',
        '\'file_id\': \'BQADBAADoAADbnLQUNO_slpADrUXAg\''
        ]

surprise = [
        '\'file_id\': \'BQADBAADGAAD389YUNVMoowzv5eCAg\'',
        '\'file_id\': \'BQADBAADGQAD389YUDD8zLASSmqqAg\'',
        '\'file_id\': \'BQADAgADoAEAAksODwABOQsIrE2jPkAC\'',
        '\'file_id\': \'BQADAgADYAcAAlOx9wPOmBwqFnKyVAI\'',
        '\'file_id\': \'BQADAgADTAADVSx4C1Euf8V7S5s0Ag\''
        ]

supect = [
        '\'file_id\': \'BQADBAADFQAD389YUPWCmNUjycZmAg\'',
        '\'file_id\': \'BQADBAADFgAD389YUK5YFBTYhX4-Ag\'',
        '\'file_id\': \'BQADBAADFwAD389YULVCf6TMwePIAg\''		
        ]
			
evil = [
        '\'file_id\': \'BQADBAADEgAD389YUFHEsHIFwkLZAg\'',
        '\'file_id\': \'BQADBAADCwAD389YUIx-ceAF5Q4oAg\'',
        '\'file_id\': \'BQADAgADOgADVSx4C7RBZBTJ4211Ag\'',
        '\'file_id\': \'BQADBAAD4wUAApv7sgABDIhzioLPZrMC\''	
        ]

math = [
        '\'file_id\': \'BQADAgADgwQAAp2mfwNctAJy52QRIAI\'',
        '\'file_id\': \'BQADBAADDlkAAioYZAf5_eBK2LySZwI\''
        ]

here = [
        '\'file_id\': \'BQADAgADWAADVSx4Cy7LVdEFvQ0gAg\'',
        '\'file_id\': \'BQADBAADSAADbWNIUFlTqNhvyFFEAg\''
        ]
			
friday = [
        '\'file_id\': \'BQADAwADvAMAAqbJWAABK3w6QpBbOb4C\'',
        '\'file_id\': \'BQADBAADHwADmDVxAsVMpnbj30pPAg\'',
        '\'file_id\': \'BQADBAADaQADbWNIUNh-nUaOYVP0Ag\'',
        '\'file_id\': \'BQADBAADaAADbWNIUBJR4pUTHRilAg\'',
        '\'file_id\': \'BQADBAADZwADbWNIUEjkYtZ763poAg\''
        ]
			
smart = [
        '\'file_id\': \'BQADBAADkwEAAtcHwgP3WKG53_bKngI\''
        ]

scary = [
        '\'file_id\': \'BQADBAADZwADbWNIUEjkYtZ763poAg\''
        ]

bye = [
        'Adios',
        'Chao',
        'Bye',
        'Ta\' luego',
        '\'file_id\': \'BQADBAADEwAD389YUO7mWSDsa8BQAg\''
        ]

leave = [
        'Una pena...'
        ]
			
maintenance = ['\'file_id\': \'BQADAgADNgADVSx4C4QN1JTc8cN3Ag\'']

def responds(words):

        if re.search( r'.*\b(bien)\b.*\b(bot)\b.*', words, re.I|re.M):
		return random.choice(thanks)

	if re.search( r'.*\b(bot)\b.*\b(cuanto)\b.*\b(es)\b.*', words, re.I|re.M):
		return random.choice(math)

	if re.search( r'.*\b(bot)\b.*\b(que)\b.*\b(ha|has)\b.*', words, re.I|re.M):
		return random.choice(dunno)

	if re.search( r'.*\b(bot)\b.*(\b(entiende)\b|\b(comprende)\b).*', words, re.I|re.M):
		return random.choice(confuse)

	if re.search( r'.*\b(bot)\b.*(\b(es)\b|\b(esta)\b|\b(parece)\b).*tont|rubi.*', words, re.I|re.M):
		return random.choice(disapprove)

	if re.search( r'.*\b(bot)\b.*(\b(estas)\b|\b(esta)\b).*\b(ahi)\b.*', words, re.I|re.M):
		return random.choice(here)

	if re.search( r'.*\b(bot)\b.*\b(es)\b.*\b(viernes)\b.*', words, re.I|re.M):
		return random.choice(friday)

	if re.search( r'.*\b(hola)\b|\b(hi)\b|((\b(buenos)\b|\b(buenas)\b) (\b(dias)\b|\b(tardes)\b|\b(noches)\b)).*', words, re.I|re.M):
		return random.choice(greetings)

	if re.search( r'.*\b(adios)\b|\b(chao)\b|\b(bye)\b|((\b(hasta)\b|\b(ta)\b) (\b(luego)\b|\b(mañana)\b)).*', words, re.I|re.M):
		return random.choice(bye)

        if words == 'member_join':
                return random.choice(welcome)

        if words == 'member_left':
                return random.choice(leave)

def hear(words):
    return responds(words)

def main(argv):
    if len(sys.argv)>1:
        print(hear(' '.join(sys.argv)))
    else:
        print('I heard nothing.')

if __name__ == "__main__":
    main(sys.argv)
