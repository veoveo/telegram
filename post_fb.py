import facebook

def fb_post(msg,img):
  groups=['180249687420161']
  token='EAAJkWb9NY98BANeZCAhQxsU1bKsVt1sJFQr71FsL9V0iMEYBrU2vgExTedN24ZBNBopOZAWN1V6GXxAZCOGcuhnIjsUGeXG8a7nGOiz8iZAtpcJZAtnRcZATBAzWAuvooMqrvg8jV36nPepkJTsXJDwao8X5M9RfZC8LvJdCzwqxoS4ZAEUKja58OwwCCQfkpqq8ZD'
  try:
    graph = facebook.GraphAPI(access_token=token)
    for group in groups:
      x = graph.put_object(group, 'photos', message=msg,url=img)
      print(x)
  except:
    pass