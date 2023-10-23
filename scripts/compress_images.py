from PIL import Image
import os

def rename_files_replace_spaces(filepath='./projects'):
    for root, _, _ in os.walk(filepath):
        if root != filepath:
            for item in os.listdir(root):
                # item_path = os.path.join(root, item)
                if ' ' in item:
                    new_filename = item.replace(' ', '_')

                    old_filepath = os.path.join(root, item)
                    new_filepath = os.path.join(root,  new_filename)

                    os.rename(old_filepath, new_filepath)
                    print(f'Renamed: {item} -> {new_filename}')

rename_files_replace_spaces()



def compress_images(filepath="/projects", quality=10):
    for root, _, _ in os.walk(filepath):
        if root != filepath:

            for item in os.listdir(root):
                if item.lower().endswith(".png"):
                    input_path = os.path.join(root, item)
                    output_path = os.path.join(root, item)

                    quality = 10
                    img = Image.open(input_path)
                    print('saving', output_path)
                    img.save(output_path, optimize=True, quality=quality)


def resize(image_file, width, height):
    '''
    Resize PIL image keeping ratio and using white background.
    '''

    image_pil = Image.open(image_file)  

    ratio_w = width / image_pil.width
    ratio_h = height / image_pil.height

    if ratio_w < ratio_h:
        # It must be fixed by width
        resize_width = width
        resize_height = round(ratio_w * image_pil.height)
    else:
        # Fixed by height
        resize_width = round(ratio_h * image_pil.width)
        resize_height = height

    image_resize = image_pil.resize((resize_width, resize_height), Image.LANCZOS)
    background = Image.new('RGBA', (width, height), (255, 255, 255, 255))
    offset = (round((width - resize_width) / 2), round((height - resize_height) / 2))
    background.paste(image_resize, offset)

    save_path = os.path.splitext(image_file)[0]+'_titlecard' + os.path.splitext(image_file)[1]

    background.convert('RGB').save(save_path)

    return save_path