import pandas as pd

file = "non_ntt_filtered"

df = pd.read_csv(f"../data/{file}.csv")
df["c"] = (
    df
    .filter(regex=r"c\d+")
    .apply(lambda r: r.dropna().to_list(), result_type="reduce", axis=1)
    )

df = df.drop(df.filter(regex=r"c\d+").columns, axis=1)


my_df = df[df["i"] == 0]
Ldf = my_df[['m', 'j']]
L = Ldf.values.tolist()
L = [ tuple(p) for p in L]

Z =  my_df['zij'].values.tolist()

x = list(zip(L,Z))
z = {tuple(k): v for k, v in x}


Ccol =  my_df['c'].values.tolist()

czip = list(zip(L,Ccol))
C = {}
for ci in czip:        
        C = C | {tuple([ci[0][0],ci[0][1], j ] ): ci[1][j]  for j in range(256)}

x = list(zip(L,Z))
S1ij = my_df["s1ij"].values.tolist()
x = list(zip(L,S1ij))
s1ij = {tuple(k): v for k, v in x}

