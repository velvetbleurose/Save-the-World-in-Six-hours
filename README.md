# Save-the-World-in-Six-hours
Web app for substance abuse and mental health assistance

Save the World in Six hours (SWISH) is a web application that is designed to assist those who are battling through substance abuse and mental health. We keep it simple: it's a daily diary that takes about 5-10 minutes to fill out. You can do this at any time of the day. Here's the catch: the person who registers is one who is committing to updating this diary on a daily basis. This means that you must update it within 24 hours of your last entry. The reason being that this is tailored to those who are truly committed to bettering their situation. SWISH is different in that you have an accountability partner. When you register, you enter the name and number of this partner. If for some reason you don't update your diary within 24 hours of your last update or there seems to be a negative trend in your responses, SWISH automatically sends a text message to the person to let them know to check in on you. Thus, this should be someone who you feel comfortable sharing your state with. SWISH **NEVER** sends your actual responses to your partner. It simply sends a general response partially tailored to your state. For example, if you have not been eating well for a few days it will send a message that sounds a bit like: "Hey, ____ hasn't been eating well the last few days. You should reach out and maybe grab a meal!" 

With this, our goal is that you will feel like you're not alone in this process. 

## SET-UP ##

The Python based web application runs locally. It uses MongoDB to store the information from the website. The following libraries are required: *flask_login* and *pymongo*. Both can be installed using pip, Pythons package manager. For Mac, these instructions assume you have Homebrew installed, MAC's package manager. If you do not have it installed follow [these instructions](https://brew.sh).

### For MAC/Linux ###

1. Clone this repository. 

2. If you do not have MongoDB and are a MAC user, you can follow [these instructions](https://ademirgabardo.wordpress.com/2016/02/02/installing-and-running-mongodb-on-mac-osx-for-beginners/) to install it. If you are running Linux, [these instructions](https://docs.mongodb.com/v3.0/administration/install-on-linux/) should help. 

3. If you do not have pip, depending on your environment: 

  `brew install pip`

or 

  `sudo apt-get install python-pip`

4. Install the necessary dependencies to run the code

  `pip install flask_login pymongo`

5. Once installed, start up MongoDB. In one terminal window, type **mongod** or **sudo mongod** (if there's an issue with permissions). The last output should be **waiting for connections on port XXXXX**. In another terminal window, go to where the cloned repository is. From the flaskr folder, run

  `python app.py` 

The website will be running on that link

## HOW TO USE ##

1. If you don't already have an account, register with a username and password. In addition, you will enter the name and the number of your accountability partner. 

2. Once you register, click on the *Login* tab at the top of the page to login

3. Click on *Daily Diary* at the top of the page to update your daily diary. 

4. Once you're finished, submit! 


