import argparse
import os

from PIL import Image


def image_argparser():
    parser = argparse.ArgumentParser(description='Resize some images.')
    parser.add_argument("image_path", help="Path to image you want to resize")
    parser.add_argument("--width", type=int, help="Width of resulting image")
    parser.add_argument("--height", type=int, help="Height of resulting image")
    parser.add_argument("--scale", type=float,
                        help="How much to scale resulting image")
    parser.add_argument("--output", help="Path to resulting image")
    arguments = parser.parse_args()
    print(arguments.image_path)
    if (arguments.width or arguments.height) and not arguments.scale:
        if arguments.width:
            print(arguments.width)
        if arguments.height:
            print(arguments.height)
    elif arguments.scale and not (arguments.width or arguments.height):
        print(arguments.scale)
    elif arguments.scale and (arguments.width or arguments.height):
        message = 'You cannot use size arguments and scale argument together'
        parser.error(message)
    if arguments.output:
        print(arguments.output)


def get_image(filepath):
    if not os.path.exists(filepath):
        return None
    return Image.open(filepath)


def save_image(image, filepath):
    try:
        image.save(filepath)
    except IOError:
        print("cannot save to disk", filepath)


def set_path_to_result(path_to_original, resulting_size):
    path_without_name, original_name = os.path.split(
        path_to_original)
    original_name_without_extension, extension = os.path.splitext(
        original_name)
    resulting_name = ''.join([original_name_without_extension, '__',
                              str(resulting_size[0]), 'x',
                              str(resulting_size[1])]) + extension
    return os.path.join(path_without_name, resulting_name)


def print_ratio_if_incorrect(original_size, resulting_size):
    original_ratio = original_size[0]/original_size[1]
    resulting_ratio = resulting_size[0]/resulting_size[1]
    if original_ratio != resulting_ratio:
        message = "Original ratio {} isn't equal to resulting ratio {}".format(
            original_ratio, resulting_ratio)
        print(message)


def resize_image_with_new_width_and_height(original_image, resulting_size):
    print_ratio_if_incorrect(original_image.size, resulting_size)
    return original_image.resize(resulting_size)


def resize_image_with_new_width_or_height(original_image, resulting_size):
    if resulting_size[0] is not None:
        resulting_height = (resulting_size[0]*original_image.size[1] /
                            original_image.size[0])
        resulting_size = (resulting_size[0], resulting_height)
    else:
        resulting_width = (resulting_size[1] * original_image.size[0] /
                           original_image.size[1])
        resulting_size = resulting_width, resulting_size[1]
    original_image.thumbnail(resulting_size)
    return original_image


def resize_image_scale(original_image, scale):
    resulting_size = (int(original_image.size[0]*scale),
                      int(original_image.size[1]*scale))
    if scale < 1:
        original_image.thumbnail(resulting_size)
        return original_image
    else:
        return original_image.resize(resulting_size)


def resize_image(path_to_original, resulting_size, scale, path_to_result):
    original_image = get_image(path_to_original)
    if (resulting_size[0] and resulting_size[1]) is not None:
        resulting_image = resize_image_with_new_width_and_height(
            original_image, resulting_size)
    elif (resulting_size[0] or resulting_size[1]) is not None:
        resulting_image = resize_image_with_new_width_or_height(original_image,
                                                                resulting_size)
    elif scale is not None:
        resulting_image = resize_image_scale(original_image, scale)
        print(resulting_image)
    else:
        resulting_image = original_image
    if path_to_result is None:
        path_to_result = set_path_to_result(path_to_original,
                                            resulting_image.size)
    save_image(resulting_image, path_to_result)
    print('image resized!')


def temp_argparse(image_path='1.png', width=None, height=None, scale=None,
                  output=None):
    if not (scale and (width or height)):
        resulting_size = (width, height)
        resize_image(image_path, resulting_size, scale, output)
    else:
        message = 'You cannot use size arguments and scale argument together'
        print(message)


if __name__ == '__main__':
    # image_argparser()
    temp_argparse(image_path='1\\1.png', width=None, height=None, scale=2.5,
                  output='1\\3.png')
