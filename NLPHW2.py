import csv
import requests
from bs4 import BeautifulSoup
cate=['','動作','冒險','科幻','奇幻','劇情','犯罪','恐怖','懸疑/驚悚','喜劇','愛情','溫馨/家庭','動畫','戰爭','音樂/歌舞','歷史/傳記','紀錄片','勵志','武俠','影展','戲劇','影集']
with open('NLPHW2.csv', 'w', encoding='utf-8-sig', newline='') as csv_file:
     
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['電影片名', '電影英文片名', '分類', '上映時間', '劇情介紹'])
    movie_id=[]
    for i in range(1,21):
      url = 'https://movies.yahoo.com.tw/moviegenre_result.html?genre_id='+str(i)
      j=1
      while (True):
        response = requests.get(url+'&page='+str(j))
        soup = BeautifulSoup(response.text, 'html.parser')
        if soup.find('p','text-center'):
            break
        info_items = soup.find_all('div', 'release_info')
        ids=soup.find_all('div','release_movie_name')
        for t in ids:
          h=t.find('a')['href'][-5:]
          if h in movie_id:
            continue
          movie_id.append(h)
        
        for item in info_items:
            name = item.find('div', 'release_movie_name').a.text.strip()
            english_name = item.find('div', 'en').a.text.strip()
            #category = item.find('div','level_name_box').gabtn.text.strip()
            #category=item.find('div','title').find('h1').text
            release_time = item.find('div', 'release_movie_time').text.split('：')[-1].strip()
            intro = item.find('div', 'release_text').span.text.strip()
            csv_writer.writerow([name, english_name,cate[i] , release_time, intro])
            print(name, english_name,cate[i] , release_time, intro,'/n')
        j=j+1
