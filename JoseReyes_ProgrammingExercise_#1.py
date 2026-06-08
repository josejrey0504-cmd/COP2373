# Jose Reyes
# Programming Exercise 1
# This program pre sells cinema tickets. Each buyer may purchase up to four tickets until all twenty tickets are sold.


def get_ticket_amount(remaining_tickets):
    """
    Ask the user for a valid number of tickets.
    """

    while True:
        tickets_requested = int(
            input
            ("Enter the number of tickets you would like to purchase: ")
                f"(1-4, {remaining_tickets} remaining): "
            )
        )

        if tickets_requested < 1:
            print("You must purchase at least 1 ticket.")

        elif tickets_requested > 4:
            print("You cannot purchase more than 4 tickets.")

        elif tickets_requested > remaining_tickets:
            print("There are not enough tickets remaining.")

        else:
            return tickets_requested


def main():
    """
    Control the ticket-selling process.
    """

    tickets_remaining = 10
    buyer_count = 0

    while tickets_remaining > 0:
        tickets_bought = get_ticket_amount(tickets_remaining)

        tickets_remaining -= tickets_bought

        buyer_count += 1

        print(f"Tickets remaining: {tickets_remaining}")
        print()

    print("All tickets have been sold.")
    print(f"Total buyers: {buyer_count}")


main()