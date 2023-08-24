# HTML to MDX Converter

This script allows you to scrape web pages, extract their content, and convert them into MDX format. MDX is a format that lets you seamlessly write JSX in your Markdown documents.

## Features

- Scrapes web pages based on provided URLs.
- Extracts links from the pages to scrape further content.
- Converts the scraped HTML content into MDX format.
- Handles headers, paragraphs, code tags, and links.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/your_username/html-to-mdx-converter.git
cd html-to-mdx-converter
```

2. Install the required Python packages:

``` bash 
pip install requests beautifulsoup4
```

Usage
Modify the base_urls list in the script to include the URLs you want to scrape.
Run the script:


```bash
python converter.py
```

Check the HTMLFiles directory for the scraped HTML content and the MDXFiles directory for the converted MDX content.

## LICENCE