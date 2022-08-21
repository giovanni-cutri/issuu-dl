import os
import requests
import bs4
import lxml
import re
import urllib.request

current_dir = os.getcwd()

print("Paste the link of the publication you want to download:")
link = input()

res = requests.get(link)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "lxml")

publication_name_raw = soup.select("meta[property='og:title']")[0].attrs["content"]
publication_name = publication_name_raw.replace("/", " ").replace(":", "").replace("*", " ").replace("?", "")\
    .replace("'", " ").replace("<", "").replace(">", "").replace("|", "").rstrip()

publication_dir = os.path.join(current_dir, "publications", publication_name, "")
os.makedirs(publication_dir)

images_link = soup.select("meta[property='og:image']")[0].attrs["content"][:-5]
pages_number = int(re.findall(re.compile("pageCount.*?,&quot"), res.text)[0][:-6][16:])

for i in range(1, pages_number+1):
    print("Saving page " + str(i) + " of " + str(pages_number) + "...")
    urllib.request.urlretrieve(images_link + str(i) + ".jpg", publication_dir + str(i) + ".jpg")

print("Done.")
input()
