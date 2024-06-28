# | HydroAlert |

#### Rasmus Jildholt (rj222rz) ------ 2024-06-28 ------


## Stepping into the world of hydration with HyrdoAlert!
The **HydroAlert** is a small scale IoT project that helps make sure that people that lose track of time (me for example) stays hydrated in the warm summer heat. Basically it's a *Raspberry Pi Pico W* hooked up to a temperature and humidity sensor combined with a red LED to make a primitive, but effective, way to make sure that I take regular breaks to go and fetch water to stay hydrated.

If you feel inclined to spend roughly 2-3 hours on a small project and if you have the necessary components available then the **HydroAlert** might be something you could be willing to build with the following tutorial! If not you can just skim trough it to judge how simple it is, i am a beginner in IoT after all. 
## The objective behind | HydroAlert |

#### Why did I make this?
I have a few reasons as for why i built the **HydroAlert**, the main thing is that i just moved into a new appartment, and it has two windows aimed directly at the sun for a majority of the day. Ontop of this I am unable to create a draft, making my student apartment into a (hopefully) unintentional heatsink... 
My appartment is usually 3-4 degrees celsius warmer than it is outside, and getting the warmth out, even during the night, is very difficult. This means that i sweat alot, and i am constantly in a mild agony due to the high heat. Therfore i decided to use the limited components i had at my disposal to create something that is actually useful to me, by giving me a reminder to drink water at constant intervals. 

Other reasons as to why i built this thing is because i had bought a LoRaWAN antenna before starting my IoT course, but it didn't cover my area due to how thick my walls are, otherwise i had intended to make use of that. I simply had to make something that connects to my PC with a USB cable and so i decided to make something quite practical. 

#### What Purpose Does It Serve
As the name implies, **HydroAlert** gives of a visible signal using a bright LED to remind me to drink a bit of water when im infront of the computer. The main reason as to why i even need this is because i can become engrossed in what im doing at my desk, be it playing games or studying, and that means that i might not realise how hot it is here. Giving myself a reminder every 30 minutes means im allways topped up on water and staying healthy despite the heat. 

#### Data display on Ubidots Dashboard
In my current build I have my MCU (Micro Controller Unit) connected to a Dashboard on [Ubidots](https://ubidots.com/), which is a website desinged to display raw data on different graphs and widgets. I don't have many practical reasons as to why i have it displayed there, but it does give me the oppurtunity to see a timeline graph of the temperature in my room over the course of a couple hours/days depending on how long i have the **HydroAlert** on. 

If a large amount of people had IoT devices like temperature measurers then maybe we would be able to piece together large data structures to see which apartments/ buildings could benefit from AC units or better access to shade , instead of for example installing cooling units on all apartments in an apartment block. 
![HydroAlert](https://hackmd.io/_uploads/B1onwd2U0.png)
Notice that the timeline dips to 21 degrees briefly, this is due to me using ice to lower the temp to see if the LED would stop blinking under 25 degrees


## Materials necessary for the | HydroAlert |


| Name                                        | Link                                                                                 | Cost    | Usage | Image                                                                                    |
| ------------------------------------------- | ------------------------------------------------------------------------------------ | --- | ----- | ---------------------------------------------------------------------------------------- |
| 1x Raspberry Pi Pico WH                     | [Electrokit.com](https://www.electrokit.com/raspberry-pi-pico-wh)                    | 109 SEK    | The main MCU that uses Python code to make sure the whole **HydroAlert** system works.       | ![700x700-product_41019_41019114_PICO-WH-HERO](https://hackmd.io/_uploads/ByX4hd2UC.jpg) |
| 1x Breadboard                               | [Eletrokit.com](https://www.electrokit.com/kopplingsdack-840-anslutningar)           |  69 SEK   |  The breadboard makes connecting the sensor and LED easier without having to solder/tape wires.     | ![10160840](https://hackmd.io/_uploads/BJFp3dhIR.jpg)                                    |
| USB-cable A-male - micro B 5p male 1.8m     | [Elektrokit.com](https://www.electrokit.com/usb-kabel-a-hane-micro-b-5p-hane-1.8m)   |  39 SEK   | USB cable necessary to connect MCU with PC.      | ![700x700-quick_54_1f_9382_41003290](https://hackmd.io/_uploads/S1pUaO3U0.png)           |
| 1x Wires 30cm male/male (Only 5 are needed) | [Electrokit.com](https://www.electrokit.com/labbsladd-40-pin-30cm-hane/hane)         |    49 SEK | The cables are used to connect the MCU with the sensor and LED.      | ![700x700-product_41012_41012684_41012684](https://hackmd.io/_uploads/SJyhpO3LA.jpg)     |
| 1x LED 5mm (Color is irrelevant)            | [Electrokit.com](https://www.electrokit.com/led-5mm-rod-diffus-1500mcd)              | 5 SEK    |  Reminder that is visible with a bright LED.     | ![40300051](https://hackmd.io/_uploads/SyHmAu3LA.jpg)                                    |
| 1x DHT11 Temperature and moisture sensor    | [Electrokit.com](https://www.electrokit.com/digital-temperatur-och-fuktsensor-dht11) |   49 SEK  |  Measures the temp in the room.     | ![41015728](https://hackmd.io/_uploads/rkyGJKn8R.jpg)                                    |


## Computer Setup
I've completed this project using a standard *Windows 10* OS in order to use the software necessary, but the same process should be possible on other operating systems like *Macintosh* etc.  Below are the steps necessary for setting up the correct dev  enviroment. From code editor to flashing of MCU.
#### 1:  Visual Studio Code

I used [Visual Studio Code](https://code.visualstudio.com/) as my IDE (integrated development environment), but you can use any sort of code editor, but it makes things alot easier to use VSC, along with the fact that you can use this as a more acurate tutorial if you follow it step by step. There are tons of tutorials on how to use VSC if you already haven't, but I used [this tutorial](https://hackmd.io/@lnu-iot/rkiTJj8O9) from the course page. 

#### 2: Necessary plugins to VSC 
In the [previously linked tutorial](https://hackmd.io/@lnu-iot/rkiTJj8O9) tutorial, it already mentions the extra plugins used in my process of setting up the code. That is [node.js](https://nodejs.org/en) and [PyMakr](https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr), in order to easily edit the code in the MCU and have greater control over the execution of said code. It's easier to download the PyMakr plugin in VSC than trough the link, but choose whichever is more suitable for you. 


#### 3: How the Code is uploaded to the MCU
The steps necessary for flashing an MCU is quite easy. First, you will need to download the latest firmware from the [official MicroPython webbsite](https://micropython.org/download/RPI_PICO_W/) in order for it to run properly. Connect the USB to the MCU, not the PC, make sure the two tiny pins are facing up so that it locks nicely into place. It won't go all the way in, and if you ever feel like removing it you need to apply a little bit of pressure to remove it from the MCU, but do this **carefully**. There will be a small white button labeled *BOOTSEL*, hold this button in whilst connecting the MCU to your PC. Release the button when a new drive is availible, copy the downloaded drivers into RPI-RP2, the board will then be ready for use. This can be tested by removing and connecting the USB cable. The MCU should then be visible as a device under the PyMakr plugin in VSC. Connect the device and create a terminal to test if it works by using the `print("test")` statement. I used [this tutorial](https://hackmd.io/@lnu-iot/rkFw7gao_#Visual-Studio-Code) in order to set my system up.

### Putting Everything Together
Due to the fact that this is a very simple project, it requires no knowledge of ressistors or that sort, it's all about connecting the wires so that they add up with the provided python code down below. I tried my best to visualise how my setup is made, but due to software restrictions i could not get a propper visualisation with the correct components. This setup is very much made for estetic reasons and could be used with less recources, like only using 3 wires for example. Therfore it is not suitable for any sort of large scale production.

#### Circuit Diagram
This circut diagram uses an *Arduino Nano (Rev3.0)* and a *LM35 Temperature Sensor* because i couldn't get access to the actuall *Raspberry Pi Pico WH* and *DHT11*, but it uses the same setup with the wires. You should therfore connect the pins to the MCU acording to this text and not the image, as it may not represent the MCU correctly. 
![Skärmbild 2024-06-28 232217](https://hackmd.io/_uploads/SJh5FsnIA.png)
On the *Raspberry Pi Pico WH* and *DHT11* there are pins that are numbered from 1 to 40 (shown below), this means that you should make sure that the wires are correctly added acording to these pins and not the number of pins on the image. For the *DHT11 sensor*, make sure that the blue wire is in the 38th pin on the right side of the board. This should connect to the left side of the sensor leg. The red wire should be on the 36th pin, and be connected to the ground in the middle. The black wire should be connected to the 32nd pin, and connect to the right leg. The LED light doesn't necessarily need wires, but i used them in order to place the light as far away on the components, as i only want the light visible in the front, so it's purely estetic. When connecting the LED, it's important that the 1 and 3 pin is connected, this means that power and ground can turn on the LED without problems.
![pico_pinout](https://hackmd.io/_uploads/rJzM6o28A.png)
[Link to image source](https://www.google.com/url?sa=i&url=https%3A%2F%2Fdocs.micropython.org%2Fen%2Flatest%2Frp2%2Fquickref.html&psig=AOvVaw0YS1stDm02GHQClrH3wqFZ&ust=1719697000572000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCKjC3tmg_4YDFQAAAAAdAAAAABAE)

## Ubidots, a simple yet effective visualisation tool
Ubidots is the *platform* i decided to stick with. This was after a long, and very unecessary, atempt at using TIG Stacks, which is something far beyond my comprehension. Ubidots works using an API token that is generated for each user to easily connect using a wifi network in order to send raw data to a dashboard, which can then display said info on different widgets and graphs that are customizable to an extent. It's also free, which is a huge plus for a student like me. 
#### Platform Details
[Ubidots](https://ubidots.com/) is a cloud-based platform, meaning that the data I have saved there could be revoked, used or changed without much of my input. This means it could potentially be inconsistent and unreliable, however, it also means I don't need to set up the database myself. It also means that they are able to store all the data without me needing to use any local storage. This is however fitting for my personal IoT project, seaing that I don't have much necessity of the data stored, and the fact that the main gimmick of the **HydroAlert** is the physical indication, and not necessarily the storage and usage of the temperature statistics. 

If it was however needed to be implemented into other bigger projects, and therefore scaled up, then there would be quite a few changes. For example a local storage to guarantee safety of stored data combined with a better visualisation of said data using more advanced graphs and potentially tables to order and display all the data. Temperature fluctuates constantly and my setup sends data every 30 minutes, this means that if you scaled it up into a bunch of places, and potentially shortened the duration to live updates, it would required way more advanced methods of both storage and handling of data to create a reasonable implementation of this specific IoT project.

If you desire to set up your own Ubidots dashboard similar to mine, the [this tutorial](https://hackmd.io/@lnu-iot/r1k63jjwo) is the one i used.

## The Code
How is the data transmitted to the internet or local server? Describe the package format. All the different steps that are needed in getting the data to your end-point. Explain both the code and choice of wireless protocols.



## Transmitting the data / connectivity
How is the data transmitted to the internet or local server? Describe the package format. All the different steps that are needed in getting the data to your end-point. Explain both the code and choice of wireless protocols.
#### How often is the data sent?
#### Which wireless protocols did you use (WiFi, LoRa, etc …)?
#### Which transport protocols were used (MQTT, webhook, etc …)

## Presenting the data
Describe the presentation part. How is the dashboard built? How long is the data preserved in the database?
#### Provide visual examples on how the dashboard looks. Pictures needed.
#### How often is data saved in the database.

## Putting Everything Together
Show the final results of your project. Give your final thoughts on how you think the project went. What could have been done in an other way, or even better? Pictures are nice!
#### Show final results of the project
#### Pictures
