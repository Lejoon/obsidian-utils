import os
import re

def replace_tags_in_yaml(directory, old_tag, new_tag):
    """
    This function traverses a directory of markdown files recursively, and replaces
    specific tags inside YAML metadata blocks.

    Parameters:
    directory (str): The directory path of Obsidian vault or any directory where the markdown files are stored.
    old_tag (str): The tag which needs to be replaced.
    new_tag (str): The tag which will replace the old tag.

    Returns:
    None

    Example Usage:
    replace_tags_in_yaml("/path/to/your/obsidian/library", "old_tag", "new_tag")
    """
    
    for subdir, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".md"):  # if file is a Markdown file
                filepath = subdir + os.sep + filename
                with open(filepath, 'r') as file:
                    lines = file.readlines()
                
                # flag to mark if we are inside YAML block
                in_yaml = False
                for i, line in enumerate(lines):
                    # Check for YAML start or end
                    if '---' in line:
                        in_yaml = not in_yaml
                        continue
                    if in_yaml:
                        # replace the tag if we are inside the YAML
                        if old_tag in line:
                            lines[i] = line.replace(old_tag, new_tag)
                
                # write back the changes to the file
                with open(filepath, 'w') as file:
                    file.writelines(lines)
