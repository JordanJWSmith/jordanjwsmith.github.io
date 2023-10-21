from PIL import Image
import os


def compress_images(input_folder, output_folder, quality=10):
    # List all files in the input folder
    files = os.listdir(input_folder)
    print(files)
    
    for file in files:
        if file.lower().endswith(".png"):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, 'compressed_', file)

            # Open the image and save it with the specified quality
            img = Image.open(input_path)
            print('saving', output_path)
            img.save(output_path, optimize=True, quality=quality)

input_folder = "../projects/5f1b773b-2dff-4dd4-a203-715739f9befb/Dancing Spider 72c42e5df4ba4858ae33287f69456bba/"  # Change this to your input folder
output_folder = "../projects/5f1b773b-2dff-4dd4-a203-715739f9befb/Dancing Spider 72c42e5df4ba4858ae33287f69456bba/"  # Change this to your output folder
quality = 50  # Adjust the quality (0-100) as needed

compress_images(input_folder, output_folder, quality)