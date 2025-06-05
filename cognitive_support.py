from datetime import datetime

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