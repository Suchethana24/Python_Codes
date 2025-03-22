import pandas as pd
Names = ["suchi", "akhi", "rohi", "pooji", "hruthi"]
Subjects = ["ds", "python", "java", "js", "c++"]
Marks = [70, 85, 90, 85, 86]
df1 = pd.DataFrame({"Names" : Names, "Subjects" : Subjects, "Marks" : Marks})
print(df1)
print("===================================")

Names = [ "suchi", "mani", "john", "pandu", "sruthi" ]
Subjects = [ "ds", "python", "java", "js", "c++" ]
Marks = [71, 82, 99, 89, 88]
df2 = pd.DataFrame({ "Names" : Names, "Subjects" : Subjects, "Marks" : Marks })
print(df2)
print("========================")

# merging = 1.inner merge
inner_df = df1.merge(df2, on="Names", how="inner")
print(inner_df)
print("========================")

# 2. right merge
right_df = df1.merge(df2, on="Names", how="right")
print(right_df)
print("========================")

# 2. left merge
left_df = df1.merge(df2, on="Names", how="left")
print(left_df)
print("========================")

# 3.outer merge
outer_df = df1.merge(df2, on="Names", how="outer")
print(outer_df)