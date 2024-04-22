import os
import pickle


def load_cookies():
    if os.path.exists("instagram_cookies.pkl"):
        with open("instagram_cookies.pkl", "rb") as cookies_file:
            cookies = pickle.load(cookies_file)
            return cookies
    else:
        return None


cookies = load_cookies()
