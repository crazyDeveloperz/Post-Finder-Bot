from utils import *
from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

@Client.on_message(filters.command("start") & ~filters.channel)
async def start(bot, message):
    await add_user(message.from_user.id, message.from_user.first_name)
    await message.reply(text=script.START.format(message.from_user.mention),
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('˵ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ˵', url=f'http://t.me/Postfindbot?startgroup=true')
            ],[InlineKeyboardButton("ʜᴇʟᴘ", callback_data="misc_help2"),
                                                            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="misc_about"),
            ],[InlineKeyboardButton("ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", callback_data="misc_bhole")]]))  


@Client.on_message(filters.command("help"))
async def help(bot, message):
    await message.reply(text=script.HELP, 
                        disable_web_page_preview=True)

@Client.on_message(filters.command("help2"))
async def help(bot, message):
    await message.reply(text=script.HELP2, 
                        disable_web_page_preview=True)

@Client.on_message(filters.command("about"))
async def about(bot, message):
    await message.reply(text=script.ABOUT.format((await bot.get_me()).mention), 
                        disable_web_page_preview=True)

@Client.on_message(filters.command("crezy"))
async def help(bot, message):
    await message.reply(text=script.CREZY, 
                        disable_web_page_preview=True)

@Client.on_message(filters.command("bhole"))
async def help(bot, message):
    await message.reply(text=script.BHOLE, 
                        disable_web_page_preview=True)

@Client.on_message(filters.command("stats"))
async def stats(bot, message):
    g_count, g_list = await get_groups()
    u_count, u_list = await get_users()
    await message.reply(script.STATS.format(u_count, g_count))

@Client.on_message(filters.command("id"))
async def id(bot, message):
    text = f"Current Chat ID: `{message.chat.id}`\n"
    if message.from_user:
       text += f"Your ID: `{message.from_user.id}`\n"
    if message.reply_to_message:
       if message.reply_to_message.from_user:
          text += f"Replied User ID: `{message.reply_to_message.from_user.id}`\n"
       if message.reply_to_message.forward_from:
          text += f"Replied Message Forward from User ID: `{message.reply_to_message.forward_from.id}`\n"
       if message.reply_to_message.forward_from_chat:
          text += f"Replied Message Forward from Chat ID: `{message.reply_to_message.forward_from_chat.id}\n`"
    await message.reply(text)

@Client.on_callback_query(filters.regex(r"^misc"))
async def misc(bot, update):
    data = update.data.split("_")[-1]
    if data=="home":
       await update.message.edit(text=script.START.format(update.from_user.mention),
                                 disable_web_page_preview=True,
                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('˵ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ˵', url=f'http://t.me/Postfindbot?startgroup=true')
            ],[InlineKeyboardButton("ʜᴇʟᴘ", callback_data="misc_help2"),
                                                            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="misc_about"),
            ],[InlineKeyboardButton("ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", callback_data="misc_bhole")]])) 
   
    elif data=="help":
        await update.message.edit(text=script.HELP,
                                  disable_web_page_preview=True,
                                  reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="misc_home")]]))
    
    elif data=="help2":
       await update.message.edit(text=script.HELP2, 
                                 disable_web_page_preview=True,
                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🧑‍💻 ᴄᴏɴᴛᴀᴄᴛ ᴛᴏ ᴏᴡɴᴇʀ 🧑‍💻", callback_data="misc_crezy"),
            ],[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="misc_home"),
                                                            InlineKeyboardButton("ɴᴇxᴛ", url=f'https://graph.org/support-04-04')]])) 

    elif data=="about":
        await update.message.edit(text=script.ABOUT.format((await bot.get_me()).mention), 
                                  disable_web_page_preview=True,
                                  reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="misc_home")]]))
      
        
    elif data=="crezy":
        await update.message.edit(text=script.CREZY, 
                                 disable_web_page_preview=True,
                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💶 ᴘʟᴇᴀsᴇ ᴅᴏɴᴀᴛᴇ 💰", url=f'https://graph.org/support-04-04'),
            ],[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="misc_home"),
                                                            InlineKeyboardButton("ᴄᴏɴᴛᴀᴄᴛ", url=f'https://telegram.me/crezyDevelopers')]]))


    elif data=="bhole":
       await update.message.edit(text=script.BHOLE, 
                                 disable_web_page_preview=True,
                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🧑‍💻 ᴄᴏɴᴛᴀᴄᴛ ᴛᴏ ᴏᴡɴᴇʀ 🧑‍💻", callback_data="misc_crezy"),
                                                                  ],[InlineKeyboardButton("🖤 ᴊᴏɪɴ ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟ 💠", url=f'https://t.me/movieflix_officall'),
            ],[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="misc_home"),
                                                            InlineKeyboardButton("ɴᴇxᴛ", url=f'https://3qallmoviez.blogspot.com')]]))   
