from bs4 import BeautifulSoup
from PIL import Image
import os

def extract_projects_info(filepath='/projects'):
    project_info = []

    for root, _, _ in os.walk(filepath):
        if root != filepath:
            # Extract subdirectory UUID
            subdirectory_uuid = os.path.basename(root)

            # Extract subdirectory contents
            imagefolder = None
            html_file = None
            title_tag = None

            for item in os.listdir(root):
                item_path = os.path.join(root, item)

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

                if os.path.isdir(item_path):
                    imagefolder = item

                if os.path.isfile(item_path) and item.endswith(".html"):
                    html_file = item

                    with open(item_path) as f:
                        modal_content = f.read()
                        soup = BeautifulSoup(modal_content, "html.parser")
                        title_tag = soup.find("title").string
            
            if all([subdirectory_uuid, imagefolder, html_file, title_tag]):
                # print('extracted', [subdirectory_uuid, imagefolder, html_file, title_tag])
                # project_info['directory_uuid'] = subdirectory_uuid
                # project_info['image_foldername'] = imagefolder
                # project_info['html_filename'] = html_file
                # project_info['title'] = title_tag
                print('appending', title_tag)
                project_info.append({
                    'directory_uuid': subdirectory_uuid, 
                    'image_foldername': imagefolder, 
                    'html_filename': html_file, 
                    'title': title_tag})

    # print(project_info)
    return project_info

# Example usage
projects_info = extract_projects_info('./projects')

# print(projects_info)
# for info in projects_info:
#     print(info)
#     print()
