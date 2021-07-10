from .deletemsgs import DeleteMsgs


def setup(bot):
    bot.add_cog(DeleteMsgs(bot))