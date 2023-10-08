import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

columns = [
    'Datetime', 'Magnetic_Field_X', 'Magnetic_Field_Y', 'Magnetic_Field_Z',
    *['Energy_{}'.format(i) for i in range(1, 51)]
]

data = pd.read_csv('dsc_fc_summed_spectra_2022_v01.csv', header=None, names=columns)

data['Datetime'] = pd.to_datetime(data['Datetime'], format='%Y-%m-%d %H:%M:%S')


plt.figure(figsize=(10, 6))
plt.plot(data['Datetime'], data['Magnetic_Field_X'], label='вектор магнітного поля BX')
plt.plot(data['Datetime'], data['Magnetic_Field_Y'], label='вектор магнітного поля BY')
plt.plot(data['Datetime'], data['Magnetic_Field_Z'], label='вектор магнітного поля BZ')
plt.xlabel('Час')
plt.ylabel('Магнінтне поле (наноТестла)')
plt.title('Компоненти магнітного поля з часом')
plt.legend()
plt.show()

# Plot the raw measurement spectrum over time (selecting a few for clarity)
plt.figure(figsize=(10, 6))
for i in range(1, 11):
    plt.plot(data['Datetime'], data[f'Energy_{i}'], label=f'Energy {i}')
    
plt.xlabel('Datetime')
plt.ylabel('Raw Measurement Spectrum')
plt.title('Raw Measurement Spectrum Over Time')
plt.legend()
plt.show()
