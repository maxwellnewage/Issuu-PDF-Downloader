import os
import urllib
import requests
from utils import IMAGE_DIR


def exists(path):
    # Check that image exists
    r = requests.head(path)
    return r.status_code == requests.codes.ok


def delete_old_images():
    for image in os.listdir(IMAGE_DIR):
        if image.endswith(".jpg"):
            os.remove(os.path.join(IMAGE_DIR, image))


def downloader(url):
    print('Started download process...')
    # List to create the PDF
    files = []
    formatter = url.replace('page_1.jpg', '')
    page_counter = 1
    while True:
        url_page = formatter + 'page_' + str(page_counter) + '.jpg'
        filename = str(page_counter) + '.jpg'
        if exists(url_page):
            # Save image directory
            filename_with_folder = os.path.join(IMAGE_DIR, filename)
            # Download images
            opener = open(filename_with_folder, 'wb')
            opener.write(urllib.request.urlopen(url_page).read())
            # Save images
            opener.close()
            print(f'Correctly saved file {filename} From URI: {url_page}')
            # Add filename to list, so we make the pdf later
            files.append(filename_with_folder)
            # Go for the next one
            page_counter += 1
        else:
            # No more images
            break

    print('Completed download process...')
    # Time to create the pdf
    return files
