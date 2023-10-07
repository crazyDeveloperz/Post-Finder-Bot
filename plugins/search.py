import asyncio
from info import *
from utils import *
from time import time 
from client import User
from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

@Client.on_message(filters.text & filters.group & filters.incoming & ~filters.command(["verify", "connect", "id"]))
async def search(bot, message):
    f_sub = await force_sub(bot, message)
    if f_sub==False:
       return     
    channels = (await get_group(message.chat.id))["channels"]
    if bool(channels)==False:
       return     
    if message.text.startswith("/"):
       return    
    query   = message.text 
    head    = "<b>𝙃𝙚𝙧𝙚 𝙞𝙨 𝙩𝙝𝙚 𝙧𝙚𝙨𝙪𝙡𝙩𝙨 👇\n\n𝙋𝙧𝙤𝙢𝙤𝙩𝙚𝙙 𝘽𝙮 <a href='https://t.me/Crazybotz'>𝘾𝙧𝙖𝙯𝙮</a></b>\n\n"
    results = ""
    try:
       for channel in channels:
           async for msg in User.search_messages(chat_id=channel, query=query):
               name = (msg.text or msg.caption).split("\n")[0]
               if name in results:
                  continue 
               results += f"<b><I>♻️ {name}\n🔗<a href='{msg.link}'>𝘾𝙡𝙞𝙘𝙠 𝙝𝙚𝙧𝙚</a></b>\n\n"                                                      
       if bool(results)==False:
          movies = await search_imdb(query)
          buttons = []
          for movie in movies: 
              buttons.append([InlineKeyboardButton(movie['title'], callback_data=f"recheck_{movie['id']}")])
          msg = await message.reply_photo(photo="https://telegra.ph/file/70317039d29a9107feac1.jpg",
                                          caption="<b><I>I Couldn't find anything related to Your Query😕.\nDid you mean any of these?</I></b>", 
                                          reply_markup=InlineKeyboardMarkup(buttons))
       else:
          msg = await message.reply_text(text=head+results, disable_web_page_preview=True)
       _time = (int(time()) + (15*60))
       await save_dlt_message(msg, _time)
    except:
       pass
       


@Client.on_callback_query(filters.regex(r"^recheck"))
async def recheck(bot, update):
    clicked = update.from_user.id
    try:      
       typed = update.message.reply_to_message.from_user.id
    except:
       return await update.message.delete(2)       
    if clicked != typed:
       return await update.answer("𝐓𝐡𝐚𝐭'𝐬 𝐧𝐨𝐭 𝐟𝐨𝐫 𝐲𝐨𝐮! 👀", show_alert=True)

    m=await update.message.edit("𝗦𝗲𝗮𝗿𝗰𝗵𝗶𝗻𝗴...")
    id      = update.data.split("_")[-1]
    query   = await search_imdb(id)
    channels = (await get_group(update.message.chat.id))["channels"]
    head    = "𝙄 𝙃𝙖𝙫𝙚 𝙎𝙚𝙖𝙧𝙘𝙝𝙚𝙙 𝙈𝙤𝙫𝙞𝙚 𝙒𝙞𝙩𝙝 𝙒𝙧𝙤𝙣𝙜 𝙎𝙥𝙚𝙡𝙡𝙞𝙣𝙜 𝘽𝙪𝙩 𝙏𝙖𝙠𝙚 𝙘𝙖𝙧𝙚 𝙣𝙚𝙭𝙩 𝙩𝙞𝙢𝙚 👇\n\n𝙋𝙧𝙤𝙢𝙤𝙩𝙚𝙙 𝘽𝙮 <a href='https://t.me/Crazybotz'>𝘾𝙧𝙖𝙯𝙮</a></b>\n\n"
    results = ""
    try:
       for channel in channels:
           async for msg in User.search_messages(chat_id=channel, query=query):
               name = (msg.text or msg.caption).split("\n")[0]
               if name in results:
                  continue 
               results += f"<b>♻️🍿 {name}</I></b>\n\n🔗 <a href='{msg.link}'>𝘾𝙡𝙞𝙘𝙠 𝙝𝙚𝙧𝙚</a></b>\n\n"
       if bool(results)==False:          
          return await update.message.edit("𝙎𝙩𝙞𝙡𝙡 𝙣𝙤 𝙧𝙚𝙨𝙪𝙡𝙩𝙨 𝙛𝙤𝙪𝙣𝙙! 𝙋𝙡𝙚𝙖𝙨𝙚 𝙍𝙚𝙦𝙪𝙚𝙨𝙩 𝙏𝙤 𝙂𝙧𝙤𝙪𝙥 𝘼𝙙𝙢𝙞𝙣...", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔺 ʀᴇQᴜᴇꜱᴛ ᴛᴏ ᴀᴅᴍɪɴ 🔺", callback_data=f"request_{id}")]]))
       await update.message.edit(text=head+results, disable_web_page_preview=True)
    except Exception as e:
       await update.message.edit(f"❌ Error: `{e}`")


@Client.on_callback_query(filters.regex(r"^request"))
async def request(bot, update):
    clicked = update.from_user.id
    try:      
       typed = update.message.reply_to_message.from_user.id
    except:
       return await update.message.delete()       
    if clicked != typed:
       return await update.answer("𝐓𝐡𝐚𝐭'𝐬 𝐧𝐨𝐭 𝐟𝐨𝐫 𝐲𝐨𝐮! 👀", show_alert=True)

    admin = (await get_group(update.message.chat.id))["user_id"]
    id    = update.data.split("_")[1]
    name  = await search_imdb(id)
    url   = "https://www.imdb.com/title/tt"+id
    text  = f"#RequestFromYourGroup\n\nName: {name}\nIMDb: {url}"
    await bot.send_message(chat_id=admin, text=text, disable_web_page_preview=True)
    await update.answer("✅ 𝙍𝙚𝙦𝙪𝙚𝙨𝙩 𝙎𝙚𝙣𝙩 𝙏𝙤 𝘼𝙙𝙢𝙞𝙣...", show_alert=True)
    await update.message.delete(60)
