import requests
from bs4 import BeautifulSoup
import json
import re
import os

def scrape_glossary(url):
    """
    Scrapes the glossary terms and definitions from the provided URL.
    """
    print(f"🌐 Starting scrape: {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        glossary_section = soup.find('section', {'data-type': 'miscellaneous'})

        if not glossary_section:
            print("Warning: Could not find the glossary section on the page.")
            return []

        data = []
        for p_tag in glossary_section.find_all('p'):
            strong_tag = p_tag.find('strong')

            if strong_tag:
                term = strong_tag.text.strip()
                definition_element = p_tag.text
                definition = definition_element.replace(term, '', 1).strip()
                definition = re.sub(r'^\s*[\u2013\u2014\u2015–\-—:]\s*', '', definition).strip()
                
                if term and definition:
                    # Clean up extra whitespace within the definition
                    definition = re.sub(r'\s+', ' ', definition).strip()
                    data.append({
                        "term": term,
                        "definition": definition
                    })

        return data

    except requests.exceptions.RequestException as e:
        print(f"Error during Request: {e}")
        return None
    except Exception as e:
        print(f"Error during Parsing: {e}")
        return None

def save_to_json(data, filename="glossary.json", directory="data"):
    """
    Saves the extracted data to a JSON file in the specified directory.
    """
    if data is not None and data:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"📁 Created directory '{directory}'.")

        file_path = os.path.join(directory, filename)

        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"✅ Glossary data successfully saved to '{file_path}'. (Total {len(data)} items)")
        except IOError as e:
            print(f"Error saving file: {e}")
    else:
        print("⚠️ Skipping JSON file save: No data was extracted.")

# Main execution block
if __name__ == "__main__":
    GLOSSARY_URL = "https://usq.pressbooks.pub/anatomy/back-matter/glossary/"
    OUTPUT_DIRECTORY = "../data" 
    OUTPUT_FILENAME = "anatomy_terms.json"

    glossary_data = scrape_glossary(GLOSSARY_URL)
    save_to_json(glossary_data, filename=OUTPUT_FILENAME, directory=OUTPUT_DIRECTORY)