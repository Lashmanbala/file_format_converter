# File Format Converter

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#Example)
- [Configuration](#configuration)
- [Supported Formats](#supported-formats)
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
- Python 3.10
- pip (Python package installer)
- dotenv for managing environment variables

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
```
- Replace ["dataset1", "dataset2"] with the list of datasets you want to process.

## Example
To convert the categories and products datasets:
```bash
python app.py '["categories", "products"]'
```
If you want to process all datasets defined in schemas.json, simply run:
```bash
python app.py
```
## Configuration
### Schema Definition
The schema for each dataset should be defined in schemas.json located in the source base directory. Each dataset's schema should specify the column names and their positions.
### Supported Formats
- Input: CSV
- Output: JSON
## Contact
For any questions, issues, or suggestions, please feel free to contact the project maintainer:

GitHub: [Lashmanbala](https://github.com/Lashmanbala)

LinkedIn: [Lashmanbala](https://www.linkedin.com/in/lashmanbala/)
