import frontmatter
from jinja2 import Template
from markdown import markdown
import os
import glob

with open("paper_entry_template.html", "r") as file:
    paper_entry_template = Template(file.read())

paper_files = glob.glob("papers/*.md")

paper_entries = []
for paper_file in paper_files:
    post = frontmatter.load(paper_file)
    metadata = post.metadata
    content = post.content
    metadata["content"] = content
    file_title = os.path.splitext(os.path.basename(paper_file))[0].replace(" ", "_")
    metadata["id"] = file_title
    paper_entries.append(metadata)

paper_entries.sort(key=lambda x: x["date"], reverse=True)
paper_entries = [{**x, "list_idx": i} for i, x in enumerate(paper_entries, start=1)]


paper_html_entries = [paper_entry_template.render(entry) for entry in paper_entries]

with open("profile.md", "r", encoding="utf-8") as file:
    profile_content = markdown(file.read())

with open("about.md", "r", encoding="utf-8") as file:
    about_content = markdown(file.read())

with open("main_template.html", "r", encoding="utf-8") as file:
    main_template = Template(file.read())

html = main_template.render(
    paper_entries=paper_html_entries,
    profile=profile_content,
    about=about_content,
    profile_picture="img/profile.jpg",
)

output_file = "index.html"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(html)
