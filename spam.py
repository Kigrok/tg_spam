from pyrogram.errors import FloodWait, PeerIdInvalid, UserDeactivatedBan, PeerFlood
from data.message import message
import asyncio, json, time
from pyrogram import Client
from data.func import *


# Get Chat Members
async def chat_member(chat):
	''' Get User Id in Chat'''
	try:
		print(f'[\033[33m{data(0)["app_title"]}\033[00m]\t\033[33mSave Members\033[00m')
		async with Client(
			name=data(0)['app_title'], 
			api_id=data(0)['api_id'], 
			api_hash=data(0)['api_hash'], 
			workdir='./sessions') as app:
			try:
				async for member in app.get_chat_members(chat):
					user = (json.loads(str(member)))['user']
					if user['is_bot'] == False and user['is_deleted'] == False:
						with open(f'./users/{chat}.txt', 'a') as file:
							file.write(f'{user["id"]}\n')
							print(f'[\033[32m+\033[00m] ~ \033[35m{user["id"]}\033[00m', end='\r')
				print(f'\n[\033[32m!\033[00m] ~ \033[32mAll members in {chat} save in file\033[00m')
			except FloodWait as e:
				time.sleep(e.x)
	except FloodWait as e:
		await asyncio.sleep(e.value)


# Get User and Send Message
async def send_message_to_user(name):
	''' Get all users in "{name}.txt" and send messages '''
	number = 0
	with open(f'./users/{name}.txt') as file:
		for index, user in enumerate(file):
			if index%15 == 0: time.sleep(10)
			match await send_message(user_id=user.strip(), number=number):
				case False:
					number +=1
					push(title='New Account', message=f'Account connection: {data(number)["app_title"]}')


# Send Message
async def send_message(user_id, number):
	''' Send message to user '''
	try:
		print(f'[\033[33m{data(number)["app_title"]}\033[00m]\t\033[33mSend Messages\033[00m')
		async with Client(
			name=data(number)['app_title'], 
			api_id=data(number)['api_id'], 
			api_hash=data(number)['api_hash'], 
			workdir='./sessions') as app:
			match str(extension()).split(':')[0]:
				case 'image':
					await app.send_photo(int(user_id), f'./data/{str(extension()).split(":")[1]}', caption=message)
				case 'video':
					await app.send_video(int(user_id), f'./data/{str(extension()).split(":")[1]}', caption=message)
				case _:
					await app.send_message(int(user_id), message)
			print(f'[\033[34mSend\033[00m] ~ \033[35m{user_id}\033[00m', end='\r')
	except FloodWait as e:
		await asyncio.sleep(e.value)
	except PeerIdInvalid:
		print(f'\n[\033[31m{data(number)["app_title"]}\033[00m] ~ \033[31mAccount is Blocked!\033[00m')
		return False
	except PeerFlood as e:
		print(f'\n[\033[31m{data(number)["app_title"]}\033[00m] ~ \033[31mSending messages is prohibited!\033[00m')
		return False
	except TypeError:
		return False


async def main():
	folder('sessions')
	folder('users')
	banner(clear(get_args().chat))
	await chat_member(clear(get_args().chat))
	await send_message_to_user(clear(get_args().chat))


if __name__ == '__main__':
	asyncio.run(main())
