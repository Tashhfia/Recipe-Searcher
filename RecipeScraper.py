from bs4 import BeautifulSoup


my_file = open("recipe_links.txt", "r")
content = my_file.read()
print(content)

data_into_list = content.split("\n")
print(len(data_into_list))
my_file.close()