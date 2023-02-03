import tkinter as tk
import random

def on_enter(e):
    player = entry.get()
    if player:
        players.append(player)
        entry.delete(0, tk.END)
        num_players.config(text="Players: " + str(len(players)))
        entry_frame.config(bg='#ddd')

def assign_teams():
    random.shuffle(players)
    for i in range(len(players)):
        if i % 2 == 0:
            team1.append(players[i])
        else:
            team2.append(players[i])
    for player in team1:
        list1.insert(tk.END, player)
    for player in team2:
        list2.insert(tk.END, player)

root = tk.Tk()
root.configure(bg='#333')
root.geometry("400x400")
root.title("Team Generator")

players = []
team1 = []
team2 = []

entry_frame = tk.Frame(root, bg='#333')
entry_frame.pack(pady=20)

label = tk.Label(entry_frame, text="Enter player name:", bg='#333', fg='white')
label.pack()

entry = tk.Entry(entry_frame, font=("Arial", 12), bd=5, bg='#ddd')
entry.pack()
entry.focus_set()
entry.bind("<Return>", on_enter)

num_players = tk.Label(entry_frame, text="Players: 0", bg='#333', fg='white')
num_players.pack()

assign_button = tk.Button(entry_frame, text="Assign Teams", command=assign_teams, bg='#fff', fg='black', relief=tk.GROOVE, bd=2, font=("Arial", 12), width=15, height=2)
assign_button.pack()

frame = tk.Frame(root, bg='#333')
frame.pack(side=tk.LEFT, padx=30)

list1 = tk.Listbox(frame, height=20, width=20, font=("Arial", 12), bd=5, bg='#ddd', fg='black')
list1.pack(side=tk.TOP)

label1 = tk.Label(frame, text="Team 1", bg='#333', fg='white')
label1.pack()

frame = tk.Frame(root, bg='#333')
frame.pack(side=tk.RIGHT, padx=30)

list2 = tk.Listbox(frame, height=20, width=20, font=("Arial", 12), bd=5, bg='#ddd', fg='black')
list2.pack(side=tk.TOP)

label2 = tk.Label(frame, text="Team 2", bg='#333', fg='white')
label2.pack()

root.mainloop()
