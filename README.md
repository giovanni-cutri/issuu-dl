# Issuu-Downloader
 
A simple tool to download publications from issuu.com, written in Python.

# Installation

You can install issuu-dl by downloading the release binary (currently available only for Windows):

[issuu-dl-win.exe](https://github.com/giovanni-cutri/issuu-downloader/releases/download/v0.1.0/issuu-dl-win.exe)

# Dependencies

All the necessary libraries are listed in the *requirements.txt* file.

You can install them by running:

```
pip install -r requirements.txt
```

# Usage

```
issuu-dl-win [OPTIONS] [--] URL [URL...] 
```

Currently, the only available options are:

```
-h, --help  show this help message and exit
-p, --pdf   generate a PDF for the publication
```

# License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/giovanni-cutri/issuu-downloader/blob/main/LICENSE) file for details.
