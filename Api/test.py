import os
# How to parse markdown 101
with open("test.md", "r") as f:
    tournaments=[x for x in f.read().split("\n") if len(x)>3 and x[:3]=='| [']
    os.remove("test_result.txt")
    for item in tournaments:
        item=item.split("](")
        tournament_name=item[0][3:]
        tournament_tag=item[1][:item[1].find(")")]
        with open("test_result.txt", "a") as output:
            output.write(tournament_name +": " + tournament_tag+"\n")