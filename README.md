# MutualCheck: Instagram Followers Checker
A tool to compare your Instagram followers and following lists to identify non-mutual connections.

## Getting Started
1. **Install Python**
    - Go to [python.org](https://www.python.org/) and download the latest version of Python
    - During installation, check **Add python.exe to PATH**, then select **Install Now** to get pip (Python's package installer)
    - After installation, verify that Python and pip are installed by running:
        ```bash
        python --version
        pip --version
        ```

2. **Download MutualCheck**
    - If you are not already on the repository page, go to the [GitHub Repository Page](https://github.com/arhamislam/mutual-check)
    - Click the green **Code** button
    - Select **Download ZIP**
    - Extract the ZIP file to a folder on your computer

3. **Set Up Your Instagram Credentials**
    - Open a terminal
    - Navigate to the extracted folder:
        - On Windows, run `cd path\to\your\folder`
        - On Linux/MacOS, run `cd path/to/your/folder`
    - Copy `.env.example` to `.env` by running `cp .env.example .env`
    - Open `.env` in a text editor of your choice and fill in your Instagram credentials by replacing the placeholder values, then save the file

4. **Install Dependecies**
    - On your terminal, run `pip install -r requirements.txt`

5. **Run**
    - On your terminal, run `python main.py`

## Notes
- Never share your `.env` file or commit it to version control
- This project is for personal use only. Use responsibly and be aware that automating Instagram may violate their Terms of Service

## Credits
Developed by [@arhamislam](https://github.com/arhamislam) on May XX, 2025.
