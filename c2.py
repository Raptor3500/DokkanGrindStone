AdId =None #line:1
UniqueId =None #line:2
identifier =None #line:3
relooped =False #line:4
access_token =None #line:5
secret =None #line:6
client ='japan'#line:7
lang ='ja'#line:8
platform ='android'#line:9
deck =1 #line:11
allow_stamina_refill =True #line:12
global_url ='https://ishin-global.aktsk.com'#line:14
japan_url ='http://ishin-production.aktsk.jp'#line:15
def set_global ():#line:18
    global client ,lang #line:19
    client ='global'#line:20
    lang ='en'#line:21
def set_japan ():#line:24
    global client ,lang #line:25
    client ='japan'#line:26
    lang ='ja'#line:27
def is_global ():#line:30
    global client ,lang #line:31
    return client =='global'#line:32
def is_japan ():#line:35
    global client ,lang #line:36
    return client =='japan'#line:37
def get_host ():#line:40
    assert is_global ()or is_japan ()#line:41
    if is_global ():#line:42
        return global_url #line:43
    else :#line:44
        return japan_url #line:45
