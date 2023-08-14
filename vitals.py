'''
Penguin’s vital life support
'''

from flask import Flask
from threading import Thread

bot = Flask("PENGUIN-bot")

@ bot.route("/")
def home():
  return "Penguin's awake!"

@ bot.route("/test")
def test():
  print("testing")
  return "test"

def run():
  bot.run(host = "0.0.0.0", port = 8080)

def huddle():  
  Thread(target = run).start()
