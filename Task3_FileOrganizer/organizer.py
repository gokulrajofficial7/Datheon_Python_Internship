"""
Datheon Python Programming Internship - Task 3
Automated File Organizer & Cleanup Utility

Features:
- Dynamically organizes cluttered directories (e.g. Downloads, Desktop)
- Categorizes by file extensions: Documents, Images, Videos, Audio, Archives, Code, Others
- Automatic filename collision resolution (e.g., 'document_1.pdf')
- Exception handling for PermissionError and FileExistsError
- Formatted execution summary report showing relocated files count
- Built-in demo cluttered test directory generator for safe demonstration
"""

import os
import shutil
from pathlib import Path

# Mapping of file extensions to target category folders
CATEGORY_MAPPING = {
    # Documents
    ".pdf": "Documents",
    ".docx": "Documents",
    ".doc": "Documents",
    ".txt": "Documents",
    ".xlsx": "Documents",
    ".csv": "Documents",
    ".pptx": "Documents",
    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".svg": "Images",
    ".webp": "Images",
    # Videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    # Archives
    ".zip": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    # Code / Scripts
    ".py": "Code",
    ".java": "Code",
    ".js": "Code",
    ".html": "Code",
    ".css": "Code",
    ".json": "Code",
    ".cpp": "Code",
    ".c": "Code"
}


def get_unique_destination_path(target_folder, filename):
    """
    Prevents file overwriting by incrementing an index suffix if a filename collision occurs.
    Example: 'report.pdf' -> 'report_1.pdf' -> 'report_2.pdf'
    """
    dest_path = target_folder / filename
    if not dest_path.exists():
        return dest_path

    stem = Path(filename).stem
    suffix = Path(filename).suffix
    counter = 1
    while True:
        new_filename = f"{stem}_{counter}{suffix}"
        new_dest_path = target_folder / new_filename
        if not new_dest_path.exists():
            return new_dest_path
        counter += 1


def organize_directory(directory_path):
    """
    Scans the given directory and sorts top-level files into category subdirectories.
    """
    target_dir = Path(directory_path).resolve()
    if not target_dir.exists() or not target_dir.is_dir():
        print(f"[Error] Target directory '{directory_path}' does not exist or is not a valid directory.")
        return

    print("\n" + "=" * 70)
    print(f"  ORGANIZING DIRECTORY: {target_dir}")
    print("=" * 70)

    category_counts = {}
    total_moved = 0
    errors_encountered = 0

    # Read items in the target directory (only top-level files, skipping existing category dirs)
    try:
        with os.scandir(target_dir) as entries:
            for entry in entries:
                # Process only files (ignore subdirectories to prevent nested infinite reorganization)
                if entry.is_file():
                    file_path = Path(entry.path)
                    ext = file_path.suffix.lower()
                    category = CATEGORY_MAPPING.get(ext, "Others")

                    category_folder = target_dir / category
                    try:
                        category_folder.mkdir(exist_ok=True)
                        dest_path = get_unique_destination_path(category_folder, file_path.name)
                        shutil.move(str(file_path), str(dest_path))
                        
                        category_counts[category] = category_counts.get(category, 0) + 1
                        total_moved += 1
                        print(f" [MOVED] {file_path.name:<25} -> /{category}/{dest_path.name}")
                    except PermissionError:
                        print(f" [PERMISSION DENIED] Could not move '{file_path.name}' (file in use or access locked).")
                        errors_encountered += 1
                    except Exception as e:
                        print(f" [ERROR] Could not relocate '{file_path.name}': {e}")
                        errors_encountered += 1

    except Exception as e:
        print(f"[Fatal Scan Error] Failed reading directory: {e}")
        return

    # Print summary report
    print("\n" + "=" * 70)
    print("                     EXECUTION SUMMARY REPORT                         ")
    print("=" * 70)
    print(f" Total Files Relocated : {total_moved}")
    print(f" Errors Encountered    : {errors_encountered}")
    print(" Category Breakdown:")
    for cat, count in sorted(category_counts.items()):
        print(f"   • {cat:<12} : {count} file(s)")
    if total_moved == 0:
        print("   • No loose files required relocation.")
    print("=" * 70)


def generate_sample_cluttered_folder(base_folder):
    """
    Generates a mock cluttered folder with dummy files to demonstrate the script safely.
    """
    demo_dir = Path(base_folder) / "demo_clutter"
    demo_dir.mkdir(exist_ok=True)

    sample_files = [
        "annual_financial_report.pdf",
        "meeting_agenda.docx",
        "notes.txt",
        "vacation_photo.jpg",
        "logo_transparent.png",
        "product_demo.mp4",
        "podcast_episode.mp3",
        "project_backup.zip",
        "etl_script.py",
        "frontend_bundle.js",
        "unknown_format.xyz"
    ]

    for fname in sample_files:
        sample_path = demo_dir / fname
        if not sample_path.exists():
            with open(sample_path, "w", encoding="utf-8") as f:
                f.write(f"This is a dummy test file content for: {fname}\n")

    print(f"\n[Demo Environment] Generated {len(sample_files)} sample files in: '{demo_dir}'.")
    return demo_dir


def main():
    print("=================================================================")
    print("    DATHEON - AUTOMATED FILE ORGANIZER & CLEANUP UTILITY         ")
    print("=================================================================")

    current_dir = Path(__file__).parent.resolve()

    while True:
        print("\n-------------------- ORGANIZER MENU --------------------")
        print("1. Organize a Custom Directory (Specify Path)")
        print("2. Run Demo Organization on Test Cluttered Directory")
        print("3. Exit")
        print("--------------------------------------------------------")

        try:
            choice = input("Select an option (1-3): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting organizer.")
            break

        if choice == "1":
            target = input("Enter directory path to organize: ").strip()
            if target:
                organize_directory(target)
            else:
                print("[Error] Path cannot be empty.")
        elif choice == "2":
            demo_path = generate_sample_cluttered_folder(current_dir)
            organize_directory(demo_path)
        elif choice == "3":
            print("\nDirectory organization utility closed. Happy Automating with Datheon!")
            break
        else:
            print("[Error] Invalid option. Choose 1 to 3.")


if __name__ == "__main__":
    main()
