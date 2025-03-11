names = ["Mayowa", "chizoba", "Chigozie"]

final_output = []

for name in names:
    if name.istitle():
        if name.endswith("a"):
            final_output.append(name)
        else:
            # Replace the last letter of said name with a
            new_name = name[:-1] + "a"
            final_output.append(new_name)

print(final_output)
            
        