import time

# Dictionary to store tickets

tickets = {}

def create_ticket():
    ticket_id = len(tickets) + 1
    subject = input("Enter the ticket subject: ")
    description = input("Enter the ticket description: ")
    status = "Open"
    tickets[ticket_id] = {"subject": subject, "description": description, "status": status}
    print(f"Ticket {ticket_id} created successfully.\n")

def update_ticket_status():
    ticket_id = int(input("Enter the ticket ID to update: "))
    if ticket_id in tickets:
        new_status = input("Enter the new status (Open, In Progress, Resolved, etc.): ")
        tickets[ticket_id]["status"] = new_status
        print(f"Ticket {ticket_id} status updated to: {new_status}\n")
    else:
        print("Ticket not found. Please enter a valid ticket ID.\n")

def list_tickets():
    print("\nTicket List:")
    for ticket_id, ticket_info in tickets.items():
        print(f"Ticket ID: {ticket_id}")
        print(f"Subject: {ticket_info['subject']}")
        print(f"Description: {ticket_info['description']}")
        print(f"Status: {ticket_info['status']}\n")

def main():
    while True:
        print("Customer Support Ticket Handling")
        print("1. Create Ticket")
        print("2. Update Ticket Status")
        print("3. List All Tickets")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            create_ticket()
        elif choice == '2':
            update_ticket_status()
        elif choice == '3':
            list_tickets()
        elif choice == '4':
            print("Exiting the ticket handling system.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
