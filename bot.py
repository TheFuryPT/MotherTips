import os
import random
import discord

#------------------------------------------------------------------------------------------------------------------------------

token_txt = open('token.txt', 'r')
token = token_txt.read()

dicas = [
        "**A tua mae é como uma lareira: cabe sempre mais um pau!**", 
        "**A tua mae e como a sopa: ninguem gosta mas todos comem!**",
        "**A tua mae e como o pingo doce: sabe bem pagar tao pouco!**",
        "**A tua mae e como a europoupança do mcdonalds: tudo a 1 euro!**",
        "**A tua mae e como a caixa registadora,abre-se por uns trocos!**", 
        "**So comes caldo verde quando a tua mae faz a depilaçao!**",
        "**A tua mae e como os macacos anda de pau em pau!**", 
        "**A tua mae e como um trator: Grande e Gorda**",
        "**A minha piça e tipo arco iris pk a tua mae muda de baton todos os dias**", 
        "**A tua mãe é como o bebe so quer e leitinho!!**",
        "**A tua mãe é tao gorda q tirei lhe uma foto no natal e ainda ta a imprimir!!**", 
        "**A tua mae é como o caldo verde, todos querem por la o xouriço**",
        "**A tua mãe é como o super Mário, salte sempre pela moedinha.**", 
        "**A tua mãe é como o corrimão, toda a gente lhe põe a mão.**",
        "**A tua mãe é como o castor, anda sempre com o pau na boca.**", 
        "**A tua mãe é como o Cachorro Quente, tem sempre uma salsicha lá dentro.**",
        "**A tua mãe é como a Rádio Popular, nem os forretas resistem.**", 
        "**A tua mãe é como a noite, quando leva no cu fica a ver estrelinhas.**",
        "**A tua mãe é como a gripe, apanha-se na rua e trata-se na cama.**", 
        "**A tua mãe é como os bebés, põe na boca tudo o que lhe aparece à frente.**",
        "**A tua mãe é como a erva todos os bois querem comer.**", 
        "**A tua mãe é como a maçã, come-se e deita-se fora.**",
        "**A tua mãe é como a maxmat , profissional dos preços baixos.**", 
        "**A tua mãe é tão gorda que passou á frente da tv e perdi a temporada dos simpsons toda.**",
        "**A diferença entre o caldo verde e a tua mãe é que no caldo verde o chouriço é cortado, na tua mãe é logo inteiro**",
        "**Se o meu pau fosse uma espada a tua mae estava morta.**",
        "**Mata a tua mae e faz arroz de puta.**",
        "**A tua mae e tao gorda que quando vai dar um mergulho na praia as baleias cantam : We are family!**",
        "**A tua mae é como um charro: roda por todos.**",
        "**Se as piças fossem de açucar a tua mae era diabetica.**",
        "**Sabem a diferença entre a tua mae e a lua? A diferença é que á lua nem todos foram.",
        "**A tua mãe é como o MC Donalds, monta negócio em todo o mundo!**",
        "**A tua mãe é como uma rotunda, uns têm prioridade, outros têm de esperar, mas acabam todos por entrar!**",
        "**A cona da tua mãe so e rapada porque o meu caralho e barbeiro.**",
        "**Se os meus espermas fossem luzinhas o cu da tua mae era uma discoteca**",
        ]

#------------------------------------------------------------------------------------------------------------------------------

TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

#------------------------------------------------------------------------------------------------------------------------------

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("with your mom!!"))
    print(f'{client.user.name} is online')

#------------------------------------------------------------------------------------------------------------------------------

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server :slight_smile:  //Fury^^'
    )

#------------------------------------------------------------------------------------------------------------------------------

@client.event
async def on_message(message):
    if message.author == client.user:
        return
#------------------------------------------------------------------------------------------------------------------------------
    if message.content.lower() == '-roast':
        response_dica = random.choice(dicas)
        await message.channel.purge(limit=1)
        await message.channel.send(response_dica)
#------------------------------------------------------------------------------------------------------------------------------
    if message.content.lower() == '-roast random':
        user = random.choice(message.channel.guild.members)
        print(user)

        dicas_random = [
            f"**{user.mention} A tua mae é como uma lareira: cabe sempre mais um pau!**", 
            f"**{user.mention} A tua mae e como a sopa: ninguem gosta mas todos comem!**",
            f"**{user.mention} A tua mae e como o pingo doce: sabe bem pagar tao pouco!**", 
            f"**{user.mention} A tua mae e como a europoupança do mcdonalds: tudo a 1 euro!**",
            f"**{user.mention} A tua mae e como a caixa registadora,abre-se por uns trocos!**", 
            f"**{user.mention} So comes caldo verde quando a tua mae faz a depilaçao!**",
            f"**{user.mention} A tua mae e como os macacos anda de pau em pau!**", 
            f"**{user.mention} A tua mae e como um trator: Grande e Gorda**",
            f"**{user.mention} A minha piça e tipo arco iris pq a tua mae muda de baton todos os dias**", 
            f"**{user.mention} A tua mãe é como o bebe so quer e leitinho!!**",
            f"**{user.mention} A tua mãe é tao gorda q tirei lhe uma foto no natal e ainda ta a imprimir!!**", 
            f"**{user.mention} A tua mae é como o caldo verde, todos querem por la o xouriço**",
            f"**{user.mention} A tua mãe é como o super Mário, salte sempre pela moedinha.**", 
            f"**{user.mention} A tua mãe é como o corrimão, toda a gente lhe põe a mão.**",
            f"**{user.mention} A tua mãe é como o castor, anda sempre com o pau na boca.**", 
            f"**{user.mention} A tua mãe é como o Cachorro Quente, tem sempre uma salsicha lá dentro.**",
            f"**{user.mention} A tua mãe é como a Rádio Popular, nem os forretas resistem.**", 
            f"**{user.mention} A tua mãe é como a noite, quando leva no cu fica a ver estrelinhas.**",
            f"**{user.mention} A tua mãe é como a gripe, apanha-se na rua e trata-se na cama.**", 
            f"**{user.mention} A tua mãe é como os bebés, põe na boca tudo o que lhe aparece à frente.**",
            f"**{user.mention} A tua mãe é como a erva todos os bois querem comer.**", 
            f"**{user.mention} A tua mãe é como a maçã, come-se e deita-se fora.**",
            f"**{user.mention} A tua mãe é como a maxmat , profissional dos preços baixos.**", 
            f"**{user.mention} A tua mãe é tão gorda que passou á frente da tv e perdi a temporada dos simpsons toda.**",
            f"**{user.mention} A diferença entre o caldo verde e a tua mãe é que no caldo verde o chouriço é cortado, na tua mãe é logo inteiro**",
            f"**{user.mention} Se o meu pau fosse uma espada a tua mae estava morta.**",
            f"**{user.mention} Mata a tua mae e faz arroz de puta.**",
            f"**{user.mention} A tua mae e tao gorda que quando vai dar um mergulho na praia as baleias cantam : We are family!**",
            f"**{user.mention} A tua mae é como um charro: roda por todos.**",
            f"**{user.mention} Se as piças fossem de açucar a tua mae era diabetica.**",
            f"**{user.mention} Sabem a diferença entre a tua mae e a lua? A diferença é que á lua nem todos foram.",
            f"**{user.mention} A tua mãe é como o MC Donalds, monta negócio em todo o mundo!**",
            f"**{user.mention} A tua mãe é como uma rotunda, uns têm prioridade, outros têm de esperar, mas acabam todos por entrar!**",
            f"**{user.mention} A cona da tua mãe so e rapada porque o meu caralho e barbeiro.**",
            f"**{user.mention} Se os meus espermas fossem luzinhas o cu da tua mae era uma discoteca**",
            ]

        if user.name == "Fury^^":
            await message.channel.purge(limit=1)                
            await message.channel.send(f"{user.mention} Nao posso insultar o meu criador :)")

        elif user.name == "-MotherTips":
            await message.channel.purge(limit=1)
            await message.channel.send(f"{user.mention} Nao me vou estar a insultar a mim mesmo né.")

        else:
            response_dica_random = random.choice(dicas_random)
            await message.channel.purge(limit=1)
            await message.channel.send(response_dica_random)
#------------------------------------------------------------------------------------------------------------------------------    
    for i in range(0,200):       
        user = random.choice(message.channel.guild.members)

        if message.content == "-roast -MotherTips":
            await message.channel.purge(limit=1)
            await message.channel.send("Comigo essa cena nao vai funcionar :man_facepalming:")
            break

        if message.content == "-roast Fury^^":
            user = ["Fury^^#3694"]
            await message.channel.purge(limit=1)
            await message.channel.send(f"Vai po caralhinho sim :slight_smile:, ele é o meu boss nao posso fazer isso :eyes: ")
            break

        if message.content == "-roast {}".format(user.name):
            print("Identificação do {}".format(user.name))
            dicas_random = [
                f"**{user.mention} A tua mae é como uma lareira: cabe sempre mais um pau!**", 
                f"**{user.mention} A tua mae e como a sopa: ninguem gosta mas todos comem!**",
                f"**{user.mention} A tua mae e como o pingo doce: sabe bem pagar tao pouco!**", 
                f"**{user.mention} A tua mae e como a europoupança do mcdonalds: tudo a 1 euro!**",
                f"**{user.mention} A tua mae e como a caixa registadora,abre-se por uns trocos!**", 
                f"**{user.mention} So comes caldo verde quando a tua mae faz a depilaçao!**",
                f"**{user.mention} A tua mae e como os macacos anda de pau em pau!**", 
                f"**{user.mention} A tua mae e como um trator: Grande e Gorda**",
                f"**{user.mention} A minha piça e tipo arco iris pq a tua mae muda de baton todos os dias**", 
                f"**{user.mention} A tua mãe é como o bebe so quer e leitinho!!**",
                f"**{user.mention} A tua mãe é tao gorda q tirei lhe uma foto no natal e ainda ta a imprimir!!**", 
                f"**{user.mention} A tua mae é como o caldo verde, todos querem por la o xouriço**",
                f"**{user.mention} A tua mãe é como o super Mário, salte sempre pela moedinha.**", 
                f"**{user.mention} A tua mãe é como o corrimão, toda a gente lhe põe a mão.**",
                f"**{user.mention} A tua mãe é como o castor, anda sempre com o pau na boca.**", 
                f"**{user.mention} A tua mãe é como o Cachorro Quente, tem sempre uma salsicha lá dentro.**",
                f"**{user.mention} A tua mãe é como a Rádio Popular, nem os forretas resistem.**", 
                f"**{user.mention} A tua mãe é como a noite, quando leva no cu fica a ver estrelinhas.**",
                f"**{user.mention} A tua mãe é como a gripe, apanha-se na rua e trata-se na cama.**", 
                f"**{user.mention} A tua mãe é como os bebés, põe na boca tudo o que lhe aparece à frente.**",
                f"**{user.mention} A tua mãe é como a erva todos os bois querem comer.**", 
                f"**{user.mention} A tua mãe é como a maçã, come-se e deita-se fora.**",
                f"**{user.mention} A tua mãe é como a maxmat , profissional dos preços baixos.**", 
                f"**{user.mention} A tua mãe é tão gorda que passou á frente da tv e perdi a temporada dos simpsons toda.**",
                f"**{user.mention} A diferença entre o caldo verde e a tua mãe é que no caldo verde o chouriço é cortado, na tua mãe é logo inteiro.**",
                f"**{user.mention} Se o meu pau fosse uma espada a tua mae estava morta.**",
                f"**{user.mention} Mata a tua mae e faz arroz de puta.**",
                f"**{user.mention} A tua mae e tao gorda que quando vai dar um mergulho na praia as baleias cantam : We are family!**",
                f"**{user.mention} A tua mae é como um charro: roda por todos.**",
                f"**{user.mention} Se as piças fossem de açucar a tua mae era diabetica.**",
                f"**{user.mention} Sabem a diferença entre a tua mae e a lua? A diferença é que á lua nem todos foram.",
                f"**{user.mention} A tua mãe é como o MC Donalds, monta negócio em todo o mundo!**",
                f"**{user.mention} A tua mãe é como uma rotunda, uns têm prioridade, outros têm de esperar, mas acabam todos por entrar!**",
                f"**{user.mention} A cona da tua mãe so e rapada porque o meu caralho e barbeiro.**",
                f"**{user.mention} Se os meus espermas fossem luzinhas o cu da tua mae era uma discoteca**",
                ]

            response_dica_random = random.choice(dicas_random)
            await message.channel.purge(limit=1)
            await message.channel.send(response_dica_random)

            break

#------------------------------------------------------------------------------------------------------------------------------

    if message.content.lower() == '-help':
        print("Alguem pediu ajuda")
        await message.channel.purge(limit=1)
        await message.channel.send('''```Basta usares < -roast > e ja vês 
            \nE exprimenta tambem o < -roast random >   
            \nE a melhor parte é que podes dar uma dica para o teu amigo,
mete o nome do teu amigo, assim : < -roast -MotherTips >
\n
\n
--------------------------------Comandos--------------------------------
-roast --> mostra uma frase de roast sem identificar ninguem
-roast random --> das roast a uma pessoal random do servidor
-roast <USER_NAME> --> por ex: -MotherTips; das roast a uma pessoa escolhida por ti
------------------------------------------------------------------------```''')

#------------------------------------------------------------------------------------------------------------------------------

client.run(token)
