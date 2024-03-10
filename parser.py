from bs4 import BeautifulSoup
import requests
def parse(Number_of_pages):
    page_number = 1
    while page_number <= Number_of_pages:
        url = ''.join(['https://www.pepper.ru/?page=', str(page_number)])
        HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
        page = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(page.text, "html.parser")
        DiscountsBlocks = soup.findAll('article')
        for block in DiscountsBlocks:
            url2 = 'https://www.pepper.ru/visit/threadbeldesc/'
            if not((block.find('div', class_='cept-vote-box vote-box overflow--hidden border border--color-borderGrey bRad--a thread-noClick')) and block.find('a', class_='cept-tt thread-link linkPlain thread-title--list js-thread-title')):
                continue
            else:
                DiscountDegree = block.find('div',class_='cept-vote-box vote-box overflow--hidden border border--color-borderGrey bRad--a thread-noClick').find('span').contents[0].replace('\t', '').replace('\n', '')
                DiscountsName = block.find('a', class_='cept-tt thread-link linkPlain thread-title--list js-thread-title').contents[0]
                DiscountLink = url2+block.find('a').get('href')[-6:]
                print(' || '.join([DiscountsName, DiscountDegree, DiscountLink]))
        page_number += 1