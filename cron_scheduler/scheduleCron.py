from crontab import CronTab

def main():
	from crontab import CronTab

	cron=CronTab(user='{}') #insert your username
	job=cron.new(command='python /path/to/script/cot.py') #insert path to cot.py script

	job.minute.every(30) #job will run every 30 minutes.
	cron.write()
	job.enable()

if __name__ == "__main__":
	main()
