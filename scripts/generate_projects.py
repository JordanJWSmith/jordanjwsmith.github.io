from bs4 import BeautifulSoup

with open("./skeletons/projects/projects_head.html", "r") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

for n in range(5):
    project_card = f"""
    <div class="col-md-6 col-lg-3 mb-4">
        <div class="card">
            <img src="assets/images/ucl_compressed_2.jpg" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">{n}</h5>
                <p class="card-text">{n}</p>
                <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#{n}">More</button>
            </div>
        </div>
            </div>
    """

    container_to_edit = soup.find("div", {"id": "project_card_container"})
    container_to_edit.append(BeautifulSoup(project_card, "html.parser"))

    new_div = soup.new_tag("div", id=f"modal={n}")
    new_div.append(f"Sample text for new-div-{n} goes here.")
    container_to_edit.insert_after(new_div)

    with open("test_output.html", "w") as output_file:
        output_file.write(soup.prettify())