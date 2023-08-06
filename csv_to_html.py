import pandas as pd
import sys

if(len(sys.argv) != 2):
    print("usage: csv_to_html.py [filename]")
    exit()

data = pd.read_csv(str(sys.argv[1]), encoding = 'unicode_escape', on_bad_lines='skip')
html = open('default.html').read()

# if you want to adjust the title of the game or the comments of the game, do it here
html = html.replace("insert_game_title_here", "")
html = html.replace("insert_game_comments_here", "")

categories = []
double_categories = []
final_jeopardy = ""

for ind in range(0, 62, 5):
    if(data['round'][ind] == 'jeopardy'):
        categories.append(data['cat'][ind])

    if(data['round'][ind] == 'double'):
        double_categories.append(data['cat'][ind])
    
    if(data['round'][ind] == 'final'):
        final_jeopardy = data['cat'][ind]

iterator = 1
for cat in categories:
    html = html.replace(f"insert_category_{iterator}_here", cat)
    html = html.replace(f"insert_category_{iterator}_comments_here", "")
    iterator += 1

iterator = 1
for cat in double_categories:
    html = html.replace(f"insert_dj_category_{iterator}_here", cat)
    html = html.replace(f"insert_dj_category_{iterator}_comments_here", "")
    iterator += 1

html = html.replace("insert_fj_category_here", final_jeopardy)
html = html.replace("insert_fj_comments_here", "")
iterator = 0
for ind in data.index:
    if data['round'][ind] == 'final':
        html = html.replace(f"insert_fj_clue_here", data['q'][ind])
        html = html.replace(f"insert_fj_answer_here", data['a'][ind])
    if iterator < 30:
        column = data['x'][ind]
        row = data['y'][ind]
        html = html.replace(f"insert_{column}_{row}_clue_here", data['q'][ind])
        html = html.replace(f"insert_{column}_{row}_answer_here", data['a'][ind])
        if data['dd'][ind]:
            html = html.replace(f"{column}_{row}_dd_replacer", '<td class="clue_value_daily_double">DD: $5,000</td>')
    else:
        column = data['x'][ind]
        row = data['y'][ind]
        html = html.replace(f"insert_dj_{column}_{row}_clue_here", data['q'][ind])
        html = html.replace(f"insert_dj_{column}_{row}_answer_here", data['a'][ind])
        if data['dd'][ind]:
            html = html.replace(f"{column}_{row}_dj_dd_replacer", '<td class="clue_value_daily_double">DD: $5,000</td>')
    iterator += 1

f = open("final.html", "w") 
f.write(html)
