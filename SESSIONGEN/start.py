from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID

start_txt = """**
•──────────────────────•
𖣠 ɪ ʜᴀᴠᴇ ɢᴇɴᴇʀᴀᴛɪɴɢ ғᴇᴀᴛᴜʀᴇs
𖣠 ᴛʜɪs ɪs ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟʟ & ᴜsᴇғᴜʟ
𖣠 ᴛʀᴜsᴛᴇᴅ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴ ʙᴏᴛ
•──────────────────────•
           [❖ │ sᴀɴᴀᴛᴀɴɪ ꭙ ʙᴏᴛ │ ❖](https://t.me/all_sanatani_bot)
•──────────────────────•**
"""




@Client.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
          [
          InlineKeyboardButton(text="🍁 ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ 🍁", callback_data="generate")
          ],
          [
          InlineKeyboardButton("✨ sᴀᴄʜɪɴ️", url="https://t.me/SACHIN_OWNER"),
          InlineKeyboardButton("ᴜsᴇʀʙᴏᴛ 💫", url="https://t.me/SANATANI_X_ROBOT")
          ],
          [
          InlineKeyboardButton("❄️ sᴜᴘᴘᴏʀᴛ️", url="https://t.me/+cW07X2RM_IBmYTI1"),
          InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs 🕸️️", url="https://t.me/ALL_SANATANI_BOT")
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/4be5b30ec5f2ff6c01656.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )