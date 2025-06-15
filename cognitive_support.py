from datetime import datetime
from random import randint

def get_activity_message() -> str:
    

    now = datetime.now()
    hour = int(now.strftime("%I").lstrip("0") or "0")
    period = now.strftime("%p")
    print(hour, period)
    schedule = {
        'PM': {
            (0, 3): 'Relax',
            (3, 6): 'Eat',
            (6, 9): 'Go for a walk',
            (9, 11): 'Sleep',
        },
        'AM': {
            (12, 7): 'Sleep',
            (7, 8): 'Have breakfast',
            (8, 12): 'Do some running or physical exercise',
        }
    }

    for (start, end), activity in schedule.get(period.upper(), {}).items():
        if start <= hour < end:
            return f"You should {activity.lower()} at this hour."

    return "No activity scheduled for this time."



def generate_questions(count : int) -> list:

    questions = [
        "How are you feeling emotionally today (happy, anxious, sad, calm)?",
        "Did anything upset or stress you today?",
        "Is there something you’re looking forward to today or tomorrow?",
        "Have you been feeling lonely or disconnected lately?",
        "Would you like to talk to someone today?",
        "How is your energy level this morning?",
        "Did you sleep well last night?",
        "Are you experiencing any pain or discomfort today?",
        "Have you eaten any meals or snacks in the last few hours?",
        "Are you feeling dizzy, weak, or unwell in any way?",
        "Did you take your medications as prescribed today?",
        "Do you need a reminder or help with any appointments?",
        "Have you had enough water today?",
        "Is there anything you forgot or feel unsure about doing today?"
    ]


    random_questions_start = randint(0,len(questions)-count-1)

    return {
        "questions" : 
            questions[random_questions_start:random_questions_start+count]
        
    }


