import base64
from typing import List
from httpx import Client
import hashlib
import datetime
import calendar
from urllib.parse import urljoin, urlparse
import json
from re import  findall
import requests

class Authentication:
    def __init__(self, app_id: str, app_secret: str):
        self.app_id = app_id
        self.app_secret = app_secret
        self.current_time = datetime.datetime.utcnow()
        self.timestamp = calendar.timegm(self.current_time.utctimetuple())

    def signature(self, payload: str) -> str:
        payload = json.dumps(payload)
        signature = f"{self.app_id}{self.timestamp}{payload}{self.app_secret}"
        hashing = hashlib.sha256(signature.encode("utf-8"))
        return hashing.hexdigest()
    
class ShortLink:
    def __init__(self, origin_url: str, sub_ids: List[str] = []):
        self.origin_url = self._clean_url(origin_url)
        self.sub_ids = sub_ids

    @property
    def payload(self):
        graphql_query = """mutation{{
            generateShortLink(input: {{
                originUrl: "{}",
                subIds: {}
            }}){{
                shortLink
            }}
        }}""".format(
            self.origin_url, json.dumps(self.sub_ids)
        )
        query_payload = {"query": graphql_query}
        return query_payload

    def _clean_url(self, url):
        clean_url = urljoin(url, urlparse(url).path)
        return clean_url

class ShopeeClient:
    base_url = "https://open-api.affiliate.shopee.vn"
    def __init__(self, app_id: str, app_secret: str):
        headers = {
        "Accept-Language" : "en-US,en;q=0.5",
        "User-Agent": "Defined",
        }
        self.app_id = app_id
        self.app_secret = app_secret
        self._client = Client(base_url=self.base_url, headers=headers)

    def post(self, payload: str):
        headers = self._headers(payload)
        return self._client.post("/graphql", headers=headers, json=payload)

    def _headers(self, payload):
        auth = Authentication(self.app_id, self.app_secret)
        headers = {
            "Authorization": f"SHA256 Credential={auth.app_id}, Signature={auth.signature(payload)}, Timestamp={auth.timestamp}",
            "Content-Type": "application/json",
            "User-Agent": "Defined",
        }
        return headers


class ShopeeAffiliate:
    def __init__(self, app_id: str, app_secret: str):
        self._client = ShopeeClient(app_id=app_id, app_secret=app_secret)

    def shortlink(self, origin_url: str, sub_ids: List[str] = []):
        link = ShortLink(origin_url=origin_url, sub_ids=sub_ids)
        resp = self._client.post(payload=link.payload)
        return resp

def getitem(url):
    id = findall(r'\d+', url.split('?')[0])[-2:]
    return id

def shorklink(link):
  url = requests.get(link).url
  url= url[:url.find("utm_campaign")-1]
  APP_ID = "17398250011"
  APP_SECRET = "U675F3TO44TAWI67LJBUZBZN44QVSJKD"
  client = ShopeeAffiliate(app_id=APP_ID, app_secret=APP_SECRET)
  return client.shortlink(url, "").json()['data']['generateShortLink']['shortLink']
    