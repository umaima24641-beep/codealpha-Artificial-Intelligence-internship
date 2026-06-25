import tkinter as tk
from tkinter import messagebox

# 🧠 Pure Python Machine Learning Engine (Zero Libraries Needed)
# Uses standard Linear Regression: Y = mX + c
def predict_next_price(prices):
    n = len(prices)
    days = list(range(1, n + 1))
    
    # Calculate Mean (Average) of Days and Prices
    mean_days = sum(days) / n
    mean_prices = sum(prices) / n
    
    # Calculate Slope (m) and Intercept (c) manually
    numerator = sum((days[i] - mean_days) * (prices[i] - mean_prices) for i in range(n))
    denominator = sum((days[i] - mean_days) ** 2 for i in range(n))
    
    if denominator == 0:
        return prices[-1] # Fallback if prices are flat
        
    m = numerator / denominator
    c = mean_prices - (m * mean_days)
    
    # Predict next day price (X_next = n + 1)
    next_day = n + 1
    prediction = (m * next_day) + c
    return round(prediction, 2)

# 🏛️ Premium GUI Application Interface
class NativeStockPredictorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Stock Trend Predictor - Task 3")
        self.root.geometry("500x550")
        self.root.configure(bg="#0d1b2a")
        self.root.resizable(False, False)

        # Header Title Area
        header = tk.Frame(root, bg="#1a0033", height=60)
        header.pack(fill=tk.X)
        title_label = tk.Label(header, text="📈 AI Stock Price Forecaster", font=("Arial", 14, "bold"), fg="#00dfd8", bg="#1a0033")
        title_label.pack(pady=5)
        subtitle_label = tk.Label(header, text="CodeAlpha AI Task 3 • Linear Regression Local Model", font=("Arial", 9), fg="#b3b3b3", bg="#1a0033")
        subtitle_label.pack()

        # Input Area Panel
        body_frame = tk.Frame(root, bg="#1b263b", bd=1, relief="solid")
        body_frame.pack(pady=40, padx=30, fill=tk.BOTH, expand=True)

        input_lbl = tk.Label(body_frame, text="Enter Historical Prices\n(Separated by Comma):", font=("Arial", 11, "bold"), fg="#ffffff", bg="#1b263b", justify="center")
        input_lbl.pack(pady=20)

        self.entry_prices = tk.Entry(body_frame, font=("Arial", 12), width=30, bg="#0d1b2a", fg="#ffffff", insertbackground="white", bd=1, justify="center")
        self.entry_prices.insert(0, "100, 105, 112, 118, 125") # Dummy stock data
        self.entry_prices.pack(pady=10)

        # Action Core Button
        predict_btn = tk.Button(body_frame, text="🧠 Forecast Next Day", font=("Arial", 11, "bold"), bg="#ff007f", fg="#ffffff", width=22, height=1, cursor="hand2", command=self.generate_forecast)
        predict_btn.pack(pady=25)

        # Visual Divider Line
        divider = tk.Frame(body_frame, bg="#00dfd8", height=2, width=350)
        divider.pack(pady=10)

        # Output Prediction Box
        self.result_label = tk.Label(body_frame, text="Prediction: Ready to Analyze", font=("Arial", 12, "bold"), fg="#00dfd8", bg="#1b263b")
        self.result_label.pack(pady=20)

    def generate_forecast(self):
        raw_input = self.entry_prices.get()
        try:
            # Parse comma separated input safely
            prices = [float(p.strip()) for p in raw_input.split(",") if p.strip()]
            
            if len(prices) < 2:
                messagebox.showwarning("Data Error", "Please enter at least 2 or more historical prices to calculate trend!")
                return
            
            # Execute math engine logic
            predicted_value = predict_next_price(prices)
            
            # Show output seamlessly on screen
            self.result_label.configure(text=f"🚀 Next Day Predicted Price:\n{predicted_value} USD", fg="#00ff00")

        except ValueError:
            messagebox.showerror("Format Error", "Invalid input! Please enter numbers separated by commas only (e.g., 100, 105, 110).")

if __name__ == "__main__":
    window = tk.Tk()
    app = NativeStockPredictorGUI(window)
    window.mainloop()