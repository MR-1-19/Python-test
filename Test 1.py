from rembg import remove
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Создаем корневое окно Tkinter
root = Tk()
root.withdraw()  # Скрываем корневое окно

# Запрашиваем у пользователя путь к файлу
input_path = askopenfilename(parent=root,
                             title='Выбрать фото',
                             filetypes=[('PNG image', '.png'), ('JPEG image', '.jpeg')])

if input_path:
    output_path = 'image_output.png'
    open_image = Image.open(input_path)
    output = remove(open_image)
    output.save(output_path)
    print("Изображение успешно обработано и сохранено как", output_path)
else:
    print("Выбор файла отменен")

# Закрываем корневое окно Tkinter
root.destroy()
