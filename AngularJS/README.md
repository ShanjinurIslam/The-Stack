# Angular JS

A great way to get introduced to AngularJS is to work through ```PhoneCat``` tutorial, which walks you through the construction of an AngularJS web app

The app you will build is a catalog that,

1. Displays a list of Android devices
2. Lets you filter the list to see only devices that interest you
3. View details for any device

## Environment Setup

Clone the angular-phonecat repository located at GitHub by running the following command:
```
git clone --depth=16 https://github.com/angular/angular-phonecat.git
```

Change your current directory to ```angular-phonecat```
```
cd angular-phonecat
```

### Node.js

Check the version of Node.js that you have installed by running the following command:

```
node --version
```

Or, you can download a Node.js installer for your operating system from [title](https://nodejs.org/en/download/)

Once you have Node.js installed on your machine, you can download these dependencies by running:

```bash
npm install
```
This command reads angular-phonecat's package.json file and downloads the following dependencies into the node_modules directory:

1. Http-Server - simple local static web server
2. Karma - unit test runner
3. Protractor - end-to-end (E2E) test runner

Running ```npm install``` will also automatically copy the AngularJS framework and other dependencies necessary for our app to work into the ```app/lib/``` directory.

The project is preconfigured with a number of npm helper scripts to make it easy to run the common tasks that you will need while developing:

1. ```npm start```: Start a local development web server.
2. ```npm test```: Start the Karma unit test runner.
3. ```npm run protractor```: Run the Protractor end-to-end (E2E) tests.
4. ```npm run update-webdriver```: Install the drivers needed by Protractor.

## Running the Development Web Server

The angular-phonecat project is configured with a simple static web server for hosting the application during development. Start the web server by running:

```
npm start
```

This will create a local web server that is listening to port 8000 on your local machine. You can now browse to the application at [title](http://localhost:8000/index.html).

To serve the web app on a different IP address or port, edit the "start" script within ```package.json```. You can use ```-a``` to set the address and ```-p``` to set the port. You also need to update the baseUrl configuration property in ```e2e-test/protractor.conf.js```.


