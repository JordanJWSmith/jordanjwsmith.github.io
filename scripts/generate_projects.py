import os
from bs4 import BeautifulSoup
from extract_project_info import extract_projects_info
from compress_images import rename_files_replace_spaces

rename_files_replace_spaces()

project_info = extract_projects_info('./projects')

with open("./skeletons/projects/projects_head.html", "r") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

for project in project_info:

    dir_uuid = project['directory_uuid']
    image_foldername = project['image_foldername']
    html_filepath = project['html_filepath']
    html_uuid = project['html_file_uuid']
    title = project['title']
    title_string = title.replace(' ', '-').lower()

    print('writing', title)

    with open(html_filepath, "r") as f:
        modal_html_content = f.read()
        # print(modal_html_content)

    modal_soup = BeautifulSoup(modal_html_content, "html.parser")
    modal_article = modal_soup.find("article")

    given_filepath = f'projects/{dir_uuid}/'

    include = ['.png', '.gif']

    for element in modal_article.find_all():
        if element.has_attr('src'):
            if os.path.splitext(element['src'])[-1] in include:
                element['src'] = given_filepath + element['src']
                # print(element['src'])

        if element.has_attr('href'):
            if os.path.splitext(element['href'])[-1]in include:
                element['href'] = given_filepath + element['href']
            # if os.path.splitext()
            # print(os.path.splitext(element['href'])[-1])
            # print(element['href'])

    # print(modal_article)

    # given_filepath = f'projects/{dir_uuid}/'

    # for modal_body_element in modal_article.find_all(class_="modal-body"):
    #     for element in modal_body_element.find_all(['src', 'href']):
    #         if element.has_attr('src'):
    #             element['src'] = given_filepath + element['src']
    #             print(element)
    #         if element.has_attr('href'):
    #             element['href'] = given_filepath + element['href']
    #             print(element)

    # print(modal_article.prettify())

    # def prepend_filepath_to_links(modal_html_content, given_filepath):
    #     modal_soup = BeautifulSoup(modal_html_content, "html.parser")
    #     modal_article = modal_soup.find("article")

    #     for modal_body_element in modal_article.find_all(class_="modal-body"):
    #         for element in modal_body_element.find_all(['src', 'href']):
    #             if element.has_attr('src'):
    #                 element['src'] = given_filepath + element['src']
    #             if element.has_attr('href'):
    #                 element['href'] = given_filepath + element['href']

        # Return the modified modal_article
        # return modal_article.prettify()
    
    # modal_body_elements = modal_article.find_all(class_="modal-body")
    
    # elements_with_src = modal_body_elements.find_all(src=True)
    # elements_with_href = modal_body_elements.find_all(href=True)

    # given_filepath = f'projects/{dir_uuid}/'

    # for modal_body_element in modal_body_elements:
    #     elements_with_src = modal_body_element.find_all(src=True)
    #     elements_with_href = modal_body_element.find_all(href=True)

    #     for element in elements_with_src:
    #         current_src = element['src']
    #         element['src'] = given_filepath + current_src

    #     for element in elements_with_href:
    #         current_href = element['href']
    #         element['href'] = given_filepath + current_href
    
    # print(modal_body_elements)

    # for modal_body_element in modal_body_elements:
    #     modal_body_element.replace_with(modal_body_element)

    # Now modal_article contains the changes
    # print(modal_article.prettify()) 


    # Convert the modified BeautifulSoup object back to an HTML string
    # modified_html_content = modal_soup.prettify()
    # print(modified_html_content)

    # Update the modal_html_content with the modified content
    # modal_html_content = modified_html_content
    # print(modal_article)


    project_card = f"""
    <div class="col-md-6 col-lg-3 mb-4">
        <div class="card">
            <img src="assets/images/ucl_compressed_2.jpg" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">{title}</h5>
                <p class="card-text">Info about {title}</p>
                <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#{title_string}">More</button>
            </div>
        </div>
            </div>
    """

    modal_content = f"""
    <div class="modal fade" id="{title_string}" tabindex="-1" role="dialog" aria-labelledby="{title_string}Label" aria-hidden="true">
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


with open("test_output.html", "w") as output_file:
    output_file.write(soup.prettify())
    print('output file written')