import os
import re
from datetime import datetime

# Specify the folder containing the markdown files
folder_path = "papers"

# Get a list of markdown files in the folder
md_files = [file for file in os.listdir(folder_path) if file.endswith(".md")]

# Create a list of tuples containing the markdown file path and its corresponding date
file_date_list = []
for md_file in md_files:
    with open(os.path.join(folder_path, md_file), "r", encoding="utf-8") as md:
        content = md.read()
        date_match = re.search(r"date: (\d{4}-\d{2}-\d{2})", content)
        if date_match:
            date_str = date_match.group(1)
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            file_date_list.append((md_file, date_obj))

# Sort the file_date_list by date in descending order
file_date_list.sort(key=lambda x: x[1], reverse=True)

# Open the paper_list.tex file for writing (overwrite if exists)
with open("paper_list.tex", "w", encoding="utf-8") as file:
    for index, (md_file, _) in enumerate(file_date_list, start=1):
        with open(os.path.join(folder_path, md_file), "r", encoding="utf-8") as md:
            content = md.read()

            # Extract the title, authors, and venue using regular expressions
            title_match = re.search(r"title: '(.*?)'", content)
            authors_match = re.search(r"authors: '(.*?)'", content)
            venue_match = re.search(r"venue: '(.*?)'", content)

            if title_match and authors_match and venue_match:
                title = title_match.group(1)
                authors = authors_match.group(1)
                venue = venue_match.group(1)

                # Escape % signs in the title and venue
                title = title.replace("%", "\\%")
                venue = venue.replace("%", "\\%")

                # Shorten the author list if it exceeds 12 people
                author_list = authors.split(", ")
                if len(author_list) > 12:
                    authors = author_list[0] + " et al."

                # Write the paper information to the paper_list.tex file
                file.write(f"{index}. \\textbf{{{title}}}\\\\\\n")
                file.write(f"   \\textit{{{authors}}}\\\\\\n")
                file.write(f"   {venue}\\\\\\n")
                file.write("\\vspace{0.3em}\\n")
