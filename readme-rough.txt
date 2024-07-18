
Project into manageable steps and tasks:
(Daily motivational quotes
serverless Email Automation) 

	save the quotes.json file to the s3 bucket

	make a serverless project 
		commands: serverless

		select python starter api or python flask wih dynamo
		python 3.12
		open it in vs code : code .

	now project is opened in vs code

	make a folder named handler 
	>> make py files into it as 
		getQuotes.py  ( used to fetch the json(quotes) form the quotes.json file stored in s3 and render it via Api gateway)

		subscribeUser.py (make a api (Api gateway) using which we can add subcribers/members to our Daily qoutes providing service , so this api will help the subcribers to register and also save the data to the Dynamo-db table (user-table))

		getSubscribers.py (this api to get the member details added to the service/bd by subscribeUser-api )

		intially make these three api files 
		make changes to the serveless.yml file accordingly

		test it by running serverless deploy --verbose
			 GET - https://5euy8efewfeeded6sr2l.execute-api.us-east-1.amazonaws.com/dev/quotes
	  		POST - https://5euy8fffewfdedede6sr2l.execute-api.us-east-1.amazonaws.com/dev/subscribe
	  		GET - https://5euy86fddwdefdvdwdwvsr2l.execute-api.us-east-1.amazonaws.com/dev/subscribers
	  	should get this api link after deploy

		If everything looks good
			make file staticMailer.py in handler folder
	       (Api for sending email notification using aws-sns to the owner or websiter(notifing who regitered))

			make changes to the serveless.yml file accordingly
			test it by running serverless deploy --verbose

			after sucessful running , should get an confirmation-email about sns for the owner's email. 
			confirm email >> get arn and add it to the serveless.yml
			again run serverless deploy --verbose
			test the api 
			 POST - https://5euy8rffrffeedwdfef6sr2l.execute-api.us-east-1.amazonaws.com/dev/mailer
			 via postman
			 	sample json:
			 	{
		    "email":"amishkhatu44@gmail.com",
		    "name":"amish",
		    "message":"hey i m here..."
				}

			the owner should receive an email by SNS.

		At last sending scheduled email to the user sevice
		make a sendEmail.py in handler folder

		-- write a python code to send emails via send-grid platform 
		-- make a send grid account , do all the verification process by connecting to there support team. 
		-- once account oppened 
			go to email-api >> integration guide >> Choose a setup method (web Api) >> choose the language python >> create a api-key 
			or goto settings >> api-keys >> create api key 
			>> give name >> select full access>> create now
			>> copy that key can put it in the serverless.yml as environment variable


		-- similarly add code for the service in the file 
			sendEmail.py 
			for this to work we need to add layers to lambda service named (sendgrid layer / requests layer)
			to make layer follow the steps:

				>> make a empty folder : lambda-layer

				>> cd lambda-layer

				>> pip install requests -t python/lib/python3.12/site-packages/ 
				or
				>> pip install sendgrid -t python/lib/python3.12/site-packages/    


				folder structure:

				base folder : lambda-layer
					- request_layer.zip ( starts from python/lib/python3.12/site-packages/*)
					- python actual folder  ( starts from python/lib/python3.12/site-packages/*)

				go to lambda layers create layer upload the zip file and get the arn , add the arns to the serverless.yml

				test it by running serverless deploy --verbose

				once ran we should get :
				POST - https://5euy86sr2l.execute-api.us-east-1.amazonaws.com/dev/sendEmail
				this link
				go to api-gateway ui and just test it.
				all the subscribers emailids should receive the emails of random quotes.

				Atlast just add the cron-job operation to the serverless.yml so users can receive emails on the scheduled time.

			run-it check the sendEmail lambda function on aws ui check for the cloudwatch-event-trigers
			we should see the daily schedules and should receive the emails at the scheduled time.


	Once this backend is done,

	Just make a simple front-end using next-js

	make folder front-ent at the root-level
	>> mkdir quotes-site
	>>npm install axios

	>>npm install next@14.2.5 react@18.2.0 react-dom@18.2.0 --force

	 >> npx create-next-app quotes-site --use-npm --example "https://github.com/vercel/next-learn/tree/1011f2f19fc821f09d2ec685e42229d0826fca71/basics/learn-starter"
	 this will download the starter template fromm this github repo, Or u can directly take my github repo code for the same.

	 >> Run : npm run dev
	 A front-end shoud start at localhost:3000
	  ▲ Next.js 14.2.5
	  - Local:        http://localhost:3000

	  use this front-end for the demo purpose






	