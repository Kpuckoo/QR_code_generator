import qrcode
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import re


# Function to validate URL format
def is_valid_url(url):
    # Regular expression for a simple URL format (http or https)
    url_pattern = re.compile(r'https?://\S+')
    return url_pattern.match(url)


# Counter to keep track of generated QR codes
qr_code_counter = 1


def generate_qr_code():
    data = url_entry.get()

    if not data:
        messagebox.showerror("Error", "Please enter a URL")
        return

    if not is_valid_url(data):
        messagebox.showerror("Error", "Invalid URL format. Please enter a valid URL (e.g., http://www.example.com)")
        return

    global qr_code_counter
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Save each QR code with a unique filename
    filename = f"qrcode_{qr_code_counter}.png"
    img.save(filename)

    qr_code_counter += 1

    # Load the generated QR code image
    qr_image = Image.open(filename)
    qr_image = ImageTk.PhotoImage(qr_image)

    # Display the QR code image in the Tkinter window
    qr_label.config(image=qr_image)
    qr_label.image = qr_image

    messagebox.showinfo("QR Code Generated", f"QR code for {data} saved as {filename}")


# Create the main application window
root = tk.Tk()
root.title("QR Code Generator")
root.eval('tk::PlaceWindow . center')

# Create a label and entry for the URL
url_label = ttk.Label(root, text="Enter URL:")
url_label.pack(pady=5)
url_entry = ttk.Entry(root, width=40)
url_entry.pack(pady=5)

# Create a "Generate" button
generate_button = ttk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=10)

# Create a label to display the QR code image
qr_label = ttk.Label(root)
qr_label.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
