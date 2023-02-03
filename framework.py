import re
import urllib
import core.downloader as downloader
import core.pdf as pdf


def main():
    url = "https://issuu.com/revistareplay/docs/numero3_replay_anticipo"
    url_open1 = str(urllib.request.urlopen(url).read().decode("utf-8"))

    # Credits to https://txt2re.com/ for the regex (Almost all of it)
    re1 = '.*?'
    re2 = '((?:http|https)(?::\\/{2}[\\w]+)(?:[\\/|\\.]?)(?:[^\\s"]*)(?:png|jpg))'

    rg = re.compile(re1+re2, re.IGNORECASE | re.DOTALL)
    m = rg.search(url_open1)
    if m:
        http_url = m.group(1)
        print('Starting from URI: ' + http_url)
        filelist = downloader.downloader(http_url)
        pdf.creator(filelist)
    else:
        print("Error! No image was found")


if __name__ == '__main__':
    main()
