import random

from telegram import Update
from telegram.ext import CallbackContext, run_async

import GabiBraunRobot.modules.animequote_string as animequote_string
from GabiBraunRobot import dispatcher
from GabiBraunRobot.modules.disable import DisableAbleCommandHandler


@run_async
def aq(update: Update, context: CallbackContext):
    context.args
    update.effective_message.reply_text(random.choice(animequote_string.ANIMEQUOTE))


__help__ = """
 • `/aq`*:* for random animequote
"""

AQ_HANDLER = DisableAbleCommandHandler("aq", aq)

dispatcher.add_handler(AQ_HANDLER)

__mod_name__ = "Animequote"
