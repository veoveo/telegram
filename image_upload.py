import requests
import base64

def uploadimg(path):
  with open(path, "rb") as image_file:
      encoded_string = base64.b64encode(image_file.read())
  url = "https://shopee.vn/api/v2/image_upload/"
  headers = {}
  headers["content-type"] = "application/json"
  headers["cookie"] = "shopee_token=JQ1Q7IejEwh/JmLa0bVySkPf61J7V26Fv1lv/LMDqXmRVlTeVVfi2dZ0Cq956sx9"
  data = '{"images":["data:image/png;base64,'+str(encoded_string)[2:-1]+'"],"thumbnails":["data:image/png;base64,'+str(encoded_string)[2:-1]+'"]}'
  resp = requests.post(url, headers=headers, data=data)
  return 'https://cf.shopee.vn/file/'+resp.json()["data"]["filenames"][0]