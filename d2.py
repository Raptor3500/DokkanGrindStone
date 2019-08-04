from pysqlsimplecipher import decryptor #line:10
def usage ():#line:13
    print ('Usage: python decrypt.py encrypted.db password output.db')#line:14
def main (p ='9bf9c6ed9d537c399a6c4513e92ab24717e1a488381e3338593abd923fc8a13b'):#line:17
    O0OOO0OOOOO0OO0OO =bytearray (p .encode ('utf8'))#line:18
    if p =='9bf9c6ed9d537c399a6c4513e92ab24717e1a488381e3338593abd923fc8a13b':#line:19
        OOO0000OOO0O0OO00 ='dataenc_glb.db'#line:20
        OO0OO0000O000O000 ='glb.db'#line:21
    else :#line:22
        OOO0000OOO0O0OO00 ='dataenc_jp.db'#line:23
        OO0OO0000O000O000 ='jp.db'#line:24
    decryptor .fast_stream_decrypt (OOO0000OOO0O0OO00 ,O0OOO0OOOOO0OO0OO ,OO0OO0000O000O000 )#line:27
if __name__ =='__main__':#line:30
    main ()#line:31
