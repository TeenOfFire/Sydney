from pyrogram import Client, filters
import datetime
import time
from database.users_chats_db import db
from info import ADMINS
from utils import broadcast_messages
import asyncio
        
@Client.on_message(filters.command("broadcast") & filters.user(ADMINS) & filters.reply)
async def verupikkals(bot, message):
    users = await db.get_all_users()
    b_msg = message.reply_to_message
    sts = await message.reply_text(
        text='📲Broadcasting ♻️'
    )
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    blocked = 0
    deleted = 0
    failed =0

    success = 0
    async for user in users:
        pti, sh = await broadcast_messages(int(user['id']), b_msg)
        if pti:
            success += 1
        elif pti == False:
            if sh == "Blocked":
                blocked+=1
            elif sh == "Deleted":
                deleted += 1
            elif sh == "Error":
                failed += 1
        done += 1
        await asyncio.sleep(2)
        if not done % 20:
            await sts.edit(f"📲<b> Broadcasting ♻️ </b>\n● Total Users » {total_users}\n● Completed » {done} / {total_users}\n● Success » {success}\n● Blocked » {blocked}\n● Deleted » {deleted}") 
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time)) 
    await sts.edit(f"<b>📲 Broadcast Complete ✅</b>\n⌚ In {time_taken} Seconds\n\n● Total Users » {total_users}\n● Completed » {done} / {total_users}\n● Success » {success}\n● Blocked » {blocked}\n● Deleted » {deleted}")
