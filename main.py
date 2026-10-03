import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")

# Data Cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Numeric columns cleaning
df["price"] = df["price"].astype(str).str.replace(",", "").astype(float) 
df["rate_per_sqft"] = df["rate_per_sqft"].astype(str).str.replace(",", "").astype(int) 
df['bhk_count'] = df['bhk_count'].astype(int)

# Categorial column cleaning
df['status'] = df['status'].str.strip().str.lower()
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approved by rera' : True, 'not approved by rera' : False})
df['flat_type'] = df['flat_type'].str.strip().str.lower()
df = df.drop_duplicates()

# Q1: Which is the costliest flat in DS
costliest_flat = df.loc[df['price'].idxmax()]
'''
write this output in a sentence
price                                1226300000.0
status                              ready to move
area                                        16500
rate_per_sqft                               74323
property_type    6 BHK Apartment in DLF Camellias
locality                                Sector 42
builder_name                    Provident Capital
rera_approval                               False
bhk_count                                       6
soceity                             DLF Camellias
company_name                                  DLF
flat_type                               apartment
'''
print(f"The costliest flat in DS is a {costliest_flat['bhk_count']} BHK apartment located in {costliest_flat['locality']} with a price of {costliest_flat['price'] / 10000000} crores. It is currently {costliest_flat['status']} and has a rate per sqft of {costliest_flat['rate_per_sqft']}. The builder is {costliest_flat['builder_name']} and it is {'approved by RERA' if costliest_flat['rera_approval'] else 'not approved by RERA'}.")

# Q2: Which locality has highest average price?

highest_avgprice_locality = df.groupby('locality')['price'].mean().idxmax()
print(f"The locality with the highest average price is {highest_avgprice_locality}.")

# Q3: Which locality has highest rate per sq. foot?

highest_rate_locality = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
print(f"The locality with the highest rate per square foot is {highest_rate_locality}.")

# Q4: Do ready-to-move properties cost more than under-construction properties?

ready_to_mobe_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under consruction']['price'].mean()

if(ready_to_mobe_avg_price > under_construction_avg_price):
    print(f"Yes, ready-to-move properties cost more on average than under-construction properties.")
else:
    print(f"No, under-construction properties cost more on average than ready-to-move properties.")

# Q5: Do RERA-approved properties command a price premium?

rera_approved_avg_price = df[df['rera_approval'] == True]['price'].mean()
rera_not_approved_avg_price = df[df['rera_approval'] == False]['price'].mean()

if(rera_approved_avg_price > rera_not_approved_avg_price):
    print(f"Yes, RERA-approved properties command a price premium on average.")             
else:                       
    print(f"No, RERA-approved properties do not command a price premium on average.")

# Q6: How does area(sqft) impact property price?

sns.scatterplot(data=df, x='area', y='price')
plt.show()

# Q7: Which BHK configuraion is most expensive?

most_exp_bhk_config = df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
print(f"The most expensive BHK configuration is {most_exp_bhk_config} BHK.")

# Q8: Which property type is the costliest?

costliest_property_type = df.groupby('flat_type')['rate_per_sqft'].mean().idxmax()
print(f"The costliest property type is a {costliest_property_type}")

# Q9: Do certian builders price higher?

top_5_builders = df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(5)

print("Top 5 builders are:", end=" ")
for builder in top_5_builders.index:
    print(builder, end=", ")

# Q10: are larger homes more expensive per sqft?

sns.scatterplot(data=df, x='area', y='rate_per_sqft')
plt.show()