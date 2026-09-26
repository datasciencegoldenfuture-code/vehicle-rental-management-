# Vehicle Rental Management System

vehicles = {
    "BIKE101": {"name": "Hero Splendor", "type": "Bike", "price": 300, "available": True},
    "BIKE102": {"name": "Royal Enfield", "type": "Bike", "price": 700, "available": True},
    "CAR101": {"name": "Swift", "type": "Car", "price": 1500, "available": True},
    "CAR102": {"name": "Creta", "type": "Car", "price": 2500, "available": True}
}

rent_history = []


# ---------------- LOGIN ----------------
def login():
    while True:
        print("\n===== ADMIN LOGIN =====")
        username = input("Username: ")
        password = input("Password: ")

        if username == "admin" and password == "1234":
            print("Login Successful!\n")
            break
        else:
            print("Wrong Username or Password.\n")


# ---------------- SHOW VEHICLES ----------------
def show_vehicles():
    print("\n===== AVAILABLE VEHICLES =====")

    found = False

    for vid, data in vehicles.items():
        if data["available"]:
            found = True
            print(f"{vid} | {data['name']} | {data['type']} | ₹{data['price']}/day")

    if not found:
        print("No Vehicle Available.")


# ---------------- RENT VEHICLE ----------------
def rent_vehicle():
    show_vehicles()

    vid = input("\nEnter Vehicle ID: ")

    if vid in vehicles and vehicles[vid]["available"]:

        customer = input("Customer Name: ")
        days = int(input("Number of Rental Days: "))

        total = vehicles[vid]["price"] * days

        vehicles[vid]["available"] = False

        rent_history.append({
            "customer": customer,
            "vehicle": vehicles[vid]["name"],
            "days": days,
            "bill": total
        })

        print("\nVehicle Rented Successfully.")
        print("Total Bill = ₹", total)

    else:
        print("Vehicle Not Available.")


# ---------------- RETURN VEHICLE ----------------
def return_vehicle():
    vid = input("Enter Vehicle ID: ")

    if vid in vehicles:

        if vehicles[vid]["available"]:
            print("Vehicle Already Returned.")
        else:
            vehicles[vid]["available"] = True
            print("Vehicle Returned Successfully.")

    else:
        print("Vehicle Not Found.")


# ---------------- ADD VEHICLE ----------------
def add_vehicle():
    vid = input("Vehicle ID: ")

    if vid in vehicles:
        print("Vehicle Already Exists.")
        return

    name = input("Vehicle Name: ")
    vtype = input("Type (Bike/Car): ")
    price = int(input("Rent Per Day: "))

    vehicles[vid] = {
        "name": name,
        "type": vtype,
        "price": price,
        "available": True
    }

    print("Vehicle Added Successfully.")


# ---------------- RENT HISTORY ----------------
def view_history():
    print("\n===== RENT HISTORY =====")

    if len(rent_history) == 0:
        print("No Records Found.")

    else:
        for record in rent_history:
            print("-------------------------")
            print("Customer :", record["customer"])
            print("Vehicle  :", record["vehicle"])
            print("Days     :", record["days"])
            print("Bill     : ₹", record["bill"])


# ---------------- MAIN MENU ----------------
def main():

    login()

    while True:

        print("\n===== VEHICLE RENTAL MANAGEMENT =====")
        print("1. View Vehicles")
        print("2. Rent Vehicle")
        print("3. Return Vehicle")
        print("4. Add Vehicle")
        print("5. Rental History")
        print("6. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            show_vehicles()

        elif choice == "2":
            rent_vehicle()

        elif choice == "3":
            return_vehicle()

        elif choice == "4":
            add_vehicle()

        elif choice == "5":
            view_history()

        elif choice == "6":
            print("\nThank You!")
            break

        else:
            print("Invalid Choice.")


main()