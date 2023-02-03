"""
This is a script for convert dict to json because the issuu urls could be very similar
"""
import os
import json

BASE_URL = "https://issuu.com/revistareplay/docs"

issuu_urls = [
    {
        "name": "Replay #3.pdf",
        "url": f"{BASE_URL}/numero3_replay_anticipo"
    },
    {
        "name": "Replay #4.pdf",
        "url": f"{BASE_URL}/numero4_replay_anticipo"
    },
]

# populate issuu url list
for number in range(5, 34):
    if number <= 12:
        # https://issuu.com/revistareplay/docs/numero4
        issuu_urls.append({
            "name": f"Replay #{number}.pdf",
            "url": f"{BASE_URL}/numero{number}"
        })
    else:
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
