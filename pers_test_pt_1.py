import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
# Function to ask questions
def ask_questions():
    questions = [
        "I tend to talk most during conversations.",
        "I feel comfortable around new people.",
        "I have a habit of judging and finding fault with others.",
        "I like to do things thoroughly and carefully.",
        "I often find myself feeling anxious or stressed.",
        "I see myself as someone who is creative, and easily come up with new ideas.",
        "I handle social situations with ease.",
        "I am generally trusting of others.",
        "I am organized and like to plan ahead.",
        "I find myself procrastinating frequently.",
        "I believe in the importance of art and beauty.",
        "I love large social gatherings.",
        "I keep my promises and obligations.",
        "In group projects, I often take the lead.",
        "I frequently experience mood swings.",
        "I enjoy trying new and exotic foods.",
        "I prefer an organized daily routine.",
        "I sympathize with others' feelings.",
        "I pay attention to details.",
        "I worry about things more than I should."
    ]
    return questions

# Function to calculate the results
def calculate_results(responses):
    trait_map = {
        'Extraversion': [0, 1, 6, 11],
        'Agreeableness': [2, 7, 16],
        'Conscientiousness': [3, 8, 12, 17],
        'Neuroticism': [4, 14, 19],
        'Openness': [5, 10, 15]
    }

    reverse_scored = {2, 9}  # reverse scoring questions
    scores = {}
    for trait, indices in trait_map.items():
        adjusted = []
        for i in indices:
            val = responses[i]
            if i in reverse_scored:
                val = 6 - val  # reverse scoring
            adjusted.append(val)

        raw = sum(adjusted)
        max_possible = len(indices) * 5
        percentage = (raw / max_possible * 100) if max_possible > 0 else 0
        scores[trait] = {'raw': raw, 'max': max_possible, 'percentage': percentage}

    return scores

# Function to get trait interpretation
def get_trait_interpretation(trait_name, percentage):
    interpretations = {
        'Extraversion': {
            'high': "You are outgoing, sociable, and energetic. You enjoy being around people and tend to be the life of the party.",
            'medium': "You are moderately social. You enjoy social interactions but also value some alone time to recharge.",
            'low': "You tend to be more introverted and prefer deeper one-on-one conversations over large social gatherings."
        },
        'Agreeableness': {
            'high': "You are compassionate, cooperative, and trusting. You value harmony and are generally helpful to others.",
            'medium': "You are reasonably agreeable but can also assert your own needs and boundaries when necessary.",
            'low': "You are more independent and competitive. You may prioritize your own interests and be more direct in confrontation."
        },
        'Conscientiousness': {
            'high': "You are organized, disciplined, and dependable. You plan ahead and follow through on your commitments.",
            'medium': "You are moderately organized and reliable. You balance structure with flexibility in your approach.",
            'low': "You are more spontaneous and flexible. You may struggle with organization and procrastination."
        },
        'Neuroticism': {
            'high': "You experience emotions intensely and may be prone to stress, anxiety, or mood changes.",
            'medium': "You experience normal emotional fluctuations. You handle stress reasonably well most of the time.",
            'low': "You are emotionally stable and calm. You handle stress well and maintain a balanced emotional state."
        },
        'Openness': {
            'high': "You are creative, curious, and open to new experiences and ideas. You enjoy exploring and learning.",
            'medium': "You are reasonably open to new ideas but also appreciate tradition and conventional approaches.",
            'low': "You prefer familiar approaches and proven methods. You tend to be practical and conventional."
        }
    }

    if percentage >= 66.7:
        level = 'high'
    elif percentage <= 33.3:
        level = 'low'
    else:
        level = 'medium'

    return interpretations.get(trait_name, {}).get(level, "")

class PersonalityTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personality Test")
        self.root.geometry("600x500")

        self.questions = ask_questions()  # Ensure the function is available here
        self.responses = []
        self.current_question = 0

        self.label = tk.Label(root, text="Welcome to the Personality Test!", font=("Arial", 14))
        self.label.pack(pady=20)

        # Description / intro area + Start button
        self.description = tk.Label(root, text="This test will determine your scores for Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. Rate each statement on a scale of 1-5 (1 = strongly disagree, 5 = strongly agree).", font=('Arial', 12), wraplength=500)
        self.description.pack(pady=10)
        self.start_button = tk.Button(root, text="Start", bg="#5aafff", command=self.start_test, font=("Arial", 12))
        self.start_button.pack(pady=(0, 12))

        # Question widgets are created but not shown until Start is pressed
        self.question_label = tk.Label(root, text="", font=("Arial", 12), wraplength=500)

        self.radio_var = tk.IntVar()

        # Create radio buttons for answers 1-5 (won't be packed until Start)
        self.radio_buttons = []
        for i in range(1, 6):
            radio_button = tk.Radiobutton(root, text=str(i), variable=self.radio_var, value=i, font=("Arial", 12))
            self.radio_buttons.append(radio_button)
        # Next button to move to the next question (hidden until Start)
        self.next_button = tk.Button(root, text="Next", bg="#5aafff", command=self.next_question, font=("Arial", 12))

        # Note: do not call update_question() yet — wait until the user starts

    def update_question(self):
        """Update the question displayed to the user."""
        # Len returns the number of items in a list, in this case the number of questions 
        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question])
            self.radio_var.set(0)  # Reset the radio button selection
        else:
            self.show_results()

    def start_test(self):
        """Begin the test: hide the intro and show question widgets."""
        try:
            self.description.pack_forget()
            self.start_button.pack_forget()
        except Exception:
            pass

        # Show question label, radio buttons and next button
        self.question_label.pack(pady=10)
        for rb in self.radio_buttons:
            rb.pack()
        self.next_button.pack(pady=20)

        # Show the first question
        self.update_question()

    def next_question(self):
        """Handle when the user clicks 'Next'."""
        if self.radio_var.get() == 0:
            messagebox.showwarning("Input Error", "Please select a response.")
        else:
            self.responses.append(self.radio_var.get())  # Uses append to Store the user's response
            self.current_question += 1  # Move to the next question
            self.update_question()  # Update the question

    def show_results(self):
        """Display the results after all questions have been answered."""
        scores = calculate_results(self.responses)
        result_text = "\nYour Results:\n"
        for trait, vals in scores.items():
            result_text += f"{trait}: {vals['raw']}/{vals['max']} ({vals['percentage']:.1f}%)\n"
        
        highest_trait = max(scores, key=lambda t: scores[t]['percentage'])
        highest_percentage = scores[highest_trait]['percentage']
        result_text += f"\nYour highest trait is: {highest_trait}\n"
        
        interpretation = get_trait_interpretation(highest_trait, highest_percentage)
        result_text += f"\nWhat this means:\n{interpretation}"

        messagebox.showinfo("Test Results", result_text)
        self.root.quit()  # Close the application after showing results
root.mainLoop()

# Run the GUI 
if __name__ == "__main__":
    root = tk.Tk()
    app = PersonalityTestApp(root)
    root.mainloop()