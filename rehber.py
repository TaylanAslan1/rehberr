import tkinter as tk
import json
from tkinter import messagebox

class PhonebookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Telefon Rehberi")

        self.contacts = {}
        self.load_contacts()

        self.name_label = tk.Label(root, text="İsim:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.number_label = tk.Label(root, text="Telefon:")
        self.number_label.grid(row=1, column=0, padx=10, pady=5)
        self.number_entry = tk.Entry(root)
        self.number_entry.grid(row=1, column=1, padx=10, pady=5)

        self.address_label = tk.Label(root, text="Adres:")
        self.address_label.grid(row=2, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=2, column=1, padx=10, pady=5)

        self.add_button = tk.Button(root, text="Kişi Ekle", command=self.add_contact)
        self.add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

        self.delete_button = tk.Button(root, text="Kişi Sil", command=self.delete_contact)
        self.delete_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

        self.update_button = tk.Button(root, text="Kişi Güncelle", command=self.update_contact)
        self.update_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

        self.find_button = tk.Button(root, text="Kişi Bul", command=self.find_contact)
        self.find_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

        self.save_button = tk.Button(root, text="Kaydet", command=self.save_contacts)
        self.save_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

    def load_contacts(self):
        try:
            with open("contacts.json", "r") as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = {}

    def save_contacts(self):
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file)

    def add_contact(self):
        name = self.name_entry.get()
        number = self.number_entry.get()
        address = self.address_entry.get()
        if name and number:
            self.contacts[name] = {"Telefon": number, "Adres": address}
            self.name_entry.delete(0, tk.END)
            self.number_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Hata", "İsim ve telefon numarası girilmelidir.")

    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            self.name_entry.delete(0, tk.END)
            self.number_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
            messagebox.showinfo("Başarılı", "Kişi başarıyla silindi.")
        else:
            messagebox.showerror("Hata", "Kişi bulunamadı.")

    def update_contact(self):
        name = self.name_entry.get()
        number = self.number_entry.get()
        address = self.address_entry.get()
        if name in self.contacts:
            self.contacts[name] = {"Telefon": number, "Adres": address}
            messagebox.showinfo("Başarılı", "Kişi bilgileri güncellendi.")
        else:
            messagebox.showerror("Hata", "Kişi bulunamadı.")

    def find_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            contact = self.contacts[name]
            self.number_entry.delete(0, tk.END)
            self.number_entry.insert(tk.END, contact["Telefon"])
            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(tk.END, contact["Adres"])
        else:
            messagebox.showerror("Hata", "Kişi bulunamadı.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhonebookApp(root)
    root.mainloop()
