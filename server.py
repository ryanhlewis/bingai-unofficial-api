"""Make some requests to Bing AI's chatbot"""
#tips https://playwright.tech/blog/end-to-end-tests-with-playwright-python

import time
import os
import flask

from flask import g


from playwright.sync_api import sync_playwright

APP = flask.Flask(__name__)
PLAY = sync_playwright().start()
BROWSER = PLAY.chromium.launch_persistent_context(
    user_data_dir='C:\\XXX\\XXX\\AppData\\Local\\ms-playwright', #location of the playwright installation
    #executable_path= ('C:\\XXX\\XXX\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'), #if you want to change
    #firefox to chromium.
    executable_path= ('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'), #only works with edge
    headless=False,
)
PAGE = BROWSER.new_page()


def get_input_box():
    """Get the textarea via class of `text-area`"""
    return PAGE.query_selector(".text-area")

def is_logged_in():
    # See if we have a textarea with data-id="root"
    return get_input_box() is not None

def is_loading_response() -> bool:
    """See if the stop button is diabled, if it does, we're not loading"""
    return PAGE.query_selector(".stop").is_enabled()

def send_message(message):
    # Send the message
    box = get_input_box()
    box.click()
    box.fill(message)
    box.press("Enter")

def get_last_message():
    """Get the latest message"""
    while is_loading_response():
        time.sleep(0.25)
    page_elements = PAGE.query_selector_all("div[class*='ac-textBlock']")
    last_element = page_elements.pop()
    return last_element.inner_text()

@APP.route("/chat", methods=["GET"]) #TODO: make this a POST
def chat():
    message = flask.request.args.get("q")
    print("Sending message: ", message)
    send_message(message)
    response = get_last_message()

    # Bing recently made it require a "New topic"
    # after a few messages, so if that was in the response,
    # we click the button with aria label "New topic"
    if "new topic" in response.lower():
        print("New topic detected. Clicking button.")        
        PAGE.query_selector("button[aria-label='New topic']").click()
        print("Sending message: ", message)
        send_message(message)
        response = get_last_message()

    print("Response: ", response)
    return response

@APP.route("/restart", methods=["POST"])
def restart():
    global PAGE,BROWSER,PLAY
    PAGE.close()
    BROWSER.close()
    PLAY.stop()
    time.sleep(0.25)
    PLAY = sync_playwright().start()
    BROWSER = PLAY.firefox.launch_persistent_context(
        user_data_dir='C:\\XXX\\XXX\\AppData\\Local\\ms-playwright',
        #executable_path=('C:\\XXX\\XXX\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'),
        executable_path= ('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'), #only works with edge
        headless=False,
    )
    PAGE = BROWSER.new_page()
    PAGE.goto("https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx")
    return "API restart!"


def start_browser():
    PAGE.goto("https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx")
    time.sleep(3.25)
    if not is_logged_in():
        print("Please log in to Bing AI Chat")
        print("Press enter when you're done")
        input()
    else:
        print("Logged in")
        APP.run(host='127.0.0.1', port=5000, threaded=False) #or
        #APP.run(port=5000, threaded=False) #can also be used

if __name__ == "__main__":
    start_browser()


