types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}


def remove_duplicates(tickets_dict):
    for key in tickets_dict:
        tickets_dict[key] = list(set(tickets_dict[key]))
    return tickets_dict


def build_tickets_by_type(types, tickets):

    tickets = remove_duplicates(tickets)

    used = set()
    result = {}

    for level in sorted(types):
        name = types[level]

        result[name] = []

        for ticket in tickets[level]:
            if ticket not in used:
                result[name].append(ticket)
                used.add(ticket)

    return result


tickets_by_type = build_tickets_by_type(types, tickets)

print(tickets_by_type)