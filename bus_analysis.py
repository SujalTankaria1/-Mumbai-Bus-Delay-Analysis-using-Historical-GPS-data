import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
df = pd.read_csv("mumbai_bus_gps.csv")

# Group by stop and calculate mean delay
avg_delay_per_stop = df.groupby("stop_name")["delay_in_minutes"].mean().sort_values()

# Plot it
plt.figure(figsize=(10,6))
sns.barplot(x=avg_delay_per_stop.values, y=avg_delay_per_stop.index, palette="coolwarm")
plt.title("📊 Average Delay per Bus Stop in Mumbai")
plt.xlabel("Average Delay (minutes)")
plt.ylabel("Bus Stop")
plt.grid(True)
plt.tight_layout()
plt.show()



# Create a new category column
df["delay_category"] = df["delay_in_minutes"].apply(
    lambda x: "Early" if x < 0 else "On-time" if x <= 5 else "Late"
)

# Count of each category
category_counts = df["delay_category"].value_counts()

# Plot
plt.figure(figsize=(6,4))
sns.barplot(x=category_counts.index, y=category_counts.values, palette="Set2")
plt.title("🕒 Delay Category Distribution")
plt.ylabel("Number of Records")
plt.xlabel("Delay Category")
plt.show()



# Average delay by route
avg_delay_route = df.groupby("route_id")["delay_in_minutes"].mean().sort_values(ascending=False)

# Top 5 delayed routes
print("Top 5 most delayed routes:")
print(avg_delay_route.head())


# First convert scheduled_arrival to datetime if not already
df['scheduled_hour'] = pd.to_datetime(df['scheduled_arrival'], format="%H:%M").dt.hour

# Average delay by hour of the day
hourly_delay = df.groupby("scheduled_hour")["delay_in_minutes"].mean()

# Plot
plt.figure(figsize=(10,5))
sns.lineplot(x=hourly_delay.index, y=hourly_delay.values, marker="o")
plt.title("⏰ Average Delay by Hour of the Day")
plt.xlabel("Hour of the Day (24hr)")
plt.ylabel("Average Delay (minutes)")
plt.xticks(range(5, 22))  # Adjust to range of your data
plt.grid(True)
plt.show()
