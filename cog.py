from arcacog import ArcaCogConfig, ArcaCog, SlashCommandGroup
from discord import Option
from discord.ext.bridge import BridgeContext


class WhoIs(ArcaCog):
    whois_group = SlashCommandGroup(name="whois", description="Commands related to general queuing.")

    def __init__(self, bot):
        super().__init__(bot=bot, config=ArcaCogConfig(cog_name="whois", cog_title="whois"))

    @whois_group.command(name="discord")
    async def whois_discord(self, ctx: BridgeContext, user_id: Option(str, "user id", required=True)):
        """
        Find out what user has this Discord ID
        """
        user = await self.bot.fetch_user(user_id)
        if user is None:
            await ctx.reply("User not found.")
            return
        await ctx.reply(f"{user_id} -> <@{user_id}>")


def setup(bot):
    bot.add_cog(WhoIs(bot))
