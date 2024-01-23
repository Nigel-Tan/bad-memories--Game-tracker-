from keep_alive import keep_alive
import discord
import os
from time import sleep
import datetime
#import pytz #outdated
#from datetime import datetime


channelid = 1050365729070911528 #change channelid based on the channel you want the bot to post to

def getTime():
    # Define the UTC time
    utc_now = datetime.datetime.utcnow()

    # Define the time difference for Singapore time
    sgt_offset = datetime.timedelta(hours=8)  # Singapore is UTC+8

    # Calculate the Singapore time
    sgt_now = utc_now + sgt_offset

    # Format the time in AM/PM format
    time_str = sgt_now.strftime("%I:%M:%S %p")
    return time_str

# Call the function and print the formatted time
print(getTime())


intents = discord.Intents.all()
intents.presences = True


#client = MyClient(intents=intents)
client = discord.Client(intents=intents)
@client.event
async def on_ready():
  print('A tax evader known as {0.user}'.format(client) +' has entered through a portal.')

@client.event
async def on_message(message): #check if the msg is sent by the bot itself
  if message.author == client.user:
    return

x = []
@client.event #consider using task like the example given above
async def on_presence_update(before, after):
    channel = client.get_channel(channelid)
    activ = after.activity
    time_str = getTime() 
    if ((after.activity != before.activity)and(before.activity == None) and (before not in x) and (after.activity!= after.status)):
      msg = '{0} started playing {1} at {2}'.format(str(before),activ.name,time_str)
      x.append(before)
      await channel.send(msg)
    if ((after.activity == None) and (before.activity != activ) and (before in x) and (activ!=after.status)):
      x.remove(before)
      msg = '{0} stopped playing {1} at {2}'.format(str(before),before.activity.name,time_str)
      await channel.send(msg)
              
while __name__ == '__main__':
  try:
    keep_alive()
    client.run(os.environ['token'])
  except discord.errors.HTTPException as e:
    print(e)
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    sleep(7)
    os.system('kill 1')