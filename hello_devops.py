import os

print("Hello, DevOps!")
print("Files in the current directory:")
for file in os.listdir('.'):
    print(f"- {file}")

