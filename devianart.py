# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• {i}devian <search query> ; <no of pics>
    Devian-Art Image Search.
"""

import re
import requests
import random
from bs4 import BeautifulSoup as bs
from . import *


@ultroid_cmd(pattern="devian ?(.*)")
async def downakd(e):
    match = e.pattern_match.group(1)
    if not match:
        return await eor(e, "`Give Query to Search...`")
    random = False
    if ";" in match:
        num = int(match.split(";")[1])
        if num == 1:
            random = True
        match = match.split(";")[0]
    else:
        num = 5
    xd = await eor(e, "`Processing...`")
    match = match.replace(" ", "+")
    link = "https://www.deviantart.com/search?q=" + match
    ct = requests.get(link).content
    st = bs(ct, "html.parser", from_encoding="utf-8")
    res = st.find_all("img", loading="lazy", src=re.compile("https://images-wixmp"))[:num]
    if random:
        res = [random.choice(res)]
    out = []
    for on in res:
        out.append(on["src"])
    if len(out) == 0:
        return await xd.edit("`No Results Found!`")
    await e.client.send_file(
        e.chat_id, out, caption=f"Uploaded {len(res)} Images\n", album=True
    )
    await xd.delete()