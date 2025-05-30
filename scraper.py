import requests
from bs4 import BeautifulSoup
from database import save_fps_entry

FPS_IDS = range(104800100001, 104800100062)
CYCLE_MONTH = 4
CYCLE_YEAR = 2025

def fetch_wheat_data(fps_id):
    payload = {
        "fps_id": str(fps_id),
        "month": CYCLE_MONTH,
        "year": CYCLE_YEAR
    }

    try:
        res = requests.post("https://epos.punjab.gov.in/FPS_Stock.jsp", data=payload)
        soup = BeautifulSoup(res.text, "html.parser")
        rows = soup.find_all("tr")
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 10 and cols[1].text.strip().lower() == "wheat":
                return {
                    "fps_id": str(fps_id),
                    "allocation": float(cols[3].text.strip() or 0),
                    "received": float(cols[5].text.strip() or 0),
                    "issued": float(cols[8].text.strip() or 0),
                    "cb": float(cols[9].text.strip() or 0)
                }
    except Exception as e:
        print(f"Error fetching data for FPS {fps_id}: {e}")
    
    return None

def refresh_fps_data():
    for fps_id in FPS_IDS:
        data = fetch_wheat_data(fps_id)
        if data:
            save_fps_entry(data)

def update_yesterday_distributions():
    from database import update_yesterday
    update_yesterday()

def get_all_fps_data():
    from database import get_wheat_data
    return get_wheat_data()
