import random

from telegram import Update
from telegram.ext import CallbackContext, run_async

import GabiBraunRobot.modules.animequotes_strings as animequotes_strings
from GabiBraunRobot import dispatcher
from GabiBraunRobot.modules.disable import DisableAbleCommandHandler


@run_async
def animequotes(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_photo = (
        message.reply_to_message.reply_photo
        if message.reply_to_message
        else message.reply_photo
    )
    reply_photo(random.choice(animequotes_strings.QUOTES_IMG))


__help__ = """
 • `/animequotes`*:* gives random anime quotes
 
"""
ANIMEQUOTES_HANDLER = DisableAbleCommandHandler("animequotes", animequotes)

dispatcher.add_handler(ANIMEQUOTES_HANDLER)

__mod_name__ = "AnimeQuotes"
__command_list__ = ["animequotes"]
__handlers__ = [ANIMEQUOTES_HANDLER]
