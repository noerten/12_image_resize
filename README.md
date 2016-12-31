# 12_image_resize
Консольный скрипт, предназначенный для изменения размера изображения посредством передачи аргументов.

## Как использовать:
* Установить зависимости `pip install -r requirements.txt`. 
* В консоли выполнить `python3 image_resize.py some_folder/image.xxx --width --height --scale --output`, где:
  - `some_folder/image.xxx` - путь к изображению (с его расширением).
  - `--width --height` - ширина, длина конечного изображения. Если указан только один аргумент, то изображение будет отмаштабировано по этому параметру.
  - `--scale` - масштаб, не может быть указан совместно с предыдущими параметрами.
  - `--output` - путь к конечному изображению, если не указан, изображение будет помещено рядом с исходым.




