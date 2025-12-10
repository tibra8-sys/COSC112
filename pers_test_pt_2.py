print("Welcome to the Big Five Personality Test!")


def ask_questions():
    print("This test will determine your scores for Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism.")
    print("Rate each statement on a scale of 1-5 (1 = strongly disagree, 5 = strongly agree).")
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


def collecting_responses(questions):
    responses = []
    for idx, question in enumerate(questions):
        while True:
            try:
                answer = input(f"Q{idx+1}: {question} (Rate 1-5): ").strip()
            except EOFError:
                print("\nInput ended unexpectedly. Exiting.")
                raise
            if answer.isdigit() and 1 <= int(answer) <= 5:
                responses.append(int(answer))
                break
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
    return responses


def get_trait_interpretation(trait_name, percentage):
    """
    Return a description of what a given trait percentage means.
    """
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
    
    # Determine if score is high, medium, or low
    if percentage >= 66.7:
        level = 'high'
    elif percentage <= 33.3:
        level = 'low'
    else:
        level = 'medium'
    
    return interpretations.get(trait_name, {}).get(level, "")


def calculate_results(responses):
    """
    Calculate and print scores for the Big Five traits.

    This script uses a simple mapping from question indices to traits. Some items
    are reverse-scored (higher value indicates lower level of that trait) and
    are adjusted with `reversed = 6 - value`.
    """
    # Map each trait to question indices that measure it (0-based)
    trait_map = {
        'Extraversion': [0, 1, 6, 11],        # talk, comfortable, social ease, love large gatherings
        'Agreeableness': [2, 7, 16],          # judging, trusting, sympathize
        'Conscientiousness': [3, 8, 12, 17],  # thorough, organized, keep promises, pay attention to details
        'Neuroticism': [4, 14, 19],           # anxious, mood swings, worry
        'Openness': [5, 10, 15]               # creative, art/beauty, try new foods
    }

    # Indices that need reverse scoring (1-5 scale): reversed_score = 6 - response
    reverse_scored = {2, 9}  # question indices where higher score means lower trait (e.g., judging, procrastinating)

    scores = {}
    for trait, indices in trait_map.items():
        adjusted = []
        for i in indices:
            if i >= len(responses):
                # If responses shorter than expected, skip missing items
                continue
            val = responses[i]
            if i in reverse_scored:
                val = 6 - val
            adjusted.append(val)

        raw = sum(adjusted)
        max_possible = len(indices) * 5
        percentage = (raw / max_possible * 100) if max_possible > 0 else 0
        scores[trait] = {'raw': raw, 'max': max_possible, 'percentage': percentage}

    print('\nCalculating results...')
    for trait, vals in scores.items():
        print(f"{trait}: {vals['raw']}/{vals['max']} ({vals['percentage']:.1f}%)")

    # Find the trait with the highest score
    highest_trait = max(scores, key=lambda t: scores[t]['percentage'])
    highest_percentage = scores[highest_trait]['percentage']

    print(f"\n{'='*60}")
    print(f"Your highest trait is: {highest_trait}")
    print(f"{'='*60}")
    print(f"\nWhat this means:")
    interpretation = get_trait_interpretation(highest_trait, highest_percentage)
    print(interpretation)

    return scores


if __name__ == '__main__':
    questions = ask_questions()
    responses = collecting_responses(questions)
    print('\nYour numeric responses:', responses)
    calculate_results(responses)