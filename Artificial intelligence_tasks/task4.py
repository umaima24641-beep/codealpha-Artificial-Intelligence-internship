import tkinter as tk
from tkinter import messagebox

# 🧠 1. Smart Text Analysis Engine (Zero Libraries Needed)
# Scans text patterns, frequencies, and spam keywords to classify safety
def analyze_message_safety(text):
    text_lower = text.lower().strip()
    
    if not text_lower:
        return "Empty", 0
    
    # High-Risk Spam Trigger Keywords
    spam_keywords = [
        "win", "winner", "free", "cash", "prize", "lottery", "urgent", "claim", 
        "click here", "subscribe", "bonus", "gift", "card", "selected", "congratulations",
        "reward", "earn money", "investment", "bitcoin", "crypto", "account blocked"
    ]
    
    # Calculate Risk Score based on keyword hits
    hit_count = 0
    for word in spam_keywords:
        if word in text_lower:
            hit_count += 1
            
    # Classification Logic
    # If it contains high-risk words or has suspicious pattern
    if hit_count >= 2 or (hit_count >= 1 and ("!" in text_lower or "http" in text_lower)):
        return "SPAM (FRAUD / RISK)", hit_count
    elif hit_count == 1:
        return "SUSPICIOUS (PROMOTIONAL)", hit_count
    else:
        return "HAM (SAFE / NORMAL)", 0

# 🏛️ 2. Premium Cyber-Security GUI Dashboard
class SpamDetectorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Spam & Fraud Detector - Task 4")
        self.root.geometry("450x500")
        self.root.configure(bg="#0d1b2a")
        self.root.resizable(False, False)

        # Header Title Area
        header = tk.Frame(root, bg="#1a0033", height=65)
        header.pack(fill=tk.X)
        title_label = tk.Label(header, text="🛡️ AI Spam Filter Dashboard", font=("Arial", 14, "bold"), fg="#00dfd8", bg="#1a0033")
        title_label.pack(pady=5)
        subtitle_label = tk.Label(header, text="CodeAlpha AI Task 4 • Text Classification Model", font=("Arial", 9), fg="#b3b3b3", bg="#1a0033")
        subtitle_label.pack()

        # Body Container
        body = tk.Frame(root, bg="#1b263b", bd=1, relief="solid")
        body.pack(pady=25, padx=25, fill=tk.BOTH, expand=True)

        input_lbl = tk.Label(body, text="Paste SMS or Email Text Below:", font=("Arial", 11, "bold"), fg="#ffffff", bg="#1b263b")
        input_lbl.pack(pady=15)

        # Multi-line Text Box Input
        self.text_input = tk.Text(body, font=("Arial", 10), width=40, height=7, bg="#0d1b2a", fg="#ffffff", insertbackground="white", bd=0, padx=10, pady=10)
        self.text_input.insert(tk.END, "Congratulations! You won a free $1000 Walmart gift card. Click here to claim your prize now!") # Default text
        self.text_input.pack(pady=5)

        # Core Action Button
        scan_btn = tk.Button(body, text="🔍 Scan Text Safety", font=("Arial", 11, "bold"), bg="#ff007f", fg="#ffffff", width=22, cursor="hand2", command=self.run_detector)
        scan_btn.pack(pady=20)

        # Output Box Interface
        self.status_lbl = tk.Label(body, text="Status: Ready to Scan", font=("Arial", 12, "bold"), fg="#00dfd8", bg="#1b263b")
        self.status_lbl.pack(pady=5)
        
        self.score_lbl = tk.Label(body, text="Risk Factor: 0", font=("Arial", 9), fg="#b3b3b3", bg="#1b263b")
        self.score_lbl.pack()

    def run_detector(self):
        user_text = self.text_input.get("1.0", tk.END).strip()
        
        if not user_text:
            messagebox.showwarning("Input Error", "Please type or paste some text first to scan!")
            return
            
        result, score = analyze_message_safety(user_text)
        
        # UI Dynamic Color Updates based on Results
        if "SPAM" in result:
            self.status_lbl.configure(text=f"🚨 {result}", fg="#ff3333")
            self.score_lbl.configure(text=f"Risk Trigger Keywords Found: {score}", fg="#ff9999")
        elif "SUSPICIOUS" in result:
            self.status_lbl.configure(text=f"⚠️ {result}", fg="#ffcc00")
            self.score_lbl.configure(text=f"Risk Trigger Keywords Found: {score}", fg="#ffe680")
        else:
            self.status_lbl.configure(text=f"✅ {result}", fg="#00ff00")
            self.score_lbl.configure(text="Message looks safe and clean.", fg="#b3b3b3")

if __name__ == "__main__":
    window = tk.Tk()
    app = SpamDetectorGUI(window)
    window.mainloop()