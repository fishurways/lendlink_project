# lendlink_project

Project ini nantinya berfungsi untuk mencatat peminjaman alat PHS.

## Python Library Needed
- flask framework
- flask login
- flask bootstrap

## Tools Needed
- mysql
- 

## Fitur
- user bisa register by email
- user bisa sign in
- mengetahui status peminjaman alat
- sebagai tools untuk inventaris alat

## Todo
- [ ] user auth
-- [ ] create login page
-- [ ] create register page
-- [ ] create profile page for registered user
- [ ] dbase schema

## How to run this project
```
$ cd project_dir
# pull from repo first
$ git pull
# install any new package (if any)
$ pip install -r requirements.txt
# activate the virtual environment
$ . bin/activate
# atau kalo di windows
$ Set-ExecutionPolicy Unrestricted -Scope Process
$ Scripts\activate
# run flask server with debug mode On
$ flask --app .app/views.py --debug run
# or if you prefer using gunicorn
$ gunicorn app.views:app
```

# heroku
```
1. install heroku
curl https://cli-assets.heroku.com/install.sh | sh
2. heroku login
heroku login
3. set git remote
heroku git:remote -a lendlink-project 
4. update to heroku repo
git push heroku main
```

## Reference
- Flask Login Tuts: https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
- Flask Login Github: https://github.com/maxcountryman/flask-login
- HTML login page: https://mdbootstrap.com/docs/standard/extended/login/