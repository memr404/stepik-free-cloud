import requests, getpass, sys, os, json, wget
from split_file import split_file
from merge_file import merge_file

s = requests.Session()
url = 'https://stepik.org/api/'


# Авторизация
response = s.get('https://stepik.org/catalog?auth=login')
csrf_token = response.cookies['csrftoken']  # Получение CSRF-токена из cookies

headers = {
	'Referer': 'https://stepik.org/catalog?auth=login',
	'X-CSRFToken': csrf_token,
}

with open('user_data.json', 'r') as file:
	data = json.loads(file.read())
	email = data['email']
	password = data['password']
if email == '' or password == '':
	print('Файл user_data.json не заполнен')
	datas = {
		'email': input('Введите почту от аккаунта: '),
		'password': getpass.getpass('Введите пароль: ')
	}
else:
	datas = {
		'email': email,
		'password': password
	}
login = s.post(url+'users/login',data=datas,headers=headers)

if login.status_code == 204:
	print('Вы успешно вошли в аккаунт!')
else:
	print('Неверный логин или пароль!')
	sys.exit()

chose = input('Вы хотите загрузить файл или скачать? (Загрузить - 0, Скачать - 1) > ')

if chose == '0':
	path = input('Введите путь до файла (или название файла если он в одной папке с программой) > ')
	try:
		size = os.path.getsize(path)
	except FileNotFoundError:
		print('Файл не найден!')
		sys.exit()

	split = False

	if size < 26214400:
		print('Файл выбран!')
	elif size >= 26214400 and size < 523239424: # 25 Мб и 500 Мб
		split = True
		print('Файл больше 25 Мб, необходимо его разделить!')
		chunk_size = 24 * 1024 * 1024
		chunks = split_file(path, chunk_size)
	else:
		print('Файл больше 500 Мб!')
		sys.exit()


	while True:
		try:
			id_lesson = int(input('Введите id урока для загрузки (укажите 0 чтобы запросить все id): '))
		except ValueError:
			print('Неверный тип!')
			sys.exit()
		if id_lesson == 0:
			spisok = []
			zapr_les = 'https://stepik.org/api/user-lessons?is_moderator=true&order=-is_pinned%2C-last_viewed'
			ids = s.get(zapr_les)
			ids = ids.text
			ids = json.loads(ids)
			for i in range(len(ids['user-lessons'])):
				spisok.append(ids['user-lessons'][i]['lesson'])

			print('ID уроков:')
			for idd in spisok:
				print(idd)
			continue
		else:
			break


	# Загрузка файла

	response = s.get(f'https://stepik.org/edit-lesson/{id_lesson}/step/1?is_show_attachments=true')
	csrf_token = response.cookies['csrftoken']  # Получение CSRF-токена из cookies

	headers = {
		'Referer': f'https://stepik.org/edit-lesson/{id_lesson}/step/1?is_show_attachments=true',
		'X-CSRFToken': csrf_token,
	}
	print('Загрузка...')
	if split:
		for i in range(chunks):
			with open(path+f'.part{i}', 'rb') as f:
				dats = {
					'file': f
				}
				dataa = {
					'lesson': str(id_lesson)
				}
				r = s.post(url+'attachments', files=dats, data=dataa, headers=headers)
			if r.status_code == 201:
				print(f'Файл {i+1} успешно загружен!')
			else:
				print(f'Ошибка на {i+1} файле\n{r.status_code}')

	else:
		with open(path, 'rb') as f:
			dats = {
				'file': f
			}
			dataa = {
				'lesson': str(id_lesson)
			}
			r = s.post(url+'attachments', files=dats, data=dataa, headers=headers)

		if r.status_code == 201:
			print('Файл успешно загружен!')
		else:
			print(f'Ошибка {r.status_code}')
elif chose == '1':
	ids = s.get('https://stepik.org/api/attachments')
	ids = ids.text
	ids = json.loads(ids)
	for i in range(len(ids['attachments'])):
		print(f"{i} - {ids['attachments'][i]['name']}")
	try:
		id_target = int(input('\nУкажите id файла (если файл поделен на части, то укажите любую часть этого файла): '))
	except ValueError:
		print('Ошибка!')
		sys.exit()
	try:
		name = ids['attachments'][id_target]['name']
	except:
		print('Ошибка!')
		sys.exit()
	if '.part' in name:
		files = []
		true_name = name.split('.part')[0]
		for attachment in ids["attachments"]:
			if "name" in attachment and "file" in attachment:
				if true_name in attachment["name"]:
					files.append(attachment["file"])
		for file in files:
			print(file)
			wget.download('https://stepik.org/'+file)

		merge_file(true_name,true_name)
	else:
		wget.download('https://stepik.org/'+ids['attachments'][id_target]['file'])
else:
	sys.exit()
