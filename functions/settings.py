import asyncio
import time
from pyrogram.emoji import *
from pyrogram.enums import MessageEntityType
from pyrogram.types import ForceReply
from config import LOGGER, PASS
from database.database import db
from pyrogram import types, errors, filters
from translation import Translation


async def Settings(m: "types.Message"):
    usr_id = m.chat.id
    is_command = m.entities[0].type is MessageEntityType.BOT_COMMAND

    if is_command:
        message = await m.reply_text('**İşleniyor..**', reply_to_message_id=m.id)
        message = message.edit
    else:
        message = m.edit

    user_data = await db.get_user_data(usr_id)

    if not user_data:
        await message("Verileriniz veritabanından alınamadı!")
        return

    upload_as_doc = user_data.get("upload_as_doc", False)
    thumbnail = user_data.get("thumbnail", None)
    # generate_sample_video = user_data.get("generate_sample_video", False)
    generate_ss = user_data.get("generate_ss", False)
    get_notif = user_data.get("notif", False)
    get_caption = user_data.get("caption", False)
    get_aria2 = user_data.get("aria2", False)

    buttons_markup = [
        [types.InlineKeyboardButton(f"{'🔔' if get_notif else '🔕'} Bildirimler",
                                    callback_data="notifon")],
        [types.InlineKeyboardButton(f"{'🎥 Video' if upload_as_doc else '🗃️ Dosya'} Olarak Yükle",
                                    callback_data="triggerUploadMode")],
        [types.InlineKeyboardButton(f"Library: {'aria2 📚' if get_aria2 else 'aiohttp 📚'}",
                                    callback_data="aria2")],
        # [types.InlineKeyboardButton(f"🎞 Kısa Video Oluştur {'✅' if generate_sample_video else '❎'}",
        # callback_data="triggerGenSample")],
        [types.InlineKeyboardButton(f"📜 Açıklama {'✅' if get_caption else '❎'}",
                                    callback_data="setCaption")],
        [types.InlineKeyboardButton(f"📸 Ekran Görüntüsü Al {'✅' if generate_ss else '❎'}",
                                    callback_data="triggerGenSS")],
        [types.InlineKeyboardButton(f"🌃 Thumbnail {'Değiştir' if thumbnail else 'Ayarla'}",
                                    callback_data="setThumbnail")]
    ]
    if thumbnail:
        buttons_markup.append([types.InlineKeyboardButton("🌆 Thumbnail Göster",
                                                          callback_data="showThumbnail")])
    if is_command:
        buttons_markup.append([types.InlineKeyboardButton(f"Kapat ✖",
                                                          callback_data="close"),
                               ])
    else:
        buttons_markup.append([types.InlineKeyboardButton(f"🔙 Geri",
                                                          callback_data="home"),
                               ])

    try:
        await message(
            text="**⚙ Bot Ayarları**",
            reply_markup=types.InlineKeyboardMarkup(buttons_markup),
            disable_web_page_preview=True
        )
    except errors.MessageNotModified:
        pass
    except errors.FloodWait as e:
        await asyncio.sleep(e.value)
    except Exception as err:
        LOGGER.error(err)


async def Login(c, m: "types.Message"):
    usr_id = m.chat.id
    if PASS:
        try:
            try:
                msg = await m.reply(
                    "**Şifreyi gönderin.**\n\n__(İşlemi iptal etmek için /iptal komutunu kullanabilirsiniz.)__",
                    reply_markup=ForceReply(True))
                _text = await c.listen(usr_id, filters=filters.text, timeout=90)
                if _text.text:
                    textp = _text.text.upper()
                    if textp == "/iptal":
                        await m.delete(True)
                        await msg.delete(True)
                        await msg.reply("__İşlem Başarıyla İptal Edildi.__")
                        return
                else:
                    return
            except TimeoutError:
                await m.reply("__Şifre için daha fazla bekleyemem, tekrar dene.__")
                return
            if textp == PASS:
                await db.add_user_pass(chat_id, textp)
                msg_text = f"__Evet! Başarıyla Oturum Açıldı.__ {FACE_SAVORING_FOOD}"
                await m.reply_text(
                    text=Translation.START_TEXT.format(m.chat.mention),
                    disable_web_page_preview=True,
                    reply_to_message_id=m.id,
                    reply_markup=Translation.START_BUTTONS
                )
            else:
                msg_text = "__Yanlış şifre, tekrar deneyin. /login__"
            await m.reply(msg_text)
        except errors.FloodWait as e:
            time.sleep(e.value)
        except Exception as e:
            LOGGER.error(e)
        await m.delete(True)
        await msg.delete(True)
