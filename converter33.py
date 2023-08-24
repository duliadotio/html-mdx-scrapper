import os
import requests
from bs4 import BeautifulSoup

# 1. Download HTML Files
def download_html(url, save_folder):
    response = requests.get(url)
    if response.status_code == 200:
        file_name = os.path.basename(url)
        if not file_name:
            file_name = "index.html"
        with open(os.path.join(save_folder, file_name), 'w') as file:
            file.write(response.text)

urls = ["https://learn.synctera.com/", "https://dev.synctera.com/"]  # Replace with your URLs
save_folder_html = "HTMLFiles"
if not os.path.exists(save_folder_html):
    os.makedirs(save_folder_html)

for url in urls:
    download_html(url, save_folder_html)

# 2. & 3. Parse HTML to MDX and Save
def html_to_mdx(html_file, save_folder):
    with open(html_file, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')

    mdx_content = ""
    for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        if tag.name == 'p':
            mdx_content += tag.get_text() + "\n\n"
        else:
            mdx_content += '#' * int(tag.name[1]) + ' ' + tag.get_text() + "\n\n"

    mdx_file_name = os.path.splitext(os.path.basename(html_file))[0] + ".mdx"
    with open(os.path.join(save_folder, mdx_file_name), 'w') as mdx_file:
        mdx_file.write(mdx_content)

save_folder_mdx = "MDXFiles"
if not os.path.exists(save_folder_mdx):
    os.makedirs(save_folder_mdx)

for html_file in os.listdir(save_folder_html):
    html_to_mdx(os.path.join(save_folder_html, html_file), save_folder_mdx)

# 4. Provide Summary
print(f"Downloaded {len(urls)} HTML files to {save_folder_html}.")
print(f"Converted {len(os.listdir(save_folder_html))} HTML files to MDX format in {save_folder_mdx}.")
