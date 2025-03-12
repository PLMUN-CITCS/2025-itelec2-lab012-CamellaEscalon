# Function to simulate a switch statement using a dictionary
def get_day_type(day):
    # Dictionary that maps days to their corresponding message
    day_messages = {
        'monday': "It's a Weekday!",
        'tuesday': "It's a Weekday!",
        'wednesday': "It's a Weekday!",
        'thursday': "It's a Weekday!",
        'friday': "It's a Weekday!",
        'saturday': "It's a Weekend!",
        'sunday': "It's a Weekend!"
    }
    
    # Normalize input to lowercase and strip any extra spaces
    day = day.strip().lower()
    
    # Try to retrieve the message for the day, or default to "Invalid day entered."
    message = day_messages.get(day, "Invalid day entered.")
    
    # Return the day and its corresponding message
    return message

# Main function to interact with the user
def main():
    # Get user input
    user_input = input("Enter a day of the week: ")
    
    # Get the message related to the day
    day_type = get_day_type(user_input)
    
    # Output the results
    if day_type == "Invalid day entered.":
        print(day_type)
        print("It's a Weekday!")
    else:
        # Display the formatted message
        print(f"Today is {user_input.capitalize()}.")
        print(day_type)

# Run the program
main()
