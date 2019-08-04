import base64 #line:3
import hashlib #line:4
import hmac #line:5
import json #line:6
import os #line:7
import time #line:8
import uuid #line:9
from typing import Dict #line:10
import requests #line:12
from Crypto .Cipher import AES #line:13
import c2 #line:15
USER_AGENT ='Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0'#line:19
BLOCK_SIZE =16 #line:21
pad =lambda OOOOOO0O0O000O0O0 :OOOOOO0O0O000O0O0 +(BLOCK_SIZE -len (OOOOOO0O0O000O0O0 )%BLOCK_SIZE )*chr (BLOCK_SIZE -len (OOOOOO0O0O000O0O0 )%BLOCK_SIZE )#line:22
unpad =lambda O0OO0O0OOO0OO0OOO :O0OO0O0OOO0OO0OOO [:-ord (O0OO0O0OOO0OO0OOO [len (O0OO0O0OOO0OO0OOO )-1 :])]#line:23
def guid ():#line:28
    OOOOOOO0OO00O0000 =str (uuid .uuid4 ())#line:29
    O0OOO000O0O00O0OO =str (uuid .uuid4 ())+':'+OOOOOOO0OO00O0000 [0 :8 ]#line:30
    return dict (AdId =str (uuid .uuid4 ()),UniqueId =O0OOO000O0O00O0OO )#line:31
def make_unauth_headers (extra_headers =None )->Dict [str ,str ]:#line:34
    if extra_headers is None :#line:35
        extra_headers ={}#line:36
    return {'User-Agent':USER_AGENT ,'Accept':'*/*','Content-type':'application/json','X-Platform':c2 .platform ,'X-ClientVersion':'////',**extra_headers }#line:43
def make_auth_headers (OO0O000O0O00OOO00 :str ,extra_headers =None )->Dict [str ,str ]:#line:46
    if extra_headers is None :#line:47
        extra_headers ={}#line:48
    return {'User-Agent':USER_AGENT ,'Accept':'*/*','Authorization':OO0O000O0O00OOO00 ,'Content-type':'application/json','X-Language':c2 .lang ,'X-Platform':c2 .platform ,'X-AssetVersion':'////','X-DatabaseVersion':'////','X-ClientVersion':'////',**extra_headers }#line:59
def make_mac_auth (O0O0O0OOOO000OO00 :str ,O000O00000O0O0OOO :str )->str :#line:64
    OO00000OOO00OO0OO =str (int (round (time .time (),0 )))#line:68
    OOO0OOOOOOOOOOO0O =OO00000OOO00OO0OO +':'+c2 .AdId #line:69
    if c2 .client =='global':#line:70
        OOOOO00O00OO00OOO =OO00000OOO00OO0OO +'\n'+OOO0OOOOOOOOOOO0O +'\n'+O0O0O0OOOO000OO00 +'\n'+O000O00000O0O0OOO +'\n'+'ishin-global.aktsk.com'+'\n'+'3001'+'\n\n'#line:71
    else :#line:72
        OOOOO00O00OO00OOO =OO00000OOO00OO0OO +'\n'+OOO0OOOOOOOOOOO0O +'\n'+O0O0O0OOOO000OO00 +'\n'+O000O00000O0O0OOO +'\n'+'ishin-production.aktsk.jp'+'\n'+'3001'+'\n\n'#line:73
    OOOO0O00O0000000O =hmac .new (c2 .secret .encode ('utf-8'),OOOOO00O00OO00OOO .encode ('utf-8'),hashlib .sha256 ).digest ()#line:75
    O000O00OO0O00O0OO =base64 .b64encode (OOOO0O00O0000000O ).decode ()#line:76
    OOO000O0O0O0OO0O0 ='MAC '+'id='+'"'+c2 .access_token +'"'+' nonce='+'"'+OOO0OOOOOOOOOOO0O +'"'+' ts='+'"'+OO00000OOO00OO0OO +'"'+' mac='+'"'+O000O00OO0O00O0OO +'"'#line:77
    return OOO000O0O0O0OO0O0 #line:78
def get_key_and_iv (OO00O0OO0O000OO0O ,O0OO0OOO00OO0O0OO ,klen =32 ,ilen =16 ,msgdgst ='md5',):#line:86
    ""#line:100
    O0O00O000OO0OOOOO =getattr (__import__ ('hashlib',fromlist =[msgdgst ]),msgdgst )#line:107
    OO00O0OO0O000OO0O =OO00O0OO0O000OO0O .encode ('ascii','ignore')#line:108
    try :#line:110
        OOO0OO0O00OOOO0OO =klen +ilen #line:111
        OO0O0OOOOOOO000O0 =O0O00O000OO0OOOOO (OO00O0OO0O000OO0O +O0OO0OOO00OO0O0OO ).digest ()#line:112
        OOOO00O0O0OO0O00O =[OO0O0OOOOOOO000O0 ]#line:113
        while len (OOOO00O0O0OO0O00O )<OOO0OO0O00OOOO0OO :#line:114
            OOOO00O0O0OO0O00O .append (O0O00O000OO0OOOOO (OOOO00O0O0OO0O00O [-1 ]+OO00O0OO0O000OO0O +O0OO0OOO00OO0O0OO ).digest ())#line:115
            OO0O0OOOOOOO000O0 +=OOOO00O0O0OO0O00O [-1 ]#line:116
        OOOOOO0O0000OOO0O =OO0O0OOOOOOO000O0 [:klen ]#line:117
        O0OOOO00O00O0O0OO =OO0O0OOOOOOO000O0 [klen :klen +ilen ]#line:118
        return OOOOOO0O0000OOO0O ,O0OOOO00O00O0O0OO #line:119
    except UnicodeDecodeError :#line:120
        return None ,None #line:121
def encrypt_sign (OO0OO00000OO00OO0 ):#line:125
    OO0OO00000OO00OO0 =pad (OO0OO00000OO00OO0 )#line:126
    OOO00O0OO000O00OO =str .encode (OO0OO00000OO00OO0 )#line:127
    OOO0O000000OO0O0O ='MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzJ9JaHioVi6rr0TAfr6j'#line:128
    O0OOOO00OOOO0OO00 =os .urandom (8 )#line:129
    (O00O00O00O0O00O00 ,O0O00OO0O0O0OOO00 )=get_key_and_iv (OOO0O000000OO0O0O ,O0OOOO00OOOO0OO00 ,klen =32 ,ilen =16 ,msgdgst ='md5')#line:130
    O000OOOO0O000O000 =AES .new (O00O00O00O0O00O00 ,AES .MODE_CBC ,O0O00OO0O0O0OOO00 )#line:131
    O0OOOO0O00O0O00OO =O000OOOO0O000O000 .encrypt (OOO00O0OO000O00OO )#line:132
    O0OOOO0O00O0O00OO =O0OOOO00OOOO0OO00 +O0OOOO0O00O0O00OO #line:133
    return base64 .b64encode (O0OOOO0O00O0O00OO ).decode ()#line:134
def decrypt_sign (O0O0O0000OOO00O0O ):#line:138
    OO0O0OOO000O00O0O =base64 .b64decode (O0O0O0000OOO00O0O )#line:139
    O0OO0O00OOO00O0O0 =base64 .b64encode (OO0O0OOO000O00O0O )#line:140
    OO0O000OO0OOOO000 ='MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzJ9JaHioVi6rr0TAfr6j'#line:141
    OO0O0O0OOO0000000 =OO0O0OOO000O00O0O [0 :8 ]#line:142
    (OOO00000O00OOOO00 ,O0OO000O0OOOOOO00 )=get_key_and_iv (OO0O000OO0OOOO000 ,OO0O0O0OOO0000000 ,klen =32 ,ilen =16 ,msgdgst ='md5')#line:143
    O00O0000OOOO0OO00 =OO0O0OOO000O00O0O [8 :len (OO0O0OOO000O00O0O )]#line:144
    OO000OO00OOO00OOO =AES .new (OOO00000O00OOOO00 ,AES .MODE_CBC ,O0OO000O0OOOOOO00 )#line:145
    O00000OOO0OO0OOOO =unpad (OO000OO00OOO00OOO .decrypt (O00O0000OOOO0OO00 )).decode ('utf8')#line:146
    return json .loads (O00000OOO0OO0OOOO )#line:147
def request (O0O0OO00OOOOO000O :str ,OOO00O0O00OO0O00O :str ,is_mac :bool =True ,**OOOOOO0000O0OOO00 )->requests .Response :#line:153
    if 'headers'not in OOOOOO0000O0OOO00 :#line:154
        OOOOOO0000O0OOO00 ['headers']={}#line:155
    if is_mac :#line:156
        OOOOOO0000O0OOO00 ['headers']={**make_auth_headers (make_mac_auth (O0O0OO00OOOOO000O ,OOO00O0O00OO0O00O )),**OOOOOO0000O0OOO00 ['headers']}#line:157
    return requests .request (O0O0OO00OOOOO000O ,c2 .get_host ()+OOO00O0O00OO0O00O ,**OOOOOO0000O0OOO00 )#line:158
def get (O000O000OOO0000OO :str ,is_mac :bool =True ,**OOOO0OO0000O000O0 )->requests .Response :#line:161
    return request ('GET',O000O000OOO0000OO ,is_mac ,**OOOO0OO0000O000O0 )#line:162
def post (OO0OO0O0000O00OOO :str ,is_mac :bool =True ,**O00OO0OO00O00OOO0 )->requests .Response :#line:165
    return request ('POST',OO0OO0O0000O00OOO ,is_mac ,**O00OO0OO00O00OOO0 )#line:166
def put (OO000O00O00O000OO :str ,is_mac :bool =True ,**OO0O00OOO0OOOOO0O )->requests .Response :#line:169
    return request ('PUT',OO000O00O00O000OO ,is_mac ,**OO0O00OOO0OOOOO0O )#line:170
