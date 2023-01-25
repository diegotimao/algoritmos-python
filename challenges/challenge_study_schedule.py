def study_schedule(permanence_period, target_time):
    people = 0

    if not isinstance(target_time, int):
        return None

    for hour in permanence_period:
        if isinstance(hour[0], int) and isinstance(hour[1], int):
            if target_time >= hour[0] and target_time <= hour[1]:
                people += 1
        else:
            return None
    return people
