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
