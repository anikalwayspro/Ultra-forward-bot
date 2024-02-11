import re, asyncio
from database import db
from config import temp
from .test import CLIENT 
from translation import Translation
from pyrogram import Client, filters 
from pyropatch.utils import unpack_new_file_id
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

CLIENT = CLIENT()
COMPLETED_BTN = InlineKeyboardMarkup([[InlineKeyboardButton('💟 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 💟', url='https://t.me/venombotsupport')],
                [InlineKeyboardButton('💠 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ 💠', url='https://t.me/venombotupdates')]])
CANCEL_BTN = InlineKeyboardMarkup([[InlineKeyboardButton('• ᴄᴀɴᴄᴇʟ', 'terminate_frwd')]])

@Client.on_message(filters.command("unequify") & filters.private)

async def unequify(client, message):
    # ... (rest of the function code)

    async with client.action(chat_id, "typing"):  # Indicate typing while processing
        try:
            await sts.edit(Translation.DUPLICATE_TEXT.format(total, deleted, "ᴘʀᴏɢʀᴇssɪɴɢ"), reply_markup=CANCEL_BTN)
            async for message in bot.search_messages(chat_id=chat_id, filter="document"):
                if temp.CANCEL.get(user_id) == True:
                    await sts.edit(Translation.DUPLICATE_TEXT.format(total, deleted, "ᴄᴀɴᴄᴇʟʟᴇᴅ"), reply_markup=COMPLETED_BTN)
                    return await bot.stop()

                try:  # Handle potential exceptions within the loop
                    file = message.document
                    file_id = file.file_id  # Use an alternative way to get the file ID
                    if file_id in MESSAGES:
                        DUPLICATE.append(message.id)
                    else:
                        MESSAGES.append(file_id)
                    total += 1
                    if total % 10000 == 0:
                        await sts.edit(Translation.DUPLICATE_TEXT.format(total, deleted, "ᴘʀᴏɢʀᴇssɪɴɢ"), reply_markup=CANCEL_BTN)
                    if len(DUPLICATE) >= 100:
                        await bot.delete_messages(chat_id, DUPLICATE)
                        deleted += 100
                        await sts.edit(Translation.DUPLICATE_TEXT.format(total, deleted, "ᴘʀᴏɢʀᴇssɪɴɢ"), reply_markup=CANCEL_BTN)
                        DUPLICATE = []
                except Exception as e:
                    print(f"Error processing message: {e}")

        except Exception as e:
            await sts.edit(str(e))
    # ... (rest of the function code)


    await sts.edit(Translation.DUPLICATE_TEXT.format(total, deleted, "ᴄᴏᴍᴘʟᴇᴛᴇᴅ"), reply_markup=COMPLETED_BTN)
