import pandas as pd

file_path = r"C:\VS files\Python\weather_data.xlsx"

df = pd.read_excel(file_path)

df.fillna({
    'Temperature': 200,
    'Windspeed': 3,
    'Event': 'no event'
}, inplace=True)


print("\nAfter Filling Missing Values:")
print(df.isnull().sum())

print("\nUpdated DataFrame:")
print(df) 

# output_path = r"C:\VS files\Python\cleaned_weather_data.xlsx"
# df.to_excel(output_path, index=False)
# print(f"\nUpdated file saved successfully at: {output_path}")
