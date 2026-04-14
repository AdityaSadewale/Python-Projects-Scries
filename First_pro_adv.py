import tkinter as tk
from tkinter import messagebox

roommates = []

def add_person():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()

    if name == "" or phone == "" or email == "":
        messagebox.showerror("Error", "Please fill all details!")
        return

    roommates.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    messagebox.showinfo("Success", f"{name} added successfully 🎉")

    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)


def calculate_and_send():
    try:
        rent = float(entry_rent.get())
        food = float(entry_food.get())
        units = float(entry_units.get())
        charge = float(entry_charge.get())

        persons = len(roommates)

        if persons == 0:
            messagebox.showerror("Error", "Add at least one person!")
            return

        electricity = units * charge
        total = rent + food + electricity
        per_person = total / persons

        # this will be genrate a message for user for total cacultion of resnt of this mounts for equily distubuted also ...
        for person in roommates:
            msg = f"""
📢 Hello {person['name']} 👋

🏠 Monthly Rent Details:
💰 Rent: ₹{rent}
🍔 Food: ₹{food}
⚡ Electricity: ₹{electricity}

📊 Total: ₹{total}
👥 Split Between: {persons} people

👉 Your Share: ₹{per_person:.2f}

🙏 Please pay on time!

Thank you 😊
"""
            # This also put information foe user also for has Phone number ,msg and  totaly rent of this mounts ...
            print(f"Sending to {person['phone']} 📱")
            print(msg)
            print("-" * 40)

        result_label.config(text=f"Each pays ₹{per_person:.2f} 💸")

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers!")



root = tk.Tk()
root.title("Smart Rent Calculator 🏠")
root.geometry("400x500")

# Person Details used for equily distubuted also 
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Phone").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Button(root, text="Add Person ➕", command=add_person).pack(pady=5)

# Rent Inputs for user this give basic info for input cost also ...
tk.Label(root, text="Rent").pack()
entry_rent = tk.Entry(root)
entry_rent.pack()

tk.Label(root, text="Food Cost").pack()
entry_food = tk.Entry(root)
entry_food.pack()

tk.Label(root, text="Electricity Units").pack()
entry_units = tk.Entry(root)
entry_units.pack()

tk.Label(root, text="Charge per Unit").pack()
entry_charge = tk.Entry(root)
entry_charge.pack()

tk.Button(root, text="Calculate & Send 📩", command=calculate_and_send).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
