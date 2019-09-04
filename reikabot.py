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
    if message.content.startswith("와산본"): #주어진 조건으로 시작하는 채팅에만 반응
        await message.channel.send("산행은 즐거워요!")

    if message.content == "레이카": #주어진 조건과 일치하는 채팅에만 반응
        await message.channel.send("저는 765프로 아이돌이에요!")

    if message.content.startswith("뿌뿌카"): #주어진 조건으로 시작하는 채팅에만 반응, 파일전송
        await message.channel.send(flie = discord.File("reika.png"))

client.run(token)

#version 1.0
made by Haruka Amami
