
![BrainUp logo](https://github.com/user-attachments/assets/f30a7087-b48c-4850-83f3-20c14564f583)    

#Check out our pitch slide-deck [here!](https://docs.google.com/presentation/d/19a7ouUCTQGIpuUiWzWxoP3Z_nMsN9VgIaNxoHqfCtaI/edit?usp=sharing)
# Inspiration
Each of us has experience with Brainrot from insta reels and TikTok, so we created a data analytics tool that allows users to use the data that they've accumulated through their use of social media sites, and searches it for hobbies they might enjoy, it then helps these users take the first step toward partaking in these hobbies

# What it does
takes in user instagram data and uses AI to process the data and creates a recommended activity that is given to user so that they can be productive

# How we built it
Used ReactJS to build the frontend, AI models: clustering (HDBscan), embedding(MPnet-base v2), frame capturing (blip2-opt-2.7b), key-frame (katna), text gen (mistral), gliner to optimize name entity recogintion, whisper-small. Selenium to scrape the web for recommended courses, and Flask to build the backend server API.

# Challenges we ran into
rate limit when gathering data from instagram
overcoming learning curve, using new technologies and frameworks
Physical challenges, coding for long periods, staying awake and healthy. ## Accomplishments that we're proud of overcoming challenges as a team: I felt that we all worked together really well and when we faced challenges, we worked through them together. having an idea we all liked: We all contributed to brainstorming ideas and found a really unique idea with exciting technologies we wanted to use.

# What we learned
For many of us, this is the first hackathon we've ever attended. So being able to manage working in a team. , with various differnt levels of comfort with the tech we were working with and pushing through hurdles was a great learning exerperiance for us

# What's next for BrainUp
We've got a ton of tweaks for the proejcts, performace optimzations and such. Supporting more classified websites, and refining the UI


# SET UP
.env
```
INSTAGRAM_SESSION_ID = \*YOUR SESSION ID*\
MODEL_DIR = \*YOUR MODEL DIR*\
ACCESS_TOKEN = \*YOUR ACCESS TOKEN*\
```
