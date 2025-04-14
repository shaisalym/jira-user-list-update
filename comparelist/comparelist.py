import pandas as pd

# file1 should be jira list
# file2 should be AD list

jira_list = pd.read_csv('export-users.csv')
azure_list = pd.read_csv('AllEmployeeED.csv')
# jira_list = pd.read_excel('file1.xlsx')
# azure_list = pd.read_excel('file2.xlsx')

jira_emails = set(jira_list['email'].dropna().str.strip().str.lower())
azure_emails = set(azure_list['EmailAddress'].dropna().str.strip().str.lower())

difference = jira_emails - azure_emails

result_df = pd.DataFrame(list(difference), columns=['Accounts to remove from Jira'])
result_df.to_excel('removefromjira.xlsx', index=False)
# result_df.to_excel('test.xlsx', index=False)

print(f"Found {len(difference)} emails still active in Jira. Saved to 'removefromjira.xlsx'.")