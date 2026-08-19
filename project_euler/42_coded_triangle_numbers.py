import urllib.request

def coded_triangle_numbers():
    count = 0
    triangle_nums = set()
    for i in range(1000):
        triangle_nums.add(i / 2 * (i + 1))
    with urllib.request.urlopen("https://projecteuler.net/resources/documents/0042_words.txt") as response:
        text_content = response.read().decode('utf-8')
        lines = [l.replace('"', "") for l in text_content.split(",")]
        for line in lines:
            word_value = sum([ord(i) - 64 for i in line])
            if word_value in triangle_nums: count += 1
    return count


print(coded_triangle_numbers())
