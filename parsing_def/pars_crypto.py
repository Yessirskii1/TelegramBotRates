from bs4 import BeautifulSoup
import fake_useragent
import requests

def get_btc():
    user = fake_useragent.UserAgent().random
    header = {"user-agent": user}

    link = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&sca_esv=7ec80514b65b74c1&sxsrf=ACQVn0_eaXL6dNNPyr-Z3wk_psOPIpnNaA%3A1707213820520&ei=_APCZZivH7j9wPAPsoaSeA&udm=&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0&gs_lp=Egxnd3Mtd2l6LXNlcnAiGdC60YPRgNGBINCx0LjRgtC60L7QuNC90LAqAggBMgoQABhHGNYEGLADMgoQABhHGNYEGLADMgoQABhHGNYEGLADMgoQABhHGNYEGLADMgoQABhHGNYEGLADMgoQABhHGNYEGLADMgoQABhHGNYEGLADMgoQABhHGNYEGLADMhAQABiABBiKBRhDGMkDGLADMg4QABiABBiKBRiSAxiwA0j6B1AAWABwAXgBkAEAmAEAoAEAqgEAuAEByAEA4gMEGAAgQYgGAZAGCg&sclient=gws-wiz-serpn"
    answer = requests.get(link, headers=header).text

    soup = BeautifulSoup(answer, "lxml")
    block = soup.find("div", id="search")

    check_btc = block.find("span", class_="pclqee").text
    result = f"Курс bitcoin - ${check_btc}"
    return result


def get_ethi():
    user = fake_useragent.UserAgent().random
    header = {"user-agent": user}

    link = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D1%8D%D1%84%D0%B8%D1%80%D0%B0+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&sca_esv=7ec80514b65b74c1&sxsrf=ACQVn0-zOZo6tQOYsbXTtglXjvLECXR6MA%3A1707214088883&ei=CAXCZb3FNfO4wPAPi9KmgA8&udm=&oq=%D0%BA%D1%83%D1%80%D1%81+%27abhf+r+&gs_lp=Egxnd3Mtd2l6LXNlcnAiEdC60YPRgNGBICdhYmhmIHIgKgIIADIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDUiH8ThQlN04WJDlOHACeAGQAQCYAbcBoAGEDKoBAzAuObgBAcgBAPgBAcICChAAGEcY1gQYsAPCAg0QABiABBiKBRhDGLADwgIKECMYgAQYigUYJ8ICEBAAGIAEGIoFGEMYsQMYgwHCAggQABiABBixA8ICCxAAGIAEGLEDGIMBwgIKEAAYgAQYigUYQ8ICCBAAGIAEGJIDwgIFEAAYgATCAgcQABiABBgKwgIKEAAYgAQYFBiHAsICCRAAGIAEGAoYKsICBhAAGBYYHsICDBAAGIAEGAoYsQMYKsICDBAAGIAEGA0YRhiCAsICGBAAGIAEGA0YRhiCAhiXBRiMBRjdBNgBAeIDBBgAIEGIBgGQBgq6BgYIARABGBM&sclient=gws-wiz-serp"
    answer = requests.get(link, headers=header).text

    soup = BeautifulSoup(answer, "lxml")
    block = soup.find("div", id="search")

    check_eth = block.find("span", class_="pclqee").text
    result = f"Курс ethereum - ${check_eth}"
    return result

def get_lite_coin():
    user = fake_useragent.UserAgent().random
    header = {"user-agent": user}

    link = "https://www.google.com/search?q=litecoin&oq=litecoin&gs_lcrp=EgZjaHJvbWUyDAgAEEUYORixAxiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCTQ5NjhqMGoxNagCALACAA&sourceid=chrome&ie=UTF-8"
    answer = requests.get(link, headers=header).text

    soup = BeautifulSoup(answer, "lxml")
    block = soup.find("div", id="search")

    check_lite = block.find("span", class_="pclqee").text
    result = f"Курс litecoin - ${check_lite}"
    return result

def get_doge_coin():
    user = fake_useragent.UserAgent().random
    header = {"user-agent": user}

    link = "https://www.google.com/search?q=dogecoin&oq=dogecoin&gs_lcrp=EgZjaHJvbWUyEQgAEEUYORhDGLEDGIAEGIoFMgcIARAAGIAEMgwIAhAAGEMYgAQYigUyBwgDEAAYgAQyBwgEEAAYgAQyDQgFEAAYgwEYsQMYgAQyBwgGEAAYgAQyBwgHEAAYgAQyBwgIEAAYgAQyBwgJEAAYgATSAQkzMzY3ajBqMTWoAgCwAgA&sourceid=chrome&ie=UTF-8"
    answer = requests.get(link, headers=header).text

    soup = BeautifulSoup(answer, "lxml")
    block = soup.find("div", id="search")

    check_doge = block.find("span", class_="pclqee").text
    result = f"Курс dogecoin - ${check_doge}"
    return result

def get_tether():
    user = fake_useragent.UserAgent().random
    header = {"user-agent": user}

    link = "https://www.google.com/search?q=tether&sca_esv=e1cf12f9f09085f6&sxsrf=ACQVn0-i3-_77UsjOzOaWAnnyJ7KsNtrrA%3A1707231725931&ei=7UnCZbm8OMvWwPAPqr6voA0&udm=&oq=tethe&gs_lp=Egxnd3Mtd2l6LXNlcnAiBXRldGhlKgIICjIPECMYgAQYigUYJxhGGIICMg0QABiABBgUGIcCGLEDMgUQABiABDIIEAAYgAQYsQMyBRAAGIAEMgoQABiABBiKBRhDMgoQABiABBiKBRhDMgUQABiABDIFEAAYgAQyBRAAGIAEMhkQABiABBiKBRhGGIICGJcFGIwFGN0E2AEBSIQ6UNcOWOEucAJ4AZABAJgBgQagAawLqgEHMC40LjYtMbgBAcgBAPgBAcICChAAGEcY1gQYsAPCAg0QABiABBiKBRhDGLADwgIKECMYgAQYigUYJ8ICBBAjGCfCAhEQLhiABBixAxiDARjHARjRA8ICCxAAGIAEGLEDGIMBwgILEC4YgAQYsQMYgwHiAwQYACBBiAYBkAYKugYGCAEQARgT&sclient=gws-wiz-serp"
    answer = requests.get(link, headers=header).text

    soup = BeautifulSoup(answer, "lxml")
    block = soup.find("div", id="search")

    check_tet = block.find("span", class_="pclqee").text
    result = f"Курс tether - ${check_tet}"
    return result

def get_xrp():
    user = fake_useragent.UserAgent().random
    header = {"user-agent": user}

    link = ("https://www.google.com/search?q=xrp&oq=xrp&gs_lcrp=EgZjaHJvbWUyFAgAEEUYORhDGIMBGLEDGIAEGIoFMhIIARAAGEMYgwEYsQMYgAQYigUyDQgCEAAYgwEYsQMYgAQyDQgDEAAYgwEYsQMYgAQyBwgEEAAYgAQyEggFEAAYQxiDARixAxiABBiKBTINCAYQABiDARixAxiABDIMCAcQABgUGIcCGIAEMgoICBAAGLEDGIAEMgcICRAAGIAE0gEJMzcwM2owajE1qAIAsAIA&sourceid=chrome&ie=UTF-8")
    answer = requests.get(link, headers=header).text

    soup = BeautifulSoup(answer, "lxml")
    block = soup.find("div", id="search")

    check_xrp = block.find("span", class_="pclqee").text
    result = f"Курс xrp - ${check_xrp}"
    return result

def get_bc():
    user = fake_useragent.UserAgent().random
    header = {"user-agent": user}

    link = "https://www.google.com/search?q=binance+coin&oq=bin&gs_lcrp=EgZjaHJvbWUqDAgCEAAYQxiABBiKBTIGCAAQRRg5MhgIARAuGEMYgwEYxwEYsQMY0QMYgAQYigUyDAgCEAAYQxiABBiKBTIMCAMQABhDGIAEGIoFMgwIBBAAGEMYgAQYigUyDAgFEAAYQxiABBiKBTIMCAYQABhDGIAEGIoFMhMIBxAuGIMBGMcBGLEDGNEDGIAEMg0ICBAAGIMBGLEDGIAEMgcICRAAGI8C0gEJNDgwNGowajE1qAIAsAIA&sourceid=chrome&ie=UTF-8"
    answer = requests.get(link, headers=header).text

    soup = BeautifulSoup(answer, "lxml")
    block = soup.find("div", id="search")

    check_bc = block.find("span", class_="pclqee").text
    result = f"Курс binance coin - ${check_bc}"
    return result

