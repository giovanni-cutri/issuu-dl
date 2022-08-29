import argparse
import requests
import bs4
import re
import os
import sys
import urllib.request
import zipfile
from PIL import Image


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="the URL of the publication you want to download")
    parser.add_argument("-p", "--pdf", help="generate a PDF for the publication", action="store_true")
    parser.add_argument("-z", "--zip", help="generate a zipped file for the publication")
    args = parser.parse_args()
    return args


def download(args):
    res = requests.get(args.url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")
    publication_name = get_publication_name(soup)
    save(soup, publication_name, res, args)


def get_publication_name(soup):
    publication_name_raw = soup.select("meta[property='og:title']")[0].attrs["content"]
    publication_name = clean_name(publication_name_raw)
    return publication_name


def clean_name(publication_name_raw):
    cleaned_name = re.sub('[^A-Za-z0-9 ]+', '', publication_name_raw)
    return cleaned_name


def save(soup, publication_name, res, args):
    current_dir = os.getcwd()
    publication_dir = os.path.join(current_dir, "issuu-publications", publication_name, "")
    create_directory(publication_dir)
    download_images(soup, res, publication_dir)
    download_pdf(args, publication_dir, publication_name)
    download_zip(args, publication_dir, publication_name)


def create_directory(publication_dir):
    try:
        os.makedirs(publication_dir)
    except FileExistsError:
        print("Publication has already been downloaded.")
        sys.exit()


def download_images(soup, res, publication_dir):
    images_link = soup.select("meta[property='og:image']")[0].attrs["content"][:-5]  # get boilerplate link for images
    pages_number = int(re.findall(re.compile("pageCount.*?,&quot"), res.text)[0][:-6][16:])
    for i in range(1, pages_number+1):
        print("Saving page " + str(i) + " of " + str(pages_number) + "...")
        urllib.request.urlretrieve(images_link + str(i) + ".jpg", publication_dir + str(i) + ".jpg")


def download_pdf(args, publication_dir, publication_name):

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


def download_zip(args, publication_dir, publication_name):

    if args.zip:
        print("Generating zipped file...")
        list_of_files = os.listdir(publication_dir)
        with zipfile.ZipFile(publication_name + '.zip', 'w') as zipped_file:
            for file in list_of_files:
                zipped_file.write(file, compress_type=zipfile.ZIP_DEFLATED)
        print("Done.")


def main():
    args = parse_arguments()
    download(args)


main()
