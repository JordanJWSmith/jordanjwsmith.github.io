from PIL import Image
import os


def compress_images(filepath="/projects", quality=10):
    for root, _, _ in os.walk(filepath):
        if root != filepath:

            for item in os.listdir(root):
                if item.lower().endswith(".png"):
                    # print('image: ', item)
                    input_path = os.path.join(root, item)
                    output_path = os.path.join(root, f'compressed_{item}')
                    # print('image: ', output_path)

                    quality = 10
                    # # Open the image and save it with the specified quality
                    img = Image.open(input_path)
                    print('saving', output_path)
                    img.save(output_path, optimize=True, quality=quality)

compress_images()