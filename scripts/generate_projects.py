from bs4 import BeautifulSoup
from extract_project_info import extract_projects_info

project_info = extract_projects_info('./projects')

with open("./skeletons/projects/projects_head.html", "r") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

for project in project_info:

    dir_uuid = project['directory_uuid']
    image_foldername = project['image_foldername']
    html_filename = project['html_filename']
    title = project['title']

    print('writing', title)

    project_card = f"""
    <div class="col-md-6 col-lg-3 mb-4">
        <div class="card">
            <img src="assets/images/ucl_compressed_2.jpg" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">{title}</h5>
                <p class="card-text">Info about {title}</p>
                <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#{title}">More</button>
            </div>
        </div>
            </div>
    """

    modal_content = f"""
    <div class="modal fade" id="{title}" tabindex="-1" role="dialog" aria-labelledby="{title}Label" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                <h5 class="modal-title" id="{title}Label">{title}</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                Content for {title} goes here.
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

    new_modal = soup.new_tag("div", id=f"modal={title}")
    new_modal.append(BeautifulSoup(modal_content, "html.parser"))
    container_to_edit.insert_after(new_modal)

with open("test_output.html", "w") as output_file:
    output_file.write(soup.prettify())
    print('output file written')