import os
import json
from bs4 import BeautifulSoup
from extract_project_info import sort_by_date
from compress_images import crop_to_fit

# TODO: publication images

with open('./publications/publication_info.json') as f:
    publication_descriptions = json.load(f)

sorted_publication_descriptions = sorted(publication_descriptions, key=sort_by_date)

with open("./skeletons/projects/publications_head.html", "r") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

tag_colours = {
    'Research Paper': 'green',
    'Professional Blog': 'grey',
    'Dev Blog': 'orange'
}

for publication in sorted_publication_descriptions:

    image_path = publication['image']

    # if not len(image_path):
    #     image_path = "projects/5f1b773b-2dff-4dd4-a203-715739f9befb/Dancing_Spider_72c42e5df4ba4858ae33287f69456bba/Untitled_titlecard.png"

    titlecard_image_path = os.path.splitext(image_path)[0]+'_titlecard' + os.path.splitext(image_path)[1]

    if not os.path.exists(titlecard_image_path):
        titlecard_image_path = crop_to_fit(image_path)
    
    publication_card = f"""

    <div class="container col-xxl-8 px-4" style="background-color: #ffffff; padding-top: 1rem; padding-bottom: 1rem; margin-top: 10px; margin-bottom: 10px;">
        <div class="row align-items-center">
            <div class="col-12 col-md-6 custom-im-width">
                <img src={titlecard_image_path} class="d-block mx-lg-auto img-fluid" alt="Bootstrap Themes" width="700" height="500" loading="lazy">
            </div>
            <div class="col-12 col-md-6 custom-text-width">
                <p class="copy-text" style="font-weight: bold">{publication['title']}</p>
                <p class="copy-text">{publication['authors']}</p>
                
                <div class="d-flex flex-wrap align-items-center">
                    <a href={publication['url']} target="_blank">
                        <button type="button" class="btn btn-primary btn-md px-4 me-2" style="background-color: #C78226; border: 1px solid black;"><i class="bi bi-book"></i></button>
                    </a>
                    <span class="selected-value select-value-color-{tag_colours[publication['tag']]}">{publication['tag']}</span>
                </div>
            </div>
        </div>
      </div>
    """

    jumbotron = soup.find("div", {"id": "title_jumbotron"})
    jumbotron.insert_after(BeautifulSoup(publication_card, "html.parser"))

with open("test_output.html", "w") as output_file:
    output_file.write(soup.prettify())
    print('output file written')
    
