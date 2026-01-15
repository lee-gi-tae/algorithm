def solution(today, terms, privacies):
    answer = []

    term = {}
    for item in terms:
        key, value = item.split()
        term[key] = int(value)

    for idx, item in enumerate(privacies, 1):
        day, rank = item.split()

        month = term[rank]

        privacy_year = int(day[:4])
        privacy_month = int(day[5:7])
        privacy_day = int(day[8:10])

        # 개월 수 더하기
        privacy_month += month
        privacy_year += (privacy_month - 1) // 12
        privacy_month = (privacy_month - 1) % 12 + 1

        # 🔴 하루 빼기 (유효기간 전날까지 보관)
        privacy_day -= 1
        if privacy_day == 0:
            privacy_day = 28
            privacy_month -= 1
            if privacy_month == 0:
                privacy_month = 12
                privacy_year -= 1

        expire_day = f"{privacy_year:04d}.{privacy_month:02d}.{privacy_day:02d}"

        if expire_day < today:
            answer.append(idx)

    return answer
