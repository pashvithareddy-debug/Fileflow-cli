# FileFlow CLI

> **Turn a cluttered folder into an organized workspace — in one command.**

FileFlow CLI is a lightweight, zero-dependency Python command-line utility that automatically organizes files into meaningful folders based on their extensions.

Instead of manually sorting a Downloads folder filled with documents, images, videos, archives, music, and source code, FileFlow handles the repetitive work for you.

---

## ✨ Highlights

* 🚀 **One-command organization** — clean up a folder instantly
* 📂 **Automatic categorization** — files are grouped by type
* 🛡️ **Safe duplicate handling** — existing files are never overwritten
* ⚡ **Zero external dependencies** — built entirely with Python's standard library
* 🖥️ **Cross-platform** — works on macOS, Linux, and Windows
* 🎯 **Simple CLI interface** — no configuration file or setup required
* 🔍 **Transparent execution** — every moved file is displayed in the terminal

---

## 🎬 How It Works

FileFlow follows a simple processing pipeline:

```text
                 ┌─────────────────┐
                 │   Target Folder │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │   Scan Files    │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Read Extension  │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Classify File   │
                 └────────┬────────┘
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
        Documents      Images       Videos
             │            │            │
             └────────────┼────────────┘
                          ▼
                 ┌─────────────────┐
                 │   Move Safely   │
                 └─────────────────┘
```

---

## 📁 Before & After

### Before

A typical unorganized folder:

```text
Downloads/
├── resume.pdf
├── photo.jpg
├── project.zip
├── song.mp3
├── lecture.mp4
├── program.py
└── notes.txt
```

### Run FileFlow

```bash
python fileflow.py ~/Downloads
```

### After

```text
Downloads/
├── Archives/
│   └── project.zip
├── Code/
│   └── program.py
├── Documents/
│   ├── notes.txt
│   └── resume.pdf
├── Images/
│   └── photo.jpg
├── Music/
│   └── song.mp3
└── Videos/
    └── lecture.mp4
```

---

## 🛠️ Supported Categories

| Category      | Extensions                                              |
| ------------- | ------------------------------------------------------- |
| **Images**    | `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.svg`        |
| **Documents** | `.pdf`, `.doc`, `.docx`, `.txt`, `.md`, `.csv`, `.xlsx` |
| **Music**     | `.mp3`, `.wav`, `.m4a`, `.flac`                         |
| **Videos**    | `.mp4`, `.mov`, `.avi`, `.mkv`                          |
| **Archives**  | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`                    |
| **Code**      | `.py`, `.java`, `.c`, `.cpp`, `.js`, `.html`, `.css`    |
| **Others**    | Any unsupported extension                               |

---

## 🚀 Getting Started

### Prerequisites

Make sure Python 3.9 or later is installed:

```bash
python --version
```

### Clone the Repository

```bash
git clone https://github.com/pashvithareddy-debug/fileflow-cli.git
cd fileflow-cli
```

### Run FileFlow

No package installation is required.

Organize the current directory:

```bash
python fileflow.py
```

Organize a specific directory:

```bash
python fileflow.py ~/Downloads
```

---

## 💻 Example

```text
$ python fileflow.py ~/Downloads

✓ report.pdf -> Documents/
✓ vacation.jpg -> Images/
✓ music.mp3 -> Music/
✓ project.zip -> Archives/
✓ app.py -> Code/

Done! Organized 5 file(s).
```

FileFlow provides immediate feedback so you can see exactly what was moved.

---

## 🛡️ Safe File Handling

FileFlow is designed to avoid accidental overwrites.

If a file with the same name already exists in the destination folder:

```text
report.pdf
report_1.pdf
report_2.pdf
report_3.pdf
```

The existing file remains untouched, while the incoming file receives a unique name.

---

## 🧩 Project Structure

```text
fileflow-cli/
│
├── fileflow.py          # Core CLI application
├── README.md            # Project documentation
├── requirements.txt     # Dependency declaration
├── LICENSE              # MIT License
└── .gitignore           # Git exclusions
```

---

## 🏗️ Technical Overview

FileFlow intentionally uses only Python's standard library.

### Core Components

**`pathlib`**

* Handles filesystem paths
* Provides platform-independent path operations
* Scans directory contents

**`shutil`**

* Performs file movement
* Handles filesystem operations

**`argparse`**

* Provides the command-line interface
* Supports optional folder arguments
* Generates CLI help automatically

### Processing Flow

```text
CLI Argument
     │
     ▼
Validate Directory
     │
     ▼
Scan Files
     │
     ▼
Extract Extension
     │
     ▼
Find Matching Category
     │
     ▼
Create Destination Folder
     │
     ▼
Check Filename Collision
     │
     ▼
Move File
     │
     ▼
Display Result
```

---

## ⚡ Why No Dependencies?

FileFlow does not require third-party Python packages.

That means:

* No `pip install` step
* No virtual environment required
* Smaller project footprint
* Faster startup
* Fewer dependency conflicts

`requirements.txt` is included for standard project structure and future extensibility.

---

## 🔮 Roadmap

Potential future improvements:

* [ ] Custom category configuration
* [ ] Dry-run mode
* [ ] Recursive directory organization
* [ ] File size-based categorization
* [ ] Date-based organization
* [ ] Undo / restore functionality
* [ ] Colored terminal output
* [ ] Interactive CLI mode
* [ ] Configuration file support
* [ ] Unit and integration tests
* [ ] PyPI package distribution

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/your-feature
```

3. Make your changes
4. Commit your work

```bash
git commit -m "Add your feature"
```

5. Push the branch

```bash
git push origin feature/your-feature
```

6. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

See [`LICENSE`](LICENSE) for details.

---

## 👩‍💻 Author

**Ashvitha Reddy**

Computer Science & Engineering student building practical developer tools and software projects.

GitHub: [@pashvithareddy-debug](https://github.com/pashvithareddy-debug)

---

## ⭐ Support

If FileFlow helped you organize your files, consider giving the repository a ⭐ on GitHub.
