# ITEC 204 - Data Structures and Algorithms
# Laboratory Exercise 1
# IT Automation Incident Ticket Manager

# Linear Data Structure: List
tickets = [
    {
        "id": "INC1392939",
        "bot": "BOT-Inventory",
        "description": "Failed to generate the daily report"
    },
    {
        "id": "INC1392940",
        "bot": "BOT-Email",
        "description": "Failed to send the scheduled notification"
    },
    {
        "id": "INC1392941",
        "bot": "BOT-DataSync",
        "description": "Encountered an error during data transfer"
    },
    {
        "id": "INC1392942",
        "bot": "BOT-Invoice",
        "description": "Failed to process an invoice"
    },
    {
        "id": "INC1392943",
        "bot": "BOT-Report",
        "description": "Failed to generate the weekly report"
    },
    {
        "id": "INC1392944",
        "bot": "BOT-FileTransfer",
        "description": "Failed to upload the required file"
    },
    {
        "id": "INC1392945",
        "bot": "BOT-DataEntry",
        "description": "Encountered an error while entering records"
    },
    {
        "id": "INC1392946",
        "bot": "BOT-Backup",
        "description": "Failed to complete the scheduled backup"
    },
    {
        "id": "INC1392947",
        "bot": "BOT-Validation",
        "description": "Failed to validate the submitted records"
    },
    {
        "id": "INC1392948",
        "bot": "BOT-Notification",
        "description": "Failed to send the system alert"
    }
]

# ADD TICKET
def add_ticket():
    print("\n" + "=" * 50)
    print("ADD NEW INCIDENT TICKET")
    print("=" * 50)

    incident_id = input("Enter Incident ID: ").strip()
    bot = input("Enter Bot Name: ").strip()
    description = input("Enter Short Description: ").strip()

    # Check if fields are empty
    if incident_id == "" or bot == "" or description == "":
        print("\n[ERROR] All fields are required.")
        return

    # Check if Incident ID already exists
    for ticket in tickets:
        if ticket["id"].lower() == incident_id.lower():
            print("\n[ERROR] Incident ID already exists.")
            return

    # Create new ticket
    new_ticket = {
        "id": incident_id,
        "bot": bot,
        "description": description
    }

    # Add ticket only once
    tickets.append(new_ticket)

    # Get updated total
    total_active = len(tickets)

    # Success notification
    print("\n" + "=" * 50)
    print("[SUCCESS] INCIDENT TICKET ADDED!")
    print("=" * 50)
    print(f"Incident ID       : {incident_id}")
    print(f"Bot               : {bot}")
    print(f"Short Description : {description}")
    print("-" * 50)
    print(f"TOTAL ACTIVE TICKETS: {total_active}")
    print("=" * 50)

# DISPLAY ACTIVE TICKETS
def display_tickets():
    print("\n" + "=" * 70)
    print("ACTIVE INCIDENT TICKETS")
    print("=" * 70)

    # Check if there are no tickets
    if len(tickets) == 0:
        print("[INFO] There are no active incident tickets.")
        return

    print(f"\nTotal Active Tickets: {len(tickets)}")
    print("-" * 70)

    # Display every ticket
    for number, ticket in enumerate(tickets, start=1):
        print(f"\nTicket #{number}")
        print(f"Incident ID       : {ticket['id']}")
        print(f"Bot               : {ticket['bot']}")
        print(f"Short Description : {ticket['description']}")
        print("-" * 70)

    print(f"\n[INFO] Successfully displayed {len(tickets)} active ticket(s).")

# SEARCH TICKET
def search_ticket():
    print("\n" + "=" * 50)
    print("SEARCH INCIDENT TICKET")
    print("=" * 50)

    incident_id = input("Enter Incident ID to search: ").strip()

    if incident_id == "":
        print("\n[ERROR] Incident ID cannot be empty.")
        return

    for ticket in tickets:
        if ticket["id"].lower() == incident_id.lower():

            print("\n[SUCCESS] Incident ticket found!")
            print("-" * 50)
            print(f"Incident ID       : {ticket['id']}")
            print(f"Bot               : {ticket['bot']}")
            print(f"Short Description : {ticket['description']}")
            print("-" * 50)

            return

    print(f"\n[NOT FOUND] No ticket found with ID: {incident_id}")

# REMOVE RESOLVED TICKET
def remove_ticket():
    print("\n" + "=" * 50)
    print("REMOVE RESOLVED INCIDENT TICKET")
    print("=" * 50)

    incident_id = input("Enter Incident ID to remove: ").strip()

    if incident_id == "":
        print("\n[ERROR] Incident ID cannot be empty.")
        return

    # Search for ticket
    for ticket in tickets:
        if ticket["id"].lower() == incident_id.lower():

            # Remove ticket
            tickets.remove(ticket)

            print("\n[SUCCESS] Incident ticket removed successfully!")
            print(f"Removed Incident ID: {ticket['id']}")
            print(f"Bot: {ticket['bot']}")
            print("\nThe ticket is now marked as resolved and removed from active tickets.")
            print(f"Remaining active tickets: {len(tickets)}")

            return

    print(f"\n[NOT FOUND] No ticket found with ID: {incident_id}")

# COUNT ACTIVE TICKETS
def count_tickets():
    print("\n" + "=" * 50)
    print("COUNT ACTIVE INCIDENT TICKETS")
    print("=" * 50)

    total = len(tickets)

    print(f"\n[INFO] Total active incident tickets: {total}")   

# MAIN MENU
def main():

    while True:

        print("\n")
        print("=" * 55)
        print("   IT AUTOMATION INCIDENT TICKET MANAGER")
        print("=" * 55)
        print("1. Add Incident Ticket")
        print("2. Display All Active Tickets")
        print("3. Search Incident Ticket")
        print("4. Remove Resolved Ticket")
        print("5. Count Active Tickets")
        print("6. Exit")
        print("=" * 55)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_ticket()

        elif choice == "2":
            display_tickets()

        elif choice == "3":
            search_ticket()

        elif choice == "4":
            remove_ticket()

        elif choice == "5":
            count_tickets()

        elif choice == "6":
            print("\n" + "=" * 55)
            print("Thank you for using the IT Automation")
            print("Incident Ticket Manager!")
            print("=" * 55)
            print("[PROGRAM CLOSED]")
            break

        else:
            print("\n[ERROR] Invalid choice.")
            print("[INFO] Please enter a number from 1 to 6.")

# RUN PROGRAM
if __name__ == "__main__":
    main()
