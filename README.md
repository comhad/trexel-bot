# Trexel bot archive
The public archive of the Trexel bot engine, a shut down twitter bot. You may use this for your own podcast transcripts of any kind. A word of warning that this engine is incredibly hacky and may not work very well. It has also modified to have all references to Stellar Firma removed from it, but if I missed something, feel free to create an issue for it.

The following is a quick instruction guide, this was done a Fedora 33 virtual machine.

## Quick start guide
1. Git clone this code to it's own directory, install the requirements using `python3 -m pip install -r requirements.txt`.
2. Create a `transcripts/` directory in this folder.
3. Move some transcripts to this folder, provided these transcripts are in plaintext files.
4. [Install NLTK data](https://www.nltk.org/data.html).
5. Using a terminal, cd into the folder and run `sh regenerate.sh`.

After doing this, you'll see some output about what words have been blocked, how many words of each type there are etc.
Once this is done, do `python3 try.py` in the terminal, if done correct, this should generate 10 lines based on the given transcripts.
If you recieve an `IndexError`, try adding more transcripts, the bot doesn't have enough data.

The engine is now functional! You may use this now as it is, or you can use the functionality of the engine for something else.
You can do this by import the engine (`import output`), creating the quote generator object (`quotes = output.generator()`), and generating quotes using the scriptLine function (`quotes.scriptLine()`), this function will return a regular string.

If you wish to add more transcripts to the bot, add them into the transcripts folder and run `sh regenerate.sh` in the terminal again.

[Read my blog post on how the engine works](https://obscure.blog/trexel-bot-shutdown/?mtm_campaign=github&mtm_kwd=trexel-bot-readme).