import os, sys, yaml, platform, argparse
from pyfiglet import Figlet


# Args 
def get_args():
	''' Add args '''
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'-c', '--chat', 
		dest = 'chat',
		help = 'Chat (name or id)')
	options = parser.parse_args()
	return options


# Create folder
def folder(name):
	''' If there is no {name} folder, create a folder '''
	path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../'+name)
	if not os.path.exists(path):
		os.mkdir(path)


# Files extension
def extension():
	''' Return file and file's format '''
	for root, dirs, files in os.walk("."):  
		for filename in files:
			match (filename.split('.')[-1]).lower():
				case 'jpg' | 'png' | 'jpeg'| 'gif'| 'ico'| 'pcx'| 'psd'| 'bpm'| 'ecw'| 'ilbm'| 'xbm'| 'xps':
					return f'image:{filename}'
				case 'mp4' | 'mov' | 'webm' | 'wmv' | 'avi' | 'flv' | 'mkv':
					return f'video:{filename}'


# TG Account Data  
def data(number):
	''' Return TG Account Data in "config.yml" '''
	try:
		with open('./data/config.yml') as f:
			data = yaml.safe_load(f)
		return data[number]
	except KeyError :
		print('[\033[31m!\033[00m] ~ \033[31mAccounts ended\033[00m')
		sys.exit()


# Push Message
def push(title, message):
	''' Output Push Message '''
	match platform.system():
		case 'Darwin':
			command = '''
				osascript -e 'display notification "{message}" with title "{title}"'
				'''
		case 'Linux':
			command = f'''
				notify-send "{title}" "{message}"
				'''
		case 'Windows':
			win10toast.ToastNotifier().show_toast(title, message)
			return
		case _:
			return
	os.system(command)


# Banner
def banner(chat):
	''' Output banner '''
	baner = Figlet(font='5lineoblique')
	print(f'\033[36m{baner.renderText("TGSpam")}\033[00m')
	print('\t Made by \033[34mhttps://github.com/Kigrok\033[00m')
	print('-' * 30)
	print(f'\033[34mhttps://t.me/{chat}\033[00m')
	print('-' * 30)


# Clear Chat Name
def clear(name):
	''' Return Chat Name by Link '''
	if 'https://t.me/' in name:
		return name.split('https://t.me/')[1]
	else:
		return name
