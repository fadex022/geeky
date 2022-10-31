""""
Copyright © GaussDev 2022 - https://github.com/fadex022
Description:
This is a template to create your own discord bot in python.

Version: 5.3
"""

import json
from typing import Callable, TypeVar
import os

from discord.ext import commands

from exceptions import *
from helpers import db_manager

T = TypeVar("T")


def is_owner() -> Callable[[T], T]:
    """
    This is a custom check to see if the user executing the command is an owner of the bot.
    """
    async def predicate(context: commands.Context) -> bool:
        
        if str(context.author.id) not in os.getenv("owners").split(" "):
            raise UserNotOwner
        return True

    return commands.check(predicate)


def not_blacklisted() -> Callable[[T], T]:
    """
    This is a custom check to see if the user executing the command is blacklisted.
    """
    async def predicate(context: commands.Context) -> bool:
        if await db_manager.is_blacklisted(context.author.id):
            raise UserBlacklisted
        return True

    return commands.check(predicate)
