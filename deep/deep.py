answer = (
    input(
        "What's the Answer to the Great Question of Life, the Universe, and Everything? "
    )
    .lower()
    .strip()
)

if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("YES")
else:
    print("No")
