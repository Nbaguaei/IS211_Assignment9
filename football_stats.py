
# football_stats.py
# Scrapes NFL touchdown leaders from CBS Sports
# URL: https://www.cbssports.com/nfl/stats/playersort/nfl/year-2023-season-regular-category-td/

import requests
from bs4 import BeautifulSoup

def scrape_football_stats():
    """Scrapes NFL touchdown leaders and prints them to the console."""
    url = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2023-season-regular-category-td/"

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        table = soup.find("table", {"class": "TableBase-table"})
        if table:
            rows = table.find_all("tr", {"class": "TableBase-bodyTr"})

            print("Top 20 NFL Touchdown Leaders (2023 Regular Season):")
            for i, row in enumerate(rows[:20]):
                cols = row.find_all("td")
                if len(cols) >= 5:
                    player = cols[0].text.strip()
                    position = cols[1].text.strip()
                    team = cols[2].text.strip()
                    touchdowns = cols[4].text.strip()
                    print(f"{i+1}. {player} ({position}, {team}): {touchdowns} TDs")
                else:
                    print(f"Skipping row {i+1} due to missing data.")

        else:
            print("Table not found on the page.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("Running football_stats.py...")
    scrape_football_stats()