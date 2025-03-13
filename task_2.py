attrs = ["first name", "last_name", "date of birth"]

transformed_attrs = []

# help(str)

for attr in attrs:
    transformed_attr = attr.replace(" ", "_")
    transformed_attrs.append(transformed_attr)

print(transformed_attrs)