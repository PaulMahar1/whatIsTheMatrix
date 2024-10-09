print("\nYou have entered the Matrix...")
print("You take the blue pill, the story ends... You wake up in your bed and believe whatever you want to believe.")
print("You take the red pill... You stay in Wonderland, and I show you how deep the rabbit hole goes.")
choice = input("\nDo you take the red pill or the blue pill? (type 'red' or 'blue'): ")
if choice.lower() == 'red':
    print("\nWelcome to reality. Brace yourself!\n")
elif choice.lower() == 'blue':
    print("\nEnjoy your illusion. Ignorance is bliss!\n")
else:
    print("\nInvalid choice. You are stuck in the Matrix forever.\n")
