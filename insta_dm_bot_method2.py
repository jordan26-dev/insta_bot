from instabot import Bot
from time import sleep


try:
    target_user_name = str(input("Enter the targeted username:"))
    total_dms = int(input("Enter the number of DMs:"))
except:
    print("Invalid input!")
    exit()

my_bot = Bot(max_followers_to_follow=500, max_follows_per_day=1000)

# login
my_bot.login(username="jorjor", password="12345")


# Method 2
# DM the likers (engaging people) of the user

liker_ids = my_bot.get_user_likers(target_user_name)

for count, each_liker in enumerate(liker_ids):
    if count > total_dms:
        break
    my_bot.follow(each_liker)
    sleep(5)
    username = my_bot.get_username_from_user_id(each_liker)
    message_text = f"Hi {username},  are you interested in python programming?\\n You can learn with me!"
    my_bot.send_message(message_text, [username])
    sleep(20)