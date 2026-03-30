import pandas as pd 

df = pd.read_csv("student_dataset.csv")


# Total marks 

df["Total"] = df["Math"] + df["Physics"] + df["Chemistry"]

# Average marks

avg = df[["Math", "Physics","Chemistry"]].mean()

# Topper student

Topper = df.sort_values(by="Total", ascending=False).head(10)
# Grade

grade = df["Grade"].value_counts()



print("📊 Average marks:\n", avg)
print("\n🏆 Top 10 Students:\n",Topper[["Student_Names", "Total"]])
print("\n📈Grade distribution:\n",grade)
print("\n💡 Insight:")
print("Most students got grade:", grade.idxmax())
print("\n Subject Toppers:")

print("\n🥇 Subject Toppers:")

math_topper = df.loc[df["Math"].idxmax(), ["Student_Names", "Math"]]
physics_topper = df.loc[df["Physics"].idxmax(), ["Student_Names", "Physics"]]
chem_topper = df.loc[df["Chemistry"].idxmax(), ["Student_Names", "Chemistry"]]

print("\nMath Topper:\n", math_topper)
print("\nPhysics Topper:\n", physics_topper)
print("\nChemistry Topper:\n", chem_topper)
