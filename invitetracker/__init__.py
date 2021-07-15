from .invitetracker import InviteTracker


def setup(bot):
    bot.add_cog(InviteTracker(bot))