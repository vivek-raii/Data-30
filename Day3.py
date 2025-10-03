students = {
    "Shraddha" : 96,
    "Khushdil" : 94,
    "Divyansh" : 82,
    "Guptang" : 93
}

ans = ""

for i in students:
    if(ans == "" or students[ans] < students[i]):
        ans = i

print("Highest Marks is scored by ",ans)