# Obsidian Utils

Obsidian Utils is a collection of Python scripts that serve as utility tools for the Obsidian note-taking application. The tool includes functions to manipulate tags, links, and metadata in Obsidian notes stored as Markdown files.

## Features

* Replace specific tags in YAML metadata across all Obsidian notes.
* Traverse recursively all subdirectories in the Obsidian library.
* And many more utility functions coming soon!

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.6+
* Obsidian

### Installation

1. Clone the repository: `git clone https://github.com/Lejoon/obsidian-utils.git`
2. Navigate to the cloned directory: `cd obsidian-utils`
3. Install the required packages: `pip install -r requirements.txt`

### Usage

* Replace tags in YAML metadata blocks:

    ```python
    from obsidian_utils import replace_tags_in_yaml

    replace_tags_in_yaml("/path/to/your/obsidian/library", "old_tag", "new_tag")
    ```

## License

This project is licensed under the MIT License.