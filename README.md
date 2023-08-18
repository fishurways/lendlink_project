# lendlink_project

Project ini nantinya berfungsi untuk mencatat peminjaman alat PHS.

## Fitur
- user bisa register by email
- user bisa sign in
- mengetahui status peminjaman alat
- sebagai tools untuk inventaris alat

## How to run this project
```
cd project_dir
# pull from repo first
git pull
# install any new package (if any)
pip install -r requirements.txt
# activate the virtual environment
. bin/activate
# atau kalo di windows
Set-ExecutionPolicy Unrestricted -Scope Process
Scripts\activate
# run flask server with debug mode On
flask --app .app/views.py --debug run
```