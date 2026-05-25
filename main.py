from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

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

        secret_key = ord(key[0])

        img = Image.open(path)
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
            defaultextension=".png"
        )

        if save_path:
            img.save(save_path)

            messagebox.showinfo(
                "Success",
                "Image Encrypted Successfully"
            )

    except:
        messagebox.showerror(
            "Error",
            "Something went wrong"
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

        secret_key = ord(key[0])

        img = Image.open(path)
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
            defaultextension=".png"
        )

        if save_path:
            img.save(save_path)

            # Show decrypted image
            show_image(save_path)

            messagebox.showinfo(
                "Success",
                "Image Decrypted Successfully"
            )

    except:
        messagebox.showerror(
            "Error",
            "Something went wrong"
        )

# Show Image
def show_image(path):

    img = Image.open(path)

    img = img.resize((250, 250))

    photo = ImageTk.PhotoImage(img)

    image_label.config(image=photo)
    image_label.image = photo

# GUI
root = Tk()
root.title("Image Encryption Tool")
root.geometry("500x550")
root.config(bg="black")

Label(root,
      text="Image Encryption Tool",
      font=("Arial", 18, "bold"),
      bg="black",
      fg="lime").pack(pady=15)

Label(root,
      text="Enter Secret Key",
      bg="black",
      fg="white").pack()

key_entry = Entry(root, width=25)
key_entry.pack(pady=10)

# Encrypt Button
Button(root,
       text="Encrypt Image",
       command=encrypt_image,
       bg="green",
       fg="white",
       width=20).pack(pady=10)

# Decrypt Button
Button(root,
       text="Decrypt Image",
       command=decrypt_image,
       bg="blue",
       fg="white",
       width=20).pack(pady=10)

# Image Display
image_label = Label(root, bg="black")
image_label.pack(pady=20)

root.mainloop()