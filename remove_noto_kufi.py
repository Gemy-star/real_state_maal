# -*- coding: utf-8 -*-
"""
Script to remove all noto-kufi-arabic class references from HTML templates
"""
import os
import re
from pathlib import Path


def remove_noto_kufi_class(file_path):
    """Remove noto-kufi-arabic class from HTML file"""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content

    # Remove "noto-kufi-arabic" class with surrounding space variations
    # Handles: class="some-class noto-kufi-arabic other-class"
    content = re.sub(r"\s+noto-kufi-arabic\s+", " ", content)
    # Handles: class="noto-kufi-arabic other-class"
    content = re.sub(r'class="noto-kufi-arabic\s+', 'class="', content)
    # Handles: class="some-class noto-kufi-arabic"
    content = re.sub(r'\s+noto-kufi-arabic"', '"', content)
    # Handles: class="noto-kufi-arabic" (only class)
    content = re.sub(r'\s+class="noto-kufi-arabic"', "", content)

    if content != original_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False


def main():
    templates_dir = Path("templates")
    modified_files = []

    # Find all HTML files
    html_files = list(templates_dir.rglob("*.html"))

    print(f"Found {len(html_files)} HTML files")
    print("Removing noto-kufi-arabic class references...\n")

    for html_file in html_files:
        if remove_noto_kufi_class(html_file):
            modified_files.append(html_file)
            print(f"✓ Modified: {html_file}")

    print(f"\n✅ Done! Modified {len(modified_files)} files")
    print(
        "\nAlmarai font is already loaded in base.html and will be the default font family."
    )


if __name__ == "__main__":
    main()
