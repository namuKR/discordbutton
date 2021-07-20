from discord.ext import commands
from discord_buttons_plugin import *

client = commands.Bot(command_prefix="!")
buttons = ButtonsClient(client)


@client.event
async def on_ready():
    print("Bot is ready!")


@client.command()
async def poll(ctx):
    if ctx.message.author.id == 696684185003360297:
        await buttons.send(
            content="<@679936298953211984> 생일 기념으로 진행하는 Nitro Giveaway에 참여할 사람은 아래 버튼을 누르세요!",
            channel=ctx.channel.id,
            components=[
                ActionRow([
                    Button(
                        label="참여",
                        style=ButtonType().Primary,
                        custom_id="join",
                        emoji={
                            "id": None,
                            "name": "🎉",
                            "animated": False
                        }
                    )
                ])
            ]
        )
    else:
        await ctx.send("Poll create는 **Bot Developer**이상의 권한을 가지고 있는 사용자만 할 수 있어요!")


@buttons.click
async def join(ctx):
    await ctx.reply(f"<@{ctx.member.id}>님이 참여를 선언하였습니다!")

client.run("ODYzNjc2NTIwODA2NDgxOTIx.YOqXcA.W6Dg0iipT4wlTMiqcgapVCN0hZU")
