# computersecurity-keystrokedynamics
This is a part of Chulalongkorn university's computer security class. This program is a simple way to implement keystroke dynamics biometrics.


# How to use the program
first, you need to register on registry.py by fill your name and provided message
![alt text](https://github.com/nasri-repositories/computersecurity-keystrokedynamics/blob/master/readmeimage/registry.png?raw=true)

Then, you can login by running login.py .
![alt text](https://github.com/nasri-repositories/computersecurity-keystrokedynamics/blob/master/readmeimage/login.png?raw=true)

Note that This program identifies who your typing behavior is closest to in the database. So if there is only one person in the database, fastman for example. No matter what your typing behavior are. The program will identify that you are fastman. Therefore, you should have registration information for more than one person. In this example, there are two registrants, fastman and slowman.

If you type the text correctly without any deletion The program will return the result.
![alt text](https://github.com/nasri-repositories/computersecurity-keystrokedynamics/blob/master/readmeimage/result.png?raw=true)

But if you type it wrong or some characters have been deleted. The program will ask you to try again.
![alt text](https://github.com/nasri-repositories/computersecurity-keystrokedynamics/blob/master/readmeimage/failed.png?raw=true)
