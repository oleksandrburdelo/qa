friends = ["John", "Marta", "James", "Adam", "Maria", "Huang", "Peter", "Samuel"]
enemies = ["John", "Johnatan", "Artur"]

if 'Marta' in friends: # Such solution is hardcoded so you should iterate your list with loop instead.
    if 'Johnatan' not in friends: # Same.
        print(f"{enemies} we are not the friends anymore")
    print(f"{friends} we are the best friends")

# Take a look on example of code and review each lesson twice for next time. All of this I have show on lesson.
# for item in items:
#     if item in some_other_list:
#         bla bla bla
#     else:
#         not bla bla bla