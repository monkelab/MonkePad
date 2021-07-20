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
    ('HTML File','*.html *.htm *.xhtml *.shtml *.jhtml'),
    ('JavaScript File','*.js'),
    ('TypeScript File','*.ts'),
    ('CSS File','*.css'),
    ('Rust File','*.rs'),
    ('Markdown File','*.md'),
    ('Assembly File','*.asm *.s'),
    ('Forth File','*.forth'),
    ('Ruby File','*.rb *.rhtml'),
    ('PHP File','*.php *.php3 *.php4 *.phtml'),
    ('Java File', '*.java *.jav'),
    ('Common Lisp File','*.lisp *.lsp'),
    ('Scheme File','*.scm'),
    ('Kotlin File', '*.kt'),
    ('Pascal File', '*.pas'),
    ('Brainf*ck File', '*.bf'),
    ('F# File', '*.fs *.fsi *.fsx'),
    ('C# File', '*.cs'),
    ('Emacs Lisp File', '*.el *.elc'),
    ('CSV File', '*.csv'),
    ('XML File', '*.xml *.rss'),
    ('Ada File', '*.ada *.adb *.ads'),
    ('Arduino File', '*.ino'),
    ('Batchfile', '*.bat *.cmd'),
    ('Shell File', '*.sh *.bash *.bats *.cgi *.command *.fcgi *.ksh *.sh.in *.tmux *.tool *.zsh'),
    ('Powershell File', '*.ps1 *.psd1 *.psm1'),
    ('CMake File', '*.cmake'),
    ('COBOL File', '*.cob *.cbl *.cobol *.cpy'),
    ('Clojure File', '*.clj *.boot'),
    ('Coq File', '*.coq'),
    ('D File', '*.d *.di'),
    ('Dart File', '*.dart'),
    ('Dockerfile', '*.dockerfile'),
    ('Go File', '*.go'),
    ('Gradle File', '*.gradle'),
    ('Haskell File', '*.hs *.hsc'),
    ('JSON File', '*.json *.lock'),
    ('Makefile', '*.mak *.mkfile'),
    ('Perl File', '*.pl'),
    ('R File', '*.r'),
    ('SQL File', '*.sql'),
    ('Swift File', '*.swift'),
    ('TeX File', '*.tex'),
    ('Unix Configuration File', '.conf')
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
    text.delete(1.0, 'end')
    root.title('New File - MonkePad')

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
    root.title(f'{filename} - MonkePad')

def save_file(event):
    global FILE_NAME, FILE_CONTENT
    file = open(FILE_NAME, 'w') if FILE_NAME else fd.asksaveasfile(initialfile = FILE_NAME,
        defaultextension = '',
        filetypes = FILETYPES
    )
    if file is None: return
    
    text_to_save = str(text.get(1.0, 'end'))
    file.write(text_to_save)
    
    FILE_NAME = file.name
    FILE_CONTENT = text_to_save
    file.close()

    print(f'{file.name} saved successfully')
    root.title(f'{file.name} - MonkePad')

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
