# Plagiarism Detection Tool

## Overview
The Plagiarism Detection Tool is designed to compare two text files and detect similarity, helping to identify potential plagiarism. The tool uses Levenshtein Distance and Cosine Similarity algorithms to measure similarity based on the content type, whether it's code or plain text.

## Features
- Reads and preprocesses text files.
- Measures similarity using:
  - **Levenshtein Distance** for code comparisons.
  - **Cosine Similarity** for plain text comparisons.
- Automatically identifies if the content is code or regular text.
- Outputs similarity percentages and detects potential plagiarism.

## Requirements
- Python 3.x
- Required libraries: `collections`, `math`, `re`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/plagiarism-detection-tool.git
2. Navigate to the project directory:
    ```bash
   cd plagiarism-detection-tool
   
## Usage
1. Place the two text files you want to compare in the ./Test/ directory. 
2. Modify the file paths in the main() function of plagiarism_detection.py if necessary.
3. Run it:
    ```bash
   python plagiarism_detection.py

## Example
To check for plagiarism between test1.txt and test2.txt in the ./Test/ directory, the tool will output the similarity percentage and whether plagiarism is detected.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

