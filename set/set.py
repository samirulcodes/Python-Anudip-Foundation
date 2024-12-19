# s={}
# print(type(s))  # dict
# print(s)  # empty -- {}

# s1={2}
# print(s1) # set

# s2={"a","e","i","o","u"}
# print(type(s2))
# print(s2)

# s3=set("hello")
# print(s3) # helo

# union
# s2={"a","e","i","o","u"}
# s4={"a","b","c","d","e","f","g","h","i","j"}
# print(s2.union(s4))

# Mutual friends
'''
def find_mutual_friends():
    """Find mutual friends between two sets of friends."""
    print("Mutual Friends Finder")

    # Input friends for Person 1
    friends_person1 = input("Enter the friends of Person 1 (comma-separated): ").strip()
    friends_set1 = set(map(str.strip, friends_person1.split(",")))

    # Input friends for Person 2
    friends_person2 = input("Enter the friends of Person 2 (comma-separated): ").strip()
    friends_set2 = set(map(str.strip, friends_person2.split(",")))

    # Find mutual friends
    mutual_friends = friends_set1.intersection(friends_set2)

    if mutual_friends:
        print("\nMutual Friends:")
        for friend in mutual_friends:
            print(friend)
    else:
        print("\nNo mutual friends found.")


if __name__ == "__main__":
    find_mutual_friends()

''' 
