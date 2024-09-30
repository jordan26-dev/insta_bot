from instabot import Bot
from time import sleep


try:
    user_name = str(input("Enter the targeted username:"))
    total_dms = int(input("Enter the number of DMs:"))
except:
    print("Invalid input!")
    exit()

my_bot = Bot()

# login
my_bot.login(username="", password="")

# Method 1
# DM the followers of the user

follower_ids =  my_bot.get_user_followers(user_name)

for count, each_follower in enumerate(follower_ids):
    if count > total_dms:
        break
    my_bot.follow(each_follower)
    sleep(5)
    username = my_bot.get_username_from_user_id(each_follower)
    message_text = f"Hi {username},  are you interested in python programming?\\n You can learn with me!"
    my_bot.send_message(message_text, [username])
    sleep(20)

