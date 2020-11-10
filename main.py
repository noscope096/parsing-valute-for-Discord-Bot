import discord
from discord.ext import commands
from selenium import webdriver
import os
import requests
from urllib.request import urlopen

TOKEN = ' ' # your discord bot token | токен вашего дискорд бота 

bot = commands.Bot(command_prefix= '!')
client = discord.Client()

@bot.command(pass_context=True)

@bot.event
async def on_ready():
    print("Bot is online")

@bot.command(pass_context = True)
async def course(ctx):
    chromedriver = " " # path to 'chromedriver.exe'| путь к 'chromedriver.exe'
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get("https://www.sberometer.ru/?DO%22%22")
    usd = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div/div[1]')
    eur = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div/div[2]')
    await ctx.send(usd.text + '\n' + eur.text)

bot.run(TOKEN)