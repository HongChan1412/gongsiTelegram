import feedparser

def do_filter(text):
  filter_list = ["TIGER","KODEX","KINDEX","HANARO","ARIRANG","KBSTAR","KOSEF","SOL","TIMEFOLIO","WOORI","KTOP","FOCUS","레버리지","인덱스","코스닥","KOSDAQ","코스피","KOSPI","나스닥","NASDAQ","항셍","유로스탁스","S&P","CSI300","합성","ETN","ETF","ELW","스팩","SPAC","선물","롱","숏","파생"]
  for i in filter_list:
    if i in text:
      return False
  return True

def get_gongsi():
  gongsi = []
  j = 0
  parse_rss = feedparser.parse("http://kind.krx.co.kr:80/disclosure/rsstodaydistribute.do?method=searchRssTodayDistribute&repIsuSrtCd=&mktTpCd=0&searchCorpName=&currentPageSize=1000")
  
  with open("last_gongsi.txt", encoding="UTF8") as f:
    last_gongsi = f.read()
  
  for i in reversed(parse_rss['entries']):
    if not do_filter(i['title']):
      continue
    if last_gongsi < i['link'][:i['link'].find("&docno=")][i['link'][:i['link'].find("&docno=")].rfind("=")+1:]:
      gongsi.append([])
      gongsi[j] = {'title':i['title'][len(i['author'])+1:],'link':i['link']}
      now_gongsi = i['link'][:i['link'].find("&docno=")][i['link'][:i['link'].find("&docno=")].rfind("=")+1:]
      j += 1
      
  
  if gongsi:    
    with open("last_gongsi.txt", "w", encoding="UTF8") as f:
      f.writelines(now_gongsi)

  return gongsi