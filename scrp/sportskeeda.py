import bs4 as bs
import urllib.request,psycopg2,time
conn = psycopg2.connect(database="gameapp",host='localhost',port='5***',user='postgres',password='*******')
cur = conn.cursor()
while True:
    for j in range(10,0,-1):
        print('scraping page https://www.sportskeeda.com/cricket?page='+str(j))
        source = urllib.request.urlopen("https://www.sportskeeda.com/go/ipl?page="+str(j)).read()
        soup = bs.BeautifulSoup(source, 'html.parser')
        storiesData=soup.findAll("div", {"class": "story-wrapper"})
        i=0
        for eachStory in storiesData:
            source='sportskeeda'
            try:
                title=eachStory.find("div", {"class": "block-story-title"}).text.strip()
                relLink=eachStory.find("a", {"class": "story-link-overlay"}).get('href')
                link="http://www.sportskeeda.com"+relLink
                id=eachStory.find("div", {"class": "list-story-link"}).get('data-id')
                cur.execute("SELECT * FROM newsfeed WHERE theirid = %s AND source = %s",(id,source,))
                if cur.fetchone()!=None:
                    continue
                littDetail=bs.BeautifulSoup(urllib.request.urlopen(link).read(), 'html.parser')
                lilDetailText=littDetail.find("div",{"id":"article-content"}).find("p").text.strip()
            except:
                continue
            try:
                imagelink=eachStory.find("div", {"class": "in-block-img"}).get('data-lazy')
                print(imagelink)
            except:
                imagelink=""
            print('inserting+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',title,link,id,lilDetailText)
            cur.execute("INSERT INTO newsfeed (theirid, title, itemlink, detail, imagelink, source, tags) VALUES (%s, %s, %s, %s, %s, %s, %s)",(id, title, link, lilDetailText, imagelink,source,""))
            # db_version = cur.fetchone()
            # print(cur.fetchone())
            if i%5==0:
                conn.commit()
            i+=1
    conn.commit()
    # print("Waiting for 60 sec.")
    # time.sleep(300)
cur.close()
