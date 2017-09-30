# smartTrash
Making your Trashcan Smart :)
Learn how to make your trashcan smart by using sensors and pushing this sensor data to the cloud. It will make a trashcan smart so that it will send you SMS notifications when there is too much trash in it.

Services used in this project:
•	IoTify
•	IBM Bluemix
•	IFTTT
Hardware used in this project:
•	Ultrasonic sensor
•	Raspberry Pi
•	Android Phone
•	Trashcan
 
We will use a service called IOTIFY which will allow us to simulate all the hardware necessary in this project. This will be useful if you don’t currently have access to this hardware and want to try this project out first. We will connect this simulation to Bluemix and allow us to trigger an event in IFTTT which will send an SMS to our phone. If you manage to successfully do all this on IoTify, it should be no problem doing it with actual hardware. 

###### Getting Started with IOTIFY
Since IOTIFY is still in beta stage, I would suggest using this link to register.
 
Once registered, click on the build tab on the top bar and build a Smart Trash project. Setting up and deploying the project will take around 7 minutes or so. And this will start a simulation of the trash can, trash level, temperature and whether the trash can is open or closed.
 
So on the main project screen will be the WebView. This interface allows you to modify the simulation. For example you want to increase the trash level; all you have to do is just move the slider up. The two main interfaces we will be working with will be the WebView as well as the Console. Clicking the Console, will bring up a new Console tab which allows you to access the simulated Pi connected to the hardware simulation. This means that the Pi runs off of the sensor data that is provided by the simulation.
 
The file explorer on the left side shows the file directory of the Raspberry Pi. Above that are 3 icons, from the left; console, webview and settings icons respectively.

###### How does the hardware interact with the software?
So before we actually learn about the software behind this project, we should learn about the hardware we’re using and how they actually interact with each other. For this project we’ll be using the Raspberry Pi, which is essentially a credit card sized computer usually running a version of Debian. And on the Raspberry Pi there are these pins called GPIO Pins (General Purpose Input Output) which are generic pins which can be used as either input or output for the Pi.  

For example, if I wanted to connect an LED to the Pi and I wanted it to blink every 5 seconds, I would take wires and connect the positive end of the LED to a GPIO pin (let’s say GPIO Pin 4) and connect the negative end of the LED to Ground (GND). Then I would write a python script that would specify that the Pi should be in GPIO mode, I would also tell the Pi which pin im using (Pin 4) and tell it that I wanted to use that pin as output (since we are giving an output to make the LED light up).
 

###### Running python scripts on the Pi
So now that we have familiarized ourselves with how the pi works with the sensors, let’s start running python scripts on our simulated pi, which will allow us to use the values from the simulation. First, we’re going to run a script that will detect if the trash can lid is open or closed. After that, we’re going to run a python script which will allow us to detect the distance between the trash and the lid of the trashcan (using an ultrasonic sensor), which will effectively tell us how much trash we have in our trashcan. Here are the 2 scripts:

`(Refer to testscript.py)`

`(Refer to ultra.py)`

First, we’ll start by testing the lid open/close function. Just run the testscript.py file by typing the following in the console:
`sudo python testscript.py`
Now just go back to the webview interface and toggle the lid to open and close. Whenever you toggle the trash bin open, the word “Open” should be printed onto the console.
The next step would be to test the ultrasonic sensor by running the ultra.py script. So go ahead and adjust the garbage level in the webview and run the script using the same command:
`sudo python ultra.py`
You should be able to get an output with readings similar to the garbage level in the webview.
 
###### Connecting it to the cloud
Now that we know that both our scripts work with the simulation, we can connect it to bluemix. Start off by making an IBM Bluemix  account. Next, go to your workspace and click on the plus icon on the top right to start add a new service from the catalog. From the catalog page, select Internet of Things from the categories on the left tab and click on Internet of Things Platform.
 
From there, change your service name and credentials to whatever you like and scroll down. Now select whichever pricing plan you want, in our case we will just use the free plan for testing purposes. Now click on create.
 
After creation, just click on the Manage tab on the top, scroll down and select launch dashboard.
 
This will open a new tab in the web browser and take us to the IoT dashboard where we can access and manage our devices. From the tab on the left, select devices and click on “+ Add Device” on the right side of the screen.
 
If this is your first device you are adding, you will have to make a new device type for it, so click on Create device type and it will give you 2 type options, gateway or device. Just select create device type.  For the name, just put whatever you want to call this type of device. In our case, we can put something like SmartTrashCan. From there just keep clicking next until it takes you back to the Add Device panel where you can now select your new device type. Select it and press next on the bottom right.
 
It will now prompt you for your device id, where you can enter a unique name for your device,  people usually use their device mac address in this case but you can typically use anything to identify your device. In our case lets’ just enter “iotifysim1”. After entering your device id, just continue pressing next and finally press Add. It will add your device and provide you with device credentials. I recommend that you copy these credentials onto a separate text file and keep it for future reference as it contains your authentication token which will only be generated once. We will also need these details to connect our pi to bluemix.
 
Now that we have our credentials, we can finally connect our simulated pi to bluemix and send data from the ultrasonic sensor.
Sending sensor data to Bluemix
Now go back to Iotify and create a new file on your raspberry pi called ultraBluemix.py
Here is the script to connect to bluemix.

`(Refer to ultraBluemix.py)`

###### NOTE: Make sure to replace the text in the highlighted areas to the matching information from your bluemix device credentials.
Before we actually run this script, we will need to install the ibm libraries required by the script so go ahead and type this command in the console:
`sudo pip install ibmiotf`
This will install all the required libraries for the python script. Please note that it can take some time. After the installation is complete, we can run the python script using sudo python ultraBlumix.py in the console. The script should run and give the following output.
 
We can now go back to the IBM IoT dashboard and check our sensor data by clicking our device. We should see the sensor data from the Sensor Information section by scrolling down.
 
Click on your device from the dashboard and scroll down to Sensor Information.
 
Now that we have our sensor information, we can use it to trigger a message to be sent using IFTTT. 

###### Setting up IFTTT
Go to IFTTT and make an account. After that, go through the whole introduction until it allows you to “Create a Recipe”. Click on Create A Recipe and for the “this” part of the recipe, search for and select Maker.
 
Select the “Receive a web request” option.
 
Next enter a descriptive event name and create the trigger.
 
Next select “that” and choose the action channel Android SMS. You may need to set up android SMS with your phone number.
 
Choose the action Send an SMS. Next, enter your phone number and a custom message and click Create Action. Finally click on Create Recipe.
Next click on channels on the top bar and search for Maker.
 
 
Scroll down and select Maker. Copy the api key provided on the next page.
 
Setting up rules and actions on Bluemix
Next go back to the IoT dashboard and select manage schemas from the bar under Devices.
 
Next click on Add Schema on the top right and choose your device type for the name field.
 
Click on next and then “Add a property”. Make sure your python script is running from the console and it is sending sensor values. Then click on From Connected on the top and wait for a bit for values to appear. When they appear, select them both and press Ok and make sure to press Finish to add the schema.
 
Next, select rules from the left menu. And create a new Cloud Rule from the top. 
 
 
Enter a new for your rule and select the device type it applies to.
 
Next select the Condition, change the property to distance under “d” and select the less than operator and change the value to 42. This condition will be met every time the distance is below 42 cm which means that the trash level is high. Next we need to make an action when this condition is met. Select new action on the right and press add action.
 
 
Enter an informative name and change the Type to IFTTT. Press next and enter your Maker API Key in the Key field. Enter your Maker Event name matching the one you set up in your IFTTT recipe. Finally press finish. Select your new action from the menu and press ok.
 Next select the “Trigger every time conditions are met.” option and select the following option.
 
This will make it so that we only get a message the first time our garbage can is full and are not constantly spammed with messages until we empty the trash can. Press Ok and save and activate the rule from the top right buttons. We should now run the script from the console and adjust the garbage level so that the distance is less than 42 cm. This should trigger the condition and we should receive an SMS from IFTTT!

######Conclusion
Now that we have successfully sent our ultrasonic sensor data from our simulated pi, it should be no problem setting it up with physical hardware. All the scripts should run in the same way on a physical Pi. 
