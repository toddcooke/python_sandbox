import urllib.request


def names_scores():
    with open("/tmp/project_euler_22.txt", "a+") as f:
        f.seek(0)
        content = f.read()
        if len(content) == 0:
            with urllib.request.urlopen("https://projecteuler.net/resources/documents/0022_names.txt") as response:
                text_content = response.read().decode('utf-8')
                f.write(text_content)
        names = sorted([i.replace('"', "") for i in content.split(',')])
        print(names)
        total = 0
        for i, name in enumerate(names):
            nametotal = 0
            for c in name:
                nametotal += ord(c) - 64
            total += nametotal * (i + 1)
        return total


print(names_scores())
