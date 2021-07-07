import tkinter as tk
from tkinter import filedialog as fd

FILE_NAME = ''
FILE_CONTENT = ''

#------------------
#Settings
FONT = 'Monospace'
FONT_SIZE = 11
FOREGROUND = '#f0f6f0'
BACKGROUND = '#222323'
CURSOR_COLOR = FOREGROUND
FILETYPES = [
    ('All Files','*.*'),
    ('Text File','*.txt'),
    ('Python File','*.py *.pyw'),
    ('Lua File','*.lua'),
    ('C File','*.c'),
    ('HolyC File','*.hc'),
    ('C++ File','*.cpp *.cxx *.c++'),
    ('HTML File','*.html *.htm'),
    ('JavaScript File','*.js'),
    ('TypeScript File','*.ts'),
    ('CSS File','*.css'),
    ('Rust File','*.rs'),
    ('Markdown File','*.md'),
    ('Assembly File','*.asm *.s'),
    ('Forth File','*.forth'),
    ('Ruby File','*.rb'),
    ('PHP File','*.php'),
    ('Java File', '*.java *.jav'),
    ('Lisp File','*.lisp *.lsp'),
    ('Scheme File','*.scm'),
    ('Kotlin File', '*.kt'),
    ('Pascal File', '*.pas'),
    ('Brainf*ck File', '*.bf'),
    ('F# File', '*.fs *.fsi *.fsx'),
    ('Emacs Lisp File', '*.el *.elc'),
    ('CSV File', '*.csv')
]

#------------------
#Window
root = tk.Tk()
root.title('MonkePad')

text = tk.Text(root,
    bg = BACKGROUND,
    fg = FOREGROUND,
    insertbackground = CURSOR_COLOR,
    font = (FONT, FONT_SIZE))

text.insert(1.0, 'Ctrl + S to save, Ctrl + O to open')
text.pack(expand = 1, fill = 'both')

def new_file(event):
    global FILE_NAME, FILE_CONTENT
    FILE_NAME = ''
    FILE_CONTENT = ''
    REVERT_CONTENT = ''
    text.delete(1.0, 'end')

#------------------
#File functions
def open_file(event):
    global FILE_NAME, FILE_CONTENT
    filename = fd.askopenfilename()
    
    if filename is None: return
    
    with open(filename, 'r') as file:
        text.delete(1.0, 'end')
        text.insert(1.0, file.read())

        FILE_NAME = filename
        FILE_CONTENT = file.read()
    print(f'{filename} opened successfully')

def save_file(event):
    global FILE_NAME, FILE_CONTENT
    file = fd.asksaveasfile(initialfile = FILE_NAME,
        defaultextension = '',
        filetypes = FILETYPES
    )
    if file is None: return
    
    text_to_save = str(text.get(1.0, 'end'))
    file.write(text_to_save)
    
    FILE_CONTENT = text_to_save
    file.close()

    print(f'{FILE_NAME} saved successfully')

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label = 'New', command = lambda: new_file(None), accelerator = 'Ctrl + N')
filemenu.add_command(label = 'Open', command = lambda: open_file(None), accelerator = 'Ctrl + O')
filemenu.add_command(label = 'Save', command = lambda: save_file(None), accelerator = 'Ctrl + S')
filemenu.add_separator()
filemenu.add_command(label = 'Exit', command = root.quit)
menubar.add_cascade(label = 'File', menu = filemenu)




#------------------
#Keybindings and window loop
root.bind('<Control-n>', new_file)
root.bind('<Control-o>', open_file)
root.bind('<Control-s>', save_file)
root.config(menu = menubar)
root.mainloop()
