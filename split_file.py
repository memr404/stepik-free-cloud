import os

def split_file(file_path, chunk_size):
	file_size = os.path.getsize(file_path)
	total_chunks = file_size // chunk_size + 1
	
	with open(file_path, 'rb') as file:
		for i in range(total_chunks):
			chunk_data = file.read(chunk_size)
			if not chunk_data:
				break
			
			chunk_filename = f'{file_path}.part{i}'
			with open(chunk_filename, 'wb') as chunk_file:
				chunk_file.write(chunk_data)
			print(f'Сохранён {chunk_filename}')
	
	print('Разделение успешно!')
	return total_chunks
if __name__ == '__main__':

	# Ввод пути к файлу
	file_path = input('Введите путь до файла: ')

	# Ввод размера части в МБ
	chunk_size = 24 * 1024 * 1024

	# Разделение файла
	split_file(file_path, chunk_size)
