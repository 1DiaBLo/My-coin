import requests, time, random

SESSIONID = "d121aef7d3daba361704983824c28110"
HEADERS = {"cookie": f"sessionid={SESSIONID}", "user-agent":"Mozilla/5.0"}

LIVE_FEED = "https://www.tiktok.com/live"

def collect_in_live(url):
    print("🔁 Visiting:", url)
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200 and "collect" in r.text.lower():
        print("🎁 Box found -> collecting...")
        # هنا نرسل request للـ collect action (نضيفه لاحقاً)
    else:
        print("❌ No box in this live")

while True:
    collect_in_live(LIVE_FEED)
    seconds = random.randint(20, 40)
    print(f"⏱️ Waiting {seconds}s before next fetch...")
    time.sleep(seconds)
  
