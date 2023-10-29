import numpy as np
import matplotlib.pyplot as plt

non_normal_data = np.random.exponential(scale=1, size=1000)

fig, axs = plt.subplots(2,1, figsize=(12.18, 6.27))
axs[0].hist(non_normal_data, bins=30, density=True, color='orange', alpha=0.7)
axs[0].set_xlabel('Non-Normal Data')
axs[0].set_ylabel('Probability Density')
axs[0].set_title('Non-Normal Data Distribution')

sample_means, sample_size, num_samples = [], 30, 1000
for _ in range(num_samples):
    sample = np.random.choice(non_normal_data, size=sample_size)
    sample_mean = np.mean(sample)
    sample_means.append(sample_mean)

axs[1].hist(sample_means, bins=30, density=True, color='skyblue', alpha=0.7, label='Sample Means')
axs[1].set_xlabel('Sample Means')
axs[1].set_ylabel('Probability Density')
axs[1].set_title('Sample Means Distribution vs. Normal Distribution')
axs[1].axvline(np.mean(sample_means), color='red', linestyle='dashed', linewidth=2, label='Sample Mean')

mu, std = np.mean(sample_means), np.std(sample_means)
x = np.linspace(min(sample_means), max(sample_means), 100)
pdf = (1 / (std * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu) / std) ** 2))
axs[1].plot(x, pdf, color='green', linewidth=2, label='Fitted Normal Distribution')

bootstrap_means = []
for _ in range(1000): 
    resample = np.random.choice(sample_means, size=len(sample_means), replace=True)
    bootstrap_mean = np.mean(resample)
    bootstrap_means.append(bootstrap_mean)

confidence_level = 0.99
lower_bound = (1 - confidence_level) / 2 * 100
upper_bound = (1 + confidence_level) / 2 * 100
confidence_interval = np.percentile(bootstrap_means, [lower_bound, upper_bound])
axs[1].axvline(confidence_interval[0], color='blue', linestyle='dashed', linewidth=2, label='Lower Confidence Interval')
axs[1].axvline(confidence_interval[1], color='blue', linestyle='dashed', linewidth=2, label='Upper Confidence Interval')
axs[1].legend()

plt.tight_layout()
plt.savefig("plot.png")
