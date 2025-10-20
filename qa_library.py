import tkinter as tk
import os
import sys
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering


# get the folder
base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))

# Persian Q&A model
# qa_pipeline = pipeline("question-answering", model="m3hrdadfi/xlmr-large-qa-fa")
model_path = os.path.join(base_path, "model_cache")
model_name = "m3hrdadfi/xlmr-large-qa-fa"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForQuestionAnswering.from_pretrained(model_path)
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

# save the 'model_cache' folder
# tokenizer.save_pretrained("./model_cache")
# model.save_pretrained("./model_cache")

# load laptop.txt
txt_path = os.path.join(base_path, "laptop.txt")
with open(txt_path, "r", encoding="utf-8") as f:
    knowledge_text = f.read()


# functions
def get_answer():
    question = entry.get().strip()
    if not question:
        show_answer("سوال خود را بپرسید")
        return
    
    try:
        result = qa_pipeline(question=question, context = knowledge_text)

        # print("MODEL RAW ANSWER:", result) 

        answer_start = max(result['start'] - 40, 0)
        answer_end = min(result['end'] + 120, len(knowledge_text))
        extracted_text = knowledge_text[answer_start:answer_end].strip()

        # print("Extracted from text:", extracted_text)
        
        final_answer = f"سوال: {question}\nپاسخ: {extracted_text}"
        show_answer(final_answer)

        # clear the answer after asking
        entry.delete(0, tk.END)

    except Exception as e:
        show_answer(f"خطا: {str(e)}")

def show_answer(text):
    answer_box.config(state=tk.NORMAL)
    answer_box.delete("1.0", tk.END)
    answer_box.insert(tk.END, text, "right")
    answer_box.config(state=tk.DISABLED)

def exit_app():
    window.destroy()

# main window
window = tk.Tk()
window.title("یادگیرنده هوش مصنوعی")
window.geometry("600x450")

tk.Label(window, text=":سوال شما", font=("Vazir", 12)).pack(pady=5)
entry = tk.Entry(window, width=60, justify="right", font=("Vazir", 12))
entry.pack(pady=10)

btn = tk.Button(window, text="بپرس", command=get_answer, bg="gray")
btn.pack(pady=5)

# press enter
entry.bind("<Return>", lambda event: get_answer())


tk.Label(window, text=":جواب", font=("Vazir", 12)).pack(pady=10)
answer_box = tk.Text(window, height=10, width=70, wrap="word", state=tk.DISABLED)
answer_box.pack(pady=3)

# scrolling
scrollbar = tk.Scrollbar(window, command = answer_box.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
answer_box.config(yscrollcommand = scrollbar.set)

answer_box.tag_configure("right", justify="right")

btn_exit = tk.Button(window, text="خروج", command=exit_app, bg="gray")
btn_exit.pack(pady=10)

window.mainloop()
