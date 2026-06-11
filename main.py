from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import threading

# Show Image
def show_image(path):
    img = Image.open(path)
    img = img.resize((250, 250))

    photo = ImageTk.PhotoImage(img)

    image_label.config(image=photo)
    image_label.image = photo

# Encrypt Image
def encrypt_image():

    path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )

    if not path:
        return

    try:
        key = key_entry.get()

        if key == "":
            messagebox.showerror(
                "Error",
                "Enter Secret Key"
            )
            return

        status_label.config(text="Processing...")

        # Use entire key
        secret_key = sum(ord(c) for c in key) % 256

        img = Image.open(path).convert("RGB")
        pixels = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):

                r, g, b = pixels[i, j]

                pixels[i, j] = (
                    r ^ secret_key,
                    g ^ secret_key,
                    b ^ secret_key
                )

        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Files", "*.png")]
        )

        if save_path:
            img.save(save_path)

            status_label.config(text="Encryption Completed")

            messagebox.showinfo(
                "Success",
                "Image Encrypted Successfully"
            )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )

# Decrypt Image
def decrypt_image():

    path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )

    if not path:
        return

    try:
        key = key_entry.get()

        if key == "":
            messagebox.showerror(
                "Error",
                "Enter Secret Key"
            )
            return

        status_label.config(text="Processing...")

        # Use entire key
        secret_key = sum(ord(c) for c in key) % 256

        img = Image.open(path).convert("RGB")
        pixels = img.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):

                r, g, b = pixels[i, j]

                pixels[i, j] = (
                    r ^ secret_key,
                    g ^ secret_key,
                    b ^ secret_key
                )

        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Files", "*.png")]
        )

        if save_path:
            img.save(save_path)

            show_image(save_path)

            status_label.config(text="Decryption Completed")

            messagebox.showinfo(
                "Success",
                "Image Decrypted Successfully"
            )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )

# GUI
root = Tk()
root.title("Image Encryption Tool")
root.geometry("550x650")
root.config(bg="black")

Label(
    root,
    text="Image Encryption Tool",
    font=("Arial", 18, "bold"),
    bg="black",
    fg="lime"
).pack(pady=15)

Label(
    root,
    text="Enter Secret Key",
    bg="black",
    fg="white"
).pack()

key_entry = Entry(root, width=30)
key_entry.pack(pady=10)

# Encrypt Button
Button(
    root,
    text="Encrypt Image",
    command=lambda: threading.Thread(
        target=encrypt_image
    ).start(),
    bg="green",
    fg="white",
    width=20
).pack(pady=10)

# Decrypt Button
Button(
    root,
    text="Decrypt Image",
    command=lambda: threading.Thread(
        target=decrypt_image
    ).start(),
    bg="blue",
    fg="white",
    width=20
).pack(pady=10)

# Status Label
status_label = Label(
    root,
    text="Ready",
    bg="black",
    fg="yellow",
    font=("Arial", 11, "bold")
)
status_label.pack(pady=10)

# Image Preview
image_label = Label(root, bg="black")
image_label.pack(pady=20)

root.mainloop()
