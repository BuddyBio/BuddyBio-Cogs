from discord.channel import CategoryChannel
from discord.ext.commands import MissingPermissions
from redbot.core import commands
import discord



class DeleteMsgs(commands.Cog):
    """DeleteMsgs cog"""

    def __init__(self, bot):
        self.bot = bot

    

    @commands.command()
    @commands.is_owner()
    async def nuke(self, ctx, channel_name: discord.TextChannel):
        """Deletes a channel mentioned by the server/bot owner."""
        if channel_name is not None:
            await channel_name.clone(reason="Has been nuked")
            await channel_name.delete()
        else:
            await ctx.send(f'No channel named **{channel_name}** was found')