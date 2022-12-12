with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

sizes = []
class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.subdirs = set()
        self.files = []

    def get_sizes(self):
        global sizes
        mysize = sum(self.files)
        mysize += sum(d.get_sizes() for d in self.subdirs)
        
        sizes.append(mysize)
        return mysize

root = pwd = Dir('/', None)
for line in lines[1:]:
    match line.split():
        case '$', 'cd', '..': pwd = pwd.parent
        case '$', 'cd', child: pwd = next(d for d in pwd.subdirs if d.name == child)
        case '$', 'ls': pass
        case 'dir', name: pwd.subdirs.add(Dir(name, pwd))
        case size, name: pwd.files.append(int(size))

used = root.get_sizes()
TOTAL = 70000000
NEEDED = 30000000
print(sum(s for s in sizes if s < 100000))
print(min(s for s in sizes if TOTAL - used + s >= NEEDED))
