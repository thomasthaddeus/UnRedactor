#!/bin/bash

# Create project directory
mkdir UnredacterProject
cd UnredacterProject

# Create necessary subdirectories and files
mkdir src tests logs data assets
touch src/image_processor.py src/styler.py src/char_tester.py src/result_displayer.py src/main.py src/tests.py

# Create a README file
echo "# Unredacter Project" > README.md
echo "A Python implementation of a program to unredact pixelated text." >> README.md

# Create a .gitignore file
cat "/mnt/e/gitignore/python.gitignore" >> .gitignore

# Initialize a git repository and make an initial commit
git init
git add .
git commit -m "Initial commit"

# Create a virtual environment and activate it
python3 -m venv .venv
source .venv/bin/activate

# Optionally, add a requirements.txt file if there are specific library dependencies
echo "tkinter" > requirements.txt
pip install -r requirements.txt

echo "Project setup complete and ready for GitHub!"
