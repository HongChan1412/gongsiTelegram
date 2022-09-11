import telegram as tel

def send_msg(gongsi):
  bot = tel.Bot(token="telegram_Token")

  chat_id = "channel_Id" #오늘의공시 채널

  for i in gongsi:
    print(i['title'], i['link'])
    bot.sendMessage(chat_id=chat_id,text=f"[{i['title'].replace('[',' ').replace(']',' ')}]({i['link']})", parse_mode="Markdown")
    
    
