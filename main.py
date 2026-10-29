# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)



def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bidder = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bidder}")

    continue_bidding = True
    while continue_bidding:
        name = input("what is your name?: ")
        price = int(input("what is your bid?: $"))
        bids[name] = price
        should_continue = input("Are there any other bidders? 'yes' or 'no'. \n").lower()
        if should_continue == "no":
            continue_bidding = False
            find_highest_bidder()
        elif should_continue == "yes":
            print("\n * 20")