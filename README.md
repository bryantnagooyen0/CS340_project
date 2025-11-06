# CS340 Project

This is a small Flask project for CS340.

What's included
- `app.py` – Flask application
- `database/` – DB connector and DB-related code
- `templates/`, `static/` – UI files

Dependencies
- Python 3.8+
- See `requirements.txt` (Flask, mysqlclient)

Quick local setup
1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python app.py
```

Notes about MySQL
- The project uses `MySQLdb` (provided by the `mysqlclient` package). On Linux you might need system packages (e.g., `libmysqlclient-dev` or `default-libmysqlclient-dev`) before installing `mysqlclient`.

Sharing on GitHub
- I initialized a local git repository and made an initial commit (see below).
- To publish to GitHub, create an empty repo on GitHub and then run:

```bash
# replace <URL> with your remote URL (https://github.com/<you>/<repo>.git)
cd /nfs/stak/users/nguyeb25/CS340/project
git remote add origin <URL>
git branch -M main
git push -u origin main
```

Or, using the GitHub CLI (logged in):

```bash
cd /nfs/stak/users/nguyeb25/CS340/project
gh repo create <repo-name> --public --source=. --remote=origin --push
```

Invite a classmate
- On GitHub: Settings -> Collaborators -> Add their username
- Or using `gh`:

```bash
gh repo add-collaborator <owner>/<repo> --user <their-username> --permission write
```

If you'd like, I can also create the repo on your GitHub account using `gh` if you authorize and have `gh` installed.
