import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("modified_table.xlsx", header=3)


df = df.iloc[2:].reset_index(drop=True)


df.columns = [
    "Email_ID",
    "Date",
    "Day_of_Week",
    "Time_Sent",
    "Sender",
    "Recipient",
    "Subject",
    "Body_Preview",
    "Folder",
    "Category",
    "Word_Count",
    "Has_Attachment",
    "Priority",
    "Is_Forwarded",
    "Response_Time_Hrs",
    "Sentiment_Score",
    "Thread_Length",
    "Email_Size_KB",
    "Read_Receipt"
]


# QUESTION 1
# Who sends the most emails?

top_senders = df["Sender"].value_counts()

print("\nTOP EMAIL SENDERS")
print(top_senders.head(10))

plt.figure(figsize=(10,5))
top_senders.head(10).plot(kind="bar")
plt.title("Top 10 Email Senders")
plt.ylabel("Number of Emails")
plt.tight_layout()
plt.show()



# QUESTION 2
# Which day has maximum activity?

day_activity = df["Day_of_Week"].value_counts()

print("\nEMAIL ACTIVITY BY DAY")
print(day_activity)

plt.figure(figsize=(8,5))
day_activity.plot(kind="bar")
plt.title("Email Activity by Day")
plt.ylabel("Number of Emails")
plt.tight_layout()
plt.show()



# QUESTION 3
# Which category receives most emails?

category_count = df["Category"].value_counts()

print("\nEMAILS BY CATEGORY")
print(category_count)

plt.figure(figsize=(10,5))
category_count.plot(kind="bar")
plt.title("Emails by Category")
plt.ylabel("Count")
plt.tight_layout()
plt.show()



# QUESTION 4
# Average email size by category

df["Email_Size_KB"] = pd.to_numeric(df["Email_Size_KB"],errors="coerce")

avg_size = (df.groupby("Category")["Email_Size_KB"].mean().sort_values(ascending=False))

print("\nAVERAGE EMAIL SIZE BY CATEGORY")
print(avg_size)

plt.figure(figsize=(10,5))
avg_size.plot(kind="bar")
plt.title("Average Email Size by Category")
plt.ylabel("Average Size (KB)")
plt.tight_layout()
plt.show()


print("\nAnalysis Completed Successfully!")