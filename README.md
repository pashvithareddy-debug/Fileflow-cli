# FileFlow CLI

A lightweight Python CLI that automatically organizes files into folders based on their file type.

## Features

- Organizes images, documents, music, videos, archives, and code
- Creates folders automatically
- Handles duplicate filenames safely
- Works with any folder path
- No external dependencies

## Project Structure

```text
fileflow-cli/
├── fileflow.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Requirements

- Python 3.9+

## Usage

Organize the current folder:

```bash
python fileflow.py
```

Organize a specific folder:

```bash
python fileflow.py ~/Downloads
```

Example:

```text
Downloads/
├── photo.jpg
├── resume.pdf
├── song.mp3
└── project.zip
```

After running FileFlow:

```text
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── resume.pdf
├── Music/
│   └── song.mp3
└── Archives/
    └── project.zip
```

## Tech Stack

- Python
- pathlib
- shutil
- argparse

## License

MIT
