import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

os.environ['NO_PROXY'] = 'learn.synctera.com'

def extract_urls(base_url):
    """Extract all URLs from a given base URL."""
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extracting URLs that start with base_url or start with /
    urls = [urljoin(base_url, a['href']) for a in soup.find_all('a', href=True) 
            if a['href'].startswith(base_url) or a['href'].startswith('/')]
    
    return urls

def download_html(url, save_folder):
    """Download HTML content of a given URL and save it to a folder."""
    response = requests.get(url)
    if response.status_code == 200:
        file_name = os.path.basename(url)
        if not file_name:
            file_name = "index.html"
        with open(os.path.join(save_folder, file_name), 'w') as file:
            file.write(response.text)

def html_to_mdx(html_file, save_folder):
    """Convert HTML content to MDX format and save it to a folder."""
    with open(html_file, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')

    mdx_content = ""
    
    for tag in soup.find_all(True):  # Find all tags
        if tag.name in ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            if tag.name == 'p':
                mdx_content += tag.get_text() + "\n\n"
            else:
                mdx_content += '#' * int(tag.name[1]) + ' ' + tag.get_text() + "\n\n"
        elif tag.name == 'code':
            mdx_content += '`' + tag.get_text() + '`\n\n'
        elif tag.name == 'a':
            mdx_content += f"[{tag.get_text()}]({tag['href']})\n\n"
            
    mdx_file_name = os.path.splitext(os.path.basename(html_file))[0] + ".mdx"
    with open(os.path.join(save_folder, mdx_file_name), 'w') as mdx_file:
        mdx_file.write(mdx_content)
# base_urls = ["https://learn.synctera.com/docs/products-fintechs","https://learn.synctera.com/docs/fintech-launch-guide","https://learn.synctera.com/docs/synctera-for-builders-and-fintechs", "https://dev.synctera.com/docs",]
# base_urls = ["https://learn.synctera.com/docs/synctera-for-builders-and-fintechs","https://learn.synctera.com/docs/t-minus10","https://learn.synctera.com/docs/products-fintechs","https://learn.synctera.com/docs/fintech-launch-guide","https://learn.synctera.com/open/docs/products-banks","https://learn.synctera.com/docs/synctera-platform","https://learn.synctera.com/docs/sfd-large-file-support-and-eof-markers","https://learn.synctera.com/docs/secure-file-delivery-conceptual-overview","https://learn.synctera.com/docs/synctera-my-data-mutability"]
base_urls =["https://dev.synctera.com/docs","https://dev.synctera.com/reference/","https://dev.synctera.com/openapi/","https://dev.synctera.com/"]

all_urls = set(base_urls)  # Using a set to avoid duplicates

# Extract all URLs from the base URLs
for url in base_urls:
    all_urls.update(extract_urls(url))

# Download HTML Files
save_folder_html = "HTMLFilesDevSynctera"
if not os.path.exists(save_folder_html):
    os.makedirs(save_folder_html)

for url in all_urls:
    download_html(url, save_folder_html)

# Parse HTML to MDX and Save
save_folder_mdx = "MDXDevSynctera"
if not os.path.exists(save_folder_mdx):
    os.makedirs(save_folder_mdx)

for html_file in os.listdir(save_folder_html):
    html_to_mdx(os.path.join(save_folder_html, html_file), save_folder_mdx)

# Provide Summary
print(f"Downloaded {len(all_urls)} HTML files to {save_folder_html}.")
print(f"Converted {len(os.listdir(save_folder_html))} HTML files to MDX format in {save_folder_mdx}.")
