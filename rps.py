user_input = input("enter rps")
computer_input = 2
user_dict={
    "r":1,
    "s":2,
    "p":3
}
final_input = user_dict[user_input]
print(final_input)
if(final_input == 1 and computer_input == 2):
    print("user win")
elif(final_input == 2 and computer_input == 3):
    print("user win")  
elif(final_input == 3 and computer_input == 1):
    print("user win")    
else:
     print("you loose")