import pandas as pd
df = pd.read_csv('expenses.csv')
def add_expense():
    try:
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category: ")
        amount = float(input("Enter the amount: "))
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        new_row = pd.DataFrame([[date, category, amount]], columns=['date', 'category', 'amount'])
        return pd.concat([df, new_row], ignore_index=True)
    except ValueError as e:
        print(f"Error: {e}")
        return df
df = add_expense()
df
total_spent = df['amount'].sum()
print(f"Total spent: ${total_spent:.2f}")
category_summary = df.groupby('category')['amount'].sum()
print("Category summary:")
print(category_summary) 