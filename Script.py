import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    START_TXT = """<i><b>🎃 Helo {}, I'm <a href=https://telegram.me/{}>{}</a></i></b> \n\n<i><b>🎗I Can Provide You Any Movies, Web-Series, Anime, K-Dramas, Animation, etc.,</i></b>"""
    HELP_TXT = """<b>🥁 </b><b><u>How To Download Any Movie, Series, Anime etc., For Free???</u></b> \n\n<b>🎗Group [01]: </b><b>https://t.me/+WzsvFY3qXa9kZGVl</b> \n\n<b>🎗Group</b> <b>[02]: </b><b>https://t.me/+EdJU1Hqk1N80ZWQ1</b> \n\n<b>🔆</b> <b>Join Any Of These Groups</b>👆"""
    ABOUT_TXT = """<i><u>🧶 </u></i><i><u><b>Follow These Steps To Connect Me To Your Group</b>👇</u>

1. Click on This [</i><a href="http://telegram.me/heroriderbot?startgroup=true"><i>Blue Text</i></a><i>]
2. Select Your Group
3. Make Me Admin in Your Group</i>"""    
    
    STATUS_TXT = """<b>🎗️ My Statistics 📲</b>

◉ <b>Total Files :</b> {}
◉ <b>Total Users :</b> {}
◉ <b>Total Chats :</b> {}
◉ <b>Used Storage :</b> {} 
◉ <b>Free Storage :</b> {}"""

    LOG_TEXT_G = """<b>#NewGroup</b>
<b>● Group »</b> {} (<code>{}</code>)
<b>● Total Members »</b> <code>{}</code>
<b>● Added By »</b> {}
"""
    LOG_TEXT_P = """<b>#NewUser</b>
◉ ID - <code>{}</code>
◉ Name - {}
"""
