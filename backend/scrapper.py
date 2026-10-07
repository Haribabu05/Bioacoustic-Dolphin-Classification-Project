import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_cve_data():
    url = "https://www.cvedetails.com/vulnerability-list.php"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'id': 'vulnslisttable'})
    rows = table.find_all('tr')[1:6]  # Only get top 5 CVEs

    data = []
    for row in rows:
        cols = row.find_all('td')
        if len(cols) > 4:
            cve_id = cols[1].text.strip()
            desc = cols[4].text.strip()
            severity = float(cols[7].text.strip() or 0)
            data.append({"cve_id": cve_id, "description": desc, "severity": severity})
    
    return pd.DataFrame(data)
