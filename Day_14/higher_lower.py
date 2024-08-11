# 1. Break the problem - large probelm into the small problem, tackle them one by one 
# 2. Make a todo list and pick the easiest one 
# 3. Turn the problem into comments
# 4. Write code - run code - fix code 
# 5. Next Task in your to do list

# import the random module 
import random
import game_data

# finding length of the list 
length = len(game_data.data)

# function which select a random person from the data and return name and followers-
def person():

    num = random.randint(0,50) # generate randmo number

    a = list(game_data.data[num].values()) # return values 
    format = f"{a[0]}, {a[2]}, form {a[3]}" # format the string
    print(format)
    return a[1] # retrun formatted string and follower count








# flag = True
# score_count = 0

# user_choice = input("Who has more follower? Type A or B:")

# if follower1 > follower2:
#     if user_choice == "A":
#         score_count += 1
#         print("Score : ", score_count)
#         name2 , follower2 = person()


# elif follower2 > follower1:
#     if user_choice == "B":
#         score_count +=1
#         print("Score : ", score_count)
#         name1, follower1 = person()


# else:
#     print("Score:", score_count)

