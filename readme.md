# VIRTUALENV

virtualenv -p python3 venv
source venv/bin/activate
pip freeze > requirements.txt
pip install -r requirements.txt


# GITHUB 
mkdir my_project
cd my_project
git init
git config --local user.email "myemail"
git config --local user.name "myusername"

touch .gitignore
# /venv
# config.py
# .DS_Store

git status
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://diegopenuela: (MYTOKEN) @github.com/diegopenuela/phonenumbers_tour.git

git remote set-url origin https://diegopenuela: (MYTOKEN) @github.com/diegopenuela/phonenumbers_tour.git
git push -u origin main

# TWILIO 
pip install twilio