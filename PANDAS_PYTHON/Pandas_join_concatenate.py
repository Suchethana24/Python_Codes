import pandas as pd
Names = ["suchi", "akhi", "rohi", "pooji", "hruthi"]
Subjects = ["ds", "python", "java", "js", "c++"]
Points = [1,2,3,4,5]
df1 = pd.DataFrame({"Names" : Names, "Subjects" : Subjects, "Marks" : Points},index=["L1", "L2", "L3","L4","L5"])
print(df1)
print("===================================")

Name = [ "suchi", "mani", "john", "pandu", "sruthi" ]
Subject = [ "ds", "python", "java", "js", "c++" ]
Mark = [71, 82, 99, 89, 88]
df2 = pd.DataFrame({ "Name" : Name, "Subject" : Subject, "Mark" : Mark },index=["L1", "L6", "L8", "L9","L10"])
print(df2)
print("========================")

# inner join
inner_df = df1.join(df2,how='inner')
print(inner_df)
print("========================")

# left join
left_df = df1.join(df2,how='left')
print(left_df)
print("========================")

# right join
right_df = df1.join(df2,how='right')
print(right_df)
print("========================")

# outer join
outer_df = df1.join(df2,how='outer')
print(outer_df)
print("========================")

# concatenating data frames
print(pd.concat([df1,df2]))