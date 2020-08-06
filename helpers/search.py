import discord
from typing import List

def validate(name: str) -> bool:
    if len(name) < 2:
        return False
    if len(name) > 32:
        return False
    return True

def search(emojis: List[discord.Emoji], query: str) -> list:
    valid = []
    for emoji in emojis:
        if query in emoji.name:
            valid.append(emoji)
    return valid

def get_emoji(emojis: List[discord.Emoji], nameOrID):
    item = None
    if nameOrID.isnumeric():
        item = emojis[int(nameOrID)]
    else:
        valid = search(emojis, nameOrID)
        item = valid[0]
    emoji = ""
    if item.animated:
        emoji = f"<a:{item.name}:{item.id}>"
    else:
        emoji = f"<:{item.name}:{item.id}>"
    return emoji

def gen_embeds(emojis: List[discord.Emoji], query: str, const = 5) -> list:
    valid = search(emojis, query)

    length = len(valid) // const + 1

    pages = []
    page = []
    for i, item in enumerate(valid):
        if i % const == 0:
            if i != 0:
                pages.append(page)
                page = []
        page.append(item)
    if len(page) > 0:
        pages.append(page)

    descs = []
    for page_item in pages:
        desc = ""
        for item in page_item:
            emoji = ""
            if item.animated:
                emoji = f"<a:{item.name}:{item.id}>"
            else:
                emoji = f"<:{item.name}:{item.id}>"
            desc += f"{emoji} {item.name} `ID: {emojis.index(item)}`\n"
        descs.append(desc)

    embeds = []
    for i, desc in enumerate(descs):
        embed = discord.Embed(title=f"'{query}' Page {i+1} of {len(descs)}", description=desc, colour=0x2FFF2F)
        embeds.append(embed)
        if len(descs) > 1:
            embed.set_footer(text="To view another page use %search <name> <page>")

    return embeds

