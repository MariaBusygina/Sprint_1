i = '1h 45m,360s,25m,30m 120s,2h 60s'
times = i.split(',')
total = 0
for t in times:

    if 'h' in t:
        part = t.split('h')[0]
        total += int(part) * 60
        t = t.split('h')[1]

    if 'm' in t:
        part = t.split('m')[0]
        if part:
            part = part.split()[-1]
            total += int(part)

    if 's' in t:
        part = t.split('s')[0]
        if part:
            part = part.split()[-1]
            total += int(part) / 60

print(total)