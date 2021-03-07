# HomieGuard - TAMUmake 2021 
#Team 
Team Members: Linjian Yang, Saini Ye, Jiaze Cai
## Inspiration
Our ideas about the project were initially inspired by our friends’ daily life experience. During COVID time, most of the students were asked to stay at home and take online courses. For students who were mostly taking their major specific courses, the course load and the school work make some of them having difficulty in managing their time between living and studying. There is a scenario when you are really busy about your school work, while your roommate does not recognize that and still come in to your room often and bother you, are you feeling stress and worries? Yes, the homieGuard is meant to be a “watchdog’ that will guard your room at your dorm so check if there is someone right outside of your room. Additionally, it does not have to be roommates, it could also be set up outside of dorms to check the people who walked pass by and make sure they don’t take your deliveries. 


## What it does
Our project was designed to provide people a device to check if there are people coming to their place, and also helping them to keep a safe and quiet place to live and study. Specifically, when there is someone present in the camera view, the program will be instructed to take a picture as well as a video recording depends on how long and what does the intruders do. Moreover, there will be email with pictures as attachment send to the over of the homieGuard to inform them about their surroundings. 


## How we built it
The homieGuard is built with a Raspberry Pi 4B, a PIR Motion Sensor, a PiCamera, a few servo motors and a platform on a car to support the motion of the PiCamera, as well as a white LED to show whether there is any intruders coming to the camera view. For the software part, we have mainly used Python as our programming language in terms of the face detection, tracking people’s (faces’) movements, take pictures of the intruders, and record a short video that depends on how long would the people in the camera view would act. 


## Challenges we ran into
We were having problems dealing with the Raspberry Pi connection and setting up the configuration of the PIR Motion Sensor. Setting up the reasonable precise delay time for the PIR Motion Sensor to response with is difficult as the lagging uncertainty of the sensor itself as well as those came through the recording is hard to gauge and predict. Additionally, for the face detection portion, our team members spent a long time figuring out how to detect faces of people who are not facing the camera completely and for some who are moving across the camera view. About the face detection portion, we were having trouble to produce accurate distance measurements between the face and the camera. 


## Accomplishments that we're proud of
Although the project was said to be around 45 hours, our group only spend about 24 hours on the project starting from the designing stage. Within a short time frame, we were able to make our platform autonomously to track the movement of faces in the camera view. 


## What we learned
For us as a team, we learned how to be collaborative and make decisions that’s after considering everyone opinions. Individually, we were working on different parts of the project so each of us have learned how to solve some problems. In the specific aspect about controlling the platform, our team have realized that PID control would be a great approach to handle, however, it is difficult and would be impossible to grasp the concepts and use it correctly within such a short time frame. 


## What's next for homieGuard
We think the next step for homieGuard would be to make the car in motion, so that it can move around and to act like an actual “guardian” of the house. Additionally, in order to penalize the intruders and the stealers a bit. We think we can add something fun to the the car such as a spray, noisy buzzer, water drops, very bright LED and other fun electronic components.
