username = "ahmad"
userpass = "ahmad123"

adminname = "admin"
adminpass = "admin123"

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    print("\n*** Welcome to the Database ***")
    entered_username = input("Enter your username: ")

    if entered_username == username:
        entered_password = input("Enter your password: ")

        if entered_password == userpass:
            print("👤 User login successful!")
            break
        else:
            attempts += 1
            print("❌ Wrong password")
            print("Remaining attempts:", max_attempts - attempts)

    elif entered_username == adminname:
        entered_password = input("Enter your password: ")

        if entered_password == adminpass:
            print("👑 Admin login successful!")
            break
        else:
            attempts += 1
            print("❌ Wrong password")
            print("Remaining attempts:", max_attempts - attempts)

    else:
        attempts += 1
        print("❌ User not found")
        print("Remaining attempts:", max_attempts - attempts)

if attempts == max_attempts:
    print("\n🔒 ACCOUNT LOCKED! Too many failed attempts.")
