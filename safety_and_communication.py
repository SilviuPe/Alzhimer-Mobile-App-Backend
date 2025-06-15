from datetime import datetime

def reminders():


    now = datetime.now()
    hour = int(now.strftime("%I").lstrip("0") or "0")
    period = now.strftime("%p")

    schedule = {
        'PM': {
            6: 'Check calories.',
            8: 'Morning medication.',
            9: 'Evening medication.',
            12: 'Check hydration.',
        },
        'AM': {
            12: 'Midnight medication.',
        }
    }

    orders = list(schedule[period].keys())
    activities = {
        'current': f'{hour} {period} - No activity',
        'next':  f'{hour} {period} - No activity',
        'previous': f'{hour} {period} - No activity',
    }


    if hour in orders:

        
        activities.update({ 'current' : f'{hour} {period} - {schedule[period][hour]}' })
        

    if len(orders) == 1:

        if period == 'AM':
            next_activity_hour = list(schedule['PM'])[0]
            previous_activity_hour = list(schedule['PM'])[-1]
            activities.update({
                'previous': f'{previous_activity_hour} PM - {schedule['PM'][previous_activity_hour]}',
                'next': f'{next_activity_hour} PM - {schedule['PM'][next_activity_hour]}',
            })
        
    else:
        if hour not in orders:
            orders.append(hour)
        orders.sort()
        current_hour_index_in_list = orders.index(hour)

        if current_hour_index_in_list == 0:

            next_hour = orders[current_hour_index_in_list+1]

            activities.update({'next' : f'{next_hour} {period} - {schedule[period][next_hour]}'})
            
            if period == 'AM':
                activities.update({'previous' : f'{list(schedule['PM'].keys())[-1]} PM - {schedule['PM'][list(schedule['PM'].keys())[-1]]}'})
            else:
                activities.update({'previous' : f'{list(schedule['AM'].keys())[-1]} AM - {schedule['AM'][list(schedule['AM'].keys())[-1]]}'})
        

        elif current_hour_index_in_list == len(orders)-1:
            
            previous_hour = orders[current_hour_index_in_list-1]

            activities.update({'previous' : f'{previous_hour} {period} - {schedule[period][previous_hour]}'})

            if period == 'AM':
                activities.update({'next' : f'{list(schedule['PM'].keys())[0]} PM - {schedule['PM'][list(schedule['PM'].keys())[0]]}'})
            else:
                activities.update({'next' : f'{list(schedule['AM'].keys())[0]} AM - {schedule['AM'][list(schedule['AM'].keys())[0]]}'})

        elif len(orders) > 2:
            print(current_hour_index_in_list-1)

            previous_hour_index = current_hour_index_in_list-1
            previous_hour = list(schedule[period].keys())[previous_hour_index]
            
            next_hour_index = current_hour_index_in_list+1
            next_hour = list(schedule[period].keys())[next_hour_index]

            activities.update({
                'previous': f'{previous_hour} {period} - {schedule[period][previous_hour]}',
                'next': f'{next_hour} {period} - {schedule[period][next_hour]}',
            })

    return activities