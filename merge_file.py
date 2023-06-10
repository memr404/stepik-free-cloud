import os

def merge_file(file_prefix, output_path):
	with open(output_path, 'wb') as output_file:
		i = 0
		while True:
			chunk_filename = f'{file_prefix}.part{i}'
			if not os.path.exists(chunk_filename):
				break

			with open(chunk_filename, 'rb') as chunk_file:
				chunk_data = chunk_file.read()
				output_file.write(chunk_data)
				print(f'Добавлен {chunk_filename} к итоговому файлу')
			os.remove(chunk_filename)
			i += 1

	print('Слияние завершено!')

if __name__ == '__main__':
	# Ввод префикса имени файлов
	file_prefix = input('Введите префикс имени файлов (без суффикса .partX): ')

	# Ввод пути для сохранения объединенного файла
	output_path = input('Введите путь для сохранения объединенного файла: ')

	# Объединение файлов
	merge_file(file_prefix, output_path)
