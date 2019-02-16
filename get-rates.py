#! /usr/bin/python3

"""
This program downloads Libor Rates and Prime Rate
"""

import requests, bs4
res = requests.get('https://www.bankrate.com/rates/interest-rates/libor.aspx')
libor_1y_title_path = '.table > tbody:nth-child(3) > tr:nth-child(7) > td:nth-child(1) > a:nth-child(1)'
libor_1y_rate_path = '.table > tbody:nth-child(3) > tr:nth-child(7) > td:nth-child(2)'
libor_1m_title_path = '.table > tbody:nth-child(3) > tr:nth-child(3) > td:nth-child(1)'
libor_1m_rate_path = '.table > tbody:nth-child(3) > tr:nth-child(3) > td:nth-child(2)'
libor_3m_title_path = '.table > tbody:nth-child(3) > tr:nth-child(4) > td:nth-child(1)'
libor_3m_rate_path = '.table > tbody:nth-child(3) > tr:nth-child(4) > td:nth-child(2)'
libor_6m_title_path = '.table > tbody:nth-child(3) > tr:nth-child(5) > td:nth-child(1)'
libor_6m_rate_path = '.table > tbody:nth-child(3) > tr:nth-child(5) > td:nth-child(2)'
# Always call res.raise_for_status() after requests.get so the program halts
# if the download fails
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, features = "lxml")
libor_1y_title = soup.select(libor_1y_title_path)
libor_1y_rate = soup.select(libor_1y_rate_path)
libor_1m_title = soup.select(libor_1m_title_path)
libor_1m_rate = soup.select(libor_1m_rate_path)
libor_3m_title = soup.select(libor_3m_title_path)
libor_3m_rate = soup.select(libor_3m_rate_path)
libor_6m_title = soup.select(libor_6m_title_path)
libor_6m_rate = soup.select(libor_6m_rate_path)

res2 = requests.get('https://www.jpmorganchase.com/corporate/About-JPMC/historical-prime-rate.htm')
prime_date_path = '.dataLite > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1)'
prime_rate_path = '.dataLite > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2)'
res2.raise_for_status()
soup2 = bs4.BeautifulSoup(res2.text, features = "lxml")
prime_rate = soup2.select(prime_rate_path)
prime_date = soup2.select(prime_date_path)

print(libor_1y_title[0].getText(), ": ", libor_1y_rate[0].getText())
print(libor_6m_title[0].getText(), ": ", libor_6m_rate[0].getText())
print(libor_3m_title[0].getText(), ": ", libor_3m_rate[0].getText())
print(libor_1m_title[0].getText(), ": ", libor_1m_rate[0].getText())
print("JPMC Prime Rate ", prime_date[0].getText(), ": ", prime_rate[0].getText())
