from clear_screen import screen_clear
auction_dict = {}
bidding_finished =False

def highest_bid(auction_dic):
    highest_bid = 0
    winner = ""
    for bidder in auction_dic:
        bid_amount=auction_dic[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"{winner} made the highest bid of {highest_bid}$")

while not bidding_finished:
    name = input("Enter your name")
    bid_value = int(input("enter the amount you want to bid"))
    auction_dict[name] = bid_value
    should_stop = input("enter 'yes' if any new bidders and 'no' if finished").lower()
    if should_stop == "yes":
        screen_clear()
    elif should_stop == "no":
        screen_clear()
        highest_bid(auction_dic=auction_dict)
        bidding_finished =True
    else:
        print("invalid option")    
            





