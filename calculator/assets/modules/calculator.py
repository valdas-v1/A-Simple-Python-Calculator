class Actions():
    def add(self, a, b) -> float:
        return a + b

    def multiply(self, a, b) -> float:
        return a * b


class List_actions():
    def add(self, a) -> float:
        answer = 0
        for num in a:
            answer += num
        return answer

    def multiply(self, a) -> float:
        answer = 1
        for num in a:
            answer *= num
        return answer
