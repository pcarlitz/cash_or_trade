# cash_or_trade
Script to scrape cash or trade phish tickets and email me with results

The cot.py script will scrape data from the first page of phish tickets that are being sold on cashortrade.org. It uses beautiful soup to parse the html and then pulls in the review body, the link to the webpage, and a flag for whether or not the tickets are currently available.

The script then limits to only tickets with status = 'BUY NOW' and sends an email from a gmail account.

The schedule_cron.py script can be used to schedule this script to run every 30 minutes. Note that some machines may have trouble finding beautifulsoup.  I included a text file explaining terminal commands that should allow your system to find the package. These instructions are in cron_scheduler/terminal_commands.txt.

The email looks like the result.png file in this repo.
