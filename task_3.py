names = ["Mayowa", "chizoba", "Chigozie"]

final_output = []

for name in names:
    # We only need names written in Title case
    if name.istitle():
        if name.endswith("a"):
            final_output.append(name)
        else:
            new_name = name[:-1] + "a"
            final_output.append(new_name)

print(final_output)