# File Format Converter

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Supported Formats](#supported-formats)
- [Examples](#examples)
- [Contributing](#contributing)
- [Contact](#contact)

## Description
The File Format Converter is a Python application designed to convert CSV files to JSON format based on a predefined schema. The tool reads CSV files, transforms them according to the specified schema, and outputs JSON files. This project is ideal for data processing pipelines where structured data transformation is required.

## Features
- **Schema-based Conversion**: Ensures that CSV data is transformed according to predefined column details.
- **Automatic Directory Handling**: Creates necessary directories for storing output files.
- **Environment Variable Configuration**: Uses environment variables for flexible configuration of source and target directories.
- **Error Handling**: Gracefully handles errors and provides informative messages during processing.

## Installation
### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)
- [dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/Lashmanbala/file_format_converter.git
    cd file_format_converter
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and set the following variables:
    ```env
    SRC_BASE_DIR=/path/to/source/base/dir
    TGT_BASE_DIR=/path/to/target/base/dir
    ```

## Usage
To convert CSV files to JSON format, use the following command:
```bash
python app.py '["dataset1", "dataset2"]'
