

The purpose of this project was to provide a free digital alternative to the $349.99

Vex V5 Brain. This started out as a small side project in an attempt to work on Robotics

II projects at home. Given the price for each brain and lackluster battery time, it seemed

too risky and overly complicated to take one home. Through the use of the school year

interacting with the brain and my level of Python, I decided it would be appropriate to

create a virtual mock up brain. This quickly evolved into a full scale project overtaking

my original project for the first half of the quarter because of its potential uses.

Currently the project gives a base level performance of the brain, but for the

foreseeable future, will not be able to outperform or in some cases meet the

performance given by the brain. This is due to the different rendering systems given by

both, and the interpreters for each. Because of the brain's proprietary nature, there can

never be a 100% accurate emulation of the brain, though given the current code, it

creates a non-noticeable to similar indifference between the two. Allowing for the user to

almost essentially copy scripts from one to the other, without issue.

The current state of the implemented sensors, tools, and other components of

Vex V5 category is limited. Creating scripts to imitate each individual sensor takes time

and effort to not only make it accurate, but creating a system of usage for something

physical in a digital space also takes innovation. The current list of available sensors or

tools goes as follows: line tracker, distance sensor, encoder, and bump switch or limit

switch. Although the list can be seen as small, each took different approaches on

reaching their designated tasks, and are generally 50 lines or longer.

In the future I plan on implementing multiple different sensors, tools, and other

components, including the Controller, Vision Sensor, Optical Sensor, Light Sensor,

Rangefinder, LED, and Virtual Motors. The two biggest challenges of which are the

Controller and Virtual Motors. The Controller’s long term plan includes the usage of

sockets to communicate from the brain script to the Controller, if this doesn't work, I will

most likely resort to using arrays containing the data of booleans and coordinates of

said Controller. The Virtual Motors will use the same display engine that the brain uses

to visualize the motors for the user. Although this wouldn't be physical, it’s meant to give

an accurate display of what the motors will look like when in use.

New future plans of this project have been laid out for spare time work. The recent

change in the installation method has proved to be effective at setup and initialization.

Minor changes have been made to the code to improve efficiency but groundwork has

been laid out for future versions

A gui build is in development at this moment in time.

