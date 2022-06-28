# This file is a part of TG-Direct-Link-Generator
from main.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Language(object):
    class en(object):
        START_TEXT = """
**👋 Hᴇʏ, {}**\n
<b>ɪ'ᴍ ɪɴꜱᴛᴀɴᴛ ᴛᴇʟᴇɢʀᴀᴍ ꜰɪʟᴇ ᴛᴏ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ.</b>
<b>ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴍᴇ ʏᴏᴜʀ ꜰɪʟᴇ </b></n>


<b>ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ᴛᴏ ɢᴇᴛ ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ</b>\n
<b><u>Warning </u></b>⚠️
<i>🔞 ᴘʀᴏɴ ᴄᴏɴᴛᴇɴᴛꜱ ʟᴇᴀᴅꜱ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ ʏᴏᴜ.</i>"""

        HELP_TEXT = """🔰 **Hᴏᴡ ᴛᴏ ᴜꜱᴇ ᴍᴇ ?**

1.ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ ᴏʀ ᴠɪᴅᴇᴏ.
2.ɪ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ !
**ʏᴏᴜ ᴄᴀɴ ᴅᴏᴡɴʟᴏᴀᴅ ᴡɪᴛʜ ꜰᴀꜱᴛ ꜱᴘᴇᴇᴅ🚀**
<b><u>Warning </u></b>⚠️
<i>🔞 ᴘʀᴏɴ ᴄᴏɴᴛᴇɴᴛꜱ ʟᴇᴀᴅꜱ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ ʏᴏᴜ.</i>"""


        ABOUT_TEXT = """
<b>⚜ ᴍʏ ɴᴀᴍᴇ : <a href='https://t.me/FileToLinkiBot'>ꜰɪʟᴇᴛᴏʟɪɴᴋɪʙᴏᴛ</a></b>
<b>📬 ᴜᴘᴅᴀᴛᴇꜱ  : @M2LiNKS</b>
<b>🔸ꜱᴜᴘᴘᴏʀᴛ  : <a href='https://t.me/M2LiNKSCommunity'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>



"""

        stream_msg_text ="""
<u>**ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ɢᴇɴᴇʀᴀᴛᴇᴅ ʏᴏᴜʀ ʟɪɴᴋ !**</u>\n
<b>📂 ꜰɪʟᴇ ɴᴀᴍᴇ :</b> {}\n
<b>📦 ꜰɪʟᴇ ꜱɪᴢᴇ :</b> {}\n
<b>📥 ᴅᴏᴡɴʟᴏᴀᴅ :</b> {}\n
<b>🖥 ᴡᴀᴛᴄʜ :</b> {}"""

        ban_text="__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ.__\n\n**[Cᴏɴᴛᴀᴄᴛ ꜱᴜᴘᴘᴏʀᴛ](https://t.me/M2linksCommunity) Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**"

# ------------------------------------------------------------------------------

class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about')
        ],        
        [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇꜱ", url='https://t.me/M2LINKS'),
        InlineKeyboardButton("ᴏᴡɴᴇʀ", url='https://t.me/Prince_Star_Lord')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about')
        ],
        [
        InlineKeyboardButton('ᴄʟᴏꜱᴇ', callback_data='close'),
        ],        
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help')
        ],
        [
        InlineKeyboardButton('ᴄʟᴏꜱᴇ', callback_data='close'),
        ]        
        ]
    )
