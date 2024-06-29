# | HydroAlert |

#### Rasmus Jildholt (rj222rz) ------ 2024-06-28 ------


## Stepping into the world of hydration with HydroAlert!
The **HydroAlert** is a small scale IoT project that helps make sure that people that lose track of time (me for example) stays hydrated in the warm summer heat. Basically it's a *Raspberry Pi Pico W* hooked up to a temperature and humidity sensor combined with a red LED to make a primitive, but effective, way to make sure that I take regular breaks to go and fetch water to stay hydrated.

If you feel inclined to spend roughly 2-3 hours on a small project and if you have the necessary components available then the **HydroAlert** might be something you could be willing to build with the following tutorial! If not you can just skim through it to judge how simple it is, I am a beginner in IoT after all. 
## The objective behind | HydroAlert |

#### Why did I make this?
I have a few reasons as for why I built the **HydroAlert**, the main thing is that I just moved into a new apartment, and it has two windows aimed directly at the sun for a majority of the day. On top of this I am unable to create a draft, making my student apartment into a (hopefully) unintentional heatsink... 

My apartment is usually 3-4 degrees celsius warmer than it is outside, and getting the warmth out, even during the night, is very difficult. This means that I sweat a lot, and I am constantly in a mild agony due to the high heat. Therefore I decided to use the limited components I had at my disposal to create something that is actually useful to me, by giving me a reminder to drink water at constant intervals. 

Other reasons as to why I built this thing is because I had bought a LoRaWAN antenna before starting my IoT course, but it didn't cover my area due to how thick my walls are, otherwise I had intended to make use of that. I simply had to make something that connects to my PC with a USB cable and so I decided to make something quite practical. 

#### What Purpose Does It Serve
As the name implies, **HydroAlert** gives of a visible signal using a bright LED to remind me to drink a bit of water when I'm infront of the computer. The main reason as to why I even need this is because I can become engrossed in what I'm doing at my desk, be it playing games or studying, and that means that I might not realise how hot it is here. Giving myself a reminder every 30 minutes means I'm always topped up on water and staying healthy despite the heat. 

#### Data display on Ubidots Dashboard
In my current build I have my MCU (Micro Controller Unit) connected to a Dashboard on [Ubidots](https://ubidots.com/), which is a website desinged to display raw data on different graphs and widgets. I don't have many practical reasons as to why I have it displayed there, but it does give me the oppurtunity to see a timeline graph of the temperature in my room over the course of a couple hours/days depending on how long I have the **HydroAlert** on. 

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

I used [Visual Studio Code](https://code.visualstudio.com/) as my IDE (integrated development environment), but you can use any sort of code editor, but it makes things a lot easier to use VSC, along with the fact that you can use this as a more accurate tutorial if you follow it step by step. There are tons of tutorials on how to use VSC if you already haven't, but I used [this tutorial](https://hackmd.io/@lnu-iot/rkiTJj8O9) from the course page. 

#### 2: Necessary plugins to VSC 
In the [previously linked tutorial](https://hackmd.io/@lnu-iot/rkiTJj8O9) tutorial, it already mentions the extra plugins used in my process of setting up the code. That is [node.js](https://nodejs.org/en) and [PyMakr](https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr), in order to easily edit the code in the MCU and have greater control over the execution of said code. It's easier to download the PyMakr plugin in VSC than through the link, but choose whichever is more suitable for you. 


#### 3: How the Code is uploaded to the MCU
The steps necessary for flashing an MCU is quite easy. First, you will need to download the latest firmware from the [official MicroPython website](https://micropython.org/download/RPI_PICO_W/) in order for it to run properly. Connect the USB to the MCU, not the PC, make sure the two tiny pins are facing up so that it locks nicely into place. It won't go all the way in, and if you ever feel like removing it you need to apply a little bit of pressure to remove it from the MCU, but do this **carefully**.

There will be a small white button labeled *BOOTSEL*, hold this button in whilst connecting the MCU to your PC. Release the button when a new drive is availible, copy the downloaded drivers into RPI-RP2, the board will then be ready for use. This can be tested by removing and connecting the USB cable. The MCU should then be visible as a device under the PyMakr plugin in VSC. Connect the device and create a terminal to test if it works by using the `print("test")` statement. I used [this tutorial](https://hackmd.io/@lnu-iot/rkFw7gao_#Visual-Studio-Code) in order to set my system up.

### Putting Everything Together
Due to the fact that this is a very simple project, it requires no knowledge of resistors or that sort, it's all about connecting the wires so that they add up with the provided python code down below. I tried my best to visualise how my setup is made, but due to software restrictions I could not get a proper visualisation with the correct components. This setup is very much made for aesthetic reasons and could be used with less resources, like only using 3 wires for example. Therefore it is not suitable for any sort of large scale production.

#### Circuit Diagram
This circut diagram uses an *Arduino Nano (Rev3.0)* and a *LM35 Temperature Sensor* because I couldn't get access to the actuall *Raspberry Pi Pico WH* and *DHT11*, but it uses the same setup with the wires. You should therfore connect the pins to the MCU according to this text and not the image, as it may not represent the MCU correctly. 
![Skärmbild 2024-06-28 232217](https://hackmd.io/_uploads/SJh5FsnIA.png)
On the *Raspberry Pi Pico WH* and *DHT11* there are pins that are numbered from 1 to 40 (shown below), this means that you should make sure that the wires are correctly added according to these pins and not the number of pins on the image. For the *DHT11 sensor*, make sure that the blue wire is in the 38th pin on the right side of the board. This should connect to the left side of the sensor leg. The red wire should be on the 36th pin, and be connected to the ground in the middle. The black wire should be connected to the 32nd pin, and connect to the right leg. 

The LED light doesn't necessarily need wires, but I used them in order to place the light as far away on the components, as I only want the light visible in the front, so it's purely aesthetic. When connecting the LED, it's important that the 1 and 3 pin is connected, this means that power and ground can turn on the LED without problems.
![pico_pinout](https://hackmd.io/_uploads/rJzM6o28A.png)
[Link to image source](https://www.google.com/url?sa=i&url=https%3A%2F%2Fdocs.micropython.org%2Fen%2Flatest%2Frp2%2Fquickref.html&psig=AOvVaw0YS1stDm02GHQClrH3wqFZ&ust=1719697000572000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCKjC3tmg_4YDFQAAAAAdAAAAABAE)

## Ubidots, a simple yet effective visualisation tool
Ubidots is the *platform* I decided to stick with. This was after a long, and very unecessary, atempt at using TIG Stacks, which is something far beyond my comprehension. Ubidots works using an API token that is generated for each user to easily connect using a wifi network in order to send raw data to a dashboard, which can then display said info on different widgets and graphs that are customizable to an extent. It's also free, which is a huge plus for a student like me. 
#### Platform Details
[Ubidots](https://ubidots.com/) is a cloud-based platform, meaning that the data I have saved there could be revoked, used or changed without much of my input. This means it could potentially be inconsistent and unreliable, however, it also means I don't need to set up the database myself. It also means that they are able to store all the data without me needing to use any local storage. This is however fitting for my personal IoT project, seeing that I don't have much necessity of the data stored, and the fact that the main gimmick of the **HydroAlert** is the physical indication, and not necessarily the storage and usage of the temperature statistics. 

If it was however needed to be implemented into other bigger projects, and therefore scaled up, then there would be quite a few changes. For example a local storage to guarantee safety of stored data combined with a better visualisation of said data using more advanced graphs and potentially tables to order and display all the data. Temperature fluctuates constantly and my setup sends data every 30 minutes, this means that if you scaled it up into a bunch of places, and potentially shortened the duration to live updates, it would required way more advanced methods of both storage and handling of data to create a reasonable implementation of this specific IoT project.

If you desire to set up your own Ubidots dashboard similar to mine, the [this tutorial](https://hackmd.io/@lnu-iot/r1k63jjwo) is the one I used.

## The Code

[Github link to the main code](https://github.com/DoloremIpsumIV/HydroAlert/tree/main)
#### Code Description

The code connects to WiFi and reads data from the DHT11 temperature and humidity sensor on the MCU. It sends the temperature data to Ubidots and flashes an LED if the temperature exceeds 25°C. `keys.py`, `DEVICE_LABEL` and `VARIABLE_LABEL` in main are the only things that you need to change for the code to work.

#### Core functions and components

*  **Imported Statements and variables**
    ```python
    import network
    import urequests as requests
    import keys
    from time import sleep
    import dht
    import machine
    DEVICE_LABEL = "name for your device" 
    VARIABLE_LABEL = "variable name that you choose in Ubidots"  
    ```

     `network`, `urequests`, `keys`, `time`, `dht`, and `machine` are imported to manage network connections, HTTP requests, store WiFi credentials, handle timing, interact with the DHT11 sensor, and control GPIO pins respectively. The keys library is a seperate file that contains private information `keys.py`, the format is like this, you will need to switch it out for your own network SSID and so on:

    ```python
    WIFI_SSID = "your public wifi name"
    WIFI_PASS = "password123"
    TOKEN = "this is the personal token from Ubidots for their API"
    ```
    You will also need to change the `DEVICE_LABEL` and `VARIABLE_LABEL` to what you've named them in Ubidots so that they match properly. These can be found at the top of the `main.py` file.
*  **Initializing Sensors and Actuators**
    ```python
    tempSensor = dht.DHT11(machine.Pin(27))
    led = machine.Pin(0, machine.Pin.OUT)
    ```

    Turns on the pins, note that the pin numbers are different from the ones used on the board, this is because the digital pins and the ones on the board uses different numbers.

*  **Main Script Execution**
    ```python
    if __name__ == "__main__":
        connect()
    
        while True:
            try:
                tempSensor.measure()
                temperature = tempSensor.temperature()
                humidity = tempSensor.humidity()
                print("Temperature is {} degrees Celsius and Humidity is {}%".format(temperature, humidity))
                
                returnValue = sendData(DEVICE_LABEL, VARIABLE_LABEL, temperature)
                
                if temperature >= 25:
                    flash_led(5, 0.5)
    
                sleep(DELAY)
            except Exception as error:
                print("Exception occurred:", error)
                sleep(2)
    ```

    After connecting to WiFi, measuring the temperature and humidity, it sends the data to Ubidots, and flashes the LED if the temperature exceeds 25°C. This process repeats every 30 minutes. You can change the duration in a variable called `duration` at the top of the main script (it's calculated in seconds). You can also change the temperature in the `if` statement if you think it's too high/low.

## Transmitting the data 
How is the data transmitted to the internet or local server? Describe the package format. All the different steps that are needed in getting the data to your end-point. Explain both the code and choice of wireless protocols.

### Data Transmission and Protocols
The data that is sent from the MCU uses a connection to your home WiFi network. This means that it doesn't required any other external components like LoRaWan, and it technically doesn't need a USB connection to your PC if you ha an external battery, though I don't do this.  The previous chapter **The Code** describes what variables you need to change in order to make sure that your WiFi is connected to the MCU. 


#### How often is the data sent?
The data is determined by the ``duration`` variable, due to it being 30 minutes, it will naturally send data every half an hour to ubidots. This is done using a WiFi network that it connects to using the aforementioned `keys.py` file. I think it's reasonable to only send the data every 30 minutes, but a different method could be that the LED blinks every 30 minutes, but temperature data gets sent every 10 minutes or so in order to build up a more accurate temperature fluctuation graph, but I did not see this as necessary. 
#### Webhooks
The API key is discussed breifly in the previous chapter, but it requires that you make an account in [Ubidots](https://ubidots.com/) and under the account settings, you should be able to find your personal API key. The key uses Webhooks in order to send small packages of **JSON** data that the website can parse, regaining the original data again, i.e the temperature readings. Webhooks are fine for the small scale usage of this specific project, a local server would be better at maintaining higher levels of data transfer and handling. This is why I choose Webhooks, it's simple, easy and does it's required job. 

## Presenting the data
![Skärmbild 2024-06-29 113430](https://hackmd.io/_uploads/HJ6tr8pL0.png)
To be frank, I didn't spend too much time customizing the look of my *Dashboard* as I didn't find it to be as crucial as the main project. Therefore it's better to just show it as more of a visual representation of what the MCU does. The components I've used are the *Line chart*, *Gauge* and an *Indicator*, the indicator is basically just a graphical representation of the LED light, due to it turning on if it's above 25 C°. 

The data that I send to the dashboard is determined by the duration variable, so every 30 minutes. The data that is saved on Ubidots should last for roughly a month acording to [this article](https://help.ubidots.com/en/articles/636669-how-long-is-my-data-stored-for). This means that long term storage isn't available unless I were to pay for a plan, which I will not do for this project. 

## The | HydroAlarm | visualised and done
The final design is a very basic, but effective, alarm. It uses a bit too many wires, as if you wantet to be efficent, you could simply stick the LED next to the MCU. However, I think it looks a little better this way, escpecially on my desk where only the LED is visible, as I have the wires and the board behind my screen to hide the semi ugly design. 
![20240628_232348-min](https://hackmd.io/_uploads/Sk7oKLpIR.jpg)
There are certanly things that could be improved, one could be having a battery connection. This could turn it into a sort of portable temperature detector, where it warns you if it's too hot or not. If you where to bring it then it would struggle with WiFi connections, but that's why you could implement a LoRaWan solution, which was my original plan, which ultimately fell through.
![20240628_232356-min](https://hackmd.io/_uploads/ryvJq868R.jpg)
I think it looks quite meh and isn't all that impressive, but for someone with zero IoT experience, i'd say it's a good first attempt! I learned a fair few things about IoT, and it's inspired me to try to build other projects in the future. 

### Thank you for reading!
