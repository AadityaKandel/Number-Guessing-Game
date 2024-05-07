from tkinter import *
import random
import tkinter.messagebox as tmsg

root = Tk()

# Initializing the root
root.geometry("450x170")
root.title("Number Guessing Game")

# Initializing Variables
font="Arial 12 italic"
addition_lists=[]
subtraction_lists=[]
loop_randomize=0
decide_operation=None # 1 Means Addition & 0 Means Subtraction
generated_texts=[]
initial=0 # This will help in displaying all the texts inside generated_texts
length=0

# Creating Functions
def initiate_magic():
	initialize_variables()
	randomize_numbers()
	calculate()

def randomize_numbers():
	loop_randomize=r_r(4,8)

	for x in range(loop_randomize):
		decide_operation=r_r(0,1)

		if decide_operation==1:
			addition_lists.append(r_r(1,20))
		elif decide_operation==0:
			subtraction_lists.append(r_r(1,20))

def r_r(fromm,to):  # r_r short form for random.randint()
	return random.randint(fromm,to)

def calculate():
	global generated_texts,length
	l1.config(text="I will try to guess your final answer. Shall we continue?")

	a = len(addition_lists)
	s = len(subtraction_lists)

	for i in range(max(a,s)):
		if i<a:
			generated_texts.append(f'Add {addition_lists[i]} to your number')
		if i<s:
			generated_texts.append(f'Subtract {subtraction_lists[i]} from your number')

	generated_texts.append('Now, subtract the original number from your final number')
	b1.config(text="Next",command=process_output)
	length=len(generated_texts)

def process_output():
	global generated_texts,initial,length
	b2.config(state=NORMAL) if initial>=1 else None
	l1.config(text=generated_texts[initial])
	if initial==(length-1):
		b1.config(command=magic_output)
	else:
		initial+=1

def magic_output():
	final_value=sum(addition_lists)-sum(subtraction_lists)

	l1.config(text=f"Your answer is {final_value}")
	b1.config(text='YAYY!!',state=DISABLED)
	b2.config(state=DISABLED)

def enter(event):
	if event.widget['text']=="Back":
		b2.config(bg="black",fg="white")
	else:
		b1.config(bg="black",fg="white")

def leave(event):
	if event.widget['text']=="Back":
		b2.config(bg="white",fg="black")
	else:
		b1.config(bg="white",fg="black")

def go_back():
	global initial
	initial=initial-2
	if initial<0:
		tmsg.showwarning('Warning',"You've reached the end!!")
		initial=1
	else:
		process_output()

l1 = Label(text="Think a number between 1 to 100",font=font)
l1.pack(pady=(10,70))

f1 = Frame()

b1 = Button(f1,text="Done",font=font,command=initiate_magic,width=15)
b2 = Button(f1,text="Back",font=font,command=go_back,width=15,bg="white",state=DISABLED)

# Packing Everything
b2.pack(side=LEFT,padx=(0,8))
b1.bind("<Enter>",enter)
b1.bind("<Leave>",leave)
b1.pack(side=LEFT)
b2.bind("<Enter>",enter)
b2.bind("<Leave>",leave)

f1.pack(anchor=N)

root.mainloop()
