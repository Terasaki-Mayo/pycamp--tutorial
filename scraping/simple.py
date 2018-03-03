import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://spitz-web.com/live/2018others/'
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    lives = soup.find_all('li', class_='m_live-detail-list-item')
    #print(lives)
    for live in lives:
        date = live.div.time.text
        title = live.div.div.text
        print(date,title)


if __name__ == '__main__':
    main()

    