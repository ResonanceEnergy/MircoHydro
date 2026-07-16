#!/usr/bin/env python3
import zipfile, tkinter as tk
from tkinter import filedialog
root=tk.Tk(); root.withdraw()
zip_path=filedialog.askopenfilename(title='Choose backup ZIP')
target=filedialog.askdirectory(title='Choose restore folder')
if zip_path and target:
    with zipfile.ZipFile(zip_path,'r') as z: z.extractall(target)
    print('Restored to',target)
else:
    print('Cancelled')
