import facebook

def fb_post(msg,img):
  groups=['180249687420161']
  token1='EAAJkWb9NY98BAKVsA3tSG5vqcdDWm9h6TDdyTUWS4KesHiKtouBtDFgz0YcfogsbvenGP'
  token2='7zxmzyWPArsfw9HtWGQNG4k1ugZBsRZCW0TRUKvDbogiL2imSn31V84TEZA9INQDJzNPZBGTBrgXY'
  token3='48gm8CRWkRInkijyEc2oagOm8oGWhy3btxYfxaEfwIWx0ZD'
  try:
    graph = facebook.GraphAPI(access_token=token1+token2+token3)
    for group in groups:
      x = graph.put_object(group, 'photos', message=msg,url=img)
      print(x)
  except:
    pass