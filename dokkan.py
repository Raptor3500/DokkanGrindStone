import sys #line:1
import os #line:2
from colorama import init ,Fore ,Style ,Back #line:3
import webbrowser #line:4
import c1 #line:5
import c2 #line:6
init (autoreset =True )#line:9
c1 .discl ()#line:10
while True :#line:12
	try :#line:14
		os .mkdir ('userfiles')#line:15
	except OSError as exc :#line:16
		pass #line:17
	if c2 .relooped is False :#line:18
		dldb =input ("Would you like to download the latest DB?\nMust-do on first Start!!!\nPress any key to continue, for download press 'y': ")#line:19
		if dldb .lower ()=='y':#line:20
			c1 .db_download ()#line:21
	else :#line:22
		print ('Exiting...\n-------------------------------')#line:23
	while True :#line:25
		client =input ("Japan or Global? J/G: ")#line:26
		if client .lower ()=='j':#line:27
			c2 .set_japan ()#line:28
			break #line:29
		elif client .lower ()=='g':#line:30
			c2 .set_global ()#line:31
			break #line:32
		else :#line:33
			continue #line:34
	while True :#line:36
		print (Back .RED +Style .BRIGHT +'\n0: New Account\n1: Transfer Account To The Bot\n2: Continue with Current Account\n3: List your Savefiles\n4: Rename a Savefile\n5: Make Save from device/identifier\n6: Do a daily on all accounts (Android and iOS)\n'+Back .YELLOW +Style .BRIGHT +'7: Join my Discord\n'+Style .RESET_ALL +'\nType "exit" to terminate\n')#line:37
		command =input ('Enter a choice ->: ')#line:38
		if command =='0':#line:39
			c2 .identifier =c1 .signup ()#line:40
			c1 .save_account ()#line:41
			c2 .access_token ,c2 .secret =c1 .signin (c2 .identifier ,c2 .UniqueId ,c2 .AdId )#line:42
			c1 .tutorial ()#line:43
			c1 .daily_login ()#line:44
			break #line:45
		elif command =='1':#line:46
			c1 .transfer_account ()#line:47
			c1 .daily_login ()#line:48
			break #line:49
		elif command =='2':#line:50
			c1 .load_account ()#line:51
			c1 .daily_login ()#line:52
			break #line:53
		elif command =='3':#line:54
			c1 .list_save_files ()#line:55
		elif command =='4':#line:56
			c1 .rename_save ()#line:57
		elif command =='5':#line:58
			c1 .acc_load_identify ()#line:59
			if not c2 .relooped :#line:60
				break #line:61
		elif command =='6':#line:62
			original_client =c2 .client #line:63
			c1 .daily_login_all_android ()#line:64
			original_platform =c2 .platform #line:65
			c2 .platform ='ios'#line:66
			c1 .daily_login_all_ios ()#line:67
			c2 .platform =original_platform #line:68
			c2 .client =original_client #line:69
		elif command =='7':#line:70
			webbrowser .open (c1 .dil ,new =0 ,autoraise =True )#line:71
		else :#line:72
			print ("Command not understood")#line:73
	while True :#line:76
		print ('---------------------------------')#line:77
		print ("Type"+Fore .YELLOW +Style .BRIGHT +" 'help'"+Style .RESET_ALL +" to view all commands.")#line:78
		try :#line:81
			command =input ()#line:82
		except :#line:83
			sys .stdin =sys .__stdin__ #line:84
			command =input ()#line:85
		if command =='exit':#line:87
			c2 .relooped =True #line:88
			break #line:89
		try :#line:91
			c1 .user_command_executor (command )#line:92
		except KeyboardInterrupt :#line:93
			print (Fore .CYAN +Style .BRIGHT +'User interrupted process.')#line:94
