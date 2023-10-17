Firstly, clone the repository in your local machine

```bash
    $ git clone url
    $ cd velox_system_sql
```

Then create virtual environment with the following command.

```bash
    $ python m-venv myenv
    $ source myenv/bin/activate
```

Then install the dependencies from the requirements.txt file.

```bash
    (myenv)$ pip install -r requirements.txt
```
Once the required dependencies are installed, change to project directory and start the project.

```bash
    (myenv)$ python manage.py runserver
```
And navigate to http://127.0.0.1:8000/