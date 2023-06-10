# README (ниже на русском языке)

Python script that allows you to use the site stepik.org as a cloud for files (up to 500 MB per file).

## Requirements
- Python 3.x
- requests
- getpass
- sys
- os
- json
- wget
- split_file (custom module)
- merge_file (custom module)

## Installation
1. Clone this repository to your local machine.
2. Install the required dependencies by running the following command:
   ```
   pip install requests getpass wget
   ```
   
## Usage
1. Run the script using the command:
   ```
   python main.py
   ```
2. The script will prompt you to enter your Stepik.org account email and password for authentication.
3. Choose whether you want to upload a file or download a file:
   - Enter `0` to upload a file.
   - Enter `1` to download a file.
4. If you chose to upload a file:
   - Enter the path to the file you want to upload or provide the file name if it's in the same folder as the script.
   - If the file is larger than 25MB, it will be split into smaller parts for upload. You will be prompted to enter the ID of the lesson you want to upload the file to.
   - The script will start the upload process, displaying progress for each part if applicable.
   - Once the upload is complete, you will see a success message.
5. If you chose to download a file:
   - The script will retrieve a list of available attachments from Stepik.org.
   - You will be presented with a list of attachments with corresponding IDs.
   - Enter the ID of the file you want to download. If the file is split into multiple parts, you can choose any part.
   - The script will download the file or the corresponding parts if necessary and save it to the current directory.
   - If the file was split into parts, the script will merge them into a single file.
6. The process is complete, and you can now use the downloaded or uploaded file.

Note: Make sure you have a stable internet connection and proper authentication credentials before using the script.

Feel free to contribute to this repository by creating pull requests or reporting issues.



# README (на русском языке)

В этом репозитории содержится скрипт на языке Python, который позволяет использовать сайт stepik.org как облако для файлов (до 500 Мб на один файл).

## Требования
- Python 3.x
- requests
- getpass
- sys
- os
- json
- wget
- split_file (пользовательский модуль)
- merge_file (пользовательский модуль)

## Установка
1. Клонируйте данный репозиторий на свой компьютер.
2. Установите необходимые зависимости, выполнив следующую команду:
   ```
   pip install requests getpass wget
   ```
   
## Использование
1. Запустите скрипт с помощью следующей команды:
   ```
   python main.py
   ```
2. Скрипт попросит вас ввести электронную почту и пароль вашей учетной записи Stepik.org для аутентификации.
3. Выберите, хотите ли вы загрузить файл или скачать файл:
   - Введите `0`, чтобы загрузить файл.
   - Введите `1`, чтобы скачать файл.
4. Если вы выбрали загрузку файла:
   - Введите путь к файлу, который вы хотите загрузить, или введите название файла, если он находится в той же папке, что и скрипт.
   - Если размер файла превышает 25 МБ, он будет разделен на более мелкие части для загрузки. Вам будет предложено ввести идентификатор урока, в который вы хотите загрузить файл.
   - Скрипт начнет процесс загрузки и будет отображать прогресс для каждой части, если это применимо.
   - После завершения загрузки вы увидите сообщение об успешном выполнении.
5. Если вы выбрали скачивание файла:
   - Скрипт получит список доступных вложений на Stepik.org.
   - Вам будет предоставлен список вложений с соответствующими идентификаторами.
   - Введите идентификатор файла, который вы хотите скачать. Если файл разделен на несколько частей, вы можете выбрать любую часть.
   - Скрипт загрузит файл или соответствующие части при необходимости и сохранит их в текущей директории.
   - Если файл был разделен на части, скрипт объединит их в один файл.
6. Процесс завершен, и вы можете использовать скачанный или загруженный файл.

Примечание: Убедитесь, что у вас стабильное интернет-соединение и правильные учетные данные для аутентификации перед использованием скрипта.

Вы можете вносить свой вклад в этот репозиторий, создавая pull-запросы или сообщая об ошибках.
