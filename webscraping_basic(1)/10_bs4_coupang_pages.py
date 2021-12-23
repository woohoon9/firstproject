import requests
import re
from bs4 import BeautifulSoup


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36" }

for i in range(1,6):
    print("page:", i)
        
    url ="https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor=".format(i)


    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    # print(items[0].find("div", attrs={"class":"name"}).get_text())

    for item in items:
        # coupang recommendation excluded
        ad_badge = item.find("img src", attrs = {"class": "badge-ico badge-coupick"})
        if ad_badge:
            print("<exclude the coupang recommendation>")
            continue

        name = item.find("div", attrs={"class":"name"}).get_text()
    # exclude apple product
        if "Apple" in name:
            print("<excluding Apple product>")
            continue

        price = item.find("strong", attrs={"class":"price-value"}).get_text()
        rate = item.find("em", attrs={"class":"rating"})

        # review_cnt > 100, rate > 4 
        if rate:
            rate = rate.get_text()
        else:
            print("<exclude the product with no rate>")
            continue

        rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) 
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()
            rate_cnt = rate_cnt[1:-1]
        else:
            print("<exclude the product with no rate_cnt>")
            continue

        link = item.find("a", attrs = {"class":"search-product-link"})["href"]
        if float(rate) >=5.0 and int(rate_cnt) >= 2000:
            # print(name, price, rate, rate_cnt)
            print(f"product name: {name}")
            print(f"price:{price}")
            print(f"rate: {rate}wja ({rate_cnt}개)")
            print("Short cut: {}".format("https://www.coupang.com" + link))
            print("-"*70)