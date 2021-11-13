
print('Template Title Information: ')

ctfname = input('Enter the ctf name: ')
challname = input('Enter the challenge name: ')
year = (int(input('Enter the year: ')))


print('\n\nChallenge Information Table: ')
print('-----------------------------')
category = input('Enter the challenge category: ')
diff = input('Enter the challenge difficulty: ')
pts = input('Enter the challenge points: ')
dev = input('Enter the challenge developer name: ')
print('\n-----------------------------')
flag = input('Enter the flag: ')

print('Saved, output file: scriptOutput.md')

temp = f"""
   
# Writeup for the challenge **_`{challname}`_** from {ctfname} {year}
----

- ## Challenge Information:

| Name        | Category   | Difficulty | Points | Dev |
|-------------|------------|------------|--------|-----|
| {challname} | {category} | {diff}     |{pts}pts|{dev}|

----

# Description: 

----

# Solution:

## Flag: **`{flag}`** 
"""

with open('scriptOutput.md', 'w') as f:
    f.write(temp)
