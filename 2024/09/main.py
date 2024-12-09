with open('real.in', 'r') as f:
    lines = f.read().strip().splitlines()

l = [int(x) for x in lines[0]]

sizes = [x for i,x in enumerate(l) if i % 2 == 0]
free = [x for i,x in enumerate(l) if i % 2 == 1]

def move_blocks(sizes, free):
    file_id = len(sizes) - 1
    checksum, idx = 0, 0
    for free_id,free_size in enumerate(free):
        if file_id < free_id:
            break
        for _ in range(sizes[free_id]):
            checksum += idx * free_id
            idx += 1
        while free_size > 0:
            for _ in range(min(sizes[file_id], free_size)):
                checksum += idx * file_id
                idx += 1
            if sizes[file_id] > free_size:
                sizes[file_id] -= free_size
                free_size = 0
            else:
                free_size -= sizes[file_id]
                file_id -= 1
    return checksum

def move_file(sizes, free):
    free_og = free.copy()
    moved = []
    checksum = 0
    for size_id,size in reversed(list(enumerate(sizes))):
        for free_id,free_size in enumerate(free):
            if free_id >= size_id:
                break
            if size <= free_size:
                free[free_id] -= size
                free[size_id-1] += size
                start = sum(free_og[:free_id]) + \
                        sum(sizes[:free_id+1]) + \
                        sum(sizes[s] for f,s in moved if f == free_id)
                for x in range(start, start+size):
                    checksum += x * size_id
                moved.append(((free_id), size_id))
                break
    
    for i,n in enumerate(sizes):
        if any(s == i for _,s in moved):
            continue
        start = sum(free_og[:i]) + sum(sizes[:i])
        for x in range(start, start+n):
            checksum += x * i
    return checksum

print(move_blocks(sizes.copy(), free.copy()))
print(move_file(sizes, free))
