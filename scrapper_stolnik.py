import requests
from bs4 import BeautifulSoup

url = "https://stroyryad.com.ua/cat/lyst-chornyi"
url1 = "https://stroyryad.com.ua/cat/lyst-ryflenyi"
url2 = "https://stroyryad.com.ua/cat/lyst-perforovanyi"
url3 = "https://stroyryad.com.ua/cat/lyst-prosichno-vytiazhnyi"
url4 = 'https://stroyryad.com.ua/cat/truby-profilni'
url5 = 'https://stroyryad.com.ua/cat/kutyk-katanyi'
url6 = 'https://stroyryad.com.ua/cat/armatura'
url7 = 'https://stroyryad.com.ua/cat/smuha'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
products = [2821, 2878]

product1 = soup.find('a', href="/cat/lyst-chornyi/product/2821")
tr = product1.find_parent('tr')
tds = tr.find_all('td')
price_1mm_1_2 = (tds[2].get_text(strip=True).split()[0])
print(price_1mm_1_2)

product2 = soup.find('a', href="/cat/lyst-chornyi/product/2823")
tr = product2.find_parent('tr')
tds = tr.find_all('td')
price_2mm_1_2 = (''.join(tds[2].get_text(strip=True).split()[:2]))
print(price_2mm_1_2)

product3 = soup.find('a', href="/cat/lyst-chornyi/product/2829")
tr = product3.find_parent('tr')
tds = tr.find_all('td')
price_2mm_125_25 = (''.join(tds[2].get_text(strip=True).split()[:2]))
print(price_2mm_125_25)

product4 = soup.find('a', href="/cat/lyst-chornyi/product/7784")
tr = product4.find_parent('tr')
tds = tr.find_all('td')
price_8mm_m2 = (''.join(tds[2].get_text(strip=True).split()[:2]))
print(price_8mm_m2)

product5 = soup.find('a', href="/cat/lyst-chornyi/product/7791")
tr = product5.find_parent('tr')
tds = tr.find_all('td')
price_10mm_m2 = (''.join(tds[2].get_text(strip=True).split()[:2]))
print(price_10mm_m2)

response = requests.get(url1)
soup = BeautifulSoup(response.text, 'lxml')
# print(soup)
product6 = soup.find('a', href="/cat/lyst-ryflenyi/product/10515")
tr = product6.find_parent('tr')
tds = tr.find_all('td')
price_3mm_1_4 = (tds[2].get_text(strip=True).split()[0])
print(price_3mm_1_4)

response = requests.get(url2)
soup = BeautifulSoup(response.text, 'lxml')
product7 = soup.find('a', href="/cat/lyst-perforovanyi/product/7165")
tr = product7.find_parent('tr')
tds = tr.find_all('td')
price_2mm_1_4_per = ''.join(tds[2].get_text(strip=True).split()[:2])
print(price_2mm_1_4_per)

response = requests.get(url3)
soup = BeautifulSoup(response.text, 'lxml')
product7 = soup.find('a', href="/cat/lyst-prosichno-vytiazhnyi/product/6650")
tr = product7.find_parent('tr')
tds = tr.find_all('td')
price_pvl_3mm_1_2 = ''.join(tds[2].get_text(strip=True).split()[:2])
print(price_pvl_3mm_1_2)

response = requests.get(url4)
soup = BeautifulSoup(response.text, 'lxml')
product8 = soup.find('a', href="/cat/truby-profilni/product/2897")
tr = product8.find_parent('tr')
tds = tr.find_all('td')
price_pipe_20_20_2 = (tds[2].get_text(strip=True).split()[0])
print(price_pipe_20_20_2)

product9 = soup.find('a', href="/cat/truby-profilni/product/3469")
tr = product9.find_parent('tr')
tds = tr.find_all('td')
price_pipe_30_30_3 = (tds[2].get_text(strip=True).split()[0])
print(price_pipe_30_30_3)

product10 = soup.find('a', href="/cat/truby-profilni/product/13525")
tr = product10.find_parent('tr')
tds = tr.find_all('td')
price_pipe_40_20_3 = (tds[2].get_text(strip=True).split()[0])
print(price_pipe_40_20_3)

product11 = soup.find('a', href="/cat/truby-profilni/product/16080")
tr = product11.find_parent('tr')
tds = tr.find_all('td')
price_pipe_40_40_3 = (tds[2].get_text(strip=True).split()[0])
print(price_pipe_40_40_3)

product12 = soup.find('a', href="/cat/truby-profilni/product/3406")
tr = product12.find_parent('tr')
tds = tr.find_all('td')
price_pipe_50_30_3 = (tds[2].get_text(strip=True).split()[0])
print(price_pipe_50_30_3)

product13 = soup.find('a', href="/cat/truby-profilni/product/3029")
tr = product13.find_parent('tr')
tds = tr.find_all('td')
price_pipe_50_50_3 = (tds[2].get_text(strip=True).split()[0])
print(price_pipe_50_50_3)

product14 = soup.find('a', href="/cat/truby-profilni/product/3027")
tr = product14.find_parent('tr')
tds = tr.find_all('td')
price_pipe_100_50_3 = (tds[2].get_text(strip=True).split()[0])
print(price_pipe_100_50_3)

response = requests.get(url5)
soup = BeautifulSoup(response.text, 'lxml')
product15 = soup.find('a', href="/cat/kutyk-katanyi/product/2975")
tr = product15.find_parent('tr')
tds = tr.find_all('td')
corner_20_20_3 = (tds[2].get_text(strip=True).split()[0])
print(corner_20_20_3)

product16 = soup.find('a', href="/cat/kutyk-katanyi/product/7458")
tr = product16.find_parent('tr')
tds = tr.find_all('td')
corner_30_30_3 = (tds[2].get_text(strip=True).split()[0])
print(corner_30_30_3)

product17 = soup.find('a', href="/cat/kutyk-katanyi/product/6216")
tr = product17.find_parent('tr')
tds = tr.find_all('td')
corner_50_50_3 = (tds[2].get_text(strip=True).split()[0])
print(corner_50_50_3)

response = requests.get(url6)
soup = BeautifulSoup(response.text, 'lxml')
product18 = soup.find('a', href="/cat/armatura/product/2857")
tr = product18.find_parent('tr')
tds = tr.find_all('td')
reinfor_8 = (tds[2].get_text(strip=True).split()[0])
print(reinfor_8)

response = requests.get(url7)
soup = BeautifulSoup(response.text, 'lxml')
product19 = soup.find('a', href="/cat/smuha/product/12764")
tr = product19.find_parent('tr')
tds = tr.find_all('td')
stripe_20_4 = (tds[2].get_text(strip=True).split()[0])
print(stripe_20_4)