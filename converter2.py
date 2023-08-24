import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
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
base_urls =[
    "https://learn.synctera.com/",
    "https://learn.synctera.com/docs/products-fintechs",
    "https://learn.synctera.com/docs/fintech-user-guide",
    "https://learn.synctera.com/docs/fintech-launch-guide",
    "https://learn.synctera.com/docs/products-banks",
    "https://learn.synctera.com/open/en",
    "https://learn.synctera.com/docs/sfd-large-file-support-and-eof-markers",
    "https://learn.synctera.com/docs/id-verification-monitoring-products",
    "https://learn.synctera.com/docs/account-management-products",
    "https://learn.synctera.com/docs/account-linking-products",
    "https://learn.synctera.com/docs/instant-account-funding",
    "https://learn.synctera.com/docs/instant-push-to-card",
    "https://learn.synctera.com/docs/payments-products",
    "https://learn.synctera.com/docs/cards-products",
    "https://learn.synctera.com/docs/lending-products",
    "https://learn.synctera.com/docs/platform-features-fintechs",
    "https://learn.synctera.com/docs/back-office-products",
    "https://learn.synctera.com/docs/t-minus10",
    "https://learn.synctera.com/docs/ground-control",
    "https://learn.synctera.com/docs/professional-services-fintechs",
    "https://learn.synctera.com/docs/roadmap",
    "https://learn.synctera.com/docs/dashboard-for-fintechs",
    "https://learn.synctera.com/docs/cases-for-fintechs",
    "https://learn.synctera.com/docs/customers-for-fintechs",
    "https://learn.synctera.com/docs/accounts-for-fintechs",
    "https://learn.synctera.com/docs/cards-for-fintechs",
    "https://learn.synctera.com/docs/company-offboarding",
    "https://learn.synctera.com/docs/daily-changelog",
    "https://learn.synctera.com/docs/transactions-for-fintechs",
    "https://learn.synctera.com/docs/promotions-or-bonus-programs",
    "https://learn.synctera.com/docs/fintech-launch-checklist",
    "https://learn.synctera.com/docs/fintech-solutioning",
    "https://learn.synctera.com/docs/pre-launch-task-guide",
    "https://learn.synctera.com/docs/product-specific-launch-guides",
    "https://learn.synctera.com/docs/post-launch-support",
    "https://learn.synctera.com/docs/payments-products-banks",
    "https://learn.synctera.com/docs/cards-products-banks",
    "https://learn.synctera.com/docs/lending-products-banks",
    "https://learn.synctera.com/docs/platform-features-banks",
    "https://learn.synctera.com/docs/compliance-support-for-fintechs",
    "https://learn.synctera.com/docs/contracting-for-banks",
    "https://learn.synctera.com/docs/secure-file-delivery-conceptual-overview",
    "https://learn.synctera.com/docs/overview",
    "https://learn.synctera.com/docs/spend-monitoring",
    "https://learn.synctera.com/docs/custom-card-review-cases-fintechs",
    "https://learn.synctera.com/docs/fraud-cases-fintechs",
    "https://learn.synctera.com/docs/dispute-cases-fintechs",
    "https://learn.synctera.com/docs/information-request-cases-fintechs",
    "https://learn.synctera.com/docs/kyb-cases-fintechs",
    "https://learn.synctera.com/docs/kyc-cases-fintechs",
    "https://learn.synctera.com/docs/marketing-materials-cases-fintechs",
    "https://learn.synctera.com/docs/spend-monitoring-cases",
    "https://learn.synctera.com/docs/watchlist-match-cases-fintechs",
    "https://learn.synctera.com/docs/card-management",
    "https://learn.synctera.com/docs/how-to-handle-return-mail-for-cards",
    "https://learn.synctera.com/open/docs/synctera-my-data-mutability",
    "https://learn.synctera.com/open/docs/case-resolution-overview-2023-07-26",
    "https://learn.synctera.com/docs/insights",
    "https://learn.synctera.com/docs/funds-flow",
    "https://learn.synctera.com/docs/using-your-own-kyc-vendor",
    "https://learn.synctera.com/docs/run-kyb-on-you-company-or-organization",
    "https://learn.synctera.com/docs/testing-and-certification",
    "https://learn.synctera.com/docs/compliance-guidance-about-marketing",
    "https://learn.synctera.com/docs/waitlists",
    "https://learn.synctera.com/docs/launch-debit-cards",
    "https://learn.synctera.com/docs/fintech-support",
    "https://learn.synctera.com/docs/synctera-platform",
    "https://learn.synctera.com/docs/synctera-my-data-mutability",
    "https://learn.synctera.com/open/docs/products-fintechs",
    "https://learn.synctera.com/open/docs/products-banks",
    "https://learn.synctera.com/open/docs/sfd-large-file-support-and-eof-markers",
    "https://learn.synctera.com/open/docs/secure-file-delivery-conceptual-overview",
    "https://learn.synctera.com/docs/insights-references-and-samples-2023-08-04",
    "https://learn.synctera.com/open/docs/insights",
    "https://learn.synctera.com/docs/case-resolution-overview-2023-07-26",
    "https://learn.synctera.com/docs/due-diligence-and-matching-overview",
    "https://learn.synctera.com/docs/mobile-wallet-resources",
    "https://learn.synctera.com/docs/admin-overview",
    "https://learn.synctera.com/open/docs/pitch-decks-and-business-plans",
    "https://learn.synctera.com/docs/pitch-decks-and-business-plans",
    "https://learn.synctera.com/open/docs/mobile-wallet-resources",
    "https://learn.synctera.com/open/docs/custom-card-review-cases-fintechs"
]

all_urls = set(base_urls)  # Using a set to avoid duplicates

# Extract all URLs from the base URLs
for url in base_urls:
    all_urls.update(extract_urls(url))

# Download HTML Files
save_folder_html = "HTMLFiles"
if not os.path.exists(save_folder_html):
    os.makedirs(save_folder_html)

for url in all_urls:
    download_html(url, save_folder_html)

# Parse HTML to MDX and Save
save_folder_mdx = "MDXFilesLearnSynctera"
if not os.path.exists(save_folder_mdx):
    os.makedirs(save_folder_mdx)

for html_file in os.listdir(save_folder_html):
    html_to_mdx(os.path.join(save_folder_html, html_file), save_folder_mdx)

# Provide Summary
print(f"Downloaded {len(all_urls)} HTML files to {save_folder_html}.")
print(f"Converted {len(os.listdir(save_folder_html))} HTML files to MDX format in {save_folder_mdx}.")
