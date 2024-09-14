vector = {"ids":[[1,2,3,0], [1,2,3,0]]}

vector["ids"][vector["ids"] == 0] = -100

print(vector)