# issuu-dl
 
A simple tool to download publications from [issuu.com](https://issuu.com/), written in Python.

## Installation

You can install issuu-dl by downloading the release binary (currently available only for Windows):

[issuu-dl.exe](https://github.com/giovanni-cutri/issuu-dl/releases/download/v1.0.0/issuu-dl.exe)


## Dependencies

All the necessary libraries are listed in the *requirements.txt* file.

You can install them by running:

```
pip install -r requirements.txt
```

## Usage

```
issuu-dl [OPTIONS] [--] URL [URL...] 
```

By default, the publication is downloaded as a collection of *.jpg* files which gets saved inside a folder with the name of the publication.

Currently, the available options are:

```
-h, --help  show this help message and exit
-p, --pdf   generate a PDF for the publication
-z, --zip   generate a zipped file for the publication
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/giovanni-cutri/issuu-downloader/blob/main/LICENSE) file for details.
