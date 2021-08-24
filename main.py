import tkinter
# messagebox是一个module
# import tkinter.messagebox
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_list = [random.choice(letters) for _ in range(nr_letters)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)

    # print(f"Your password is: {password}")
    # password_entry.config(text=f"{password}")
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo("提示：", "新生成的密码已经复制进粘贴板")


# ---------------------------- SAVE PASSWORD ------------------------------- #
# TODO: 2.点击add，创建保存网站，用户名，密码入data.txt文档，并清空相应栏目

# 点击事项
def save_data():
    web_str = web_input.get()
    user_str = email_input.get()
    pass_str = password_entry.get()
    # print(f"{web_str} | {user_str} | {pass_str}")
    # 返回bool值.或者len(web_str) == 0
    if web_str == "" or pass_str == "":
        messagebox.showinfo("提示", "抱歉，请不要留空")
    else:
        is_true = messagebox.askokcancel("确认是否保存", f"你确认以下信息正确吗？\n web:{web_str}\n用户名{user_str}\n密码：{pass_str}")
        if is_true:
            with open("data.txt", 'a') as data:
                data.write(f"{web_str} | {user_str} | {pass_str}\n")
            web_input.delete(0, tkinter.END)
            # email_input.delete(0, tkinter.END)

            password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Password Manager")
canvas = tkinter.Canvas()
canvas.config(width=200, height=200)
image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)
window.config(padx=50, pady=50)

# TODO: 1.添加组件
# labels
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)
# entrys
web_input = tkinter.Entry(width=40)
web_input.grid(row=1, column=1, columnspan=2)
# 将指针显现
web_input.focus()
email_input = tkinter.Entry(width=40)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "aaa@gmail.com")
password_entry = tkinter.Entry(width=25)
password_entry.grid(row=3, column=1)
# buttons
gpassword_button = tkinter.Button(text="Generate Password", command=generate_password)
gpassword_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", command=save_data)
add_button["width"] = 41
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
