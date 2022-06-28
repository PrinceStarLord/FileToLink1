# This file is a part of TG-Direct-Link-Generator
from main.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Language(object):
    class en(object):
        START_TEXT = """
**👋 Hᴇʏ, {}**\n
<b>ɪ'ᴍ ɪɴꜱᴛᴀɴᴛ ᴛᴇʟᴇɢʀᴀᴍ ꜰɪʟᴇ ᴛᴏ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ.</b>\n
<b>ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ᴛᴏ ɢᴇᴛ ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ</b>\n
<b><u>Warning ⚠️</u></b>\n
<i>🔞 ᴘʀᴏɴ ᴄᴏɴᴛᴇɴᴛꜱ ʟᴇᴀᴅꜱ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ ʏᴏᴜ.</i>"""

        HELP_TEXT = """🔰 **Hᴏᴡ ᴛᴏ ᴜꜱᴇ ᴍᴇ ?**

<i>1.Send Me Any File Or Video.</i>
<i>2.I Will Provide You Direct Download Link !</i>

**You Can Download With Fast Speed 🚀**

<b><u>Warning ⚠️</u></b>
<i>🔞 ᴘʀᴏɴ ᴄᴏɴᴛᴇɴᴛꜱ ʟᴇᴀᴅꜱ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ ʏᴏᴜ.</i>"""


        ABOUT_TEXT = """
<b>⚜ ᴍʏ ɴᴀᴍᴇ : <a href='https://t.me/FileToLinkiBot'>ꜰɪʟᴇᴛᴏʟɪɴᴋɪʙᴏᴛ</a></b>\n
<b>⚜ ᴜᴘᴅᴀᴛᴇꜱ  : @M2LiNKS</b>\n
<b>🔸ꜱᴜᴘᴘᴏʀᴛ  : @M2LiNKSCOMMUNITY</b>\n

"""

        stream_msg_text ="""
<u>**Successfully Generated Your Link !**</u>\n
<b>📂 File Name :</b> {}\n
<b>📦 File Size :</b> {}\n
<b>📥 Download :</b> {}\n
<b>🖥 Watch :</b> {}"""

        ban_text="__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ.__\n\n**[Cᴏɴᴛᴀᴄᴛ Dᴇᴠᴇʟᴏᴘᴇʀ](https://t.me/groupdc) Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**"

# ------------------------------------------------------------------------------

class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about')
        ],        
        [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇꜱ", url='https://t.me/groupdcbots'),
        InlineKeyboardButton("ʀᴇᴘᴏ", url='https://github.com/selfie-bd/TG-Direct-Link-Generator')]
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
