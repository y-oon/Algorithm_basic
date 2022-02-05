input_star = int(input())

for star in range(1, input_star+1):
    # space: n-i, star: 2i-1
    print((input_star-star)*" " + (star*2-1)*"*")
