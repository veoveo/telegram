from telethon import TelegramClient, sync
import telethon
import os
import time
import image_upload
import re

api_id = 29461139
api_hash = '61d8d5fbfd1bc9afeeaaf9db1b4f64ed'
session_name = 'nghienshopeelazada'
client = TelegramClient(session_name, api_id, api_hash).start()

def fetch_one_message(msg):
    if msg.message.count("://shope.ee/") !=0 and msg.media and isinstance(msg.media, telethon.tl.types.MessageMediaPhoto):
        # Download image
        media_path = msg.download_media('media/{}_{}_{}'.format(msg.chat.id, msg.from_id, msg.id))
        path_file = os.path.basename(media_path)
        media_file = image_upload.uploadimg("/content/media/"+path_file)
    else:
        media_file = None
        if not msg.message:
            return
    
    mess = msg.message
    link = re.findall(r'(https?://shope.ee[^\s]+)', mess)
    for i in link:
      #sửa ở đây
      mess.replace(i,móihdjshdhsj)

    item = {
        "message": msg.message,  # message content
        "media_file": media_file
    }

    print(item)

def fetch_all_group_message(client):
    dialog_list = client.get_dialogs()
    for dialog in dialog_list:
        entity = client.get_entity(dialog.title)
        if isinstance(entity, telethon.tl.types.Channel) and dialog.is_group:
            max_message_id = 0
            msg_iter = client.iter_messages(entity.id, min_id=max_message_id)
            for msg in msg_iter:
              fetch_one_message(msg)
              break
            max_message_id = msg.id
            while True:
                msg_iter = client.iter_messages(entity.id, min_id=max_message_id)

                for msg in msg_iter:
                    fetch_one_message(msg)
                max_message_id = msg.id
                time.sleep(2)
             

def run():
    fetch_all_group_message(client)
