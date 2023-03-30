# 실전문제 전보
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수 , 간선의 개수 , 시작 입력받기

n,m,start = map(int,input().split())
# 노드의 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
# 최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def dijkstart(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하며, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면?
        dist,now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
        
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))

dijkstart(start)

# 도달할 수 있는 노드의 개수
count = 0
# 도달 할 수 있는 노드 중에서 , 갖ㅇ 멀리 있는 노드와의 최단 거리
max_distance = 0 
for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance,d)


#시작 노드는 제외해야 함으로 count -1을 출력

print(count -1 , max_distance)

