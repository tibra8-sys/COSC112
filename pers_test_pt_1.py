from logging import root
import tkinter as tk
from tkinter import messagebox
import json

def home_screen():
    root = tk.Tk()

    root.title("Personality Test")
    root.geometry("400x500")
    root.config(bg='tan')

    label = tk.Label(root, text="Welcome to the Big Five Personality Test!", bg='tan', font=('Times New Roman', 40))
    label.pack(pady=60, padx=70)
    subheading = tk.Label(root, text="This test will determine what your personality type is on a basis of Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. The test consists of 30 multiple choice questions which you will rate how much you agree with on a scale of 1-5. 1 being the strongly disagree and 5 being strongly agree. See how you score on our scale!", bg='tan', font=('Arial', 20), wraplength =1400, justify='center')
    subheading.pack(pady=20, padx=20)

    button = tk.Button(root, text="Start Quiz", bg='lightblue', font=('Times New Roman', 20))
    button.pack(pady=100)

    home_screen()
    root.mainloop()

def move_page():



    move_page()


def question_pg1():

   root = tk.Tk()
    questions_text = (
    "I tend to talk most during conversations.\n"
    "I feel comfortable around new people.\n"
    "I have a habit of judging andfinding fault with others.\n"
    "I like to do things thoroughly and carefully.\n"
    "I often find myself feeling anxious or stressed.\n"
    "I see myself as someone who is creative, and easily come up with new ideas.\n"
    'I handle social situations with ease.\n'
    "I am generally trusting of others.\n"
    "I am organized and like to plan ahead.\n"
    'I find myself procrastinating frequently.\n'
    )
    questions_label = tk.Label(root, text=questions_text, bg='tan', font=('Arial', 16), justify='left')
    questions_label.pack(pady=50, padx=50)

    button = tk.Button(root, text="Submit", bg='lightblue', font=('Times New Roman', 20))
    button.pack(pady=100)
    root.mainloop()

question_pg1()