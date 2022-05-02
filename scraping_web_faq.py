from pip._vendor import requests
from bs4 import BeautifulSoup













if __name__ == '__main__':

    URL = "https://www.stanzasemplice.com/en/faq"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    questions = soup.find_all("div", class_="domanda")
    answers = soup.find_all("div", itemprop="text")

    diz_qa = {}
    for i in range(len(questions)):
        diz_qa[questions[i]] = answers[i]
    print(diz_qa)








