import argparse
import sys
import os
import requests
import bs4
import lxml
import re
from PIL import Image
import urllib.request

parser = argparse.ArgumentParser()
parser.add_argument("url", help="the URL of the video you want to download")
parser.add_argument("-p", "--pdf", help="generate a PDF for the publication", action="store_true")
args = parser.parse_args()

link = args.url

res = requests.get(link)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "lxml")

publication_name_raw = soup.select("meta[property='og:title']")[0].attrs["content"]
publication_name = re.sub('[^A-Za-z0-9]+', '', publication_name_raw)

current_dir = os.getcwd()
publication_dir = os.path.join(current_dir, "publications", publication_name, "")

try:
    os.makedirs(publication_dir)
except FileExistsError:
    print("Publication has already been downloaded.")
    sys.exit()

images_link = soup.select("meta[property='og:image']")[0].attrs["content"][:-5]
pages_number = int(re.findall(re.compile("pageCount.*?,&quot"), res.text)[0][:-6][16:])

for i in range(1, pages_number+1):
    print("Saving page " + str(i) + " of " + str(pages_number) + "...")
    urllib.request.urlretrieve(images_link + str(i) + ".jpg", publication_dir + str(i) + ".jpg")

if args.pdf:

    print("Generating PDF...")

    images = [
        Image.open(publication_dir + f)
        for f in os.listdir(publication_dir)
    ]

    pdf_path = publication_dir + publication_name + ".pdf"

    images[0].save(
        pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
    )

print("Done.")
