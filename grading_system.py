m = input("Enter your marks: ")

# Step 1: Check if the input is numeric
if not m.isdigit():
    print("Invalid input! Please enter a number between 0 and 100.")
else:
    M = int(m)

    # Step 2: Check if the number is in valid range
    if M < 0 or M > 100:
        print("Invalid marks! Marks should be between 0 and 100.")
    elif M >= 90:
        print("Outstanding")
    elif M >= 75:
        print("Excellent")
    elif M >= 60:
        print("Good")
    elif M >= 40:
        print("Pass")
    else:
        print("Fail")
