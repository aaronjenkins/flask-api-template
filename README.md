# flask-api-template

how to run 
1. docker-compose up --build
2. go to http://localhost:5000/ping
3. it will return 'pong'

# how to debug backend
1. ```pip install --user -r requirements.txt```
2. put this in your .vscode/launch.json
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
3. run command 
    - Linux or MacOs ```export_APP_SETTINGS=$PWD/config/LOCALCONFIG.py```
    - Windows ```set APP_SETTINGS=%cd%/config/LOCALCONFIG.py```
4. then launch debug in VSCode
