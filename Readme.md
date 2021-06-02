*/Steps To Install*

Install slackclient
Install python-dotenv

Add Slack Token in .env file

Python Code:

Install flask
Install slackeventsapi
 
Pytton Code Changes:

DEFAULT PORT NUM - 5000

NGROK Setup:

--Double CLick NGROK APP
--Once the CMD Window is open, run the command
-- ngrok http DeafultPortNum
        Ex: ngrok http 5000

This Link will Open - http://3ecaf03f006f.ngrok.io (This Enables traffic to forward to locoalhost 5000 port)

Once this done:

You need to update the url in Slack App.
Update the scope for channels.messages.
Reinstall App.


