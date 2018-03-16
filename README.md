# custom-mailmerger

## Purpose:
To give you the freedom to send personalized mass emails the way you want

## Developer Notes:
**config/**
 1. email\_list.csv 
 	- List of recipients for your email.
	- Follows the format of *First\_Name*, *Last\_Name*, *email*
		- only *email* is required, other fields can be used and created as needed
	- Will be used during email creation, to fill in target email address and other custom placeholder variables in emailbody template

 2. secrets.txt
	- Contains the credentials and account name of your email account
	- Will be used to log into the server to send the emails
	- NOTE please dont push your account secrets on github

**attachments/**
- Place all your attachement that should be sent out with your email in here
- WIP
	- [ ] configure to send all files in this directory
	- [ ] remove successfully sent attachments after completion of a run

**emailtext.html**
 - The template for your email body
 - Use placeholders like *{varName}* to fill in with information later
 - Consolidates info from email\_list.csv to send personalize the email
 - Uses HTML tags -> use the browser to view the final formating of the template

## Dependencies:
 1. python3


## Execution
 1. Update config files with correct information
 2. Update emailtext.html to new email template format
 3. Ensure you have active internet connection	
 4. ```	python3 emailmerge.py```
