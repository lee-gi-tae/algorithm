def solution(survey, choices):
    answer = ''
    score = {
        "R" : 0, "T" : 0,
        "C" : 0, "F" : 0,
        "J" : 0, "M" : 0,
        "A" : 0, "N" : 0, 
    }

    for i in range(len(survey)):
        disagree = survey[i][0]
        agree = survey[i][1]
        choice = choices[i]

        if choice < 4:
            score[disagree] += 4 - choice

        if choice > 4:
            score[agree] += choice - 4

    for a, b in [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]:
        if score[a] >= score[b]:
            answer += a
        else:
            answer += b
    return answer