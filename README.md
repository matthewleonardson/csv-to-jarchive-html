<h1>About</h1>
This is a simple python script that takes a .csv file and converts it to an .html file that is equivalent to J!Archive's html.
<br></br>
This was a hihgly personalized script written to interact with two existing repos, and because of that, it's not particularly well written. <a href="https://github.com/howardchung/jeopardy">Jeopardy</a> by Howard Chung uses a .csv file to import custom games, 
but <a href="https://github.com/theGrue/jeopardy">Jeopardy</a> by Josh Gruenberg uses .html files from J!Archive for their games. I already had scripts written to create my custom games in .csv format,
but I wanted to migrate to using the latter project.

<h1>default.html</h1>
Included in this repository is default.html. It contains a barebones version of the .html format that J!Archive uses and that Josh's Jeopardy app will properly parse. It contains "replacement" text across the file that is 
obvious to notice. The only unintuitive part is the "Daily Doubles". To mark a question as Daily Double, you have to replace "{column}_{row}_dj_dd_replacer" with "&lttd class="clue_value_daily_double">DD&lt/td>".

<h1>Getting it to work with Josh Gruenberg's Jeopardy</h1>
Josh's Jeopardy app interfaces directly with J!Archive, with no option for custom games. However, if you have an .html file you'd like to use, I reccomend the following process.
<br></br>
In the <a href="https://github.com/theGrue/jeopardy">Jeopardy</a> repo, in the routes/api.js file, replace line 89 with the following line:
<br></br>
<b>fs.readFile(YOUR_PATH_HERE, 'utf8', function(error, html) {</b>
<br></br>
Where YOUR_PATH_HERE is the path to the .html file.

