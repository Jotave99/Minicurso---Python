from tkinter import Tk, messagebox, PhotoImage;
from tkinter.ttk import *;
import tkinter as tk;

root = Tk();
root.title("Desenv Python");
root.geometry("950x600");
root.configure(background="#1e1e1e");

#=====Images======#

mainLogoImg = PhotoImage(file = "imgs/BigBrand.png");
logoImg = PhotoImage(file="imgs/logo.png");
authFrameImg = PhotoImage(file="imgs/AuthFrame.png");

#=====Telas=====#

initScreen = tk.Frame(root, width=950, height=600, bg="#1e1e1e");
#initScreen.pack();

authScreen = tk.Frame(root, width=950, height=600, bg="#1e1e1e");
authScreen.pack();

#=====Init Screen=====#

mainLogoLbl = tk.Label(initScreen, image = mainLogoImg, bg = "#1e1e1e");
mainLogoLbl.place(relx=0.5, rely=0.5, anchor=tk.CENTER);

signInBtn = Button(initScreen, text="Signin");
signInBtn.place(relx=0.45, rely=0.6, anchor=tk.CENTER);

signUpBtn = Button(initScreen, text="Signup");
signUpBtn.place(relx=0.55, rely=0.6, anchor=tk.CENTER);

#=====Auth Screen=====#

authFrameLbl = tk.Label(authScreen, image=authFrameImg, bg="#1e1e1e");
authFrameLbl.place(relx=0.5, rely=0.5, anchor=tk.CENTER);

signInframe = tk.Frame(authScreen, width=320, height=300, bg="#47b5ff");
signInframe.place(x=410, y=150);

loginTitle = tk.Label(signInframe, text="SignIn", bg="#47b5ff");

usernameLbl = tk.Label(signInframe, text="Username:", bg="#47b5ff", fg="white", font=("arial", 18));
usernameLbl.place(relx=0.5, rely=0.4, anchor=tk.CENTER);

usernameEnter = Entry(signInframe);
usernameEnter.place(relx=0.5, rely=0.5, anchor=tk.CENTER);

passwordLbl = tk.Label(signInframe, text="Password:", bg="#47b5ff", fg="white", font=("arial", 18));
passwordLbl.place(relx=0.5, rely=0.6, anchor=tk.CENTER);

passwordEnter = Entry(signInframe);
passwordEnter.place(relx=0.5, rely=0.7, anchor=tk.CENTER);

loginBtn = Button(signInframe, text="Login");
loginBtn.place(relx=0.5, rely=0.8, anchor=tk.CENTER);

def goToRegister():
    signInframe.place_forget();
    signUpBtn.place(x=410, y=150);

createAccountBtn = Button(signInframe, text="Create Account");
createAccountBtn.place(relx=0.5, rely=0.9, anchor=tk.CENTER);

#=====SignUp Screen=====#

signUpframe = tk.Frame(authScreen, width=320, height=300, bg="#47b5ff");
signUpframe.place(x=410, y=150);

newUsernameLbl = tk.Label(signUpframe, text="Username:", bg="#47b5ff", fg="white", font=("arial", 18));
newUsernameLbl.place(relx=0.5, rely=0.4, anchor=tk.CENTER);

newUsernameEnter = Entry(signUpframe);
newUsernameEnter.place(relx=0.5, rely=0.5, anchor=tk.CENTER);

newPasswordLbl = tk.Label(signUpframe, text="Password:", bg="#47b5ff", fg="white", font=("arial", 18));
newPasswordLbl.place(relx=0.5, rely=0.6, anchor=tk.CENTER);

newPasswordEnter = Entry(signUpframe);
newPasswordEnter.place(relx=0.5, rely=0.7, anchor=tk.CENTER);

registerBtn = Button(signUpframe, text="Register");
registerBtn.place(relx=0.5, rely=0.8, anchor=tk.CENTER);

createAccountBtn = Button(signUpframe, text="Create Account");
createAccountBtn.place(relx=0.5, rely=0.9, anchor=tk.CENTER);

root.mainloop();
