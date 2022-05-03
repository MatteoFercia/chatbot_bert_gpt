from pip._vendor import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':

    URL = "https://www.stanzasemplice.com/en/faq"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    questions = soup.find_all("div", class_="domanda")
    answers = soup.find_all("div", itemprop="text")

    #creatig a dictionary where every key is the question and every answer is the value
    diz_qa = {}
    for i in range(len(questions)):
        diz_qa[questions[i].text.strip().replace("\n"," ")] = answers[i].text.strip().replace("\n","").replace("\xa0"," ").replace("\"","").replace("\r"," ")
    print(diz_qa)








