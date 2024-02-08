from bs4 import BeautifulSoup
import fake_useragent
import requests

def get_usd():
    user = fake_useragent.UserAgent().random
    header = {"user-agent" : user}

    link = "https://www.cbr.ru/currency_base/daily/"
    answer = requests.get(link, headers=header).text

    soup = BeautifulSoup(answer, "lxml")
    block = soup.find("main", id="content")

    #Check USD
    check_usd = block.find("tbody")
    usd_all = check_usd.find_all("tr")[14]
    us_result = usd_all.find_all("td")[-1].text
    USD = f"Курс доллара к рублю - <b>{us_result}₽</b>"
    return USD

def get_euro():
    user = fake_useragent.UserAgent().random
    header = {"user-agent": user}

    link = "https://www.cbr.ru/currency_base/daily/"
    answer = requests.get(link, headers=header).text

    soup = BeautifulSoup(answer, "lxml")
    block = soup.find("main", id="content")

    # Check Euro
    check_eur = block.find("tbody")
    eur_all = check_eur.find_all("tr")[15]
    us_result = eur_all.find_all("td")[-1].text
    result = f"Курс евро к рублю - <b>{us_result}₽</b>"
    return result

def get_thai():
    user = fake_useragent.UserAgent().random
    header = {"user-agent": user}
    link = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B0%D1%82+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B0%D1%82+&gs_lcrp=EgZjaHJvbWUqBwgBEAAYgAQyBggAEEUYOTIHCAEQABiABDIHCAIQABiABDIMCAMQABgUGIcCGIAEMgcIBBAAGIAEMgcIBRAAGIAEMgcIBhAAGIAEMgcIBxAAGIAEMgcICBAAGIAEMgcICRAAGIAE0gEKMTM4NDVqMGoxNagCALACAA&sourceid=chrome&ie=UTF-8"
    answer = requests.get(link, headers=header).text

    soup = BeautifulSoup(answer, "lxml")
    block = soup.find("div", id="search")

    check_bat = block.find("span", class_="DFlfde SwHCTb").text
    result = f"Курс бата к рублю - <b>{check_bat}</b>"
    return result

def get_china():
    user = fake_useragent.UserAgent().random
    header = {"user-agent": user}
    link = "https://www.google.com/search?q=rehc+.fyz&sca_esv=7ec80514b65b74c1&sxsrf=ACQVn0_0N2UV_Vk-9pgSYfl51lFXQ8zSrg%3A1707217468628&ei=PBLCZcr-JeW5wPAP_YiIkAE&udm=&ved=0ahUKEwjKjJbWyJaEAxXlHBAIHX0EAhIQ4dUDCBA&uact=5&oq=rehc+.fyz&gs_lp=Egxnd3Mtd2l6LXNlcnAiCXJlaGMgLmZ5ejIHECMYsQIYJzIHEAAYgAQYCjIHEAAYgAQYCjIHEAAYgAQYCjIHEAAYgAQYCjINEAAYgAQYChixAxiDATIHEAAYgAQYCjIHEAAYgAQYCjIHEAAYgAQYCjIHEAAYgAQYCkjHFFDyCVjeEnABeAGQAQCYAb0BoAGyDKoBAzAuObgBA8gBAPgBAagCEcICBxAjGOoCGCfCAhQQABiABBjjBBjpBBjqAhi0AtgBAcICFhAAGIAEGOMEGOkEGOoCGLQCGArYAQHCAgsQLhiABBixAxiDAcICCxAAGIAEGLEDGIMBwgIREC4YgAQYsQMYgwEYxwEY0QPCAgUQABiABMICCBAAGIAEGLEDwgIaEC4YgAQYsQMYgwEYlwUY3AQY3gQY4ATYAQLCAgoQIxiABBiKBRgnwgIFEC4YgATCAg4QABgBGIAEGMkDGAoYKsICCRAAGAEYgAQYCsICDhAAGAEYgAQYigUYQxgKwgILEAAYgAQYigUYkgPCAgwQABiABBiKBRhDGArCAhMQABiABBiKBRhDGLEDGIMBGMkDwgIQEAAYgAQYigUYQxixAxiDAcICChAAGIAEGAoYkgPCAgoQABiABBiKBRhDwgIQEAAYgAQYChixAxiDARjJA8ICChAAGIAEGAoYsQPCAgkQABiABBgKGCriAwQYACBBugYGCAEQARgBugYGCAIQARgU&sclient=gws-wiz-serp"
    answer = requests.get(link, headers=header).text

    soup = BeautifulSoup(answer, "lxml")
    block = soup.find("div", id="search")

    check_cny = block.find("span", class_="DFlfde SwHCTb").text
    result = f"Курс юаня к рублю - <b>{check_cny}</b>"
    return result

def get_korean():
    user = fake_useragent.UserAgent().random
    header = {"user-agent": user}
    link = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B2%D0%BE%D0%BD%D1%8B&sca_esv=7ec80514b65b74c1&sxsrf=ACQVn096VJW1KN_xcrV4LE4B18VwYJk4AA%3A1707218211922&ei=IxXCZdbrN8-lwPAP5tig4A4&udm=&ved=0ahUKEwiWic24y5aEAxXPEhAIHWYsCOwQ4dUDCBA&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B2%D0%BE%D0%BD%D1%8B&gs_lp=Egxnd3Mtd2l6LXNlcnAiEdC60YPRgNGBINCy0L7QvdGLMg8QIxiABBiKBRgnGEYYggIyCxAAGIAEGLEDGIMBMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyGRAAGIAEGIoFGEYYggIYlwUYjAUY3QTYAQJIqSdQmR1Y_SRwAXgBkAEAmAGuAaAB1wuqAQMwLjm4AQPIAQD4AQGoAhTCAgcQIxjqAhgnwgITEAAYgAQYigUYQxjqAhi0AtgBAcICChAjGIAEGIoFGCfCAgoQABiABBiKBRhDwgIQEAAYgAQYigUYQxixAxiDAcICEBAAGIAEGBQYhwIYsQMYgwHCAg0QABiABBiKBRhDGLEDwgIOEAAYgAQYsQMYgwEYyQPCAggQABiABBixA-IDBBgAIEHiAwUSATEgQLoGBggBEAEYAboGBggCEAEYEw&sclient=gws-wiz-serp"
    answer = requests.get(link, headers=header).text

    soup = BeautifulSoup(answer, "lxml")
    block = soup.find("div", id="search")

    check_krw = block.find("span", class_="DFlfde SwHCTb").text
    result = f"Курс воны к рублю - <b>{check_krw}</b>"
    return result

def get_kz():
    user = fake_useragent.UserAgent().random
    header = {"user-agent": user}
    link = "https://www.google.com/search?q=rehc+ntyut&oq=rehc+ntyut&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQABgKGIAEMgkIAhAAGAoYgAQyCQgDEAAYChiABDIJCAQQABgKGIAEMgkIBRAAGAoYgATSAQkyNTk3ajBqMTWoAgCwAgA&sourceid=chrome&ie=UTF-8"
    answer = requests.get(link, headers=header).text

    soup = BeautifulSoup(answer, "lxml")
    block = soup.find("div", id="search")

    check_kzt = block.find("span", class_="DFlfde SwHCTb").text
    result = f"Курс тенге к рублю - <b>{check_kzt}</b>"
    return result

def get_jap():
    user = fake_useragent.UserAgent().random
    header = {"user-agent": user}
    link = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80+%D1%81%D0%B9%D0%B5%D0%BD%D1%8B&oq=%D0%BA%D1%83%D1%80+%D1%81%D0%B9%D0%B5%D0%BD%D1%8B&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIPCAEQABgNGIMBGLEDGIAEMgkIAhAAGA0YgAQyCQgDEAAYDRiABDIJCAQQABgNGIAEMgkIBRAAGA0YgAQyCQgGEAAYDRiABDIJCAcQABgNGIAEMgkICBAAGA0YgAQyCQgJEAAYDRiABNIBCjEwMjA0ajBqMTWoAgCwAgA&sourceid=chrome&ie=UTF-8"
    answer = requests.get(link, headers=header).text

    soup = BeautifulSoup(answer, "lxml")
    block = soup.find("div", id="search")

    check_jpy = block.find("span", class_="DFlfde SwHCTb").text
    result = f"Курс иены к рублю - <b>{check_jpy}</b>"
    return result













