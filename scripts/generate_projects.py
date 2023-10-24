import os
import json
from bs4 import BeautifulSoup
from extract_project_info import extract_projects_info, sort_by_date
from compress_images import rename_files_replace_spaces

rename_files_replace_spaces()

# get data for each project and sort by creation date
project_info = extract_projects_info('./projects')
sorted_project_info = sorted(project_info, key=sort_by_date, reverse=True)
    
# get the title descrptions
with open('./project_descriptions.json') as f:
    project_descriptions = json.load(f)

# load the empty project page
with open("./skeletons/projects_head.html", "r") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

for project in sorted_project_info:

    dir_uuid = project['directory_uuid']
    image_foldername = project['image_foldername']
    title_image = project['first_image']
    html_filepath = project['html_filepath']
    html_uuid = project['html_file_uuid']
    title = project['title']
    title_string = title.replace(' ', '-').lower()

    print('writing', title)

    # get the html content for the project
    with open(html_filepath, "r") as f:
        modal_html_content = f.read()

    modal_soup = BeautifulSoup(modal_html_content, "html.parser")
    modal_article = modal_soup.find("article")

    # amend the filepaths so it can find the images
    given_filepath = f'projects/{dir_uuid}/'
    include = ['.png', '.gif']

    for element in modal_article.find_all():
        if element.has_attr('src'):
            if os.path.splitext(element['src'])[-1] in include:
                element['src'] = given_filepath + element['src'].replace('%20', '_')
                element['style'] = "width: 100%"

        if element.has_attr('href'):
            if os.path.splitext(element['href'])[-1]in include:
                element['href'] = given_filepath + element['href']

    project_card = f"""
    <div class="col-md-6 col-lg-3 mb-4">
        <div class="card">
            <img src={title_image} class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">{title}</h5>
                <p class="card-text">{project_descriptions[dir_uuid]}</p>
                <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#{title_string}" style="background-color: #C78226; border: 1px solid black;">More</button>
            </div>
        </div>
            </div>
    """

    modal_content = f"""
    <div class="modal fade modal-lg" id="{title_string}" tabindex="-1" role="dialog" aria-labelledby="{title_string}Label" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                <h5 class="modal-title" id="{title_string}Label">{title}</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                {modal_article}
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
            </div>
        </div>
    </div>
        """

    container_to_edit = soup.find("div", {"id": "project_card_container"})
    container_to_edit.append(BeautifulSoup(project_card, "html.parser"))

    container_to_edit.insert_after(BeautifulSoup(modal_content, "html.parser"))


with open("projects.html", "w") as output_file:
    output_file.write(soup.prettify())
    print('output file written')