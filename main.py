import os
import re
import urllib
import core.downloader as downloader
import core.pdf as pdf
import json


def get_issuu_json_as_dict():
    """
    Create a json file named issuu_urls.json on json folder
    Then, respect this json scheme:
    [
        {
            "name": "name of the pdf",
            "url": "issuu url"
        }
    ]
    :return: list[Dict]
    """
    issuu_url_json = os.path.join('./json/', 'issuu_urls.json')
    issuu_url_file = open(issuu_url_json, "r").read()
    return json.loads(issuu_url_file)


def main():
    issuu_url_list = get_issuu_json_as_dict()

    for issuu_url in issuu_url_list:
        name, url = issuu_url.values()

        url_to_open = str(urllib.request.urlopen(url).read().decode("utf-8"))

        # Credits to https://txt2re.com/ for the regex (Almost all of it)
        re1 = '.*?'
        re2 = '((?:http|https)(?::\\/{2}[\\w]+)(?:[\\/|\\.]?)(?:[^\\s"]*)(?:png|jpg))'

        rg = re.compile(re1+re2, re.IGNORECASE | re.DOTALL)
        m = rg.search(url_to_open)
        if m:
            http_url = m.group(1)
            print('Starting from URI: ' + http_url)
            filelist = downloader.downloader(http_url)
            pdf.creator(filelist, name)
        else:
            print("Error! No image was found")

        downloader.delete_old_images()


if __name__ == '__main__':
    main()
