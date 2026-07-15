def kp(n):
    faces = {
        "Tetrahedron" : 4,
        "Cube" : 6,
        "Octahedron" : 8,
        "Dodecahedron" : 12,
        "Icosahedron" : 20
    }

    total = 0
    for _ in range(n):
        a = input()
        total += faces[a]

    print(total)

n = int(input())        
kp(n)