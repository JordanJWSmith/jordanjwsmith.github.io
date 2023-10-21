from PIL import Image
import os

def rename_files_replace_spaces(filepath='/projects'):
    for root, _, _ in os.walk(filepath):
        if root != filepath:
            for item in os.listdir(root):
                item_path = os.path.join(root, item)
                if ' ' in item:
                    new_filename = item.replace(' ', '_')
                    # Construct the full paths for the old and new filenames
                    old_filepath = os.path.join(item_path, item)
                    new_filepath = os.path.join(item_path,  new_filename)
                    # Rename the file
                    os.rename(old_filepath, new_filepath)
                    # print(f'Renamed: {item} -> {new_filename}')


                # if os.path.isdir(item_path):
                    # print(item_path)
                    # print(os.listdir(item_path))

# rename_files_replace_spaces('./projects')



    # for root, _, _ in os.walk(directory_path):
    #     if root != directory_path:
    #         for filename in os.listdir(root):
    #             item_path = os.path.join(root, filename)
    #             if os.path.isdir(item_path):
    #             # Check if the filename contains spaces
    #                 if ' ' in filename:
    #                     new_filename = filename.replace(' ', '_')
    #                     # Construct the full paths for the old and new filenames
    #                     old_filepath = os.path.join(directory_path, filename)
    #                     new_filepath = os.path.join(directory_path, new_filename)
    #                     # Rename the file
    #                     os.rename(old_filepath, new_filepath)
    #                     print(f'Renamed: {filename} -> {new_filename}')


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

# compress_images()