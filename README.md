# Bing AI Unofficial api

* It uses playwright and firefox to open browser and parse html.
* It is an unofficial api for development purpose only.

```
Playwright comes with three web browsers to my knowledge;

* Chromiun - Chrome
* Firefox
* Webkit
```

However, as of currently, Microsoft requires you use Microsoft Edge for Bing AI, so install Edge from the Windows Store or https://www.microsoft.com/en-us/edge.

# How to install

* Make sure that python and virtual environment is installed. In my case, i'm using PyCharm.

* Create a new virtual environment

```python
# one time
virtualenv -p $(which python3) pyenv

# everytime you want to run the server
source pyenv/bin/activate

## in my case, I used a virtual environment in pycharm, so i didn't use the two steps above.
```

* Now install the requirements

```
pip install -r requirements.txt

PyCharm should automatically notify you to install this, if it finds the file in the project env.
```

* If you are installing playwright for the first time, it will ask you to run this command for one time only.

```
playwright install or

ms-playwright install (if playwright doesn't work)

Playwright didn't work for me so I used `ms-playwrigt` which worked well.
```

* Now run the server

```
python server.py or

python file_path of server.py on your pc/dev env.
```

* The server runs at port `5000`. If you want to change, you can change it in server.py


# Api Documentation

* There is a single end point only. It is available at `/chat`

```sh
curl -XGET http://localhost:5001/chat?q=Write%20a%20python%20program%20to%20reverse%20a%20list
```

# Updates

* [17 Feb 2023]: Initial release

