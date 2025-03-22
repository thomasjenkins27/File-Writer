from pathlib import Path

# Provide the file path and desired name to write to.
# Can also copy and paste the entire file path to the directory of choice.
path = Path("guest_book.txt")

# While loop to type multiple names until 'q' is typed.
while True:
    contents = input("What is your name? (press 'q' to end program)")

    if contents.lower() == "q":
        print("The guestbook is created.")
        break

    with path.open("a") as file:
        file.write(contents + "\n")

with path.open("r") as file:
    lines = file.readlines()

# If name is not unique(only 1) you will delete all duplicates.
unique_lines = list(dict.fromkeys(lines))

with path.open("w") as file:
    file.writelines(unique_lines)

print("Duplicates removed from the file.")
