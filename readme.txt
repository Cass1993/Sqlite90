D:\Python projects\Sqlite\90's Flask Sqlite>

D:\Python projects\Sqlite\90's Flask Sqlite>git add .

D:\Python projects\Sqlite\90's Flask Sqlite>git commit -m "Update app to use Gunicorn and ensure correct port binding"
[master 73fc7a7] Update app to use Gunicorn and ensure correct port binding
 3 files changed, 5 insertions(+), 4 deletions(-)

D:\Python projects\Sqlite\90's Flask Sqlite>git push heroku master
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 592 bytes | 296.00 KiB/s, done.
Total 5 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Updated 5 paths from ddb4d53
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Building on the Heroku-24 stack
remote: -----> Using buildpack: heroku/python
remote: -----> Python app detected
remote: -----> No Python version was specified. Using the same major version as the last build: Python 3.13
remote:        To use a different version, see: https://devcenter.heroku.com/articles/python-runtimes
remote: -----> Discarding cache since:
remote:        - The contents of requirements.txt changed
remote: -----> Installing Python 3.13.1
remote: -----> Installing pip 24.3.1
remote: -----> Installing dependencies using 'pip install -r requirements.txt'
remote:        Collecting Flask (from -r requirements.txt (line 1))
remote:          Downloading flask-3.1.0-py3-none-any.whl.metadata (2.7 kB)
remote:        Collecting psycopg2-binary (from -r requirements.txt (line 2))
remote:          Downloading psycopg2_binary-2.9.10-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
remote:        Collecting gunicorn (from -r requirements.txt (line 3))
remote:          Downloading gunicorn-23.0.0-py3-none-any.whl.metadata (4.4 kB)
remote:        Collecting Werkzeug>=3.1 (from Flask->-r requirements.txt (line 1))
remote:          Downloading werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
remote:        Collecting Jinja2>=3.1.2 (from Flask->-r requirements.txt (line 1))
remote:          Downloading jinja2-3.1.5-py3-none-any.whl.metadata (2.6 kB)
remote:        Collecting itsdangerous>=2.2 (from Flask->-r requirements.txt (line 1))
remote:          Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
remote:        Collecting click>=8.1.3 (from Flask->-r requirements.txt (line 1))
remote:          Downloading click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
remote:        Collecting blinker>=1.9 (from Flask->-r requirements.txt (line 1))
remote:          Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
remote:        Collecting packaging (from gunicorn->-r requirements.txt (line 3))
remote:          Downloading packaging-24.2-py3-none-any.whl.metadata (3.2 kB)
remote:        Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->Flask->-r requirements.txt (line 1))
remote:          Downloading MarkupSafe-3.0.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.0 kB)
remote:        Downloading flask-3.1.0-py3-none-any.whl (102 kB)
remote:        Downloading psycopg2_binary-2.9.10-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
remote:        Downloading gunicorn-23.0.0-py3-none-any.whl (85 kB)
remote:        Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
remote:        Downloading click-8.1.8-py3-none-any.whl (98 kB)
remote:        Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
remote:        Downloading jinja2-3.1.5-py3-none-any.whl (134 kB)
remote:        Downloading werkzeug-3.1.3-py3-none-any.whl (224 kB)
remote:        Downloading packaging-24.2-py3-none-any.whl (65 kB)
remote:        Downloading MarkupSafe-3.0.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (23 kB)
remote:        Installing collected packages: psycopg2-binary, packaging, MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, gunicorn, Flask
remote:        Successfully installed Flask-3.1.0 Jinja2-3.1.5 MarkupSafe-3.0.2 Werkzeug-3.1.3 blinker-1.9.0 click-8.1.8 gunicorn-23.0.0 itsdangerous-2.2.0 packaging-24.2 psycopg2-binary-2.9.10
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote:
remote: -----> Compressing...
remote:        Done: 21.2M
remote: -----> Launching...
remote:        Released v6
remote:        https://sqlite90s-759926b87d78.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/sqlite90s.git
   00aac79..73fc7a7  master -> master