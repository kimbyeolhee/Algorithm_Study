# 2022-05-23
# 4:00-

# TODO 다시풀기


### Sol1 ###
def solution(tickets):
    routes = dict()

    for (start, end) in tickets:
        routes[start] = routes.get(start, []) + [end]

    for r in routes.keys():
        routes[r].sort(reverse=True)

    stack = ["ICN"]
    path = []

    while stack:
        top = stack[-1]

        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    answer = path[::-1]
    return answer

### Sol2 ###
from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list)
    
    for start,end in tickets:
        routes[start].append(end)
    for key in routes.keys():
        routes[key].sort()

    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]
        
        if routes[top] != []:
            stack.append(routes[top].pop(0))
        else:
            path.append(stack.pop())

    return path[::-1]