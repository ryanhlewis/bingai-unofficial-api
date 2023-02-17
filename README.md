# Bing AI Unofficial API

* It uses Playwright and Microsoft Edge to automate the browser and parse html from Bing.
* It is an unofficial API for development and educational purposes only.

```
Playwright comes with three web browsers:

* Chromiun - Chrome/Edge
* Firefox
* Webkit
```

However, as of currently, Microsoft requires you use Microsoft Edge for Bing AI, so install Edge from the Windows Store or https://www.microsoft.com/en-us/edge.

# How to install

* Install the requirements

```
pip install -r requirements.txt
```

* If you are installing Playwright for the first time, it will ask you to run this command for one time only.

```
playwright install or

ms-playwright install (if playwright doesn't work)

```

* Now run the server

```
python server.py or

python file_path of server.py on your pc/dev env.
```

* The server runs at port `5000`. If you want to change, you can change it in server.py


# API Documentation

* There is a single end-point only. It is available at `/chat`

```sh
curl -XGET http://localhost:5001/chat?q=Write%20a%20python%20program%20to%20reverse%20a%20list
```

# Updates

* [17 Feb 2023]: Initial release

