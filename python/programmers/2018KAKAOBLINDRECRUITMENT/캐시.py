def solution(cacheSize, cities):
    answer = 0
    cache = []

    for city in cities:
        city = city.upper()
        if city not in cache:
            answer += 5
            cache.append(city)
            if len(cache) > cacheSize:
                cache.pop(0)
        else:
            answer += 1
            cache.pop(cache.index(city))
            cache.append(city)

    return answer

# solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])
solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])