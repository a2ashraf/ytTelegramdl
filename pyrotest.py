from pyrogram import Client

client = Client("example")
client.start()



client.send_message("me", "Hi there! I'm using Pyrogram")
client.send_photo("me", "/Users/Ahsan/Desktop/screen.png", "Nice photo!")

client.stop()