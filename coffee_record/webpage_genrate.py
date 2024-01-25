# Get user's name and description
name = input("Enter your name: ")
description = input("Describe yourself: ")

# Create HTML content
html_content = f"""\
<html>
<head>
</head>
<body>
<center>
<h1>{name}</h1>
</center>
<hr />
{description}
<hr />
</body>
</html>
"""

# Write HTML content to a file
with open("mypage.html", "w") as f:
    f.write(html_content)

print("Web page created successfully!")