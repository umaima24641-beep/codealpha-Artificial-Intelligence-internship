import tkinter as tk
import datetime

def get_offline_smart_reply(user_query):
    query_clean = user_query.strip().lower()
    if not query_clean:
        return "Please type something so I can think! 🤔"
    
    if "hello" in query_clean or "hi" in query_clean or "hey" in query_clean:
        return "Hello there! 👋 I am AlphaBot. How can I help you in your AI journey today?"
    elif "who made you" in query_clean or "developer" in query_clean or "creator" in query_clean:
        return "I was developed by the brilliant AI developer, Umaima, for the CodeAlpha Internship Task! 🚀"
    elif "codealpha" in query_clean:
        return "CodeAlpha is an incredible platform providing top-tier virtual internship opportunities!"
    elif "what is ai" in query_clean or "artificial intelligence" in query_clean:
        return "Artificial Intelligence (AI) is the simulation of human intelligence by computers. It includes learning! 🤖"
    elif "how are you" in query_clean:
        return "I am doing great, running locally on your machine at lightning speed! How are you doing? 😊"
    elif "time" in query_clean:
        return f"The current system time is {datetime.datetime.now().strftime('%I:%M %p')}. 🕒"
    elif "bye" in query_clean or "exit" in query_clean:
        return "Goodbye! Have a fantastic day ahead. Keep coding! ✨"
    else:
        return "That's an interesting question! As an AI model trained by Umaima, I am ready to assist you further! 💡"

class UltraAIChatbotLocal:
    def __init__(self, root):
        self.root = root
        self.root.title("AlphaBot Ultra AI - Umaima's Project")
        self.root.geometry("420x550")
        self.root.configure(bg="#0f0c20")  
        self.root.resizable(False, False)

        header = tk.Frame(root, bg="#1a0033", height=65)
        header.pack(fill=tk.X)
        
        title_label = tk.Label(header, text="🧠 AlphaBot ULTRA AI", font=("Arial", 14, "bold"), fg="#00dfd8", bg="#1a0033")
        title_label.pack(pady=(8, 2))
        subtitle_label = tk.Label(header, text="CodeAlpha AI Task 1 • 100% Local Safe Engine", font=("Arial", 9), fg="#b3b3b3", bg="#1a0033")
        subtitle_label.pack(pady=(0, 5))

        self.chat_display = tk.Text(root, bg="#0d1b2a", fg="#ffffff", font=("Arial", 10), state='disabled', wrap='word', bd=0, padx=15, pady=15)
        self.chat_display.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        input_frame = tk.Frame(root, bg="#0f0c20")
        input_frame.pack(fill=tk.X, padx=15, pady=(0, 15), side=tk.BOTTOM)

        self.entry_box = tk.Entry(input_frame, bg="#1a0033", fg="#ffffff", font=("Arial", 11), insertbackground="white", bd=1, relief="solid")
        self.entry_box.pack(fill=tk.X, side=tk.LEFT, expand=True, ipady=8, padx=(0, 10))
        
        self.entry_box.bind("<Return>", lambda event: self.trigger_send())
        self.entry_box.focus()

        send_btn = tk.Button(input_frame, text="SEND", font=("Arial", 10, "bold"), bg="#ff007f", fg="#ffffff", bd=0, width=9, cursor="hand2", command=self.trigger_send)
        send_btn.pack(side=tk.RIGHT, ipady=6)

        self.post_message("AlphaBot", "Welcome back Umaima! Ask me anything about your project! 🌍✨")

    def post_message(self, sender, text):
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.chat_display.configure(state='normal')
        self.chat_display.insert(tk.END, f"{sender} [{current_time}]:\n{text}\n\n")
        self.chat_display.configure(state='disabled')
        self.chat_display.see(tk.END)

    def trigger_send(self):
        user_text = self.entry_box.get().strip()
        if not user_text:
            return
        self.post_message("You", user_text)
        self.entry_box.delete(0, tk.END)
        self.root.after(50, lambda: self.fetch_local_reply(user_text))

    def fetch_local_reply(self, text):
        bot_reply = get_offline_smart_reply(text)
        self.post_message("AlphaBot", bot_reply)

if __name__ == "__main__":
    main_window = tk.Tk()
    app = UltraAIChatbotLocal(main_window)
    main_window.mainloop()