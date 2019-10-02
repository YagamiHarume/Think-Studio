import discord
import asyncio
from discord.ext import commands

client = discord.Client()
token = "" #따옴표 안에 토큰 입력(디코API에서 구할 수 있음)


@client.event
async def on_ready():
    print(client.user.id)
    print(client.user.name)
    print("와산본!")
    print("-------------------") #로그인할때 터미널에 이게 뜸
    activity = discord.Game("하루카의 생각공방") #여기에다 게임 입력
    await client.change_presence(status = discord.Status.online, activity = activity) #discord.Status.뒤에 online이면 녹색, idle이면 노란색, offline이면 빨간색으로 점등 

@client.event
async def on_message(message):
    if message.author == client.user: #봇의 대화에 감지 X
        return
    if message.content.startswith("와산본"): #주어진 조건으로 시작하는 채팅에만 반응
        await message.channel.send("산행은 즐거워요!")
    if message.content == "레이카": #주어진 조건과 일치하는 채팅에만 반응
        await message.channel.send("저는 765프로 아이돌이에요!")
    if message.content.startswith("뿌뿌카"): #주어진 조건으로 시작하는 채팅에만 반응, 파일전송
        await message.channel.send(file = discord.File("reika.png"))
    if "푸딩" in message.content: #특정 문구가 포함되어있으면 반응
        await message.channel.send("잘 먹겠습니다!")
    if message.content.startswith("reika"): #명령어 코드
        if message.content[6:] == "version":
            await message.channel.send("REIKA BOT version 2.0")
        elif message.content[6:] == "help": #embed 유형 보내기
            embed = discord.Embed(title = '뿌뿌~ 레이카봇 명령어에요♪', description = '각각의 명령어들을 잘 쓰시면 되요♪', colour = 0x6BB6B0) #url 추가 가능
            embed.set_author(name = "키타카미 레이카")
            embed.add_field(name = '와산본', value = '와산본으로 시작하는 메시지를 입력하면 봇이 **산행은 즐거워요**라고 반응해요♪',inline = False)
            embed.add_field(name = '레이카', value='레이카를 입력하면 본인 소속을 알려줘요♪', inline = False)
            embed.add_field(name = '뿌뿌카', value='뿌뿌카로 시작하는 메시지를 입력하면 제 사진이 나와요♪', inline =  False)
            embed.add_field(name = '푸딩', value='푸딩이 들어가는 메시지를 입력하면 맛있게 먹을게요♪', inline = False)
            embed.add_field(name = 'reika help', value='명령어 목록을 볼 수 있어요♪', inline = False)
            embed.add_field(name = 'reika version', value='저의 버전 정보를 볼 수 있어요♪', inline = False)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send("그런 명령어는 없어요♪")

client.run(token)

#version 2.0
#made by Haruka Amami
