# String Advanced Methods

text = "python programming"

# ---------------- Slicing ----------------
print("Full text:", text)

print("First 6 chars:", text[0:6])
print("From index 7:", text[7:])
print("Last 3 chars:", text[-3:])
print("Reverse:", text[::-1])


# ---------------- Find ----------------
print("Find 'pro':", text.find("pro"))
print("Find 'xyz':", text.find("xyz"))


# ---------------- Replace ----------------
new_text = text.replace("python", "java")
print("Replaced text:", new_text)
