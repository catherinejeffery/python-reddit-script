# python-reddit-script
A script that allows you to pull content using the Reddit API, respecting the tree structure of comment threads.

This script can be used on a link to a Reddit post to produce a plain text (.txt) document that includes the post and the discussion thread. It uses the Python Reddit API Wrapper (PRAW).

To use this script, you’ll need to register to access Reddit’s API. In the script, there are notations to show you where you’ll need to enter your authentication information in order to be able to use the API. Make sure to look through the script and add in this information where necessary.

All you have to do is navigate to a Reddit post and copy the URL. When the script runs, it will prompt you twice in the shell. First, it returns a prompt asking for the URL, which you can paste in. Second, it returns a prompt asking you to name the file. Make sure to manually add in the .txt at the end so it produces a plain text document. These prompts are a limitation to how scalable the script can be: it still takes a bit of time as you have to get to the post you want and do the file naming.

Another key limitation with the script is that on especially long discussion threads, it simply cannot collect all the comments and replies without taking an absurd amount of time. There is a section of the code that allows you to set how many ‘read more’ or ‘continue this thread’ buttons you want Python to open. I had this set at 5 for my project and found that this helped ensure that everything would be scraped pretty quickly (within a few seconds), but you may want to change that if you have more computational power or are needing a perfectly thorough collecting procedure.
