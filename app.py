def vote(voter_name, candidate):
    # Open the file in append mode to store the votes
    with open("votes.txt", "a") as file:
        file.write(voter_name + "," + candidate + "\n")
    print(f"Thank you, {voter_name}, for voting for {candidate}.")

def tally_votes():
    # Open the file in read mode to read the votes
    with open("votes.txt", "r") as file:
        votes = file.readlines()

    # Initialize a dictionary to store the vote count for each candidate
    vote_count = {}
    for vote in votes:
        _, candidate = vote.strip().split(",")
        if candidate in vote_count:
            vote_count[candidate] += 1
        else:
            vote_count[candidate] = 1

    # Print the tally of votes for each candidate
    print("Vote Tally:")
    for candidate, count in vote_count.items():
        print(f"{candidate}: {count}")

def main():
    print("Welcome to the Voting Application!")
    while True:
        print("\n1. Vote\n2. Tally Votes\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            voter_name = input("Enter your name: ")
            candidate = input("Enter the candidate you are voting for: ")
            vote(voter_name, candidate)
        elif choice == "2":
            tally_votes()
        elif choice == "3":
            print("Exiting the Voting Application. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
