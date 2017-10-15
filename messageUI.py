import tkinter as tk
import messaging

class messageUI:
	def __init__(self):
		self.root= tk.Tk()
		self.root.geometry("800x500+100+100")
		self.root.resizable(False,False)

		self.e_contactEntry = tk.Entry(self.root)
		self.b_addContact = tk.Button(self.root, text="Add",command=self.addContact)
		self.l_contactList = tk.Listbox(self.root)
		self.m_conversation = tk.Message(self.root)
		self.e_messageEntry = tk.Entry(self.root)
		self.b_send = tk.Button(self.root, text="Send",command=self.sendMsg)

		self.e_contactEntry.place(x=10,y=470,height=30, width=150)
		self.b_addContact.place(x=165,y=470,height=30, width=55)
		self.l_contactList.place(x=10,y=10,height=450,width=210)
		self.m_conversation.config(fg="red", borderwidth=50, highlightcolor="green",
               background='gray')
		self.m_conversation.place(x=230,y=10,height=350,width=560)
		self.e_messageEntry.place(x=230,y=365,height=130,width=400)
		self.b_send.place(x=650,y=365,height=130,width=135)

		self.root.mainloop()

	def addContact(self):
		pass

	def sendMsg(self):
		pass


if __name__ == "__main__":
	U = messageUI()