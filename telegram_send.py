import telegram as tel

def send_msg(gongsi):
  bot = tel.Bot(token="5451972497:AAHAN02dNskjCMzp3wC5vDON9fOXSaw0_tg")
  # 5451972497:AAHAN02dNskjCMzp3wC5vDON9fOXSaw0_tg
  #chat_id = "5343555758" 테스트 채널
  chat_id = "-1001768710940" #오늘의공시 채널

  for i in gongsi:
    print(i['title'], i['link'])
    bot.sendMessage(chat_id=chat_id,text=f"[{i['title'].replace('[',' ').replace(']',' ')}]({i['link']})", parse_mode="Markdown")
    
    
