def solution(s):

    words = s.split(' ')
    answer = []

    for idx1, word in enumerate(words):

        word2 = ''
        for idx2, w in enumerate(word):

            if idx2 % 2 == 0:
                word2 += w.upper()
            else:
                word2 += w.lower()

        answer.append(word2)

    return ' '.join(answer)