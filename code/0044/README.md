Reinforcement Learning (RL) is a newer approach to machine learning that instead of optimizing a function for a single dataset, we optimize for a sequence of events (games) upon repeated trials. 

Typical setups include an environment, a set of possible states, and figuring out how to navigate this state space with some objective in mind. 

Most introductions to this will make use of the gym library, which I haven't used myself, until now! I spent more time getting my video to render than I did on setting up the game, which is provided to you. 

The basic idea is, I guess, to optimize keeping the stick upright by moving the cart left or right. So, how did my cart do? This is my first time publishing a video, so hope it works!

Have you used RL before? What applications of it have you seen? Share in the comments below!

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

```
import gym
from gym.wrappers.monitoring.video_recorder import VideoRecorder

env = gym.make('CartPole-v1', render_mode="rgb_array")
recorder = VideoRecorder(env, "gym.mp4", enabled=True)
episodes = 100

for episode in range(episodes):
    state, total_reward = env.reset(), 0
    
    while True:
        env.render()
        recorder.capture_frame()
        action = env.action_space.sample()
        state, reward, done, _, _= env.step(action)
        total_reward += reward
        
        if done:
            print(f"Episode {episode + 1}, Total Reward: {total_reward}")
            break

recorder.close()
env.close()
```

<img src="../../static/0044.png" />

# Output

<video src="gym.mp4">
