meeting_alpha = {201, 205, 210, 220}
meeting_beta = {205, 215, 220, 230}

attended_both_meetings = meeting_alpha.intersection(meeting_beta)

meeting_attandance = {}

for item in attended_both_meetings:
    meeting_attandance[item] = True


print(meeting_attandance)