import discord
from discord.ext import commands
from decouple import config

bot = commands.Bot("?")


@bot.event
async def on_ready():
    print(f"Simbora! Estou conectado como {bot.user}")

@bot.event
async def on_reaction_add(reaction, user):
    print(reaction.emoji)
    if reaction.emoji == "☑️":
        role = user.guild.get_role(680102628797317165)
        await user.add_roles(role)
    elif reaction.emoji == "🏎️":
        role = user.guild.get_role(760639242359013376)
        await user.add_roles(role)
    elif reaction.emoji == "🔫":
        role = user.guild.get_role(888712374012477460)
        await user.add_roles(role)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "put" in message.content:
        await message.channel.send(f"```Por favor, {message.author.name}, evite usar palavrões, para não ser punido!```")

        await message.delete()

    if "lixo" in message.content:
        await message.channel.send(f"```Por favor, {message.author.name}, evite usar palavrões, para não ser punido!```")

        await message.delete()

    if "fdp" in message.content:
        await message.channel.send(f"```Por favor, {message.author.name}, evite usar palavrões, para não ser punido!```")

        await message.delete()

    if "rui" in message.content:
        await message.channel.send(f"```Por favor, {message.author.name}, evite usar palavrões, para não ser punido!```")

        await message.delete()

    if "vsf" in message.content:
        await message.channel.send(f"```Por favor, {message.author.name}, evite usar palavrões, para não ser punido!```")

        await message.delete()

    if "fud" in message.content:
        await message.channel.send(f"```Por favor, {message.author.name}, evite usar palavrões, para não ser punido!```")

        await message.delete()

    if "fod" in message.content:
        await message.channel.send(f"```Por favor, {message.author.name}, evite usar palavrões, para não ser punido!```")

        await message.delete()

    if "merd" in message.content:
        await message.channel.send(f"```Por favor, {message.author.name}, evite usar palavrões, para não ser punido!```")

        await message.delete()

    if "bost" in message.content:
        await message.channel.send(f"```Por favor, {message.author.name}, evite usar palavrões, para não ser punido!```")

        await message.delete()

    if "podre" in message.content:
        await message.channel.send(f"```Por favor, {message.author.name}, evite usar palavrões, para não ser punido!```")

        await message.delete()

    if "vermifogo" in message.content:
        await message.channel.send(f"```Por favor, {message.author.name}, evite usar palavrões, para não ser punido!```")

        await message.delete()

    await bot.process_commands(message)

    
@bot.command(name="oi")
async def mandar_oi(ctx):
    name = ctx.author.name

    resposta = "Olá, " + name

    await ctx.send(resposta)

@bot.command(name="gol")
async def music_ribamar(ctx):
    name = ctx.author.name

    resposta = "```Hoje tem gol do Ribamaaaaar, Ribamaaaaar```"

    await ctx.send(resposta)

@bot.command(name="live")
async def stream(ctx):
    name = ctx.author.name

    resposta = "```Uude está fazendo lives na twitch, então já segue lá!!``` link: https://www.twitch.tv/uude_"

    await ctx.send(resposta)

@bot.command(name="sociais")
async def social_media(ctx):
    name = ctx.author.name

    resposta = "```Siga Uude nas redes sociais!!``` Instagram: https://www.instagram.com/uude1 Twitter: https://www.twitter.com/uudebr"

    await ctx.send(resposta)

@bot.command(name="comandos")
async def commands(ctx):
    name = ctx.author.name

    resposta = "```?sociais ?live ?gol ?oi```"

    await ctx.send(resposta)

@bot.command(name="mafia")
async def get_random_image(ctx):
    url_image = "https://cdn.discordapp.com/attachments/959710109251010631/973514106638331904/unknown.png"

    embed_image = discord.Embed(
        title="UUDE MAFIOSO",
        description="VOCE FOI PEGO PELO UUDE MAFIOSO",
        color=0x0000FF,
    )

    embed_image.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed_image.set_footer(text="Feito por " + bot.user.name, icon_url=bot.user.avatar_url)

    embed_image.add_field(name="INSTAGRAM", value="SIGA UUDE NO INSTAGRAM https://instagram.com/uude1")
    embed_image.add_field(name="BOT", value="BOT RIBAMAR")

    embed_image.add_field(name="MAFIOSO", value=url_image, inline=False)

    embed_image.set_image(url=url_image)

    await ctx.send(embed=embed_image)

@bot.command(name="registro")
async def get_random_image(ctx):
    url_image = "https://www.google.com/url?sa=i&url=https%3A%2F%2Finformebaiano.com.br%2F154226%2Fnoticia%2Fbrasil%2Femissao-de-passaportes-sera-feita-apenas-em-casos-de-extrema-necessidade&psig=AOvVaw0pymqJ86xsQtLnTyCqA-eE&ust=1632045889004000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCLia3e-iiPMCFQAAAAAdAAAAABAD"

    embed_image = discord.Embed(
        title="REGISTRO DE VIEWER",
        description="Clique no emoji e se registre como viewer",
        color=0x9638ff,
    )

    embed_image.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed_image.set_footer(text="Feito por " + bot.user.name, icon_url=bot.user.avatar_url)

    embed_image.set_image(url=url_image)

    await ctx.send(embed=embed_image)

@bot.command(name="fugaxbala")
async def get_random_image(ctx):
    url_image = "https://www.google.com/url?sa=i&url=https%3A%2F%2Finformebaiano.com.br%2F154226%2Fnoticia%2Fbrasil%2Femissao-de-passaportes-sera-feita-apenas-em-casos-de-extrema-necessidade&psig=AOvVaw0pymqJ86xsQtLnTyCqA-eE&ust=1632045889004000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCLia3e-iiPMCFQAAAAAdAAAAABAD"

    embed_image = discord.Embed(
        title="FUGA X BALA",
        description="Clique no emoji que se identifica",
        color=0x9638ff,
    )

    embed_image.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed_image.set_footer(text="Feito por " + bot.user.name, icon_url=bot.user.avatar_url)

    embed_image.add_field(name="( Rei da fuga) x ( Rei da bala)", value="Faça sua escolha", inline=False)

    embed_image.set_image(url=url_image)

    await ctx.send(embed=embed_image)

TOKEN = config("TOKEN_RIBAMAR")
bot.run(TOKEN)