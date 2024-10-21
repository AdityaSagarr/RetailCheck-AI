from langchain_community.document_loaders import WebBaseLoader

def scrape(item_link):
    """Scrapes the item page content from the given link and cleans it up."""
    loader = WebBaseLoader(item_link)
    page_data = loader.load()

    if not page_data:
        return "No content found or the page could not be loaded."

    # Get the page content
    page_content = page_data.pop().page_content

    # Remove unnecessary newlines and extra spaces
    cleaned_content = ' '.join(page_content.split())

    return cleaned_content
