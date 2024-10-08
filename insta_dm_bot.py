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

# Method 1
# DM the followers of the user

follower_ids =  my_bot.get_user_followers(target_user_name)
print(follower_ids)

for count, each_follower in enumerate(follower_ids):
    print("follow/dm number:", count)
    if count > total_dms:
        break
    my_bot.follow(each_follower)
    sleep(5)
    username = my_bot.get_username_from_user_id(each_follower)
    message_text = f"Hi {username},  are you interested in python programming?\\n You can learn with me!"
    my_bot.send_message(message_text, [username])
    sleep(20)
