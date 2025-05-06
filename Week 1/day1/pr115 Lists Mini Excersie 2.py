# .strip() input
name = input("Enter your full name, extra space and not title case: ")

# Without .strip()
print("Without strip:", name)

# With .strip()
print("With strip:", name.strip())

# .title() input With .strip()
title_name = name.strip()

# With .title()
print("With title:", title_name.title())
