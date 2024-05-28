import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)

print(df.dtypes)

print(df.head(2))
print(df.tail(1))

print(df.index)
print(df.columns)

print(df.describe())

print(df.T)

# print(df.sort_index(axis=0, ascending=False))
# print(df.sort_values(by="D"))

# print(df["B"])
# print(df[1:2])
# print(df["20130102":"20130104"])

# print(df.loc[dates[0]])
# print(df.loc["20130101":"20130103", ["C", "D"]])

# print(df.at[dates[0], "B"])

# print(df.iloc[0])
# print(df.iloc[1:3, 2:4])
# print(df.iloc[[0, 3, 4], [0, 3]])
# print(df.iloc[:, :])

# print(df.iloc[1, 1])
# print(df.iat[1, 1])

dfTitanic = pd.read_csv("titanic.csv")
print(dfTitanic[dfTitanic["Fare"] > 500])
print(dfTitanic.index)
plt.close("all")


# seriesFare = dfTitanic["Fare"]
# seriesFare.plot()
# plt.show()

fare = dfTitanic.groupby(["Fare"]).size().reset_index(name='Count')
print(fare)

fare.plot(x='Fare', y='Count')
plt.grid(True)
plt.show()


# print(df[df > 0])

# df2 = df.copy()
# df2["E"] = ["one", "one", "two", "three", "four", "three"]
# print(df2[df2["E"].isin(["one", "three"])])

# s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130101", periods=6))
# print(s1)
# df["F"] = s1

# df.at[dates[0], "A"] = 0
# print(df)
# df.iat[1, 1] = 0
# print(df)
# df.loc[:, "D"] = np.array([5] * len(df))
# print(df)

# df2 = df.copy()
# df2[df2 > 0] = -df2
# print(df2)

# df1 = df.reindex(index=dates[1:3], columns=list(df.columns) + ["E"])
# df1.loc[dates[0] : dates[1], "E"] = 1
# print(df1)

# print(df1.dropna(how="any"))
# print(df1.fillna(value=3.3))

# print(pd.isna(df1))

# print(df.mean())
# print(df.mean(axis=1))

# s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
# print(s)
# print(df.sub(s, axis="index"))

# print(df.agg(lambda x: np.mean(x) * 5.6))
# print(df.transform(lambda x: x * 101.2))

# s = pd.Series(np.random.randint(0, 10, size=1000))
# print(s.value_counts())

# s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
# print(s.str.lower())

# df = pd.DataFrame(np.random.randn(5, 5))
# print(df)

# pieces = [df[:3], df[3:7], df[7:]]
# print(pd.concat(pieces))

# left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
# right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
# print(left)
# print(right)
# print(pd.merge(left, right, on="key"))

# df = pd.DataFrame(
#     {
#         "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
#         "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
#         "C": np.random.randn(8),
#         "D": np.random.randn(8),
#     }
# )
# print(df)
# print(df.groupby("A")[["C", "D"]].sum())
# print(df.groupby(["A", "B"]).sum())

# arrays = [
#    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
#    ["one", "two", "one", "two", "one", "two", "one", "two"],
# ]
# index = pd.MultiIndex.from_arrays(arrays, names=["first", "second"])
# df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
# df2 = df[:4]
# print(df2)

# stacked = df2.stack(future_stack=True)
# print(stacked)
# print(stacked.unstack(1))

# df = pd.DataFrame(
#     {
#         "A": ["one", "one", "two", "three"] * 3,
#         "B": ["A", "B", "C"] * 4,
#         "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
#         "D": np.random.randn(12),
#         "E": np.random.randn(12),
#     }
# )
# print(pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"]))

# # time

# df = pd.DataFrame(
#     {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
# )
# df["grade"] = df["raw_grade"].astype("category")
# print(df["grade"])

# new_categories = ["very good", "good", "very bad"]
# df["grade"] = df["grade"].cat.rename_categories(new_categories)

# df["grade"] = df["grade"].cat.set_categories(
#     ["very bad", "bad", "medium", "good", "very good"]
# )
# print(df["grade"])

# print(df.sort_values(by="grade"))
# print(df.groupby("grade", observed=False).size())


