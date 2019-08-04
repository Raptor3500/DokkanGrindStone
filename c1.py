import base64 #line:1
import errno #line:2
import io #line:3
import json #line:4
import os #line:5
import random #line:6
import datetime #line:7
import re #line:8
import sys #line:9
import time #line:10
import webbrowser #line:11
from os import listdir #line:12
from os .path import isfile ,join #line:13
from random import choice #line:14
from random import randint #line:15
from string import ascii_uppercase #line:16
from typing import Tuple ,Optional ,Union #line:17
from Crypto .Cipher import AES #line:18
from enum import Enum ,IntEnum #line:19
import peewee #line:21
import requests #line:22
from colorama import init ,Fore ,Back ,Style #line:23
from peewee import DoesNotExist #line:24
from tqdm import tqdm #line:25
import c2 #line:27
import d1 #line:28
import d2 #line:29
import p1 #line:30
import h1 #line:31
import l1 #line:32
init (autoreset =True )#line:35
def select_os ():#line:38
	while True :#line:39
		O00OOO00OOOOOOO0O =input ("'a'|Android -- 'i'|iOS: ")#line:40
		if O00OOO00OOOOOOO0O [0 ].lower ()in ['a','i']:#line:41
			if O00OOO00OOOOOOO0O [0 ].lower ()=='a':#line:42
				c2 .platform ='android'#line:43
			elif O00OOO00OOOOOOO0O [0 ].lower ()=='i':#line:44
				c2 .platform ='ios'#line:45
			else :#line:46
				continue #line:47
			break #line:48
		else :#line:49
			print (Fore .RED +'Could not identify correct platform to use.')#line:50
def rankup ():#line:52
	OO0000OO00O000000 =input ('\n\nWhat level are you trying to reach :D?\n')#line:54
	O000OO000O0OO0000 =get_user ()['user']['rank']#line:55
	OO00O0OOO0O0OOOOO =input ('\nWhat is the current multiplier? ')#line:56
	OOOO0O000OOOOO00O =input ('Use Dragonstones? (Y/N): ')#line:57
	if OOOO0O000OOOOO00O .lower ()=='n':#line:58
		c2 .allow_stamina_refill =False #line:59
	elif OOOO0O000OOOOO00O .lower ()=='y':#line:60
		c2 .allow_stamina_refill =True #line:61
		pass #line:62
	else :#line:63
		print ('No valid choice entered. Default Setting: Use Stones.')#line:64
	if int (OO0000OO00O000000 )>999 :#line:66
		print (f"{OO0000OO00O000000} is not a valid rank. Setting to 999.")#line:67
		OO0000OO00O000000 ="999"#line:68
	elif int (OO0000OO00O000000 )<1 :#line:69
		print (f"Rank cannot be smaller than 1. Setting to next rank from current one ({int(O000OO000O0OO0000) + 1}).")#line:70
		OO0000OO00O000000 =str (int (O000OO000O0OO0000 +1 ))#line:71
	O000OOO0000OOOOOO =int (d1 .RankStatuses .get_by_id (OO0000OO00O000000 ).exp_total )-int (d1 .RankStatuses .get_by_id (O000OO000O0OO0000 ).exp_total )#line:72
	OO0O0O0000O00O0O0 =O000OOO0000OOOOOO /(float (27600 )*float (OO00O0OOO0O0OOOOO ))#line:74
	OO0O0O0000O00O0O0 =round (OO0O0O0000O00O0O0 +0.999 )#line:75
	print ('Amount of Exp needed= '+str (O000OOO0000OOOOOO ))#line:76
	print ('Last stage will be done '+str (OO0O0O0000O00O0O0 )+' times.')#line:77
	for O0O00O00OOO0OOOO0 in range (int (OO0O0O0000O00O0O0 )):#line:79
		complete_stage ('27003','3',kagi =None )#line:80
		get_user_info (only_rank =True )#line:81
def list_save_files ():#line:83
	O00000O0000O000OO =input ('\nWhat OS do you want to see your savefiles for? ([A]ndroid / [i]OS)\nYour input: ')#line:84
	O00OOOO0OO00O000O =os .getcwd ()#line:85
	OOO0OO000000OOOO0 =O00OOOO0OO00O000O +'/Saves/android'#line:86
	O0O0O0OOO0O00O00O =O00OOOO0OO00O000O +'/Saves/ios'#line:87
	if O00000O0000O000OO .lower ()=='a':#line:88
		print (Fore .GREEN +'Your Savefiles for Android: ')#line:89
		O000O000O00OOOO0O =[O00OO0O0000OO0O0O for O00OO0O0000OO0O0O in listdir (OOO0OO000000OOOO0 )if isfile (join (OOO0OO000000OOOO0 ,O00OO0O0000OO0O0O ))]#line:90
		print (str (O000O000O00OOOO0O ))#line:91
	elif O00000O0000O000OO .lower ()=='i':#line:92
		print (Fore .GREEN +'Your Savefiles for iOS: ')#line:93
		OO00OOOOO0O000OO0 =[O0OO00OO0O0OOOOOO for O0OO00OO0O0OOOOOO in listdir (O0O0O0OOO0O00O00O )if isfile (join (O0O0O0OOO0O00O00O ,O0OO00OO0O0OOOOOO ))]#line:94
		print (str (OO00OOOOO0O000OO0 ))#line:95
	else :#line:96
		print (Fore .RED +'Command not understood. Please try again')#line:97
def rename_save ():#line:100
	O0O0000OO0O0OOO0O =input ('\nWhat OS do you want to Rename your savefiles for? ([A]ndroid / [i]OS)\nYour input: ')#line:101
	O00OO000OO000O000 =os .getcwd ()#line:102
	O0O00OOOOO00000OO =O00OO000OO000O000 +'/Saves/android/'#line:103
	OOO0O0OOO00OOO00O =O00OO000OO000O000 +'/Saves/ios/'#line:104
	if O0O0000OO0O0OOO0O .lower ()=='a':#line:105
		print (Fore .GREEN +'\nYour Savefiles for Android: ')#line:106
		O0OOO0O00O0000OOO =[OO00OOOO0OOOO0O0O for OO00OOOO0OOOO0O0O in listdir (O0O00OOOOO00000OO )if isfile (join (O0O00OOOOO00000OO ,OO00OOOO0OOOO0O0O ))]#line:107
		print (str (O0OOO0O00O0000OOO ))#line:108
		OO0OOO000OOO0O0O0 =input ('What savefile do you want to rename? [Type exit to leave]: ')#line:109
		if OO0OOO000OOO0O0O0 =='exit':#line:110
			return 1 #line:111
		else :#line:112
			OO00O00OO0O00O000 =O0O00OOOOO00000OO +OO0OOO000OOO0O0O0 #line:113
			O0O000OOOO0000OO0 =input ('What do you want to rename it to?: ')#line:114
			OO00OO000OO0O0000 =O0O00OOOOO00000OO +O0O000OOOO0000OO0 #line:115
			try :#line:116
				os .rename (OO00O00OO0O00O000 ,OO00OO000OO0O0000 )#line:117
				print (Fore .GREEN +'Your file has successfully been renamed from '+OO0OOO000OOO0O0O0 +' to '+O0O000OOOO0000OO0 +'.')#line:118
			except :#line:119
				print (Fore .RED +'Your file could not be renamed. Check if it exists or you entered a valid name.')#line:120
	elif O0O0000OO0O0OOO0O .lower ()=='i':#line:121
		print (Fore .GREEN +'\nYour Savefiles for iOS: ')#line:122
		OOO00OO0OO0OO00OO =[O0O00OO0OO0000OO0 for O0O00OO0OO0000OO0 in listdir (OOO0O0OOO00OOO00O )if isfile (join (OOO0O0OOO00OOO00O ,O0O00OO0OO0000OO0 ))]#line:123
		print (str (OOO00OO0OO0OO00OO ))#line:124
		O0O0OO0OO00000000 =input ('What savefile do you want to rename? [Type exit to leave]: ')#line:125
		if O0O0OO0OO00000000 =='exit':#line:126
			return 1 #line:127
		else :#line:128
			OOO0000O0O0O0OO0O =OOO0O0OOO00OOO00O +O0O0OO0OO00000000 #line:129
			OO0O0OOO00O0000O0 =input ('What do you want to rename it to?: ')#line:130
			O0O0O0OOOO0OOO00O =OOO0O0OOO00OOO00O +OO0O0OOO00O0000O0 #line:131
			try :#line:132
				os .rename (OOO0000O0O0O0OO0O ,O0O0O0OOOO0OOO00O )#line:133
				print (Fore .GREEN +'Your file has successfully been renamed from '+O0O0OO0OO00000000 +' to '+OO0O0OOO00O0000O0 +'.')#line:134
				print (Fore .RED +'Your file could not be renamed. Check if it exists or you entered a valid name.')#line:135
			except :#line:136
				print (Fore .RED +'Your file could not be renamed. Check if it exists or you entered a valid name.')#line:137
	else :#line:138
		print (Fore .RED +'Command not understood. Please try again')#line:139
def complete_stage (OO0OO0OOO00O0O00O ,OO0O0OO00O00000OO ,kagi =None ):#line:142
	if not OO0OO0OOO00O0O00O .isnumeric ():#line:146
		try :#line:147
			OO0OO0OOO00O0O00O =str (d1 .Quests .get (d1 .Quests .name %f"%{OO0OO0OOO00O0O00O}%").id )#line:148
		except DoesNotExist :#line:149
			print (Fore .RED +Style .BRIGHT +"Could not find stage name in databases")#line:150
			return 0 #line:151
	O0OO00000OOOO000O =d1 .Quests .get_by_id (int (OO0OO0OOO00O0O00O )).name #line:155
	try :#line:157
		print (f"Begin stage: {O0OO00000OOOO000O} {OO0OO0OOO00O0O00O} | Difficulty: {OO0O0OO00O00000OO} Deck: {c2.deck}")#line:158
	except :#line:159
		print (Fore .RED +Style .BRIGHT +'Does this quest exist?')#line:160
		return 0 #line:161
	OO0OOO0OO0OOOOO00 =int (round (time .time (),0 ))#line:164
	OO0O0O00OO0000OO0 =get_friend (OO0OO0OOO00O0O00O ,OO0O0OO00O00000OO )#line:167
	if not OO0O0O00OO0000OO0 ['is_cpu']:#line:169
		if kagi is not None :#line:170
			O000OOOOOOOOOO0OO =json .dumps ({'difficulty':OO0O0OO00O00000OO ,'eventkagi_item_id':kagi ,'friend_id':OO0O0O00OO0000OO0 ['id'],'is_playing_script':True ,'selected_team_num':c2 .deck })#line:177
		else :#line:178
			O000OOOOOOOOOO0OO =json .dumps ({'difficulty':OO0O0OO00O00000OO ,'friend_id':OO0O0O00OO0000OO0 ['id'],'is_playing_script':True ,'selected_team_num':c2 .deck })#line:184
	else :#line:185
		if kagi is not None :#line:186
			O000OOOOOOOOOO0OO =json .dumps ({'difficulty':OO0O0OO00O00000OO ,'eventkagi_item_id':kagi ,'cpu_friend_id':OO0O0O00OO0000OO0 ['id'],'is_playing_script':True ,'selected_team_num':c2 .deck })#line:193
		else :#line:194
			O000OOOOOOOOOO0OO =json .dumps ({'difficulty':OO0O0OO00O00000OO ,'cpu_friend_id':OO0O0O00OO0000OO0 ['id'],'is_playing_script':True ,'selected_team_num':c2 .deck })#line:200
	OO00000O0O0OOO000 =p1 .encrypt_sign (O000OOOOOOOOOO0OO )#line:202
	OO00O00O0O000O0OO =json .dumps ({'sign':OO00000O0O0OOO000 })#line:208
	OO000OOOOO0000OO0 =f'/quests/{OO0OO0OOO00O0O00O}/sugoroku_maps/start'#line:209
	OOO0O0O0O0O000O0O =p1 .post (OO000OOOOO0000OO0 ,data =OO00O00O0O000O0OO )#line:210
	if 'sign'in OOO0O0O0O0O000O0O .json ():#line:215
		O000OOOOOO0000OOO =p1 .decrypt_sign (OOO0O0O0O0O000O0O .json ()['sign'])#line:216
	elif 'error'in OOO0O0O0O0O000O0O .json ():#line:217
		print (Fore .RED +Style .BRIGHT +str (OOO0O0O0O0O000O0O .json ()['error']))#line:218
		if OOO0O0O0O0O000O0O .json ()['error']['code']=='act_is_not_enough':#line:220
			if c2 .allow_stamina_refill :#line:222
				refill_stamina ()#line:223
				OOO0O0O0O0O000O0O =p1 .post (OO000OOOOO0000OO0 ,data =OO00O00O0O000O0OO )#line:224
			else :#line:225
				print (Fore .RED +Style .BRIGHT +'Stamina refill not allowed. Press Ctrl+C to cancel current Rankup.')#line:226
				return 0 #line:227
		elif OOO0O0O0O0O000O0O .json ()['error']['code']=='active_record/record_not_found':#line:228
			return 0 #line:229
		elif OOO0O0O0O0O000O0O .json ()['error']['code']=='invalid_area_conditions_potential_releasable':#line:230
			print (Fore .RED +Style .BRIGHT +'You do not meet the coniditions to complete potential events')#line:231
			return 0 #line:232
		else :#line:233
			print (Fore .RED +Style .BRIGHT +str (OOO0O0O0O0O000O0O .json ()['error']))#line:234
			return 0 #line:235
	else :#line:236
		print (Fore .RED +Style .BRIGHT +str (OOO0O0O0O0O000O0O .json ()))#line:237
		return 0 #line:238
	if 'sign'in OOO0O0O0O0O000O0O .json ():#line:239
		O000OOOOOO0000OOO =p1 .decrypt_sign (OOO0O0O0O0O000O0O .json ()['sign'])#line:240
	else :#line:241
		print (Fore .RED +Style .BRIGHT +'Unable to decrypt game packet')#line:242
		return 0 #line:243
	O0O00000O0O000O0O =[]#line:245
	for OOOO0000OO00O00OO in O000OOOOOO0000OOO ['sugoroku']['events']:#line:246
		O0O00000O0O000O0O .append (OOOO0000OO00O00OO )#line:247
	OO0O0OO0O0OOOOOO0 =int (round (time .time (),0 )+2000 )#line:249
	OOOOOO0OOO0OO0O00 =OO0O0OO0O0OOOOOO0 -randint (6200000 ,8200000 )#line:250
	O000O0O0OO0OO0000 =randint (500000 ,1500000 )#line:251
	if str (OO0OO0OOO00O0O00O )[0 :3 ]=='711':#line:254
		O000O0O0OO0OO0000 =randint (100000000 ,101000000 )#line:255
	O000OOOOOOOOOO0OO ={'actual_steps':O0O00000O0O000O0O ,'difficulty':OO0O0OO00O00000OO ,'elapsed_time':OO0O0OO0O0OOOOOO0 -OOOOOO0OOO0OO0O00 ,'energy_ball_counts_in_boss_battle':[4 ,6 ,0 ,6 ,4 ,3 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,],'has_player_been_taken_damage':False ,'is_cheat_user':False ,'is_cleared':True ,'is_defeated_boss':True ,'is_player_special_attack_only':True ,'max_damage_to_boss':O000O0O0OO0OO0000 ,'min_turn_in_boss_battle':0 ,'quest_finished_at_ms':OO0O0OO0O0OOOOOO0 ,'quest_started_at_ms':OOOOOO0OOO0OO0O00 ,'steps':O0O00000O0O000O0O ,'token':O000OOOOOO0000OOO ['token'],}#line:273
	OO00000O0O0OOO000 =p1 .encrypt_sign (json .dumps (O000OOOOOOOOOO0OO ))#line:275
	OO00O00O0O000O0OO =json .dumps ({'sign':OO00000O0O0OOO000 })#line:281
	OO000OOOOO0000OO0 =f'/quests/{OO0OO0OOO00O0O00O}/sugoroku_maps/finish'#line:282
	OOO0O0O0O0O000O0O =p1 .post (OO000OOOOO0000OO0 ,data =OO00O00O0O000O0OO )#line:283
	O000OOOOOO0000OOO =p1 .decrypt_sign (OOO0O0O0O0O000O0O .json ()['sign'])#line:284
	if 'items'in O000OOOOOO0000OOO :#line:287
		O000O00O00O0O000O =[]#line:288
		O0OO0OO000OOO0OO0 =[]#line:289
		O0000O00O0O000OO0 =[]#line:290
		O000O0O0OOO0O000O =[]#line:291
		OOO0OOO0O000O00OO =[]#line:292
		O0O00O00000O000OO =[]#line:293
		OO000O000OO0OOOO0 =[]#line:294
		OOO000O00OO0OO00O =0 #line:295
		O000OOO00OOOO0O0O =set ()#line:296
		O00OO00O000O00OOO =set ()#line:297
		O000OO0OO0OO0OO0O =set ()#line:298
		O0O00O0OO0O000O00 =set ()#line:299
		O0O0O0O00OOOO00OO =set ()#line:300
		O0OOO0O0OO0OO0O0O =set ()#line:301
		OO0OO0OO0O00O0OO0 =set ()#line:302
		print ('Items:')#line:303
		print ('-------------------------')#line:304
		if 'quest_clear_rewards'in O000OOOOOO0000OOO :#line:305
			for OOOO0000OO00O00OO in O000OOOOOO0000OOO ['quest_clear_rewards']:#line:306
				if OOOO0000OO00O00OO ['item_type']=='Point::Stone':#line:307
					OOO000O00OO0OO00O +=OOOO0000OO00O00OO ['amount']#line:308
		for OOOO0000OO00O00OO in O000OOOOOO0000OOO ['items']:#line:309
			if OOOO0000OO00O00OO ['item_type']=='SupportItem':#line:310
				for O00O00OO0OO0O0O0O in range (OOOO0000OO00O00OO ['quantity']):#line:314
					O000O00O00O0O000O .append (OOOO0000OO00O00OO ['item_id'])#line:315
				O000OOO00OOOO0O0O .add (OOOO0000OO00O00OO ['item_id'])#line:316
			elif OOOO0000OO00O00OO ['item_type']=='PotentialItem':#line:317
				for O00O00OO0OO0O0O0O in range (OOOO0000OO00O00OO ['quantity']):#line:321
					O000O0O0OOO0O000O .append (OOOO0000OO00O00OO ['item_id'])#line:322
				O0O00O0OO0O000O00 .add (OOOO0000OO00O00OO ['item_id'])#line:323
			elif OOOO0000OO00O00OO ['item_type']=='TrainingItem':#line:324
				for O00O00OO0OO0O0O0O in range (OOOO0000OO00O00OO ['quantity']):#line:328
					O0000O00O0O000OO0 .append (OOOO0000OO00O00OO ['item_id'])#line:329
				O000OO0OO0OO0OO0O .add (OOOO0000OO00O00OO ['item_id'])#line:330
			elif OOOO0000OO00O00OO ['item_type']=='AwakeningItem':#line:331
				for O00O00OO0OO0O0O0O in range (OOOO0000OO00O00OO ['quantity']):#line:335
					O0OO0OO000OOO0OO0 .append (OOOO0000OO00O00OO ['item_id'])#line:336
				O00OO00O000O00OOO .add (OOOO0000OO00O00OO ['item_id'])#line:337
			elif OOOO0000OO00O00OO ['item_type']=='TreasureItem':#line:338
				for O00O00OO0OO0O0O0O in range (OOOO0000OO00O00OO ['quantity']):#line:342
					OOO0OOO0O000O00OO .append (OOOO0000OO00O00OO ['item_id'])#line:343
				O0O0O0O00OOOO00OO .add (OOOO0000OO00O00OO ['item_id'])#line:344
			elif OOOO0000OO00O00OO ['item_type']=='Card':#line:345
				O0O00O00000O000OO .append (OOOO0000OO00O00OO ['item_id'])#line:349
				O0OOO0O0OO0OO0O0O .add (OOOO0000OO00O00OO ['item_id'])#line:350
			elif OOOO0000OO00O00OO ['item_type']=='Point::Stone':#line:351
				OOO000O00OO0OO00O +=1 #line:356
			elif OOOO0000OO00O00OO ['item_type']=='TrainingField':#line:357
				for O00O00OO0OO0O0O0O in range (OOOO0000OO00O00OO ['quantity']):#line:361
					OO000O000OO0OOOO0 .append (OOOO0000OO00O00OO ['item_id'])#line:362
				OO0OO0OO0O00O0OO0 .add (OOOO0000OO00O00OO ['item_id'])#line:363
			else :#line:364
				print (OOOO0000OO00O00OO ['item_type'])#line:365
		for OOOO0000OO00O00OO in O000OOO00OOOO0O0O :#line:368
			print (Fore .CYAN +Style .BRIGHT +d1 .SupportItems .get_by_id (OOOO0000OO00O00OO ).name +' x'+str (O000O00O00O0O000O .count (OOOO0000OO00O00OO )))#line:369
		for OOOO0000OO00O00OO in O00OO00O000O00OOO :#line:371
			print (Fore .MAGENTA +Style .BRIGHT +d1 .AwakeningItems .get_by_id (OOOO0000OO00O00OO ).name +' x'+str (O0OO0OO000OOO0OO0 .count (OOOO0000OO00O00OO )))#line:372
		for OOOO0000OO00O00OO in O000OO0OO0OO0OO0O :#line:374
			print (Fore .RED +Style .BRIGHT +d1 .TrainingItems .get_by_id (OOOO0000OO00O00OO ).name +' x'+str (O0000O00O0O000OO0 .count (OOOO0000OO00O00OO )))#line:375
		for OOOO0000OO00O00OO in O0O00O0OO0O000O00 :#line:377
			print (d1 .PotentialItems .get_by_id (OOOO0000OO00O00OO ).name +' x'+str (O000O0O0OOO0O000O .count (OOOO0000OO00O00OO )))#line:378
		for OOOO0000OO00O00OO in O0O0O0O00OOOO00OO :#line:380
			print (Fore .GREEN +Style .BRIGHT +d1 .TreasureItems .get_by_id (OOOO0000OO00O00OO ).name +' x'+str (OOO0OOO0O000O00OO .count (OOOO0000OO00O00OO )))#line:381
		for OOOO0000OO00O00OO in OO0OO0OO0O00O0OO0 :#line:383
			print (d1 .TrainingFields .get_by_id (OOOO0000OO00O00OO ).name +' x'+str (OO000O000OO0OOOO0 .count (OOOO0000OO00O00OO )))#line:384
		for OOOO0000OO00O00OO in O0OOO0O0OO0OO0O0O :#line:386
			print (d1 .Cards .get_by_id (OOOO0000OO00O00OO ).name +' x'+str (O0O00O00000O000OO .count (OOOO0000OO00O00OO )))#line:387
		print (Fore .YELLOW +Style .BRIGHT +'Stones x'+str (OOO000O00OO0OO00O ))#line:389
	OOOO0O0O0O00O0000 ='{:,}'.format (O000OOOOOO0000OOO ['zeni'])#line:391
	print ('Zeni: '+OOOO0O0O0O00O0000 )#line:392
	if 'gasha_point'in O000OOOOOO0000OOO :#line:393
		print ('Friend Points: '+str (O000OOOOOO0000OOO ['gasha_point']))#line:394
	print ('--------------------------')#line:396
	get_user_info (only_stone =True )#line:397
	get_user_info (only_gasha =True )#line:398
	O00O00OO0OO0O0O0O =0 #line:402
	O000OOO0OO00000O0 =[]#line:403
	if 'user_items'in O000OOOOOO0000OOO :#line:404
		if 'cards'in O000OOOOOO0000OOO ['user_items']:#line:405
			for OOOO0000OO00O00OO in O000OOOOOO0000OOO ['user_items']['cards']:#line:406
				if d1 .Cards .get_by_id (OOOO0000OO00O00OO ['card_id']).rarity ==0 :#line:407
					O000OOO0OO00000O0 .append (OOOO0000OO00O00OO ['id'])#line:408
	if len (O000OOO0OO00000O0 )>0 :#line:410
		sell_cards (O000OOO0OO00000O0 )#line:411
	O000OOOO0OO000OOO =int (round (time .time (),0 ))#line:415
	O00O0OO000OO0O0O0 =O000OOOO0OO000OOO -OO0OOO0OO0OOOOO00 #line:416
	print (Fore .GREEN +Style .BRIGHT +'Completed stage: '+str (OO0OO0OOO00O0O00O )+' in '+str (O00O0OO000OO0O0O0 )+' seconds')#line:420
	print ('')#line:421
def get_friend (O00000OOO0OOO0000 ,O0OOO0O00OO0O0OOO ):#line:424
	O0OO00O0O00O00O0O =f'/quests/{O00000OOO0OOO0000}/supporters'#line:428
	OO0O000O0O000O000 =p1 .get (O0OO00O0O00O00O0O )#line:429
	if 'cpu_supporters'in OO0O000O0O000O000 .json ():#line:432
		if int (O0OOO0O00OO0O0OOO )==5 :#line:433
			if 'super_hard3'in OO0O000O0O000O000 .json ()['cpu_supporters']:#line:434
				if len (OO0O000O0O000O000 .json ()['cpu_supporters']['super_hard3']['cpu_friends'])>0 :#line:435
					return {'is_cpu':True ,'id':OO0O000O0O000O000 .json ()['cpu_supporters']['super_hard3']['cpu_friends'][0 ]['id']}#line:439
		if int (O0OOO0O00OO0O0OOO )==4 :#line:440
			if 'super_hard2'in OO0O000O0O000O000 .json ()['cpu_supporters']:#line:441
				if len (OO0O000O0O000O000 .json ()['cpu_supporters']['super_hard2']['cpu_friends'])>0 :#line:442
					return {'is_cpu':True ,'id':OO0O000O0O000O000 .json ()['cpu_supporters']['super_hard2']['cpu_friends'][0 ]['id']}#line:446
		if int (O0OOO0O00OO0O0OOO )==3 :#line:447
			if 'super_hard1'in OO0O000O0O000O000 .json ()['cpu_supporters']:#line:448
				if len (OO0O000O0O000O000 .json ()['cpu_supporters']['super_hard1']['cpu_friends'])>0 :#line:449
					return {'is_cpu':True ,'id':OO0O000O0O000O000 .json ()['cpu_supporters']['super_hard1']['cpu_friends'][0 ]['id']}#line:453
		if int (O0OOO0O00OO0O0OOO )==2 :#line:454
			if 'very_hard'in OO0O000O0O000O000 .json ()['cpu_supporters']:#line:455
				if len (OO0O000O0O000O000 .json ()['cpu_supporters']['very_hard']['cpu_friends'])>0 :#line:456
					return {'is_cpu':True ,'id':OO0O000O0O000O000 .json ()['cpu_supporters']['very_hard']['cpu_friends'][0 ]['id']}#line:460
		if int (O0OOO0O00OO0O0OOO )==1 :#line:461
			if 'hard'in OO0O000O0O000O000 .json ()['cpu_supporters']:#line:462
				if len (OO0O000O0O000O000 .json ()['cpu_supporters']['hard']['cpu_friends'])>0 :#line:463
					return {'is_cpu':True ,'id':OO0O000O0O000O000 .json ()['cpu_supporters']['hard']['cpu_friends'][0 ]['id']}#line:467
		if int (O0OOO0O00OO0O0OOO )==0 :#line:468
			if 'normal'in OO0O000O0O000O000 .json ()['cpu_supporters']:#line:469
				if len (OO0O000O0O000O000 .json ()['cpu_supporters']['normal']['cpu_friends'])>0 :#line:470
					return {'is_cpu':True ,'id':OO0O000O0O000O000 .json ()['cpu_supporters']['normal']['cpu_friends'][0 ]['id']}#line:474
	return {'is_cpu':False ,'id':OO0O000O0O000O000 .json ()['supporters'][0 ]['id']}#line:479
def refill_stamina ():#line:482
	O00000OO0O0O000O0 =get_user ()['user']['stone']#line:485
	if O00000OO0O0O000O0 <1 :#line:486
		print (Fore .RED +Style .BRIGHT +'You have no stones left..')#line:487
		return #line:488
	p1 .put ('/user/recover_act_with_stone')#line:490
	print (Fore .GREEN +Style .BRIGHT +'Stamina successfully restored.')#line:491
def get_user ():#line:494
	O00000OOOOOOOO0OO =p1 .get ('/user')#line:495
	return O00000OOOOOOOO0OO .json ()#line:496
def sell_cards (O0000000OOO00OOO0 ):#line:499
	O0OO0O00OOO00OO0O ='/cards/sell'#line:502
	OO000OOO0000O0000 =[]#line:504
	O00OOOO0OOO00OOO0 =0 #line:505
	for OO00O0OO0OOO00OOO in O0000000OOO00OOO0 :#line:506
		O00OOOO0OOO00OOO0 +=1 #line:507
		OO000OOO0000O0000 .append (OO00O0OO0OOO00OOO )#line:508
		if O00OOOO0OOO00OOO0 ==99 :#line:509
			OO00O000OOOO0OOO0 ={'card_ids':OO000OOO0000O0000 }#line:512
			OOO0O0OOOOO00OOO0 =p1 .post (O0OO0O00OOO00OO0O ,data =json .dumps (OO00O000OOOO0OOO0 ))#line:513
			print ('Sold Cards x'+str (len (OO000OOO0000O0000 )))#line:514
			if 'error'in OOO0O0OOOOO00OOO0 .json ():#line:515
				print (OOO0O0OOOOO00OOO0 .json ()['error'])#line:516
				return 0 #line:517
			O00OOOO0OOO00OOO0 =0 #line:518
			OO000OOO0000O0000 [:]=[]#line:519
	if O00OOOO0OOO00OOO0 !=0 :#line:520
		OO00O000OOOO0OOO0 ={'card_ids':OO000OOO0000O0000 }#line:523
		OOO0O0OOOOO00OOO0 =p1 .post (O0OO0O00OOO00OO0O ,data =json .dumps (OO00O000OOOO0OOO0 ))#line:524
		print ('Sold Cards x'+str (len (OO000OOO0000O0000 )))#line:525
def signup (platform =None ):#line:528
	if platform is None :#line:532
		set_platform ()#line:533
	else :#line:534
		c2 .platform =platform #line:535
	O00O000O0O0OO0OO0 =p1 .guid ()#line:538
	c2 .AdId =O00O000O0O0OO0OO0 ['AdId']#line:539
	c2 .UniqueId =O00O000O0O0OO0OO0 ['UniqueId']#line:540
	OO000OOO0OO00O0O0 ={'ad_id':c2 .AdId ,'country':'AU','currency':'AUD','device':'samsung','device_model':'SM-E7000','os_version':'7.0','platform':c2 .platform ,'unique_id':c2 .UniqueId ,}#line:550
	OOO00O00O00OOOOO0 =json .dumps ({'user_account':OO000OOO0OO00O0O0 })#line:554
	while True :#line:556
		OO000O0000OO0O00O =p1 .post ('/auth/sign_up',is_mac =False ,data =OOO00O00O00OOOOO0 ,headers =p1 .make_unauth_headers ())#line:557
		if 'captcha_url'not in OO000O0000OO0O00O .json ():#line:559
			print (Fore .RED +Style .BRIGHT +'Captcha could not be loaded..')#line:560
			return None #line:561
		O00O0OO0O000OO0O0 =OO000O0000OO0O00O .json ()['captcha_url']#line:563
		webbrowser .open (O00O0OO0O000OO0O0 ,new =2 )#line:564
		OOO0O00OO0OOOO0O0 =OO000O0000OO0O00O .json ()['captcha_session_key']#line:565
		print ('Opening Captcha. Press ENTER key once solved.')#line:566
		input ()#line:567
		O000O000OO0OOO0OO ={'captcha_session_key':OOO0O00OO0OOOO0O0 ,'user_account':OO000OOO0OO00O0O0 }#line:575
		OO000O0000OO0O00O =p1 .post ('/auth/sign_up',is_mac =False ,data =json .dumps (O000O000OO0OOO0OO ),headers =p1 .make_unauth_headers ())#line:577
		OOOO00O0OO00OOOOO =OO000O0000OO0O00O .json ()#line:578
		if 'captcha_result'not in OOOO00O0OO00OOOOO or OOOO00O0OO00OOOOO ['captcha_result']!='failed':#line:579
			return base64 .b64decode (OOOO00O0OO00OOOOO ['identifier']).decode ('utf-8')#line:580
def signin (O0OOO0OOOO0O0000O :str ,OOO0OO000O000O00O :str ,O0OO0O000000OOO00 :str )->Optional [Tuple [str ,str ]]:#line:583
	OO0O000OOO0O0O00O =O0OOO0OOOO0O0000O .split (':')#line:589
	OOO0O0OO00OO0OO00 =OO0O000OOO0O0O00O [1 ]+':'+OO0O000OOO0O0O00O [0 ]#line:590
	O00OO00OOOO0OOO0O ='Basic '+base64 .b64encode (OOO0O0OO00OO0OO00 .encode ('utf-8')).decode ('utf-8')#line:591
	OO00O0OOO0OO00O00 =json .dumps ({'ad_id':O0OO0O000000OOO00 ,'unique_id':OOO0OO000O000O00O })#line:595
	O0000O000OOOOO00O =p1 .make_auth_headers (O00OO00OOOO0OOO0O ,{'X-UserCountry':'AU','X-UserCurrency':'AUD',})#line:601
	O0O0000O0OO0O0O00 =p1 .post ('/auth/sign_in',is_mac =False ,data =OO00O0OOO0OO00O00 ,headers =O0000O000OOOOO00O )#line:603
	OO000OO0OOO00O00O =O0O0000O0OO0O0O00 .json ()#line:604
	if 'captcha_url'in O0O0000O0OO0O0O00 .json ():#line:606
		print (O0O0000O0OO0O0O00 .json ())#line:607
		O0OOOO0O0O00OOO00 =O0O0000O0OO0O0O00 .json ()['captcha_url']#line:608
		webbrowser .open (O0OOOO0O0O00OOO00 ,new =2 )#line:609
		print ('Opening Captcha. Press ENTER key once solved')#line:610
		input ()#line:611
		O0O0000O0OO0O0O00 =requests .post (O0OOOO0O0O00OOO00 ,data =OO00O0OOO0OO00O00 ,headers =O0000O000OOOOO00O )#line:612
		OO000OO0OOO00O00O =O0O0000O0OO0O0O00 .json ()#line:613
	if 'captcha_result'in OO000OO0OOO00O00O and OO000OO0OOO00O00O ['captcha_result']=='failed':#line:615
		return signin (O0OOO0OOOO0O0000O ,OOO0OO000O000O00O ,O0OO0O000000OOO00 )#line:616
	O000000O0O0OO0O00 =OO000OO0OOO00O00O ['access_token'],OO000OO0OOO00O00O ['secret']#line:618
	print (Fore .RED +Style .BRIGHT +'SIGN IN COMPLETE'+Style .RESET_ALL )#line:619
	return O000000O0O0OO0O00 #line:620
def get_transfer_code ():#line:623
	get_user_info (only_id =True )#line:625
	OOOO00O00O0000O0O ={'eternal':1 }#line:628
	OOOO00OOOO000O00O =p1 .post ('/auth/link_codes',data =json .dumps (OOOO00O00O0000O0O ))#line:629
	print ('Transfer Code: ')#line:630
	try :#line:631
		print (OOOO00OOOO000O00O .json ()['link_code'])#line:632
		return {'transfer_code':OOOO00OOOO000O00O .json ()['link_code']}#line:635
	except :#line:636
		return None #line:637
def tutorial ():#line:640
	print (Fore .CYAN +Style .BRIGHT +'Tutorial Progress: 1/8')#line:643
	O0000OOO00OOOO000 =p1 .put ('/tutorial/finish')#line:644
	p1 .post ('/tutorial/gasha')#line:647
	print (Fore .CYAN +Style .BRIGHT +'Tutorial Progress: 2/8')#line:648
	OOOO000O00OO00OO0 ={'progress':'999'}#line:653
	O0000OOO00OOOO000 =p1 .put ('/tutorial',data =json .dumps (OOOO000O00OO00OO0 ))#line:654
	print (Fore .CYAN +Style .BRIGHT +'Tutorial Progress: 3/8')#line:655
	OOO00OO0OO00O000O ={'user':{'name':''}}#line:662
	O0000OOO00OOOO000 =p1 .put ('/user',data =json .dumps (OOO00OO0OO00O000O ))#line:664
	print (Fore .CYAN +Style .BRIGHT +'Tutorial Progress: 4/8')#line:665
	O0000OOO00OOOO000 =p1 .post ('/missions/put_forward')#line:668
	print (Fore .CYAN +Style .BRIGHT +'Tutorial Progress: 5/8')#line:669
	O0000OOO00OOOO000 =p1 .put ('/apologies/accept')#line:672
	O0OO0OOO00OO0OOOO ={'user':{'is_ondemand':False }}#line:679
	O0000OOO00OOOO000 =p1 .put ('/tutorial/finish',data =json .dumps (O0OO0OOO00OO0OOOO ))#line:680
	print (Fore .CYAN +Style .BRIGHT +'Tutorial Progress: 6/8')#line:681
	print (Fore .CYAN +Style .BRIGHT +'Tutorial Progress: 7/8')#line:684
	print (Fore .CYAN +Style .BRIGHT +'Tutorial Progress: 8/8')#line:685
	print (Fore .RED +Style .BRIGHT +'TUTORIAL COMPLETE')#line:686
def download_file (OOOO0000O00O0O0O0 :str ,O00O00OOOO00OO0O0 :str ,O0OO0O0O00O00O000 :str ):#line:689
	OOO0OO0OO000O00O0 =requests .get (OOOO0000O00O0O0O0 ,allow_redirects =True ,stream =True )#line:690
	OOO00OO00O000O0OO =int (OOO0OO0OO000O00O0 .headers .get ('content-length',0 ))#line:691
	O0OO0O0O000OOOOOO =OOO00OO00O000O0OO !=0 #line:692
	with open (O00O00OOOO00OO0O0 ,'wb')as O0O0O0000OO0O00OO :#line:693
		OOO00O0O00000O000 =tqdm (desc =O0OO0O0O00O00O000 ,unit ='B',total =OOO00OO00O000O0OO ,unit_scale =True )#line:694
		OOOO0O0OO0OO00O00 =0 #line:695
		O00O0O00O000O000O =1024 #line:696
		for O0OOOOO0O0O00O0OO in OOO0OO0OO000O00O0 .iter_content (chunk_size =O00O0O00O000O000O ):#line:697
			if O0OOOOO0O0O00O0OO :#line:698
				OO0O0OOOO0O0O00OO =len (O0OOOOO0O0O00O0OO )#line:699
				OOOO0O0OO0OO00O00 +=OO0O0OOOO0O0O00OO #line:700
				if not O0OO0O0O000OOOOOO :#line:701
					OOO00O0O00000O000 .total =1 <<(OOOO0O0OO0OO00O00 -1 ).bit_length ()#line:702
				OOO00O0O00000O000 .update (OO0O0OOOO0O0O00OO )#line:703
				O0O0O0000OO0O00OO .write (O0OOOOO0O0O00O0OO )#line:704
				O0O0O0000OO0O00OO .flush ()#line:705
		OOO00O0O00000O000 .total =OOOO0O0OO0OO00O00 #line:706
		OOO00O0O00000O000 .update (0 )#line:707
		OOO00O0O00000O000 .close ()#line:708
def db_download ():#line:711
	OO0OO0OO00OO0O00O =False #line:712
	OO0OOOO0OOOO000O0 =False #line:713
	OO0000O0OO0000OOO =0 #line:714
	OO0O0O0O0OO00OO0O =0 #line:715
	if os .path .isfile ('db.txt'):#line:718
		with open (os .path .join ('db.txt'),'r')as OOOOO0OO0OO0O0OO0 :#line:719
			OO0O000O0O0O0O00O =OOOOO0OO0OO0O0OO0 .readline ().rstrip ()#line:720
			OO0OO0OO00O0OO00O =OOOOO0OO0OO0O0OO0 .readline ().rstrip ()#line:721
	else :#line:722
		print ('File: db.txt not found. Creating...')#line:723
		with open (os .path .join ('db.txt'),'w')as OOOOO0OO0OO0O0OO0 :#line:724
			OOOOO0OO0OO0O0OO0 .write ('0\n')#line:725
			OOOOO0OO0OO0O0OO0 .write ('0\n')#line:726
	with open (os .path .join ('db.txt'),'r')as OOOOO0OO0OO0O0OO0 :#line:728
		OO0O000O0O0O0O00O =OOOOO0OO0OO0O0OO0 .readline ().rstrip ()#line:729
		OO0OO0OO00O0OO00O =OOOOO0OO0OO0O0OO0 .readline ().rstrip ()#line:730
	OO00OO0OO0O0O0OOO =c2 .client #line:732
	c2 .set_global ()#line:735
	if not load_account ('android','botdbdownloadglb'):#line:736
		c2 .identifier =signup ('android')#line:737
		c2 .access_token ,c2 .secret =signin (c2 .identifier ,c2 .UniqueId ,c2 .AdId )#line:738
		save_account ('botdbdownloadglb')#line:739
	OO0O00O00O000000O =p1 .get ('/client_assets/database',allow_redirects =True )#line:740
	if OO0O000O0O0O0O00O !=str (OO0O00O00O000000O .json ()['version']):#line:741
		OO0OOOO0OOOO000O0 =True #line:742
		OO0000O0OO0000OOO =OO0O00O00O000000O .json ()['version']#line:743
		print (Fore .RED +Style .BRIGHT +'Downloading Global d1...')#line:745
		O0000O0OO0OO00OOO =OO0O00O00O000000O .json ()['url']#line:746
		download_file (O0000O0OO0OO00OOO ,'dataenc_glb.db',"Global d1.db")#line:747
	c2 .set_japan ()#line:750
	if not load_account ('android','botdbdownloadjp'):#line:751
		c2 .identifier =signup ('android')#line:752
		c2 .access_token ,c2 .secret =signin (c2 .identifier ,c2 .UniqueId ,c2 .AdId )#line:753
		save_account ('botdbdownloadjp')#line:754
	OO0O00O00O000000O =p1 .get ('/client_assets/database',allow_redirects =True )#line:755
	if OO0OO0OO00O0OO00O !=str (OO0O00O00O000000O .json ()['version']):#line:756
		OO0OO0OO00OO0O00O =True #line:757
		OO0O0O0O0OO00OO0O =OO0O00O00O000000O .json ()['version']#line:758
		print (Fore .RED +Style .BRIGHT +'Downloading Japan d1...')#line:760
		O0000O0OO0OO00OOO =OO0O00O00O000000O .json ()['url']#line:761
		download_file (O0000O0OO0OO00OOO ,'dataenc_jp.db',"Japan d1.db")#line:762
	c2 .client =OO00OO0OO0O0O0OOO #line:765
	print (Fore .RED +Style .BRIGHT +'Decrypting Latest Databases.. This can take a few minutes..')#line:767
	if OO0OOOO0OOOO000O0 :#line:770
		print ('Decrypting Global Database')#line:771
		d2 .main ()#line:772
		with open ('db.txt','r')as OO000000OOO00OO0O :#line:773
			O0OOO0O0OOOOO0OOO =OO000000OOO00OO0O .readlines ()#line:774
			O0OOO0O0OOOOO0OOO [0 ]=str (OO0000O0OO0000OOO )+'\n'#line:775
		with open ('db.txt','w')as OO000000OOO00OO0O :#line:776
			OO000000OOO00OO0O .writelines (O0OOO0O0OOOOO0OOO )#line:777
	if OO0OO0OO00OO0O00O :#line:779
		print ('Decrypting JP Database')#line:780
		d2 .main (p ='2db857e837e0a81706e86ea66e2d1633')#line:781
		with open ('db.txt','r')as OO000000OOO00OO0O :#line:782
			O0OOO0O0OOOOO0OOO =OO000000OOO00OO0O .readlines ()#line:783
			O0OOO0O0OOOOO0OOO [1 ]=str (OO0O0O0O0OO00OO0O )+'\n'#line:784
		with open ('db.txt','w')as OO000000OOO00OO0O :#line:785
			OO000000OOO00OO0O .writelines (O0OOO0O0OOOOO0OOO )#line:786
	print (Fore .GREEN +Style .BRIGHT +'Database update complete.')#line:788
def accept_missions ():#line:791
	O0O0O00O0O0O0O000 =p1 .get ('/missions')#line:794
	OO00OOOO0OOOOO0OO =O0O0O00O0O0O0O000 .json ()#line:795
	OOO00O0OOOOO0O000 =[]#line:796
	for O00O00O0O00O0O0O0 in OO00OOOO0OOOOO0OO ['missions']:#line:797
		if O00O00O0O00O0O0O0 ['completed_at']is not None and O00O00O0O00O0O0O0 ['accepted_reward_at']is None :#line:798
			OOO00O0OOOOO0O000 .append (O00O00O0O00O0O0O0 ['id'])#line:799
	OOOO0000000000OOO ={"mission_ids":OOO00O0OOOOO0O000 }#line:803
	O0O0O00O0O0O0O000 =p1 .post ('/missions/accept',data =json .dumps (OOOO0000000000OOO ))#line:804
	if 'error'not in O0O0O00O0O0O0O000 .json ():#line:805
		print (Fore .GREEN +Style .BRIGHT +'Accepted missions')#line:806
def accept_gifts ():#line:809
	OO0O0OO000000O00O =p1 .get ('/gifts')#line:812
	O0OO0OO0O00O00O0O =[]#line:814
	for OO0O0O0000O0OOO00 in OO0O0OO000000O00O .json ()['gifts']:#line:815
		O0OO0OO0O00O00O0O .append (OO0O0O0000O0OOO00 ['id'])#line:816
	if len (O0OO0OO0O00O00O0O )==0 :#line:819
		print ('No gifts to accept..')#line:820
		return 0 #line:821
	OO0OOO000OO0O00O0 =[O0OO0OO0O00O00O0O [OO00O0O00O0OO0OOO :OO00O0O00O0OO0OOO +25 ]for OO00O0O00O0OO0OOO in range (0 ,len (O0OO0OO0O00O00O0O ),25 )]#line:822
	for OO0OO0000000000OO in OO0OOO000OO0O00O0 :#line:823
		OO0OO0000000000OO ={'gift_ids':OO0OO0000000000OO }#line:826
		OO0O0OO000000O00O =p1 .post ('/gifts/accept',data =json .dumps (OO0OO0000000000OO ))#line:827
		if 'error'not in OO0O0OO000000O00O .json ():#line:828
			print (Fore .GREEN +Style .BRIGHT +'Gifts Accepted..')#line:829
		else :#line:830
			print (OO0O0OO000000O00O .json ())#line:831
def get_kagi_id (OOOO0OOOO0O0OOO0O ):#line:833
	OO00OO00O0O0OO00O =p1 .get ('/eventkagi_items')#line:835
	O00O0000OO000O000 =OO00OO00O0O0OO00O .json ()['eventkagi_items']#line:836
	OO00OOO0OOOOO0OOO =d1 .Quests .get_by_id (OOOO0OOOO0O0OOO0O ).area_id #line:837
	OO0O000O0O0O0OO0O =d1 .Areas .get_by_id (OO00OOO0OOOOO0OOO ).category #line:838
	O00OO0OO00O0O0OO0 =d1 .AreaTabs .select ()#line:839
	O0O0OO0O000O0O000 =None #line:840
	for O0OO0000000O00O0O in O00OO0OO00O0O0OO0 :#line:841
		try :#line:842
			OO0OOO000O0OOOOO0 =json .loads (O0OO0000000O00O0O .area_category_ids )#line:843
		except :#line:844
			print ("Could not retrieve Kagi ID")#line:845
			return None #line:846
		if OO0O000O0O0O0OO0O in OO0OOO000O0OOOOO0 ['area_category_ids']:#line:847
			O0O0OO0O000O0O000 =int (O0OO0000000O00O0O .id )#line:848
			break #line:849
	if O0O0OO0O000O0O000 is None :#line:850
		return None #line:851
	for OO0OO0OO00O000O0O in O00O0000OO000O000 :#line:852
		if OO0OO0OO00O000O0O ['eventkagi_item_id']==O0O0OO0O000O0O000 :#line:853
			if OO0OO0OO00O000O0O ['quantity']>0 :#line:854
				return O0O0OO0O000O0O000 #line:855
			else :#line:856
				return None #line:857
	return None #line:858
def complete_unfinished_quest_stages ():#line:861
	O00OOO00OO0O00OOO =p1 .get ('/user_areas')#line:864
	OO00OO0O0O00OOO00 =[]#line:866
	for OO0OO00OOOOOO00OO in O00OOO00OO0O00OOO .json ()['user_areas']:#line:867
		for OOO0OOOO0OO00000O in OO0OO00OOOOOO00OO ['user_sugoroku_maps']:#line:868
			if (OOO0OOOO0OO00000O ['cleared_count']==0 )and (100 <OOO0OOOO0OO00000O ['sugoroku_map_id']<999999 ):#line:869
				OO00OO0O0O00OOO00 .append (OOO0OOOO0OO00000O )#line:870
	if len (OO00OO0O0O00OOO00 )==0 :#line:872
		print ("No quests to complete!")#line:873
		print ('--------------------------------------------')#line:874
		return 0 #line:875
	OOO0OOOO0000O0000 =0 #line:877
	while OOO0OOOO0000O0000 ==0 :#line:878
		for OOO0OOOO0OO00000O in OO00OO0O0O00OOO00 :#line:879
			complete_stage (str (OOO0OOOO0OO00000O ['sugoroku_map_id'])[:-1 ],str (OOO0OOOO0OO00000O ['sugoroku_map_id'])[-1 ])#line:880
		O00OOO00OO0O00OOO =p1 .get ('/user_areas')#line:882
		OO00O0O0OOO000O0O =[]#line:883
		for OOOO00O000OO00000 in O00OOO00OO0O00OOO .json ()['user_areas']:#line:885
			for OOO0OOOO0OO00000O in OOOO00O000OO00000 ['user_sugoroku_maps']:#line:886
				if (OOO0OOOO0OO00000O ['cleared_count']==0 )and (100 <OOO0OOOO0OO00000O ['sugoroku_map_id']<999999 ):#line:887
					OO00O0O0OOO000O0O .append (OOO0OOOO0OO00000O )#line:888
		if OO00O0O0OOO000O0O ==OO00OO0O0O00OOO00 :#line:889
			OOO0OOOO0000O0000 =1 #line:890
		else :#line:891
			OO00OO0O0O00OOO00 =OO00O0O0OOO000O0O #line:892
			refresh_client ()#line:893
	return 1 #line:894
def refresh_client ():#line:897
	c2 .access_token ,c2 .secret =signin (c2 .identifier ,c2 .UniqueId ,c2 .AdId )#line:899
def change_name ():#line:902
	O0OO00O00O0000OO0 =input ('What would you like to change your name to?: ')#line:904
	OO0OOO00O0000OO0O ={'user':{'name':O0OO00O00O0000OO0 }}#line:909
	O000O00OO0OO0O0O0 =p1 .put ('/user',data =json .dumps (OO0OOO00O0000OO0O ))#line:910
	if 'error'in O000O00OO0OO0O0O0 .json ():#line:911
		print (O000O00OO0OO0O0O0 .json ())#line:912
	else :#line:913
		print ("Name changed to: "+O0OO00O00O0000OO0 )#line:914
def increase_capacity ():#line:917
	O00000O0O0OOOO000 =int (input ('\nHow many times do you want to increase your capacity? (5 each): '))#line:919
	for OO0OO00000OOO00O0 in range (O00000O0O0OOOO000 ):#line:920
		O000O0O00OO0OOOOO =p1 .post ('/user/capacity/card')#line:921
		if 'error'in O000O0O00OO0OOOOO .json ():#line:922
			print (Fore .RED +Style .BRIGHT +str (O000O0O00OO0OOOOO .json ()))#line:923
		else :#line:924
			print (Fore .GREEN +Style .BRIGHT +'Card capacity +5')#line:925
def get_space ():#line:927
	O00O0O0OOO0O00O0O =p1 .get ('/cards')#line:928
	OOO0OO0000OO00O00 =0 #line:929
	O000O0OOO00OO0O00 =O00O0O0OOO0O00O0O .json ()['cards']#line:930
	for O000000000OO0O0O0 in O000O0OOO00OO0O00 :#line:931
		OOO0OO0000OO00O00 +=1 #line:932
	O00O0O0OOO0O00O0O =p1 .get ('/user')#line:933
	O0O0OOOO00OO0O00O =O00O0O0OOO0O00O0O .json ()#line:934
	O00000OOO0O00OOO0 =int (O0O0OOOO00OO0O00O ['user']['total_card_capacity'])#line:935
	O00OOOOOOOO000O00 =O00000OOO0O00OOO0 -OOO0OO0000OO00O00 #line:936
	print ("Total Space: "+str (O00000OOO0O00OOO0 ))#line:937
	print ("Currently occupied box space: "+str (OOO0OO0000OO00O00 ))#line:938
	print ("Space left: "+str (O00OOOOOOOO000O00 ))#line:939
def get_user_info (only_id =False ,only_stone =False ,only_zeni =False ,only_gasha =False ,only_rank =False ,only_baba =False ):#line:941
	O00OOO0OOOO00OOOO =p1 .get ('/user')#line:943
	O000O0O00O000O00O =O00OOO0OOOO00OOOO .json ()#line:944
	if only_stone :#line:945
		print (f"Total Stones: {str(O000O0O00O000O00O['user']['stone'])}")#line:946
	elif only_id :#line:947
		print (f"User ID: {str(O000O0O00O000O00O['user']['id'])}")#line:948
	elif only_zeni :#line:949
		print (f"Total Zeni: {str(O000O0O00O000O00O['user']['zeni'])}")#line:950
	elif only_gasha :#line:951
		print (f"Friend-Points: {str(O000O0O00O000O00O['user']['gasha_point'])}")#line:952
	elif only_rank :#line:953
		print (f"Rank: {str(O000O0O00O000O00O['user']['rank'])}")#line:954
	elif only_baba :#line:955
		print (f"Total Points: {str(O000O0O00O000O00O['user']['exchange_point'])}")#line:956
	else :#line:957
		print (f"Region: {c2.client.upper()}")#line:958
		print (f"Account OS: {c2.platform.upper()}")#line:959
		print (f"User ID: {str(O000O0O00O000O00O['user']['id'])}")#line:960
		print (f"Stones: {str(O000O0O00O000O00O['user']['stone'])}")#line:961
		print (f"Zeni: {str(O000O0O00O000O00O['user']['zeni'])}")#line:962
		print (f"Rank: {str(O000O0O00O000O00O['user']['rank'])}")#line:963
		print (f"Stamina: {str(O000O0O00O000O00O['user']['act'])}")#line:964
		print (f"Name: {str(O000O0O00O000O00O['user']['name'])}")#line:965
		print (f"Total Card Capacity: {str(O000O0O00O000O00O['user']['total_card_capacity'])}")#line:966
		print (f"Friend-Points: {str(O000O0O00O000O00O['user']['gasha_point'])}")#line:967
def complete_unfinished_events ():#line:969
	OOOO0OOO0OOO00000 =p1 .get ('/events')#line:973
	OO00O0OO00O00OO00 =OOOO0OOO0OOO00000 .json ()#line:974
	OO000O0O000OOOO00 =[]#line:975
	for OOO000O0OOO00OO00 in OO00O0OO00O00OO00 ['events']:#line:976
		OO000O0O000OOOO00 .append (OOO000O0OOO00OO00 ['id'])#line:977
	OO000O0O000OOOO00 =sorted (OO000O0O000OOOO00 )#line:978
	try :#line:979
		OOO0000OOO0OO00OO =135 #line:980
		OO000O0O000OOOO00 .remove (OOO0000OOO0OO00OO )#line:981
	except :#line:982
		pass #line:983
	OOOO0OOO0OOO00000 =p1 .get ('/user_areas')#line:986
	O0O0O00000O00O000 =OOOO0OOO0OOO00000 .json ()['user_areas']#line:987
	OOO00O0O0O0OOOO00 =1 #line:988
	for OO0OO00O0O000OO0O in O0O0O00000O00O000 :#line:989
		if OO0OO00O0O000OO0O ['area_id']in OO000O0O000OOOO00 :#line:990
			for O0O0000OO00O0OO0O in OO0OO00O0O000OO0O ['user_sugoroku_maps']:#line:991
				if O0O0000OO00O0OO0O ['cleared_count']==0 :#line:992
					complete_stage (str (O0O0000OO00O0OO0O ['sugoroku_map_id'])[:-1 ],str (O0O0000OO00O0OO0O ['sugoroku_map_id'])[-1 ])#line:993
					OOO00O0O0O0OOOO00 +=1 #line:994
		if OOO00O0O0O0OOOO00 %30 ==0 :#line:995
			refresh_client ()#line:996
def complete_clash ():#line:999
	print ('Fetching current clash..')#line:1000
	O0O00O000O0O00OOO =p1 .get ('/resources/home?rmbattles=true')#line:1001
	O0000000OO00O0000 =O0O00O000O0O00OOO .json ()['rmbattles']['id']#line:1002
	print ('Resetting clash to beginning..')#line:1005
	OO0O00O0O0OOOOOOO ={'reason':"dropout"}#line:1008
	O0O00O000O0O00OOO =p1 .post (f'/rmbattles/{O0000000OO00O0000}/stages/dropout',data =json .dumps (OO0O00O0O0OOOOOOO ))#line:1009
	print ('Reset complete..')#line:1010
	print ('Fetching list of stages from Bandai..')#line:1012
	O0O00O000O0O00OOO =p1 .get (f'/rmbattles/{O0000000OO00O0000}')#line:1013
	O00OO0OOO0O0000O0 =[]#line:1015
	for OOOO0O00O00OOO000 in O0O00O000O0O00OOO .json ()['level_stages'].values ():#line:1016
		for O0O00O00OO0OO0O0O in OOOO0O00O00OOO000 :#line:1017
			O00OO0OOO0O0000O0 .append (O0O00O00OO0OO0O0O ['id'])#line:1018
	print ('Stages obtained..')#line:1019
	print ('Asking Bandai for available cards..')#line:1020
	O0O00O000O0O00OOO =p1 .get ('/rmbattles/available_user_cards')#line:1022
	print ('Cards received..')#line:1023
	OOO00O0O0000OO000 =[]#line:1024
	for OO0OOO0OO0OOOO000 in O0O00O000O0O00OOO .json ():#line:1026
		OOO00O0O0000OO000 .append (OO0OOO0OO0OOOO000 )#line:1027
	OOO00O0O0000OO000 =OOO00O0O0000OO000 [:99 ]#line:1028
	if len (OOO00O0O0000OO000 )==0 :#line:1030
		print (Fore .RED +Style .BRIGHT +"Not enough cards to complete Battlefield with!")#line:1031
		return 0 #line:1032
	O0O000OO00OOO0OO0 =True #line:1034
	print ('Sending Bandai full team..')#line:1036
	O000000000OOO00O0 ={'user_card_ids':OOO00O0O0000OO000 }#line:1039
	O0O00O000O0O00OOO =p1 .put ('/rmbattles/teams/1',data =json .dumps (O000000000OOO00O0 ))#line:1040
	print ('Sent!\nCommencing Ultimate Clash!\n----------------------------\n')#line:1041
	try :#line:1042
		for O0O00O00OO0OO0O0O in O00OO0OOO0O0000O0 :#line:1043
			OO0O0OO0O00O0OOO0 =OOO00O0O0000OO000 [0 ]#line:1044
			O00O000O0OO0OOOOO =OOO00O0O0000OO000 [1 ]#line:1045
			O0000O00O0OO00000 =OOO00O0O0000OO000 [2 ]#line:1046
			OO0O00O0O0OOOOOOO ={'is_beginning':O0O000OO00OOO0OO0 ,'user_card_ids':{'leader':OO0O0OO0O00O0OOO0 ,'members':O00O000O0OO0OOOOO ,'sub_leader':O0000O00O0OO00000 }}#line:1055
			O0O00O000O0O00OOO =p1 .post (f'/rmbattles/{O0000000OO00O0000}/stages/{O0O00O00OO0OO0O0O}/start',data =json .dumps (OO0O00O0O0OOOOOOO ))#line:1057
			print ('Commencing Stage '+Fore .YELLOW +str (O0O00O00OO0OO0O0O ))#line:1058
			O0O000OO00OOO0OO0 =False #line:1060
			OOOOOOOOOO0OO0OO0 =int (round (time .time (),0 )+2000 )#line:1063
			OOO0OO00OOOOOOO00 =OOOOOOOOOO0OO0OO0 -randint (40000000 ,50000000 )#line:1064
			O0OO00OOOO0OO0O0O =p1 .decrypt_sign (O0O00O000O0O00OOO .json ()['sign'])#line:1066
			O00OOOO0OOO00O0OO =0 #line:1067
			try :#line:1068
				for OO00OOO0O00OOOOOO in O0OO00OOOO0OO0O0O ['enemies']:#line:1069
					O00OOOO0OOO00O0OO +=OO00OOO0O00OOOOOO [0 ]['hp']#line:1070
			except :#line:1071
				print ('nah')#line:1072
			OO0O00O0O0OOOOOOO ={'damage':O00OOOO0OOO00O0OO ,'finished_at_ms':OOOOOOOOOO0OO0OO0 ,'finished_reason':'win','is_cleared':True ,'remaining_hp':0 ,'round':0 ,'started_at_ms':OOO0OO00OOOOOOO00 ,'token':O0OO00OOOO0OO0O0O ['token']}#line:1083
			O0O00O000O0O00OOO =p1 .post (f'/rmbattles/{O0000000OO00O0000}/stages/finish',data =json .dumps (OO0O00O0O0OOOOOOO ))#line:1086
			print ('Completed Stage '+Fore .YELLOW +str (O0O00O00OO0OO0O0O ))#line:1087
			O0O00O000O0O00OOO =p1 .get ('/rmbattles/teams/1')#line:1089
			print ('----------------------------')#line:1090
			if 'sortiable_user_card_ids'not in O0O00O000O0O00OOO .json ():#line:1091
				return 0 #line:1092
			OOO00O0O0000OO000 =O0O00O000O0O00OOO .json ()['sortiable_user_card_ids']#line:1093
	except Exception as O0O0O000OO0O00O0O :#line:1094
		print (O0O0O000OO0O00O0O )#line:1095
		print ("Check if you have enough cards. The bot cannot do 1 unit clashes.")#line:1096
def complete_area (OOO00OOO0OOOO0OOO ):#line:1099
	OO0OOO0OOO0OOO0O0 =d1 .Quests .select ().where (d1 .Quests .area_id ==OOO00OOO0OOOO0OOO )#line:1102
	OO0OOO0000000OO00 =0 #line:1104
	for OO0O0O0OOOOOOOO0O in OO0OOO0OOO0OOO0O0 :#line:1105
		OO00O0O00OOO00OOO =d1 .SugorokuMaps .select ().where (d1 .SugorokuMaps .quest_id ==OO0O0O0OOOOOOOO0O .id )#line:1106
		OO0OOO0000000OO00 +=len (OO00O0O00OOO00OOO )#line:1107
	O0OOOOO0O0OO0OOOO =1 #line:1108
	for OO0O0O0OOOOOOOO0O in OO0OOO0OOO0OOO0O0 :#line:1109
		OO00O0O00OOO00OOO =d1 .SugorokuMaps .select ().where (d1 .SugorokuMaps .quest_id ==OO0O0O0OOOOOOOO0O .id )#line:1110
		for OOOO0OO00O0OO000O in OO00O0O00OOO00OOO :#line:1111
			print ('Completion of area: '+str (O0OOOOO0O0OO0OOOO )+'/'+str (OO0OOO0000000OO00 ))#line:1112
			complete_stage (str (OO0O0O0OOOOOOOO0O .id ),OOOO0OO00O0OO000O .difficulty )#line:1113
			O0OOOOO0O0OO0OOOO +=1 #line:1114
def save_account (save_name :str =None ):#line:1117
	try :#line:1118
		os .mkdir ('Saves')#line:1119
		os .mkdir ('Saves/android')#line:1120
		os .mkdir ('Saves/ios')#line:1121
	except OSError as OOOO0O0O00O0O00O0 :#line:1122
		if OOOO0O0O00O0O00O0 .errno !=errno .EEXIST :#line:1123
			print (Fore .RED +Style .BRIGHT +'Unable to create saves file')#line:1124
			return 0 #line:1125
		pass #line:1126
	if save_name is None :#line:1128
		O00O000O000000OO0 =False #line:1129
		while not O00O000O000000OO0 :#line:1130
			save_name =input ("What would you like to name the file?: ")#line:1131
			if save_name !='':#line:1132
				O00O000O000000OO0 =True #line:1133
			else :#line:1134
				print (Fore .RED +Style .BRIGHT +"Name not allowed!")#line:1135
			if os .path .exists ('Saves'+os .sep +c2 .platform +os .sep +save_name ):#line:1136
				print (Fore .RED +Style .BRIGHT +"File by that name already exists.")#line:1137
				continue #line:1138
	try :#line:1140
		OO00OOO00OO0OO0O0 =open (os .path .join ('Saves'+os .sep +c2 .platform +os .sep +save_name ),'w+')#line:1141
		OO00OOO00OO0OO0O0 .write (str (c2 .identifier )+'\n')#line:1142
		OO00OOO00OO0OO0O0 .write (str (c2 .AdId )+'\n')#line:1143
		OO00OOO00OO0OO0O0 .write (str (c2 .UniqueId )+'\n')#line:1144
		OO00OOO00OO0OO0O0 .write (str (c2 .platform )+'\n')#line:1145
		OO00OOO00OO0OO0O0 .write (str (c2 .client )+'\n')#line:1146
		OO00OOO00OO0OO0O0 .close ()#line:1147
		print ('--------------------------------------------')#line:1148
		print (Fore .CYAN +Style .BRIGHT +'Written details to file: '+save_name )#line:1149
		print (Fore .RED +Style .BRIGHT +'If '+save_name +' is deleted your account will be lost!')#line:1150
		print ('--------------------------------------------')#line:1151
	except Exception as O00O00O000000O0OO :#line:1152
		print (O00O00O000000O0OO )#line:1153
def read_save (OOO000O00000000O0 :str )->bool :#line:1156
	if os .path .isfile ('Saves'+os .sep +c2 .platform +os .sep +OOO000O00000000O0 ):#line:1157
		try :#line:1158
			O00000O00O00O0OO0 =open (os .path .join ('Saves',c2 .platform ,OOO000O00000000O0 ),'r')#line:1159
			c2 .identifier =O00000O00O00O0OO0 .readline ().rstrip ()#line:1160
			c2 .AdId =O00000O00O00O0OO0 .readline ().rstrip ()#line:1161
			c2 .UniqueId =O00000O00O00O0OO0 .readline ().rstrip ()#line:1162
			c2 .platform =O00000O00O00O0OO0 .readline ().rstrip ()#line:1163
			OOO00O0OOOO000O00 =O00000O00O00O0OO0 .readline ().rstrip ()#line:1164
			if c2 .client ==OOO00O0OOOO000O00 :#line:1165
				return True #line:1166
			else :#line:1167
				print (Fore .RED +Style .BRIGHT +'Save does not match client version.')#line:1168
				return False #line:1169
		except Exception as O0OOOOO000O0OOO0O :#line:1170
			print (O0OOOOO000O0OOO0O )#line:1171
			return False #line:1172
	else :#line:1173
		print (Fore .RED +Style .BRIGHT +"Could not find "+OOO000O00000000O0 )#line:1174
		return False #line:1175
def load_account (platform :str =None ,save_name :str =None )->bool :#line:1178
	if platform is None :#line:1179
		while True :#line:1180
			platform =input ("'a'|Android -- 'i'|iOS: ")#line:1181
			if platform [0 ].lower ()in ['a','i']:#line:1182
				if platform [0 ].lower ()=='a':#line:1183
					c2 .platform ='android'#line:1184
				elif platform [0 ].lower ()=='i':#line:1185
					c2 .platform ='ios'#line:1186
				else :#line:1187
					continue #line:1188
				break #line:1189
			else :#line:1190
				print (Fore .RED +'Could not identify correct platform to use.')#line:1191
	if save_name is None :#line:1193
		while True :#line:1194
			save_name =input ("What save would you like to load?: ")#line:1195
			if read_save (save_name ):#line:1196
				break #line:1197
	else :#line:1198
		if not read_save (save_name ):#line:1199
			return False #line:1200
	refresh_client ()#line:1202
	return True #line:1203
def daily_login ():#line:1206
	O00OOOO000OO0O00O =p1 .get ('/resources/home?apologies=true&banners=true&bonus_schedules=true&budokai=true&comeback_campaigns=true&gifts=true&login_bonuses=true&rmbattles=true')#line:1208
	if 'error'in O00OOOO000OO0O00O .json ():#line:1209
		print (O00OOOO000OO0O00O .json ())#line:1210
	O00OOOO000OO0O00O =p1 .post ('/login_bonuses/accept')#line:1212
	if 'error'in O00OOOO000OO0O00O .json ():#line:1213
		print (O00OOOO000OO0O00O .json ())#line:1214
def dragonballs ():#line:1217
	OOOO0O0O0OOOO00O0 =0 #line:1218
	OO00O0OO0O00000O0 =p1 .get ('/dragonball_sets')#line:1220
	if 'error'in OO00O0OO0O00000O0 .json ():#line:1221
		print (OO00O0OO0O00000O0 )#line:1222
		return 0 #line:1223
	OOO0O0000O0O0O0OO =OO00O0OO0O00000O0 .json ()['dragonball_sets'][0 ]['id']#line:1226
	for OOOO0OO0OO0O0OO00 in OO00O0OO0O00000O0 .json ()['dragonball_sets']:#line:1229
		for O00O000O0OOO00OOO in reversed (OOOO0OO0OO0O0OO00 ['dragonballs']):#line:1230
			if O00O000O0OOO00OOO ['id']>10000 :#line:1231
				continue #line:1232
			if O00O000O0OOO00OOO ['is_got']:#line:1233
				OOOO0O0O0OOOO00O0 +=1 #line:1234
			elif not O00O000O0OOO00OOO ['is_got']:#line:1235
				OOOO0O0O0OOOO00O0 +=1 #line:1236
				complete_stage (str (O00O000O0OOO00OOO ['quest_id']),O00O000O0OOO00OOO ['difficulties'][0 ])#line:1237
	if OOOO0O0O0OOOO00O0 ==7 :#line:1240
		OO00O0OO0O00000O0 =p1 .get (f'/dragonball_sets/{OOO0O0000O0O0O0OO}/wishes')#line:1241
		if 'error'in OO00O0OO0O00000O0 .json ():#line:1242
			print (Fore .RED +Style .BRIGHT +str (OO00O0OO0O00000O0 .json ()))#line:1243
			return 0 #line:1244
		OO0O0O0OO0O000O0O =[]#line:1245
		for OOO0OO000OO0000OO in OO00O0OO0O00000O0 .json ()['dragonball_wishes']:#line:1246
			if OOO0OO000OO0000OO ['is_wishable']:#line:1247
				print ('Wish ID: '+str (OOO0OO000OO0000OO ['id']))#line:1248
				OO0O0O0OO0O000O0O .append (str (OOO0OO000OO0000OO ['id']))#line:1249
				print (OOO0OO000OO0000OO ['title'])#line:1250
				print ('')#line:1251
		print (Fore .YELLOW +'What wish would you like to ask shenron for? ID: ',end ='')#line:1253
		O0O000OOOO0OOO0O0 =input ()#line:1254
		while O0O000OOOO0OOO0O0 not in OO0O0O0OO0O000O0O :#line:1255
			print ("Shenron did not understand you! ID: ",end ='')#line:1256
			O0O000OOOO0OOO0O0 =input ()#line:1257
		OO0O0O0OO0O000O0O [:]=[]#line:1258
		OOO0O0OOOO0OOO000 ={'dragonball_wish_ids':[int (O0O000OOOO0OOO0O0 )]}#line:1261
		OO00O0OO0O00000O0 =p1 .post (f'/dragonball_sets/{OOO0O0000O0O0O0OO}/wishes',data =json .dumps (OOO0O0OOOO0OOO000 ))#line:1262
		if 'error'in OO00O0OO0O00000O0 .json ():#line:1263
			print (Fore .RED +Style .BRIGHT +str (OO00O0OO0O00000O0 .json ()))#line:1264
		else :#line:1265
			print (Fore .YELLOW +'Wish granted!')#line:1266
			print ('')#line:1267
		OOO00OOO000OOO000 =input ("Continue?(Y/N): ")#line:1269
		if OOO00OOO000OOO000 .lower ()=='y':#line:1270
			dragonballs ()#line:1271
		return 0 #line:1272
def transfer_account ():#line:1275
	set_platform ()#line:1277
	OOO000OOOOO00O0O0 =input ('Enter your transfer code: ')#line:1279
	while True :#line:1280
		O0O0000OO0O00000O =input ('What would you like to name the Save?: ')#line:1281
		if os .path .exists ('Saves'+os .sep +c2 .platform +os .sep +O0O0000OO0O00000O ):#line:1282
				O000OOOO000000OO0 =True #line:1283
				print ('File already exists.\n')#line:1284
				continue #line:1285
		else :#line:1286
			break #line:1287
	if O0O0000OO0O00000O is None :#line:1288
		OOO0OOO00000OOOO0 =False #line:1289
		while not OOO0OOO00000OOOO0 :#line:1290
			try :#line:1291
				OO0000OOO0O00000O =open (os .path .join ('Saves'+os .sep +c2 .platform +os .sep +O0O0000OO0O00000O ),'w')#line:1292
			except :#line:1293
				print ('Savefile could not be created. Exiting for Safety reasons.\n')#line:1294
				exit ()#line:1295
	c2 .AdId =p1 .guid ()['AdId']#line:1296
	c2 .UniqueId =p1 .guid ()['UniqueId']#line:1297
	OOO0000O0OOOO0O00 ={'User-Agent':'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0','Accept':'*/*','Content-type':'application/json','X-Platform':c2 .platform ,'X-AssetVersion':'////','X-DatabaseVersion':'////','X-ClientVersion':'////',}#line:1306
	OO0O0000O0O0O000O ={'eternal':True ,'old_user_id':'','user_account':{'device':'samsung','device_model':'SM-E7000','os_version':'7.0','platform':c2 .platform ,'unique_id':c2 .UniqueId ,}}#line:1313
	if c2 .client =='global':#line:1314
		OOO0OOO0O0O0000OO ='https://ishin-global.aktsk.com/auth/link_codes/'+str (OOO000OOOOO00O0O0 )#line:1316
	else :#line:1317
		OOO0OOO0O0O0000OO ='http://ishin-production.aktsk.jp/auth/link_codes/'+str (OOO000OOOOO00O0O0 )#line:1319
	O0O0O000O0O00000O =requests .put (OOO0OOO0O0O0000OO ,data =json .dumps (OO0O0000O0O0O000O ),headers =OOO0000O0OOOO0O00 )#line:1320
	if 'error'in O0O0O000O0O00000O .json ():#line:1321
		print (O0O0O000O0O00000O )#line:1322
		print (base64 .b64decode (O0O0O000O0O00000O .json ()['identifiers']).decode ('utf-8'))#line:1323
	print (base64 .b64decode (O0O0O000O0O00000O .json ()['identifiers']).decode ('utf-8'))#line:1324
	c2 .identifier =base64 .b64decode (O0O0O000O0O00000O .json ()['identifiers']).decode ('utf-8')#line:1325
	print (Fore .RED +'[Caution !] It is recommended to screenshot the following Screen as the Bot is known to sometimes crash at this point.[Caution !]\n'+Style .RESET_ALL +'Press any key to continue.\n')#line:1327
	OOO00O0O00O000O00 =input ('')#line:1328
	try :#line:1329
		save_account (O0O0000OO0O00000O )#line:1330
	except Exception as O0OO0O00OO0O0OO0O :#line:1331
		print (O0OO0O00OO0O0OO0O )#line:1332
		print ("The bot encountered a Problem! Back this up to keep your save: '"+c2 .identifier +"'")#line:1333
		OOOO00O0O00O0O0O0 =input ("")#line:1334
	refresh_client ()#line:1335
def user_command_executor (O00OOOO0OO000O0O0 ):#line:1338
	if ','in O00OOOO0OO000O0O0 :#line:1339
		O00OOOO0OO000O0O0 =O00OOOO0OO000O0O0 .replace (" ","")#line:1340
		O00OOOO0OO000O0O0 =O00OOOO0OO000O0O0 .replace (",","\n")#line:1341
		O0000OO0000000000 =io .StringIO (O00OOOO0OO000O0O0 +'\n')#line:1342
		sys .stdin =O0000OO0000000000 #line:1343
		O00OOOO0OO000O0O0 =input ()#line:1344
	if O00OOOO0OO000O0O0 =='help':#line:1346
		print (h1 .text )#line:1347
	elif O00OOOO0OO000O0O0 =='stage':#line:1348
		c2 .allow_stamina_refill =True #line:1349
		stage_executor ()#line:1350
	elif O00OOOO0OO000O0O0 =='area':#line:1351
		c2 .allow_stamina_refill =True #line:1352
		OOO0O0O0O0O0O00OO =input ('Enter the area (1 to 27) to complete: ')#line:1353
		if int (OOO0O0O0O0O0O00OO )>0 and int (OOO0O0O0O0O0O00OO )<28 :#line:1354
			OO0OO0OO00000OO0O =int (input ('How many times to complete the entire area: '))#line:1355
			for O00000OO0OOO00OO0 in range (OO0OO0OO00000OO0O ):#line:1356
				complete_area (OOO0O0O0O0O0O00OO )#line:1357
		else :#line:1358
			print (f"{OOO0O0O0O0O0O00OO} is not a valid Area ID.")#line:1359
	elif O00OOOO0OO000O0O0 =='gift':#line:1360
		accept_gifts ()#line:1361
		accept_missions ()#line:1362
	elif O00OOOO0OO000O0O0 =='finishall':#line:1363
		c2 .allow_stamina_refill =True #line:1364
		accept_gifts ()#line:1365
		accept_missions ()#line:1366
		complete_unfinished_quest_stages ()#line:1367
		complete_unfinished_events ()#line:1368
		complete_unfinished_zbattles (31 )#line:1369
		complete_clash ()#line:1370
	elif O00OOOO0OO000O0O0 =='finishquest':#line:1372
		c2 .allow_stamina_refill =True #line:1373
		complete_unfinished_quest_stages ()#line:1374
	elif O00OOOO0OO000O0O0 =='streamline':#line:1375
		c2 .allow_stamina_refill =True #line:1376
		complete_unfinished_quest_stages ()#line:1377
	elif O00OOOO0OO000O0O0 =='finishevents':#line:1378
		c2 .allow_stamina_refill =True #line:1379
		complete_unfinished_events ()#line:1380
	elif O00OOOO0OO000O0O0 =='streamlineevents':#line:1381
		c2 .allow_stamina_refill =True #line:1382
		complete_unfinished_events ()#line:1383
	elif O00OOOO0OO000O0O0 =='finishzbattle':#line:1384
		c2 .allow_stamina_refill =True #line:1385
		complete_unfinished_zbattles (31 )#line:1386
	elif O00OOOO0OO000O0O0 =='sbr':#line:1387
		c2 .allow_stamina_refill =True #line:1388
		sbr_finish ()#line:1389
	elif O00OOOO0OO000O0O0 =='bossrush':#line:1390
		c2 .allow_stamina_refill =True #line:1391
		bossrush ()#line:1392
	elif O00OOOO0OO000O0O0 =='clash':#line:1393
		complete_clash ()#line:1394
	elif O00OOOO0OO000O0O0 =='potential':#line:1395
		complete_potential ()#line:1396
	elif O00OOOO0OO000O0O0 =='daily':#line:1397
		c2 .allow_stamina_refill =True #line:1398
		daily_events ()#line:1399
	elif O00OOOO0OO000O0O0 =='listevents':#line:1400
		list_events ()#line:1401
	elif O00OOOO0OO000O0O0 =='cmdsummon':#line:1402
		summon_nogui ()#line:1403
	elif O00OOOO0OO000O0O0 =='listsummons':#line:1404
		list_summons ()#line:1405
	elif O00OOOO0OO000O0O0 =='dragonballs':#line:1406
		dragonballs ()#line:1407
	elif O00OOOO0OO000O0O0 =='info':#line:1408
		get_user_info ()#line:1409
	elif O00OOOO0OO000O0O0 =='cmditems':#line:1410
		items_viewer_nogui ()#line:1411
	elif O00OOOO0OO000O0O0 =='sell':#line:1412
		sell_r_and_n ()#line:1413
	elif O00OOOO0OO000O0O0 =='terminate':#line:1414
		sys .exit ()#line:1415
	elif O00OOOO0OO000O0O0 =='deck':#line:1416
		c2 .deck =int (input ('Enter a deck number to use: '))#line:1417
	elif O00OOOO0OO000O0O0 =='transfer':#line:1418
		get_transfer_code ()#line:1419
	elif O00OOOO0OO000O0O0 =='capacity':#line:1420
		increase_capacity ()#line:1421
	elif O00OOOO0OO000O0O0 =='name':#line:1422
		change_name ()#line:1423
	elif O00OOOO0OO000O0O0 =='refresh':#line:1424
		refresh_client ()#line:1425
	elif O00OOOO0OO000O0O0 =='sellhercule':#line:1426
		sell_hercule_cards ()#line:1427
	elif O00OOOO0OO000O0O0 =='baba':#line:1428
		baba_cards ()#line:1429
	elif O00OOOO0OO000O0O0 =='hydros':#line:1430
		complete_unfinished_quest_stages ()#line:1431
		try :#line:1432
			rankup ()#line:1433
		except :#line:1434
			print ("Error while doing Rankup. Aborted.")#line:1435
	elif O00OOOO0OO000O0O0 =='areaevents':#line:1436
		c2 .allow_stamina_refill =True #line:1437
		area_event ()#line:1438
	elif O00OOOO0OO000O0O0 =='rename':#line:1439
		rename_save ()#line:1440
		refresh_client ()#line:1441
	elif O00OOOO0OO000O0O0 =='cmdcards':#line:1442
		view_cards ()#line:1443
	elif O00OOOO0OO000O0O0 =='rankup':#line:1444
		complete_unfinished_quest_stages ()#line:1445
		rankup ()#line:1446
	elif O00OOOO0OO000O0O0 =='keys':#line:1447
		stage_executor (use_keys =True )#line:1448
	elif O00OOOO0OO000O0O0 =='zeni':#line:1449
		complete_unfinished_zbattles (1000 )#line:1450
	elif O00OOOO0OO000O0O0 =='zbattle':#line:1451
		c2 .allow_stamina_refill =True #line:1452
		complete_zbattle_stage ()#line:1453
	elif O00OOOO0OO000O0O0 =='vegito':#line:1454
		l1 .vegito ()#line:1455
	elif O00OOOO0OO000O0O0 =='space':#line:1456
		get_space ()#line:1457
	else :#line:1458
		print ('Command not found.')#line:1459
def stage_executor (use_keys =False ):#line:1461
	if use_keys :#line:1462
		OOO0000000O0O0O00 =input ('What stage would you like to complete? [With Keys]: ')#line:1463
	else :#line:1464
		OOO0000000O0O0O00 =input ('What stage would you like to complete?: ')#line:1465
	O00O0O00O0O0OO0O0 =input ('Enter the difficulty|(0:Easy, 1:Hard etc..): ')#line:1466
	OOOO00OOO0000OOOO =input ('Enter how many times to execute: ')#line:1467
	if use_keys :#line:1468
		OOO00O000O0O0O0OO =get_kagi_id (OOO0000000O0O0O00 )#line:1469
		if OOO00O000O0O0O0OO is None :#line:1470
			print ("No keys for stage found or stage is currently active")#line:1471
			return None #line:1472
		print ('Key ID: '+str (OOO00O000O0O0O0OO ))#line:1473
		try :#line:1474
			for OO0O00O0OOOOO0O0O in range (int (OOOO00OOO0000OOOO )):#line:1475
				complete_stage (OOO0000000O0O0O00 ,O00O0O00O0O0OO0O0 ,kagi =OOO00O000O0O0O0OO )#line:1476
		except :#line:1477
			print (Fore .RED +'Invalid Stage/ID/Difficulty. If this error is recurring redownload the DB.')#line:1478
	else :#line:1479
		try :#line:1480
			for OO0O00O0OOOOO0O0O in range (int (OOOO00OOO0000OOOO )):#line:1481
				complete_stage (OOO0000000O0O0O00 ,O00O0O00O0O0OO0O0 )#line:1482
		except :#line:1483
			print (Fore .RED +'Invalid Stage/ID/Difficulty. If this error is recurring redownload the DB.')#line:1484
def complete_unfinished_zbattles (OOO00OO00OOOO000O ,kagi =False ):#line:1486
	O0O0000OO0O000OO0 =p1 .get ('/events')#line:1488
	OO0000OO000O00OO0 =O0O0000OO0O000OO0 .json ()#line:1489
	try :#line:1490
		for O0O0000OO00000O0O in OO0000OO000O00OO0 ['z_battle_stages']:#line:1491
			print (d1 .ZBattleStageViews .get (d1 .ZBattleStageViews .z_battle_stage_id ==O0O0000OO00000O0O ['id']).enemy_name ,end ='')#line:1492
			print (Fore .CYAN +Style .BRIGHT +' | ID: '+str (O0O0000OO00000O0O ['id']))#line:1493
			O0O0000OO0O000OO0 =p1 .get (f"/z_battles/{O0O0000OO00000O0O['id']}/rankings")#line:1495
			O00000O0O0O00O000 =1 #line:1497
			if len (O0O0000OO0O000OO0 .json ()['friends'])>0 :#line:1499
				OO000OO000OOOO00O =0 #line:1501
				OO0000O00O00O0OOO =p1 .get ('/user')#line:1502
				for OOO0OO0000000000O in O0O0000OO0O000OO0 .json ()['friends']:#line:1503
					if str (O0O0000OO0O000OO0 .json ()['friends'][OO000OO000OOOO00O ]['user_id'])==str (OO0000O00O00O0OOO .json ()['user']['id']):#line:1504
						O00000O0O0O00O000 =int (O0O0000OO0O000OO0 .json ()['friends'][OO000OO000OOOO00O ]['max_clear_level'])+1 #line:1505
					OO000OO000OOOO00O =OO000OO000OOOO00O +1 #line:1506
			while O00000O0O0O00O000 <int (OOO00OO00OOOO000O ):#line:1508
				O0O0000OO0O000OO0 =p1 .get (f"/z_battles/{O0O0000OO00000O0O['id']}/supporters")#line:1510
				if 'supporters'in O0O0000OO0O000OO0 .json ():#line:1511
					O00OOOO0O0000O0OO =O0O0000OO0O000OO0 .json ()['supporters'][0 ]['id']#line:1512
				elif 'error'in O0O0000OO0O000OO0 .json ():#line:1513
					print (Fore .RED +Style .BRIGHT +O0O0000OO0O000OO0 .json ())#line:1514
					return 0 #line:1515
				else :#line:1516
					print (Fore .RED +Style .BRIGHT +'Problem with ZBattle')#line:1517
					print (O0O0000OO0O000OO0 .raw ())#line:1518
					return 0 #line:1519
				if kagi :#line:1522
					OO0OOO0000O00OO00 =json .dumps ({'friend_id':O00OOOO0O0000O0OO ,'level':O00000O0O0O00O000 ,'selected_team_num':c2 .deck ,'eventkagi_item_id':5 })#line:1528
				else :#line:1529
					OO0OOO0000O00OO00 =json .dumps ({'friend_id':O00OOOO0O0000O0OO ,'level':O00000O0O0O00O000 ,'selected_team_num':c2 .deck ,})#line:1534
				O0OOOOOO0O0O00OO0 =p1 .encrypt_sign (OO0OOO0000O00OO00 )#line:1536
				O0OOOO0O0O000OOO0 ={'sign':O0OOOOOO0O0O00OO0 }#line:1539
				O0O0000OO0O000OO0 =p1 .post (f"/z_battles/{O0O0000OO00000O0O['id']}/start",data =json .dumps (O0OOOO0O0O000OOO0 ))#line:1540
				if 'sign'in O0O0000OO0O000OO0 .json ():#line:1542
					OOOO0O0O000OO0OO0 =p1 .decrypt_sign (O0O0000OO0O000OO0 .json ()['sign'])#line:1543
				elif 'error'in O0O0000OO0O000OO0 .json ():#line:1544
					print (O0O0000OO0O000OO0 .json ())#line:1545
					return 0 #line:1546
				else :#line:1547
					print (Fore .RED +Style .BRIGHT +'Problem with ZBattle')#line:1548
					print (O0O0000OO0O000OO0 .raw ())#line:1549
					return 0 #line:1550
				OO0OOOO000O00O0OO =int (round (time .time (),0 )+2000 )#line:1552
				OOO0OO0O0O0O0OO0O =OO0OOOO000O00O0OO -randint (6200000 ,8200000 )#line:1553
				O0OOOO0O0O000OOO0 ={'elapsed_time':OO0OOOO000O00O0OO -OOO0OO0O0O0O0OO0O ,'is_cleared':True ,'level':O00000O0O0O00O000 ,'s':'rGAX18h84InCwFGbd/4zr1FvDNKfmo/TJ02pd6onclk=','t':'eyJzdW1tYXJ5Ijp7ImVuZW15X2F0dGFjayI6MTAwMzg2LCJlbmVteV9hdHRhY2tfY291bnQiOjUsImVuZW15X2hlYWxfY291bnRzIjpbMF0sImVuZW15X2hlYWxzIjpbMF0sImVuZW15X21heF9hdHRhY2siOjEwMDAwMCwiZW5lbXlfbWluX2F0dGFjayI6NTAwMDAsInBsYXllcl9hdHRhY2tfY291bnRzIjpbMTBdLCJwbGF5ZXJfYXR0YWNrcyI6WzMwNjYwNTJdLCJwbGF5ZXJfaGVhbCI6MCwicGxheWVyX2hlYWxfY291bnQiOjAsInBsYXllcl9tYXhfYXR0YWNrcyI6WzEyMzY4NTBdLCJwbGF5ZXJfbWluX2F0dGFja3MiOls0NzcxOThdLCJ0eXBlIjoic3VtbWFyeSJ9fQ==','token':OOOO0O0O000OO0OO0 ['token'],'used_items':[],'z_battle_finished_at_ms':OO0OOOO000O00O0OO ,'z_battle_started_at_ms':OOO0OO0O0O0O0OO0O ,}#line:1566
				O0O0000OO0O000OO0 =p1 .post (f"/z_battles/{O0O0000OO00000O0O['id']}/finish",data =json .dumps (O0OOOO0O0O000OOO0 ))#line:1569
				OOOO0O0O000OO0OO0 =p1 .decrypt_sign (O0O0000OO0O000OO0 .json ()['sign'])#line:1570
				print ('Level: '+str (O00000O0O0O00O000 ))#line:1572
				if 'items'in OOOO0O0O000OO0OO0 :#line:1574
					O0OOOO0O000O00000 =[]#line:1575
					O000OOO00000O0000 =[]#line:1576
					OO00OOO0OO00O0O00 =[]#line:1577
					O0OOO0OOO00000000 =[]#line:1578
					OOOO0O000O00OO0OO =[]#line:1579
					OO0OOOO00O000OOO0 =[]#line:1580
					O0OOO00OOO0000O00 =[]#line:1581
					OO0OOOOOO0O0000O0 =0 #line:1582
					O00O00OOO0000O0OO =set ()#line:1583
					OOO00O0O0000O00OO =set ()#line:1584
					O00000OOO000O0O00 =set ()#line:1585
					OO00O000OO0O000O0 =set ()#line:1586
					OO0O0OO00OO00O00O =set ()#line:1587
					O00O00OO0000O0OOO =set ()#line:1588
					OOOOOO0O0O0OOOO00 =set ()#line:1589
					print ('Items:')#line:1590
					print ('-------------------------')#line:1591
					if 'quest_clear_rewards'in OOOO0O0O000OO0OO0 :#line:1592
						for O000OO0OO0O0OOOO0 in OOOO0O0O000OO0OO0 ['quest_clear_rewards']:#line:1593
							if O000OO0OO0O0OOOO0 ['item_type']=='Point::Stone':#line:1594
								OO0OOOOOO0O0000O0 +=O000OO0OO0O0OOOO0 ['amount']#line:1595
					for O000OO0OO0O0OOOO0 in OOOO0O0O000OO0OO0 ['items']:#line:1596
						if O000OO0OO0O0OOOO0 ['item_type']=='SupportItem':#line:1597
							for OO000OO000OOOO00O in range (O000OO0OO0O0OOOO0 ['quantity']):#line:1601
								O0OOOO0O000O00000 .append (O000OO0OO0O0OOOO0 ['item_id'])#line:1602
							O00O00OOO0000O0OO .add (O000OO0OO0O0OOOO0 ['item_id'])#line:1603
						elif O000OO0OO0O0OOOO0 ['item_type']=='PotentialItem':#line:1604
							for OO000OO000OOOO00O in range (O000OO0OO0O0OOOO0 ['quantity']):#line:1608
								O0OOO0OOO00000000 .append (O000OO0OO0O0OOOO0 ['item_id'])#line:1609
							OO00O000OO0O000O0 .add (O000OO0OO0O0OOOO0 ['item_id'])#line:1610
						elif O000OO0OO0O0OOOO0 ['item_type']=='TrainingItem':#line:1611
							for OO000OO000OOOO00O in range (O000OO0OO0O0OOOO0 ['quantity']):#line:1615
								OO00OOO0OO00O0O00 .append (O000OO0OO0O0OOOO0 ['item_id'])#line:1616
							O00000OOO000O0O00 .add (O000OO0OO0O0OOOO0 ['item_id'])#line:1617
						elif O000OO0OO0O0OOOO0 ['item_type']=='AwakeningItem':#line:1618
							for OO000OO000OOOO00O in range (O000OO0OO0O0OOOO0 ['quantity']):#line:1622
								O000OOO00000O0000 .append (O000OO0OO0O0OOOO0 ['item_id'])#line:1623
							OOO00O0O0000O00OO .add (O000OO0OO0O0OOOO0 ['item_id'])#line:1624
						elif O000OO0OO0O0OOOO0 ['item_type']=='TreasureItem':#line:1625
							for OO000OO000OOOO00O in range (O000OO0OO0O0OOOO0 ['quantity']):#line:1629
								OOOO0O000O00OO0OO .append (O000OO0OO0O0OOOO0 ['item_id'])#line:1630
							OO0O0OO00OO00O00O .add (O000OO0OO0O0OOOO0 ['item_id'])#line:1631
						elif O000OO0OO0O0OOOO0 ['item_type']=='Card':#line:1632
							OO0OOOO00O000OOO0 .append (O000OO0OO0O0OOOO0 ['item_id'])#line:1636
							O00O00OO0000O0OOO .add (O000OO0OO0O0OOOO0 ['item_id'])#line:1637
						elif O000OO0OO0O0OOOO0 ['item_type']=='Point::Stone':#line:1638
							OO0OOOOOO0O0000O0 +=1 #line:1643
						elif O000OO0OO0O0OOOO0 ['item_type']=='TrainingField':#line:1644
							for OO000OO000OOOO00O in range (O000OO0OO0O0OOOO0 ['quantity']):#line:1648
								O0OOO00OOO0000O00 .append (O000OO0OO0O0OOOO0 ['item_id'])#line:1649
							OOOOOO0O0O0OOOO00 .add (O000OO0OO0O0OOOO0 ['item_id'])#line:1650
						else :#line:1651
							print (O000OO0OO0O0OOOO0 ['item_type'])#line:1652
					for O000OO0OO0O0OOOO0 in O00O00OOO0000O0OO :#line:1655
						print (Fore .CYAN +Style .BRIGHT +d1 .SupportItems .get_by_id (O000OO0OO0O0OOOO0 ).name +' x'+str (O0OOOO0O000O00000 .count (O000OO0OO0O0OOOO0 )))#line:1656
					for O000OO0OO0O0OOOO0 in OOO00O0O0000O00OO :#line:1658
						print (Fore .MAGENTA +Style .BRIGHT +d1 .AwakeningItems .get_by_id (O000OO0OO0O0OOOO0 ).name +' x'+str (O000OOO00000O0000 .count (O000OO0OO0O0OOOO0 )))#line:1659
					for O000OO0OO0O0OOOO0 in O00000OOO000O0O00 :#line:1661
						print (Fore .RED +Style .BRIGHT +d1 .TrainingItems .get_by_id (O000OO0OO0O0OOOO0 ).name +' x'+str (OO00OOO0OO00O0O00 .count (O000OO0OO0O0OOOO0 )))#line:1662
					for O000OO0OO0O0OOOO0 in OO00O000OO0O000O0 :#line:1664
						print (d1 .PotentialItems .get_by_id (O000OO0OO0O0OOOO0 ).name +' x'+str (O0OOO0OOO00000000 .count (O000OO0OO0O0OOOO0 )))#line:1665
					for O000OO0OO0O0OOOO0 in OO0O0OO00OO00O00O :#line:1667
						print (Fore .GREEN +Style .BRIGHT +d1 .TreasureItems .get_by_id (O000OO0OO0O0OOOO0 ).name +' x'+str (OOOO0O000O00OO0OO .count (O000OO0OO0O0OOOO0 )))#line:1668
					for O000OO0OO0O0OOOO0 in OOOOOO0O0O0OOOO00 :#line:1670
						print (d1 .TrainingFields .get_by_id (O000OO0OO0O0OOOO0 ).name +' x'+str (O0OOO00OOO0000O00 .count (O000OO0OO0O0OOOO0 )))#line:1671
					for O000OO0OO0O0OOOO0 in O00O00OO0000O0OOO :#line:1673
						print (d1 .Cards .get_by_id (O000OO0OO0O0OOOO0 ).name +' x'+str (OO0OOOO00O000OOO0 .count (O000OO0OO0O0OOOO0 )))#line:1674
					print (Fore .YELLOW +Style .BRIGHT +'Stones x'+str (OO0OOOOOO0O0000O0 ))#line:1676
				if 'gasha_point'in OOOO0O0O000OO0OO0 :#line:1678
					print ('Friend Points: '+str (OOOO0O0O000OO0OO0 ['gasha_point']))#line:1679
				print ('--------------------------')#line:1681
				print ('')#line:1682
				O00000O0O0O00O000 +=1 #line:1683
				OO000OO000OOOO00O =0 #line:1684
				O0OOOO0O0OOO00000 =[]#line:1685
				if 'user_items'in OOOO0O0O000OO0OO0 :#line:1686
					if 'cards'in OOOO0O0O000OO0OO0 ['user_items']:#line:1687
						for O000OO0OO0O0OOOO0 in OOOO0O0O000OO0OO0 ['user_items']['cards']:#line:1688
							if 149 <int (d1 .Cards .get_by_id (O000OO0OO0O0OOOO0 ['card_id']).hp_max )<401 :#line:1689
								O0OOOO0O0OOO00000 .append (O000OO0OO0O0OOOO0 ['id'])#line:1690
					if len (O0OOOO0O0OOO00000 )>0 :#line:1693
						sell_cards (O0OOOO0O0OOO00000 )#line:1694
				get_user_info (only_zeni =True )#line:1695
			refresh_client ()#line:1696
	except Exception as O00O000OOO0OOOO00 :#line:1698
		print (Fore .RED +Style .BRIGHT +str (O00O000OOO0OOOO00 ))#line:1699
		print (Fore .RED +Style .BRIGHT +'Trouble finding new Z-Battle events')#line:1700
def set_platform ():#line:1703
	while True :#line:1704
		OO00OOOO0000000OO =input ("'a'|Android -- 'i'|iOS: ")#line:1705
		if OO00OOOO0000000OO [0 ].lower ()in ['a','i']:#line:1706
			if OO00OOOO0000000OO [0 ].lower ()=='a':#line:1707
				c2 .platform ='android'#line:1708
			elif OO00OOOO0000000OO [0 ].lower ()=='i':#line:1709
				c2 .platform ='ios'#line:1710
			else :#line:1711
				continue #line:1712
			break #line:1713
		else :#line:1714
			print (Fore .RED +Style .BRIGHT +'Could not identify correct platform to use.')#line:1715
def list_events ():#line:1718
	O0OO00OO0OOO000O0 =p1 .get ('/events')#line:1719
	OOO000O0OO00000OO =O0OO00OO0OOO000O0 .json ()#line:1720
	O0OOOOOOOOOOOOOOO =None #line:1722
	for O0OOOO0000O0O00O0 in OOO000O0OO00000OO ['events']:#line:1723
		for OO00OOOO000OO00OO in O0OOOO0000O0O00O0 ['quests']:#line:1724
			if str (O0OOOO0000O0O00O0 ['id'])!=O0OOOOOOOOOOOOOOO :#line:1725
				O0OOOOOOOOOOOOOOO =str (O0OOOO0000O0O00O0 ['id'])#line:1726
				OO0OOO00OOO0OOO00 =str (d1 .Areas .get (d1 .Areas .id ==O0OOOOOOOOOOOOOOO ).name )#line:1727
				print ('--------------------------------------------')#line:1728
				print (Back .BLUE +Fore .WHITE +Style .BRIGHT +OO0OOO00OOO0OOO00 )#line:1729
				print ('--------------------------------------------')#line:1730
			OOO00OOOO0O000OOO =OO00OOOO000OO00OO ['id']#line:1732
			OOO0O0OOOOO00OO00 =d1 .SugorokuMaps .select ().where (d1 .SugorokuMaps .quest_id ==int (OOO00OOOO0O000OOO ))#line:1733
			OOO0O0000OOOOOO00 =[]#line:1734
			for OO0OO0O0O00000OO0 in OOO0O0OOOOO00OO00 :#line:1735
				OOO0O0000OOOOOO00 .append (OO0OO0O0O00000OO0 .difficulty )#line:1736
			print (d1 .Quests .get_by_id (OOO00OOOO0O000OOO ).name +' '+str (OOO00OOOO0O000OOO )+' Difficulties: '+str (OOO0O0000OOOOOO00 )+' AreaID: '+str (O0OOOO0000O0O00O0 ['id']))#line:1737
def area_event ():#line:1739
	O0O0O00O0O000O0O0 =input ("What event area would you like to complete?: ")#line:1740
	O0O000OOOO0O0OOOO =p1 .get ('/events')#line:1741
	OO00000O00OOOO0OO =O0O000OOOO0O0OOOO .json ()#line:1742
	OOOO0O0O0O0OOO0OO =None #line:1743
	for O00OOO00O0O00OO0O in OO00000O00OOOO0OO ['events']:#line:1744
		for O0OOOOO00O0O00OO0 in O00OOO00O0O00OO0O ['quests']:#line:1745
			if str (O00OOO00O0O00OO0O ['id'])!=OOOO0O0O0O0OOO0OO :#line:1746
				OOOO0O0O0O0OOO0OO =str (O00OOO00O0O00OO0O ['id'])#line:1747
				O0O0OOO0OOO0OO00O =str (d1 .Areas .get (d1 .Areas .id ==OOOO0O0O0O0OOO0OO ).name )#line:1748
			O00O00O00O00OOO00 =O0OOOOO00O0O00OO0 ['id']#line:1749
			O0O0OO00O0OOO0000 =d1 .SugorokuMaps .select ().where (d1 .SugorokuMaps .quest_id ==int (O00O00O00O00OOO00 ))#line:1750
			OO00O00OOOO000O00 =[]#line:1751
			OOOO0OO0OOOO0000O =[]#line:1752
			for OOOO000OO0OO0O0O0 in O0O0OO00O0OOO0000 :#line:1753
				OO00O00OOOO000O00 .append (OOOO000OO0OO0O0O0 .difficulty )#line:1754
				OOOO0OO0OOOO0000O .append (str (OOOO000OO0OO0O0O0 ))#line:1755
			for O000OOOOOOO0OO0OO in OOOO0OO0OOOO0000O :#line:1756
				if O0O0O00O0O000O0O0 ==str (O000OOOOOOO0OO0OO [0 :3 ]):#line:1757
					try :#line:1758
						O0O00O0O00O00000O =O000OOOOOOO0OO0OO [0 :-1 ]#line:1759
						O0OOOO00OO0OO0O0O =O000OOOOOOO0OO0OO [6 :]#line:1760
						complete_stage (O0O00O0O00O00000O ,O0OOOO00OO0OO0O0O )#line:1761
					except :#line:1762
						pass #line:1763
def complete_potential ():#line:1766
	OO0OOOO0OO0O0000O =p1 .get ('/events')#line:1767
	OO00OOO00O0O0OO00 =OO0OOOO0OO0O0000O .json ()#line:1768
	for O00OOO00OOOO00000 in OO00OOO00O0O0OO00 ['events']:#line:1769
		if 140 <=O00OOO00OOOO00000 ['id']<145 :#line:1770
			for OOOOO00O0O0OO0000 in O00OOO00OOOO00000 ['quests']:#line:1771
				OOOO000OOOOO0O000 =OOOOO00O0O0OO0000 ['id']#line:1772
				OO0000OO0000O0OO0 =d1 .SugorokuMaps .select ().where (d1 .SugorokuMaps .quest_id ==int (OOOO000OOOOO0O000 ))#line:1773
				for O000O00O0O000OOOO in OO0000OO0000O0OO0 :#line:1774
					complete_stage (str (OOOO000OOOOO0O000 ),O000O00O0O000OOOO .difficulty )#line:1775
re_template_filter =re .compile (r'{[^{}]+?}')#line:1779
def list_summons ():#line:1782
	O0O0O00OO00000O0O =p1 .get ('/gashas')#line:1785
	for O0000OO0O0OOOO0O0 in O0O0O00OO00000O0O .json ()['gashas']:#line:1786
		OOO0OOO000OO00000 =O0000OO0O0OOOO0O0 ['name'].replace ('\n',' ').strip ()#line:1787
		print (f'ID: {O0000OO0O0OOOO0O0["id"]} - {OOO0OOO000OO00000}')#line:1788
		if len (O0000OO0O0OOOO0O0 ['description'])>0 :#line:1789
			OO00O00OO00O0O0O0 =re_template_filter .sub ('',O0000OO0O0OOOO0O0 ['description']).replace ('\n',' ').strip ()#line:1790
			print (Fore .YELLOW +'\t'+OO00O00OO00O0O0O0 )#line:1791
def summon_nogui ():#line:1793
	O0OOOO00OO0O00OO0 =input ('[S]ingle or [M]ulti: ')#line:1794
	OO00OO0O0O00OO000 =input ('What banner do you want to summon on: ')#line:1795
	if O0OOOO00OO0O00OO0 .lower ()=='m':#line:1796
		OOOO00OO000000O0O =input ('How many times would you like to do a Multi?: ')#line:1797
	else :#line:1798
		OOOO00OO000000O0O =input ('How many times would you like to do a Single?: ')#line:1799
	O000O0O0OOOO0OOOO =p1 .get ('/gashas')#line:1800
	OO0O00O0O00000OO0 =[]#line:1801
	for O0OOOOO0O00OOOOO0 in O000O0O0OOOO0OOOO .json ()['gashas']:#line:1802
		if str (O0OOOOO0O00OOOOO0 ['id'])==OO00OO0O0O00OO000 :#line:1803
			if str (O0OOOOO0O00OOOOO0 ['id'])=='454':#line:1804
				print (f"Summoning on: Friend-Summon ID: {str(O0OOOOO0O00OOOOO0['id'])}")#line:1805
			else :#line:1806
				print (f"Summoning on: {O0OOOOO0O00OOOOO0['name']} ID: {str(O0OOOOO0O00OOOOO0['id'])}")#line:1807
	if O0OOOO00OO0O00OO0 .lower ()=='m':#line:1808
		try :#line:1809
			for OOOOO0000OO0OOOO0 in range (int (OOOO00OO000000O0O )):#line:1810
				O000O0O0OOOO0OOOO =p1 .post (f'/gashas/{OO00OO0O0O00OO000}/courses/2/draw')#line:1812
				if O000O0O0OOOO0OOOO .json ()['error']['code']=='stone_is_not_enough':#line:1813
					print ("You do not have enough stones.")#line:1814
					return 0 #line:1815
				else :#line:1816
					pass #line:1817
				O0O0OOOOOOOO00OOO =[]#line:1818
				for OOO0O00O0OO0OOOO0 in O000O0O0OOOO0OOOO .json ()['gasha_items']:#line:1819
					OO0O0O0OO0000000O =d1 .Cards .get_by_id (int (OOO0O00O0OO0OOOO0 ['item_id']))#line:1820
					class OOOOOOO0OOOOO0000 (Enum ):#line:1821
						N ,R ,SR ,SSR ,UR ,LR =range (6 )#line:1822
					OOOO0OOO0OOO0O00O =OOOOOOO0OOOOO0000 (OO0O0O0OO0000000O .rarity ).name #line:1824
					class O00O00OO00OOO0O00 (Enum ):#line:1826
						AGL ,TEQ ,INT ,STR ,PHY =range (5 )#line:1827
					OOOO0OO0OOOOOO00O =str (OO0O0O0OO0000000O .element )[-1 ]#line:1829
					OO0O00OOOO0O0OOO0 =O00O00OO00OOO0O00 (int (OOOO0OO0OOOOOO00O )).name #line:1830
					if str (OO0O0O0OO0000000O )in l1 .liste :#line:1831
						O0O0OOOOOOOO00OOO .append (OO0O00OOOO0O0OOO0 +' '+OO0O0O0OO0000000O .name +' '+OOOO0OOO0OOO0O00O +'[LR]')#line:1832
					else :#line:1833
						O0O0OOOOOOOO00OOO .append (OO0O00OOOO0O0OOO0 +' '+OO0O0O0OO0000000O .name +' '+OOOO0OOO0OOO0O00O )#line:1834
				print ('Multi-Summon\nCards: ')#line:1835
				for OOO0O00O0OO0OOOO0 in O0O0OOOOOOOO00OOO :#line:1836
					print (OOO0O00O0OO0OOOO0 )#line:1837
				print ('------------------------------------------')#line:1838
		except Exception as O00O0OO0O0O000OOO :#line:1839
			print (O00O0OO0O0O000OOO )#line:1840
	else :#line:1841
		try :#line:1842
			for OOOOO0000OO0OOOO0 in range (int (OOOO00OO000000O0O )):#line:1843
				O000O0O0OOOO0OOOO =p1 .post (f'/gashas/{OO00OO0O0O00OO000}/courses/1/draw')#line:1845
			O0O0OOOOOOOO00OOO =[]#line:1846
			for OOO0O00O0OO0OOOO0 in O000O0O0OOOO0OOOO .json ()['gasha_items']:#line:1847
				OO0O0O0OO0000000O =d1 .Cards .get_by_id (int (OOO0O00O0OO0OOOO0 ['item_id']))#line:1848
				class OOOOOOO0OOOOO0000 (Enum ):#line:1850
					N ,R ,SR ,SSR ,UR ,LR =range (6 )#line:1851
				OOOO0OOO0OOO0O00O =OOOOOOO0OOOOO0000 (OO0O0O0OO0000000O .rarity ).name #line:1853
				class O00O00OO00OOO0O00 (Enum ):#line:1855
					AGL ,TEQ ,INT ,STR ,PHY =range (5 )#line:1856
				OOOO0OO0OOOOOO00O =str (OO0O0O0OO0000000O .element )[-1 ]#line:1858
				OO0O00OOOO0O0OOO0 =O00O00OO00OOO0O00 (int (OOOO0OO0OOOOOO00O )).name #line:1859
				if str (OO0O0O0OO0000000O )in l1 .liste :#line:1860
					O0O0OOOOOOOO00OOO .append (OO0O00OOOO0O0OOO0 +' '+OO0O0O0OO0000000O .name +' '+OOOO0OOO0OOO0O00O +'[LR]')#line:1861
				else :#line:1862
					O0O0OOOOOOOO00OOO .append (OO0O00OOOO0O0OOO0 +' '+OO0O0O0OO0000000O .name +' '+OOOO0OOO0OOO0O00O )#line:1863
				print ('Single-Summon\nCards: ')#line:1864
			for OOO0O00O0OO0OOOO0 in O0O0OOOOOOOO00OOO :#line:1865
				print (OOO0O00O0OO0OOOO0 )#line:1866
			print ('------------------------------------------')#line:1867
			if 'error'in O000O0O0OOOO0OOOO .json ():#line:1869
				print (O000O0O0OOOO0OOOO .json ())#line:1870
				return 1 #line:1871
		except Exception as O00O0OO0O0O000OOO :#line:1872
			print (O00O0OO0O0O000OOO )#line:1873
def baba_cards ():#line:1875
	OOO0OOO00O0000O00 =p1 .get ('/cards')#line:1877
	OO00OO0O0O00O000O =[]#line:1878
	OO0OOO000OOO00O0O =0 #line:1879
	OOO00OOOOOOO0000O =[]#line:1880
	for O0OOO00OOO0OOO0OO in OOO0OOO00O0000O00 .json ()['cards']:#line:1881
		OO0OO00O0OOOOOOOO =d1 .Cards .get_by_id (O0OOO00OOO0OOO0OO ['card_id']).hp_max #line:1882
		if OO0OO00O0OOOOOOOO ==1 :#line:1883
			continue #line:1884
		if 149 <OO0OO00O0OOOOOOOO <401 :#line:1885
			continue #line:1886
		OOO000O0O0O0O0OOO =d1 .Cards .get_by_id (O0OOO00OOO0OOO0OO ['card_id']).rarity #line:1887
		if str (OOO000O0O0O0O0OOO )=='2':#line:1888
			OO0OOO000OOO00O0O +=1 #line:1889
			OOO00OOOOOOO0000O .append (O0OOO00OOO0OOO0OO ['id'])#line:1890
			if OO0OOO000OOO00O0O ==99 :#line:1891
				break #line:1892
	if OO0OOO000OOO00O0O ==0 :#line:1893
		print ("No cards to baba.")#line:1894
		return 0 #line:1895
	OO0000O0O0O0000OO ='/cards/exchange'#line:1896
	OO0000000OO0OOOO0 ={'card_ids':OOO00OOOOOOO0000O }#line:1899
	OOO0OOO00O0000O00 =p1 .post (OO0000O0O0O0000OO ,data =json .dumps (OO0000000OO0OOOO0 ))#line:1901
	if 'error'in OOO0OOO00O0000O00 .json ():#line:1902
		if OOO0OOO00O0000O00 .json ()['error']['code']=='can_not_destroy_the_card_that_using_team':#line:1903
			print ("There are currently SR Cards in your teams. Please change and try again")#line:1904
			return 0 #line:1905
		elif OOO0OOO00O0000O00 .json ['error']['code']=='can_not_destroy_the_supporter_leader_card':#line:1906
			print ("There are currently SR set as Support Leaders. Please change and try again")#line:1907
			return 0 #line:1908
		else :#line:1909
			print (OOO0OOO00O0000O00 .json ()['error'])#line:1910
			return 0 #line:1911
	print ('Exchanged Cards x'+str (len (OOO00OOOOOOO0000O )))#line:1912
	get_user_info (only_baba =True )#line:1914
def sell_r_and_n ():#line:1916
	OOOOO000OO0OOOO0O =p1 .get ('/cards')#line:1918
	O00O000O000OOOOO0 =[]#line:1919
	OO0O0O00OO0000O0O =0 #line:1920
	O00O00O00O0OO0OOO =[]#line:1921
	for OOOOO0O000O0OO0O0 in OOOOO000OO0OOOO0O .json ()['cards']:#line:1922
		O0OOOO0000OO00O00 =d1 .Cards .get_by_id (OOOOO0O000O0OO0O0 ['card_id']).rarity #line:1923
		if int (O0OOOO0000OO00O00 )==0 or int (O0OOOO0000OO00O00 )==1 :#line:1924
			OO0O0O00OO0000O0O +=1 #line:1925
			O00O00O00O0OO0OOO .append (OOOOO0O000O0OO0O0 ['id'])#line:1926
			if OO0O0O00OO0000O0O ==99 :#line:1927
				break #line:1928
	if OO0O0O00OO0000O0O ==0 :#line:1929
		print ("No cards to Sell.")#line:1930
		return 0 #line:1931
	O0O000OOO00OOO000 ='/cards/sell'#line:1932
	OO000O0O00000OO00 ={'card_ids':O00O00O00O0OO0OOO }#line:1935
	OOOOO000OO0OOOO0O =p1 .post (O0O000OOO00OOO000 ,data =json .dumps (OO000O0O00000OO00 ))#line:1937
	print ('Selling N and R Cards x'+str (len (O00O00O00O0OO0OOO ))+'...')#line:1938
	if 'error'in OOOOO000OO0OOOO0O .json ():#line:1939
		print (OOOOO000OO0OOOO0O .json ()['error'])#line:1940
		return 0 #line:1941
	get_user_info (only_zeni =True )#line:1942
def items_viewer_nogui ():#line:1944
	print ("What Items do you want to display?")#line:1945
	print ("1 | Potential")#line:1946
	print ("2 | Awakening")#line:1947
	print ("3 | Support")#line:1948
	print ("4 | Training")#line:1949
	print ("5 | Treasure")#line:1950
	print ("6 | Special")#line:1951
	O000OOO00O0O0OO00 =input ("Choice: ")#line:1952
	if O000OOO00O0O0OO00 =='1':#line:1953
		OO00OO0O0OOOOOO0O =p1 .get ('/resources/login?potential_items=true')#line:1954
		print ("Potential Items\n---------------------------------")#line:1955
		for O0OO0000OOO00000O in reversed (OO00OO0O0OOOOOO0O .json ()['potential_items']['user_potential_items']):#line:1956
			print (str (d1 .PotentialItems .get_by_id (O0OO0000OOO00000O ['potential_item_id']).name )+' x'+str (O0OO0000OOO00000O ['quantity']))#line:1957
		print ("---------------------------------")#line:1958
	elif O000OOO00O0O0OO00 =='2':#line:1959
		OO00OO0O0OOOOOO0O =p1 .get ('/resources/login?awakening_items=true')#line:1960
		print ("Awakening Items\n---------------------------------")#line:1961
		for O0OO0000OOO00000O in OO00OO0O0OOOOOO0O .json ()['awakening_items']:#line:1962
			print (str (d1 .AwakeningItems .get_by_id (O0OO0000OOO00000O ['awakening_item_id']).name )+' x'+str (O0OO0000OOO00000O ['quantity']))#line:1963
		print ("---------------------------------")#line:1964
	elif O000OOO00O0O0OO00 =='3':#line:1965
		OO00OO0O0OOOOOO0O =p1 .get ('/resources/login?support_items=true')#line:1966
		print ("Support Items\n---------------------------------")#line:1967
		for O0OO0000OOO00000O in OO00OO0O0OOOOOO0O .json ()['support_items']['items']:#line:1968
			print (str (d1 .SupportItems .get_by_id (O0OO0000OOO00000O ['item_id']).name )+' x'+str (O0OO0000OOO00000O ['quantity']))#line:1969
		print ("---------------------------------")#line:1970
	elif O000OOO00O0O0OO00 =='4':#line:1971
		OO00OO0O0OOOOOO0O =p1 .get ('/resources/login?training_items=true')#line:1972
		print ("Training Items\n---------------------------------")#line:1973
		for O0OO0000OOO00000O in OO00OO0O0OOOOOO0O .json ()['training_items']:#line:1974
			print (str (d1 .TrainingItems .get_by_id (O0OO0000OOO00000O ['training_item_id']).name )+' x'+str (O0OO0000OOO00000O ['quantity']))#line:1975
		print ("---------------------------------")#line:1976
	elif O000OOO00O0O0OO00 =='5':#line:1977
		OO00OO0O0OOOOOO0O =p1 .get ('/resources/login?treasure_items=true')#line:1978
		print ("Treasure Items\n---------------------------------")#line:1979
		for O0OO0000OOO00000O in OO00OO0O0OOOOOO0O .json ()['treasure_items']['user_treasure_items']:#line:1980
			print (str (d1 .TreasureItems .get_by_id (O0OO0000OOO00000O ['treasure_item_id']).name )+' x'+str (O0OO0000OOO00000O ['quantity']))#line:1981
		print ("---------------------------------")#line:1982
	elif O000OOO00O0O0OO00 =='6':#line:1983
		OO00OO0O0OOOOOO0O =p1 .get ('/resources/login?special_items=true')#line:1984
		print ("Special Items\n---------------------------------")#line:1985
		for O0OO0000OOO00000O in OO00OO0O0OOOOOO0O .json ()['special_items']:#line:1986
			print (str (d1 .SpecialItems .get_by_id (O0OO0000OOO00000O ['special_item_id']).name )+' x'+str (O0OO0000OOO00000O ['quantity']))#line:1987
		print ("---------------------------------")#line:1988
	else :#line:1989
		print ("Error. Invalid command\n")#line:1990
def sbr_finish ():#line:1992
	O0OOO0OOO0OO00OO0 =710001 #line:1993
	for OO0OOO0O000OOOO0O in range (20 ):#line:1994
		complete_stage (str (O0OOO0OOO0OO00OO0 ),5 )#line:1995
		O0OOO0OOO0OO00OO0 +=1 #line:1996
def bossrush ():#line:1999
	complete_stage ('701001',3 )#line:2000
	complete_stage ('701001',4 )#line:2001
	complete_stage ('701002',4 )#line:2002
	complete_stage ('701002',5 )#line:2003
	complete_stage ('701003',5 )#line:2004
	complete_stage ('701004',5 )#line:2005
	complete_stage ('701005',5 )#line:2006
	complete_stage ('701006',5 )#line:2007
	complete_stage ('701007',5 )#line:2008
	if c2 .client =='japan':#line:2009
		complete_stage ('701008',5 )#line:2010
def identity_crypt (OOO0O00OO0OOO0O0O :Union [bytes ,bytearray ,memoryview ],O000OO0OOOO00OO00 :bool ,device :bool =False )->bytes :#line:2014
	""#line:2020
	OO0OOO00OOOOO0OO0 =b"fe397b1f53008cccf8e8636aad967fbf"#line:2022
	O00OO0OO0O0O0O000 =AES .new (OO0OOO00OOOOO0OO0 ,AES .MODE_ECB )#line:2026
	O0OOO0O0OO00O0OO0 =16 #line:2027
	if O000OO0OOOO00OO00 :#line:2029
		if not device :#line:2030
			OOO0O00OO0OOO0O0O =base64 .b64encode (OOO0O00OO0OOO0O0O )#line:2031
		OOO0O00OO0OOO0O0O =bytearray (OOO0O00OO0OOO0O0O )#line:2033
		if len (OOO0O00OO0OOO0O0O )%O0OOO0O0OO00O0OO0 !=0 :#line:2036
			OOO0OOOOO000O0000 =O0OOO0O0OO00O0OO0 -len (OOO0O00OO0OOO0O0O )%O0OOO0O0OO00O0OO0 #line:2037
			OOO0O00OO0OOO0O0O .extend ([OOO0OOOOO000O0000 ]*OOO0OOOOO000O0000 )#line:2038
		O00OO0O0OO00000O0 =O00OO0OO0O0O0O000 .encrypt (OOO0O00OO0OOO0O0O )#line:2040
		return base64 .b64encode (O00OO0O0OO00000O0 )#line:2041
	else :#line:2042
		OOO0O00OO0OOO0O0O =base64 .b64decode (OOO0O00OO0OOO0O0O )#line:2044
		O00OO0O0OO00000O0 =O00OO0OO0O0O0O000 .decrypt (OOO0O00OO0OOO0O0O )#line:2046
		O00OO0O0OO00000O0 =O00OO0O0OO00000O0 [:-ord (O00OO0O0OO00000O0 [len (O00OO0O0OO00000O0 )-1 :])]#line:2049
		if not device :#line:2051
			return base64 .b64decode (O00OO0O0OO00000O0 )#line:2052
		return O00OO0O0OO00000O0 #line:2053
def acc_load_identify ():#line:2055
	while True :#line:2057
		OOO000OOO000OO0O0 =input ("Please put both files into the userfiles folder, press enter once you've done so...\n")#line:2058
		if os .path .exists ('./userfiles/identifier')and os .path .exists ('./userfiles/device'):#line:2059
			OO0O0O00O00O00000 =input ('What would you like to name the savefile?: ')#line:2060
			while True :#line:2061
				O0OO00O0OOOOOO000 =input ('What OS is the account on?([A]ndroid, [i]OS): ')#line:2062
				if O0OO00O0OOOOOO000 .lower ()=='a':#line:2063
					O0OO00O0OOOOOO000 ='android'#line:2064
					break #line:2065
				elif O0OO00O0OOOOOO000 .lower ()=='i':#line:2066
					O0OO00O0OOOOOO000 ='ios'#line:2067
					break #line:2068
				else :#line:2069
					print (f"Please repeat '{O0OO00O0OOOOOO000}' is not a valid input.")#line:2070
					continue #line:2071
			while True :#line:2072
				OO0O0O000OOOOOO00 =input ('What region is the account on? | [J]apan, [G]lobal?: ')#line:2073
				if OO0O0O000OOOOOO00 .lower ()=='j':#line:2074
					OO0O0O000OOOOOO00 ='japan'#line:2075
					break #line:2076
				elif OO0O0O000OOOOOO00 .lower ()=='g':#line:2077
					OO0O0O000OOOOOO00 ='global'#line:2078
					break #line:2079
				else :#line:2080
					print (f"Please repeat '{OO0O0O000OOOOOO00}' is not a valid input.")#line:2081
					continue #line:2082
			with open ('userfiles/identifier','r')as O000OOOOO0O00000O :#line:2083
				OOO00000OO0O0OOO0 =identity_crypt (O000OOOOO0O00000O .read ().rstrip ().encode (),False ).decode ("utf-8")#line:2084
			with open ('userfiles/device','r')as OOO00OO000OO000O0 :#line:2085
				OOO0O000OOO000O0O =identity_crypt (OOO00OO000OO000O0 .read ().rstrip ().encode (),False ,device =True ).decode ("utf-8")#line:2086
			OOO00O0O000O0O0O0 =open (OO0O0O00O00O00000 ,"w+")#line:2087
			OOO00O0O000O0O0O0 .write (OOO00000OO0O0OOO0 +"\n")#line:2088
			OOO00O0O000O0O0O0 .write ("\n")#line:2089
			OOO00O0O000O0O0O0 .write (OOO0O000OOO000O0O +"\n")#line:2090
			OOO00O0O000O0O0O0 .write (O0OO00O0OOOOOO000 +"\n")#line:2091
			OOO00O0O000O0O0O0 .write (OO0O0O000OOOOOO00 +"\n")#line:2092
			OOO00O0O000O0O0O0 .close ()#line:2093
			os .rename (os .getcwd ()+'/'+OO0O0O00O00O00000 ,os .getcwd ()+'/Saves/'+O0OO00O0OOOOOO000 +'/'+OO0O0O00O00O00000 )#line:2094
			O0000OO00OOO00O00 =input (f"Savefile: '{OO0O0O00O00O00000}'|  for OS: '{O0OO00O0OOOOOO000}' | and Region: '{OO0O0O000OOOOOO00}' created. Load account?(Y/N): \n")#line:2095
			if O0000OO00OOO00O00 .lower ()=='y':#line:2096
				load_account (str (O0OO00O0OOOOOO000 ),str (OO0O0O00O00O00000 ))#line:2097
				break #line:2098
			else :#line:2099
				c2 .relooped =True #line:2100
				break #line:2101
		else :#line:2102
			print (Fore .RED +"Files not found. Please put 'identifier' and 'device' file into the 'userfiles' folder.\n")#line:2103
			continue #line:2104
def daily_login_all_android ():#line:2106
	O0OO0OO0O00OOO000 =os .getcwd ()+'/Saves/android/'#line:2107
	for OOOO00O0OO00O000O in os .listdir (O0OO0OO0O00OOO000 ):#line:2108
		if OOOO00O0OO00O000O =="botdbdownloadglb":#line:2109
			continue #line:2110
		elif OOOO00O0OO00O000O =="botdbdownloadjp":#line:2111
			continue #line:2112
		try :#line:2114
			O00OO0000OO00OOOO =open (O0OO0OO0O00OOO000 +str (OOOO00O0OO00O000O ))#line:2115
			OO0O000O00O00O0O0 =O00OO0000OO00OOOO .read ().strip ().split ()#line:2116
			O00OO0000OO00OOOO .close ()#line:2117
		except :#line:2118
			pass #line:2119
		if 'japan'in OO0O000O00O00O0O0 :#line:2121
			try :#line:2122
				print (f"Savefile: {str(OOOO00O0OO00O000O)} | Region: Japan | OS: Android\n")#line:2123
				c2 .set_japan ()#line:2124
				c2 .client ='japan'#line:2125
				if load_account ('android',str (OOOO00O0OO00O000O )):#line:2126
					daily_login ()#line:2127
					daily_events ()#line:2128
					get_user_info (only_stone =True )#line:2129
					print ("\n")#line:2130
				else :#line:2131
					pass #line:2132
			except :#line:2133
				print (f"Account {OOOO00O0OO00O000O} could not be loaded.")#line:2134
				pass #line:2135
		elif 'global'in OO0O000O00O00O0O0 :#line:2137
			try :#line:2138
				print (f"Savefile: {str(OOOO00O0OO00O000O)} | Region: Global | OS: Android\n")#line:2139
				c2 .set_global ()#line:2140
				c2 .client ='global'#line:2141
				if load_account ('android',str (OOOO00O0OO00O000O )):#line:2142
					daily_login ()#line:2143
					daily_events ()#line:2144
					get_user_info (only_stone =True )#line:2145
					print ("\n")#line:2146
				else :#line:2147
					pass #line:2148
			except :#line:2149
				print (f"Account {OOOO00O0OO00O000O} could not be loaded.")#line:2150
				pass #line:2151
		else :#line:2153
			print (f"No valid os for {OOOO00O0OO00O000O}.")#line:2154
			pass #line:2155
def daily_login_all_ios ():#line:2157
	O000OOOO0O00OOOO0 =os .getcwd ()+'/Saves/ios/'#line:2158
	for OOO0OO00O0000O0OO in os .listdir (O000OOOO0O00OOOO0 ):#line:2159
		try :#line:2160
			O0O0O000O0OO000OO =open (O000OOOO0O00OOOO0 +str (OOO0OO00O0000O0OO ))#line:2161
			OOO0O0O0OOOO0O000 =O0O0O000O0OO000OO .read ().strip ().split ()#line:2162
			O0O0O000O0OO000OO .close ()#line:2163
		except :#line:2164
			pass #line:2165
		if 'japan'in OOO0O0O0OOOO0O000 :#line:2167
			try :#line:2168
				print (f"Savefile: {str(OOO0OO00O0000O0OO)} | Region: Japan | OS: iOS\n")#line:2169
				c2 .set_japan ()#line:2170
				c2 .client ='japan'#line:2171
				if load_account (c2 .platform ,str (OOO0OO00O0000O0OO )):#line:2172
					daily_login ()#line:2173
					daily_events ()#line:2174
					get_user_info (only_stone =True )#line:2175
					print ("\n")#line:2176
				else :#line:2177
					pass #line:2178
			except :#line:2179
				print (f"Account {OOO0OO00O0000O0OO} could not be loaded.")#line:2180
				pass #line:2181
		elif 'global'in OOO0O0O0OOOO0O000 :#line:2183
			try :#line:2184
				print (f"Savefile: {str(OOO0OO00O0000O0OO)} | Region: Global | OS: iOS\n")#line:2185
				c2 .set_global ()#line:2186
				c2 .client ='global'#line:2187
				if load_account (c2 .platform ,str (OOO0OO00O0000O0OO )):#line:2188
					daily_login ()#line:2189
					daily_events ()#line:2190
					get_user_info (only_stone =True )#line:2191
					print ("\n")#line:2192
				else :#line:2193
					pass #line:2194
			except :#line:2195
				print (f"Account {OOO0OO00O0000O0OO} could not be loaded.")#line:2196
				pass #line:2197
		else :#line:2199
			print (f"No valid os for {OOO0OO00O0000O0OO}.")#line:2200
			pass #line:2201
def daily_events ():#line:2203
		complete_stage ('130001',0 )#line:2204
		complete_stage ('131001',0 )#line:2205
		complete_stage ('132001',0 )#line:2206
		complete_potential ()#line:2207
		accept_gifts ()#line:2208
		accept_missions ()#line:2209
def discl ():#line:2211
	print (Fore .RED +'\n----------Dokka'+'n Batt'+'le Bot - by Kar'+'yonix and Thie'+'ving'+'Si'+'x---------')#line:2212
	print (Back .GREEN +'---------------Version 4.2 : The YOSHA Update----------------\n')#line:2213
	print ("----------")#line:2214
	print (Back .CYAN +'Old Code licensed under: GNU General Public License v3.0')#line:2215
	print (Back .CYAN +'New Code licensed under: Apache License 2.0')#line:2216
	print (Back .RED +'This is a fr'+'ee bot if you pa'+'id for it, imme'+'diately ask for your money back.')#line:2217
	print ("----------")#line:2218
dil ='h'+'t'+'tp'+'s:'+'//'+'d'+'i'+'s'+'co'+'rd'+'.g'+'g/'+'5'+'Z'+'K'+'A'+'D'+'E'+'q'#line:2219
def view_cards ():#line:2223
	print (Fore .CYAN +Style .BRIGHT +'Fetching user cards..')#line:2225
	O000OO0O0000OO000 =p1 .get ('/cards')#line:2226
	OOOO000OOOO00OOOO =O000OO0O0000OO000 .json ()['cards']#line:2227
	print (Fore .GREEN +Style .BRIGHT +'Done..')#line:2228
	print (Fore .CYAN +Style .BRIGHT +'Fetching card attributes..')#line:2231
	OOO0O0O0O0O00OO0O =[]#line:2232
	for O00O0OO000O00O0O0 in OOOO000OOOO00OOOO :#line:2233
		O00O00O0O00OO0OOO =d1 .Cards .get_by_id (O00O0OO000O00O0O0 ['card_id'])#line:2234
		class O00000OOO00O000O0 (Enum ):#line:2236
			N ,R ,SR ,SSR ,UR ,LR =range (6 )#line:2237
		OO0O0OO0OO00O0O0O =O00000OOO00O000O0 (O00O00O0O00OO0OOO .rarity ).name #line:2239
		class OO00OOO00OOOO00OO (Enum ):#line:2241
			AGL ,TEQ ,INT ,STR ,PHY =range (5 )#line:2242
		O00O0O0OO000OO00O =str (O00O00O0O00OO0OOO .element )[-1 ]#line:2245
		O00O00OOOOOOO00OO =OO00OOO00OOOO00OO (int (O00O0O0OO000OO00O )).name #line:2246
		OOO0O0O0O0O00OO0O .append ({'ID':O00O00O0O00OO0OOO .id ,'Rarity':OO0O0OO0OO00O0O0O ,'Name':O00O00O0O00OO0OOO .name ,'Type':O00O00OOOOOOO00OO ,'Cost':O00O00O0O00OO0OOO .cost ,'UniqueID':O00O0OO000O00O0O0 ['id']})#line:2255
	print (Fore .GREEN +Style .BRIGHT +"Done..")#line:2256
	print (Fore .CYAN +Style .BRIGHT +"Sorting cards..")#line:2259
	OOO0O0O0O0O00OO0O =sorted (OOO0O0O0O0O00OO0O ,key =lambda OO00O0000OO0O00O0 :OO00O0000OO0O00O0 ['Name'])#line:2260
	OOO0O0O0O0O00OO0O =sorted (OOO0O0O0O0O00OO0O ,key =lambda OO0OOOOO00OO0OO0O :OO0OOOOO00OO0OO0O ['Rarity'])#line:2261
	OOO0O0O0O0O00OO0O =sorted (OOO0O0O0O0O00OO0O ,key =lambda O00O0OO000000O0O0 :O00O0OO000000O0O0 ['Cost'])#line:2262
	print (Fore .GREEN +Style .BRIGHT +"Done..")#line:2263
	OOO0O0O00O00OOOO0 =[]#line:2265
	OO0O0O000OOO000O0 =[]#line:2266
	for O00OO0O00O0O00O00 in OOO0O0O0O0O00OO0O :#line:2268
		OOO0O0O00O00OOOO0 .append (O00OO0O00O0O00O00 )#line:2269
		OO0O0O000OOO000O0 .append (str (O00OO0O00O0O00O00 ['Type']+' '+O00OO0O00O0O00O00 ['Rarity']+' '+O00OO0O00O0O00O00 ['Name']+' | '+str (O00OO0O00O0O00O00 ['ID'])))#line:2270
	O0OO000OO0O0000OO =[]#line:2271
	for O00OO0O00O0O00O00 in OO0O0O000OOO000O0 :#line:2272
		if O00OO0O00O0O00O00 not in O0OO000OO0O0000OO :#line:2273
			O0OO000OO0O0000OO .append (O00OO0O00O0O00O00 +' x'+str (OO0O0O000OOO000O0 .count (O00OO0O00O0O00O00 )))#line:2274
	O0OO000OO0O0000OO =list (dict .fromkeys (O0OO000OO0O0000OO ))#line:2275
	for OOO0OO000OOO0000O in O0OO000OO0O0000OO :#line:2276
		print (OOO0OO000OOO0000O )