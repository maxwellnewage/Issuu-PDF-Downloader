"""
This is a script for convert dict to json because the issuu urls could be very similar
"""
import os
import json

BASE_URL = "https://issuu.com/revistareplay/docs"

issuu_urls = [
    {
        "name": f"Replay #1.pdf",
        "url": f"{BASE_URL}/numero1_anticipo"
    },
    {
        "name": f"Replay #2.pdf",
        "url": f"{BASE_URL}/numero2_replay_anticipo"
    },
    {
        "name": f"Replay #3.pdf",
        "url": f"{BASE_URL}/numero3_replay_anticipo"
    },
    {
        "name": f"Replay #4.pdf",
        "url": f"{BASE_URL}/numero4_replay_anticipo"
    },
    {
        "name": f"Replay #5.pdf",
        "url": f"{BASE_URL}/anticipo_numero5_replay"
    },
    {
        "name": f"Replay #6.pdf",
        "url": f"{BASE_URL}/numero6_replay_issuu"
    },
    {
        "name": f"Replay #7.pdf",
        "url": f"{BASE_URL}/numero7_replay"
    },
    {
        "name": f"Replay #8.pdf",
        "url": f"{BASE_URL}/numero8_replay"
    },
    {
        "name": f"Replay #9.pdf",
        "url": f"{BASE_URL}/numero9_replay_issuu"
    },
    {
        "name": f"Replay #10.pdf",
        "url": f"{BASE_URL}/numero10_replay"
    },
    {
        "name": f"Replay #11.pdf",
        "url": f"{BASE_URL}/numero11_replay"
    },
    {
        "name": f"Replay #12.pdf",
        "url": f"{BASE_URL}/numero12_replay"
    },
]

# populate issuu url list
for number in range(13, 34):
    # https://issuu.com/revistareplay/docs/replay_numero_13
    issuu_urls.append({
        "name": f"Replay #{number}.pdf",
        "url": f"{BASE_URL}/replay_numero_{number}"
    })

# convert to json string
jsonStr = json.dumps(issuu_urls)

# save on issuu_urls.json
filename_with_folder = os.path.join('./json/', 'issuu_urls.json')
opener = open(filename_with_folder, 'w')
opener.write(jsonStr)
opener.close()
