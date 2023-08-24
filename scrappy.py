import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def base_url_to_folder(base_url):
    """Convert a base URL to a safe folder name."""
    if base_url is None:
        raise ValueError("The provided base_url is None. Please provide a valid URL.")
    return base_url.replace('http://', '').replace('https://', '').replace('/', '_').replace('.', '_')


def extract_urls(base_url):
    """Extract all URLs from a given base URL."""
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    urls = [urljoin(base_url, a['href']) for a in soup.find_all('a', href=True) 
            if a['href'].startswith(base_url) or a['href'].startswith('/') or a['href'].startswith('#')]
    return urls

def download_html(url, base_folder):
    """Download HTML content of a given URL and save it to a specific base folder."""
    response = requests.get(url)
    file_name = os.path.basename(url) or "index.html"  # Define file_name here to ensure it always has a value
    if response.status_code == 200:
        folder_path = base_folder 
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        with open(os.path.join(folder_path, file_name), 'w') as file:
            file.write(response.text)
    return file_name

def html_to_mdx(html_file, save_folder, base_url):
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
            link_url = tag['href']
            # If the link is relative, prepend with the base URL
            link_url = urljoin(base_url, link_url)
    # Remove protocol from the link URL for the desired MDX format
    link_url = link_url.replace("http://", "").replace("https://", "")
    mdx_content += f"[{tag.get_text()}]({link_url})\n\n"
            
    mdx_file_name = os.path.splitext(os.path.basename(html_file))[0] + ".mdx"
    mdx_folder_for_base = save_folder_mdx
    if not os.path.exists(mdx_folder_for_base):
        os.makedirs(mdx_folder_for_base)
    with open(os.path.join(mdx_folder_for_base, mdx_file_name), 'w') as mdx_file:
        mdx_file.write(mdx_content)

base_urls = ["https://learn.synctera.com/"]
all_urls = set(base_urls)  # Using a set to avoid duplicates

# This dictionary will map each downloaded file to its base URL
file_to_base_url = {}

# Extract all URLs from the base URLs
for base_url in base_urls:
    all_urls.update(extract_urls(base_url))

# Download HTML Files
save_folder_html = "HTMLFiles"
for url in all_urls:
    # Store the filename and its base URL in the dictionary
    filename = download_html(url, save_folder_html)
    for base_url in base_urls:
        if url.startswith(base_url):
            file_to_base_url[filename] = base_url
            break

# Parse HTML to MDX and Save
save_folder_mdx = "MDXFiles"
for base_url in base_urls:
    mdx_folder_for_base = save_folder_mdx
    if not os.path.exists(mdx_folder_for_base):
        os.makedirs(mdx_folder_for_base)

for base_url in base_urls:
    html_folder = 
    for html_file in os.listdir(html_folder):
        # Retrieve the base URL for the file from the dictionary
        base_url_for_file = file_to_base_url.get(html_file)
        html_to_mdx(os.path.join(html_folder, html_file), save_folder_mdx, base_url_for_file)

# Provide Summary
print(f"Downloaded {len(all_urls)} HTML files to {save_folder_html}.")
print(f"Converted {len(os.listdir(save_folder_html))} HTML files to MDX format in {save_folder_mdx}.")
