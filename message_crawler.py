from telethon import TelegramClient, sync
import telethon
import os
import time

api_id = 29461139
api_hash = '61d8d5fbfd1bc9afeeaaf9db1b4f64ed'
session_name = 'nghienshopeelazada'
client = TelegramClient(session_name, api_id, api_hash).start()

def fetch_one_message(msg):

    if msg.media and isinstance(msg.media, telethon.tl.types.MessageMediaPhoto):
        # Download image
        media_path = msg.download_media('media/group_{}/{}_{}_{}'.format(msg.chat.id, msg.chat.id, msg.from_id, msg.id))
        media_file = os.path.basename(media_path)
    elif msg.media and isinstance(msg.media, telethon.tl.types.MessageMediaDocument) \
            and msg.media.document.mime_type in ['audio/ogg']:
        # Download voice
        media_path = msg.download_media('media/group_{}/{}_{}_{}'.format(msg.chat.id, msg.chat.id, msg.from_id, msg.id))
        media_file = os.path.basename(media_path)
    else:
        media_file = None
        if not msg.message:
            return

    item = {
        "message_id": msg.id,  # Message id of current chat
        "chat_id": msg.chat.id,  # ID of current chat
        ## "is_out": msg.out,
        # Whether the message is outgoing (i.e. you sent it from another session) or incoming (i.e. someone else sent it).
        ## "is_mentioned": msg.mentioned,
        # Whether you were mentioned in this message or not. Note that replies to your own messages also count as mentions
        "message": msg.message,  # message content
        "date": msg.date,
        "from_id": msg.from_id,  # The ID of the user who sent this message
        "is_reply": msg.is_reply,  # True if the message is a reply to some other
        "reply_to_msg_id": msg.reply_to_msg_id,  # The ID to which this message is replying to, if any
        "is_channel": msg.is_channel,
        "is_group": msg.is_group,
        "media_file": media_file
    }

    print(msg.message)

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
