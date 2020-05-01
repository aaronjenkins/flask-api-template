# flask-api-template

how to run 
1. docker-compose up --build
2. go to http://localhost:80

# how to debug backend
1. ```cd ./backend```
2. ```pip install --user -r requirements.txt```
3. put this in your .vscode/launch.json
```
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Flask",
      "type": "python",
      "request": "launch",
      "module": "flask",
      "env": {
        "FLASK_APP": "./api.py",
        "FLASK_ENV": "development",
        "FLASK_DEBUG": "1"
      },
      "args": ["run", "--no-debugger", "--no-reload"],
      "jinja": true
    }
  ]
}
```
2. run command 
    - Linux or MacOs ```export_APP_SETTINGS=$PWD/backend/config/LOCALCONFIG.py```
    - Windows ```set APP_SETTINGS=%cd%/backend/config/LOCALCONFIG.py```
3. then launch debug in VSCode