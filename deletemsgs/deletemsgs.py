from discord.channel import CategoryChannel
from discord.ext.commands import MissingPermissions, has_permissions
from redbot.core import commands
import discord



class DeleteMsgs(commands.Cog):
    """DeleteMsgs cog"""

    def __init__(self, bot):
        self.bot = bot

    trigger = False

    @commands.command()
    async def nuke(self, ctx, channel_name: discord.TextChannel):
        """Deletes a channel mentioned by the server/bot owner."""
        if ctx.message.author.guild_permissions.administrator:
            if channel_name is not None:
                await channel_name.clone(reason="Has been nuked")
                await channel_name.delete()
            else:
                await ctx.send(f'No channel named **{channel_name}** was found')
        else:
            await ctx.send("You don't have permission to do that.")
    @commands.command()
    async def autodelete(self, ctx, value):
        """Use on/off to enable or disable autodelete function."""
        if value == "on":
           global trigger
           trigger = True
           await ctx.send("You turned on the autodeletion.")
        elif value == "off":
            trigger = False
            await ctx.send("You turned off the autodeletion.")
        else:
            await ctx.send("You gave a wrong value")

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        global trigger
        if trigger:
            for c in member.guild.text_channels:
                await c.purge(limit=None, check=lambda m: m.author==member)