from pathlib import Path
import shutil
import argparse

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".md", ".csv", ".xlsx"},
    "Music": {".mp3", ".wav", ".m4a", ".flac"},
    "Videos": {".mp4", ".mov", ".avi", ".mkv"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Code": {".py", ".java", ".c", ".cpp", ".js", ".html", ".css"},
}

def get_category(extension):
    extension = extension.lower()
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return "Others"

def organize(folder):
    folder = Path(folder).expanduser().resolve()

    if not folder.exists() or not folder.is_dir():
        print(f"Folder not found: {folder}")
        return

    moved = 0

    for item in folder.iterdir():
        if not item.is_file() or item.name.startswith("."):
            continue

        category = get_category(item.suffix)
        destination = folder / category
        destination.mkdir(exist_ok=True)

        target = destination / item.name
        counter = 1

        while target.exists():
            target = destination / f"{item.stem}_{counter}{item.suffix}"
            counter += 1

        shutil.move(str(item), str(target))
        print(f"✓ {item.name} -> {category}/")
        moved += 1

    print(f"\nDone! Organized {moved} file(s).")

def main():
    parser = argparse.ArgumentParser(
        description="FileFlow - Organize files by type."
    )
    parser.add_argument(
        "folder",
        nargs="?",
        default=".",
        help="Folder to organize (default: current folder)"
    )
    args = parser.parse_args()
    organize(args.folder)

if __name__ == "__main__":
    main()
