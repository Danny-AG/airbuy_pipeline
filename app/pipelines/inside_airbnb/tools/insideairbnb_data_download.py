import os

import requests
from bs4 import BeautifulSoup

from app.common.utils import is_word_in_string_list
from app.config import AIRBNB_DATA_DIR, AIRBNB_DATA_URL
from app.pipelines.global_property_sqm.utils import get_cleaned_global_sqm_prices_df

# Tool to quickly download relevant Airbnb data


def download_airbnb_data(cities: list):
    """Download Airbnb data for the given cities."""

    # Create a directory to save the downloaded files
    if not os.path.exists(AIRBNB_DATA_DIR):
        os.makedirs(AIRBNB_DATA_DIR)

    # Make a request to the webpage and parse it with BeautifulSoup
    response = requests.get(AIRBNB_DATA_URL)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all links on the webpage
    links = soup.find_all("a")

    # Loop through the links and download the files that match the city names
    for link in links:
        href = link.get("href")
        if href and "listings.csv.gz" in href:
            city_name = href.split("/")[-4]  # Extract city name from the URL
            country = href.split("/")[3]  # Extract country name from URL
            date_of_data = href.split("/")[-3]  # Extract date of data from URL

            if not is_word_in_string_list(city_name, cities):
                print(f"{city_name} not in Global Property SQM data. Skipping download...")
                print(href)
                continue

            file_url = href
            file_name = f"{city_name}_{country}_{date_of_data}_listings.csv.gz"
            file_path = os.path.join(AIRBNB_DATA_DIR, file_name)

            # Download the file
            response = requests.get(file_url)
            with open(file_path, "wb") as file:
                file.write(response.content)

            print(f"Downloaded: {file_name}")

    print("Download completed.")


if __name__ == '__main__':
    cities = get_cleaned_global_sqm_prices_df()["Capital City"].tolist()
    download_airbnb_data(cities)
