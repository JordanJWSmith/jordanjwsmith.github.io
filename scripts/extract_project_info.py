from bs4 import BeautifulSoup
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
            first_image = None

            for item in os.listdir(root):
                item_path = os.path.join(root, item)

                if os.path.isdir(item_path):
                    imagefolder = item
                    if 'Untitled.png' in os.listdir(item_path):
                        first_image = os.path.join(item_path, 'Untitled.png')
                    

                    # print(os.listdir(item_path))


                if os.path.isfile(item_path) and item.endswith(".html"):
                    html_file = os.path.join(root, item)
                    html_uuid = os.path.splitext(item.split(' ')[-1])[0]

                    # print(item, html_uuid)
                    

                    with open(item_path) as f:
                        modal_content = f.read()
                        soup = BeautifulSoup(modal_content, "html.parser")
                        title_tag = soup.find("title").string

            if all([subdirectory_uuid, imagefolder, html_file, title_tag]):

                # print(f'.projects/{subdirectory_uuid}/{imagefolder}')

                project_info.append({
                    'directory_uuid': subdirectory_uuid, 
                    'image_foldername': imagefolder, 
                    'first_image': first_image,
                    'html_file_uuid' : html_uuid,
                    'html_filepath': html_file, 
                    'title': title_tag})

    return project_info

projects_info = extract_projects_info('./projects')
