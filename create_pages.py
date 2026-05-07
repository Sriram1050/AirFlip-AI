for i in range(1, 101):
    with open(f"pages/page{i}.html", "w") as f:
        f.write(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Page {i}</title>
</head>
<body>
    <h1>Welcome to Page {i}</h1>
</body>

</html>
""")
print("100 pages created")