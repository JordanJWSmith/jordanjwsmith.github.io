from bs4 import BeautifulSoup
from datetime import datetime
from compress_images import resize
import json
import os


def get_project_descriptions(filepath='project_descriptions.json'):
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            project_descriptions = json.load(file)
    else:
        project_descriptions = {}

    return project_descriptions


def sort_by_date(item):
    date_str = item['date']  
    date_format = "%B %d, %Y %I:%M %p"
    return datetime.strptime(date_str, date_format)


def extract_projects_info(filepath='/projects'):
    project_info = []
    project_descriptions = get_project_descriptions()

    for root, _, _ in os.walk(filepath):
        if root != filepath:

            subdirectory_uuid = os.path.basename(root)

            if subdirectory_uuid not in project_descriptions.keys() and os.path.split(root)[0] == filepath:
                project_descriptions[subdirectory_uuid] = ""

                with open('project_descriptions.json', 'w') as f:
                    json.dump(project_descriptions, f, indent=4)

            # Extract subdirectory contents
            imagefolder = None
            html_file = None
            title_tag = None
            first_image = None
            time = None

            for item in os.listdir(root):
                item_path = os.path.join(root, item)

                if os.path.isdir(item_path):
                    imagefolder = item
                    if 'Untitled.png' in os.listdir(item_path) and 'Untitled_titlecard.png' not in os.listdir(item_path):
                        raw_image = os.path.join(item_path, 'Untitled.png')
                        first_image = resize(raw_image, 1200, 600)
                    else:
                        raw_image = os.path.join(item_path, 'Untitled.png')
                        first_image = os.path.splitext(raw_image)[0]+'_titlecard' + os.path.splitext(raw_image)[1]
                        
                    # print(os.listdir(item_path))


                if os.path.isfile(item_path) and item.endswith(".html"):
                    html_file = os.path.join(root, item)
                    html_uuid = os.path.splitext(item.split(' ')[-1])[0]

                    with open(html_file, "r") as f:
                        modal_html_content = f.read()

                    modal_soup = BeautifulSoup(modal_html_content, "html.parser")
                    modal_article = modal_soup.find("article")

                    time = modal_article.find("time")
                    # date_format = "@%B %d, %Y %I:%M %p"
                    time = time.text.strip()[1:]

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
                    'title': title_tag,
                    'date': time})
                

    return project_info

# projects_info = extract_projects_info('./projects')
