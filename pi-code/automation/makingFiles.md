To schedule our script to be executed, we need to enter the crontab scheduling expression into the crontab file. To do that, simply enter the following in the terminal:

crontab -e

You might be prompted to select an editor, choose nano and append the following line to the end of the opened crontab file:

*/5 * * * * /home/$(USER)/my_script.py
