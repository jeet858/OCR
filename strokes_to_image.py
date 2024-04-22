import pandas as pd
import os
import matplotlib.pyplot as plt

# List to store the counts for each file
counts_list = []


# Iterate through each file in the folder
def plot_data(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            print(file_name)
            df = pd.read_csv(f'{folder_path}/{file_name}',delim_whitespace=True, header=None,names=['i', 'x', 'y', 'z'])


            # Rename the columns for clarity
            # df.columns = ['i', 'x', 'y', 'z']
            # print(df)
            #
            # # Drop the 'z' column if you don't need it
            # df.drop(columns=['z'], inplace=True)
            # df.drop(columns=['i'], inplace=True)

            # Convert the DataFrame to a list of lists
            # all_points = df.values.tolist()
            #
            # x_values = [point[0] for point in all_points]
            # y_values = [point[1] for point in all_points]

            plt.plot(df['x'], df['y'])
            plt.title('Scatter Plot of Points')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.grid(True)
            if not os.path.exists('Strokes-Images'):
                os.makedirs('Strokes-Images')
            output_file_path = os.path.join('Strokes-Images', file_name.replace('.txt', '.png'))
            plt.savefig(output_file_path, format='png')  # Explicitly specifying PNG format
            plt.close()




# store_data()
folderpath = 'Strokes Dataset'
c = 0
plot_data(folderpath)

