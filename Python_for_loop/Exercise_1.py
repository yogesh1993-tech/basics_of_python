"""After flipping a coin 10 times you got this result,
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
Using for loop figure out how many times you got heads """

result = ["heads", "tails", "tails", "heads", "tails", "heads", "heads", "tails", "tails", "tails"]
head_count= 0
tails_count =0
for i  in result:
    if i == "heads":
        head_count += 1
    elif  i == "tails":
        tails_count += 1
print(f"Heads Count is = {head_count} and tails count is ={tails_count}")




