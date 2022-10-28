def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if target_time != 0 and not target_time:
        return None
    count = 0
    for i in permanence_period:
        if not (type(i[0]) == int) or not (type(i[1]) == int):
            return None
        if target_time >= i[0] and target_time <= i[1]:
            count += 1
    return count


permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
print(study_schedule(permanence_period, 0))
