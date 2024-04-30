import random

# List of mental health advice messages
advice_messages = {
    "stressed": [
        "Remember to take breaks and give yourself time to recharge.",
        "Practice deep breathing exercises to help calm your mind.",
        "Break tasks into smaller, more manageable steps to reduce feelings of overwhelm.",
        "Consider talking to a counselor or trusted individual about what's causing your stress: [link]",
    ],
    "anxious": [
        "Practice mindfulness or meditation to help ground yourself in the present moment.",
        "Challenge negative thoughts by asking yourself if they're based on facts or just worries.",
        "Engage in physical activity to help release tension and reduce anxiety.",
        "Seek out professional help if your anxiety is interfering with your daily life: [link]",
    ],
    "sad": [
        "Reach out to friends or family members for support and company.",
        "Engage in activities you enjoy to boost your mood and distract yourself from sadness.",
        "Consider volunteering or helping others to gain perspective and feel more connected.",
        "If you're feeling persistently sad, it's okay to seek help from a therapist or counselor: [link]",
    ],
    "overwhelmed": [
        "Take a step back and prioritize your tasks, focusing on what's most important.",
        "Delegate tasks when possible and don't be afraid to ask for help.",
        "Practice self-compassion and remind yourself that it's okay not to do everything perfectly.",
        "Consider speaking with a counselor or advisor for support in managing your workload: [link]",
    ],
    "happy": [
        "Celebrate your achievements, big and small, and take time to appreciate the good moments.",
        "Spread positivity by expressing gratitude and kindness towards others.",
        "Use your happiness as motivation to continue pursuing your goals and passions.",
        "Remember to take care of yourself even when things are going well; self-care is important for maintaining happiness.",
    ],
}

# Function to give advice based on the user's feeling
def give_advice(feeling):
    # Check if the given feeling has corresponding advice messages
    if feeling.lower() in advice_messages:
        print("Advice based on how you're feeling:")
        advice = random.choice(advice_messages[feeling.lower()])
        # Add link to advice if feeling is not "happy"
        if feeling.lower() != "happy":
            advice_with_link = advice.replace("[link]", "https://www.kennesaw.edu/student-affairs/wellbeing/counseling/services/index.php")
            print(advice_with_link)
        else:
            print(advice)
    else:
        print("Sorry, I don't have specific advice for that feeling.")

# Prompt the user to input how they feel
user_feeling = input("How are you feeling today? (stressed, anxious, sad, overwhelmed, happy): ")

# Call the function to give advice based on the user's input
give_advice(user_feeling)
