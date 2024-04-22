import os

import pandas as pd

folderpath = 'Dataset'
c = 0
# for subfolder in os.listdir(folderpath):
#     subfolder_path = os.path.join(folderpath, subfolder)
#     for i in os.listdir(subfolder_path):
#         textfile_path = os.path.join(subfolder_path, i)
#         df = pd.read_csv(textfile_path, sep=" ", header=None)
#         stroke_indices = df[df[2] == 0].index.tolist()
#         stroke_indices.append(len(df))
#         strokes = [df.iloc[stroke_indices[i]:stroke_indices[i + 1]] for i in range(len(stroke_indices) - 1)]
#         output_subfolder = os.path.join('Extracted Strokes', subfolder, i)
#         os.makedirs(output_subfolder, exist_ok=True)
#         for j, stroke in enumerate(strokes):
#             stroke.to_csv(f'{output_subfolder}/{j + 1}.txt', sep=' ', header=None, index=False)
#     c+=1
#     print(f'{subfolder} done, total completion {(c / 71) * 100}%')

# for subfolder in os.listdir(folderpath):
#     stroke_count = 1
#     subfolder_path = os.path.join(folderpath, subfolder)
#     for i in os.listdir(subfolder_path):
#         textfile_path = os.path.join(subfolder_path, i)
#         df = pd.read_csv(textfile_path, sep=" ", header=None)
#         stroke_indices = df[df[2] == 0].index.tolist()
#         stroke_indices.append(len(df))
#         strokes = [df.iloc[stroke_indices[i]:stroke_indices[i + 1]] for i in range(len(stroke_indices) - 1)]
#         output_subfolder = os.path.join('All Strokes', subfolder)
#         os.makedirs(output_subfolder, exist_ok=True)
#         for j, stroke in enumerate(strokes):
#             stroke.to_csv(f'{output_subfolder}/Strokes_{stroke_count}.txt', sep=' ', header=None, index=False)
#             stroke_count += 1
#     c += 1
#     print(f'{subfolder} done, total completion {(c / 71) * 100}%')
os.makedirs('Strokes Dataset', exist_ok=True)

for subfolder in os.listdir(folderpath):
    subfolder_path = os.path.join(folderpath, subfolder)
    for i in os.listdir(subfolder_path):
        textfile_path = os.path.join(subfolder_path, i)
        df = pd.read_csv(textfile_path, sep=" ", header=None)
        stroke_indices = df[df[2] == 0].index.tolist()
        stroke_indices.append(len(df))
        strokes = [df.iloc[stroke_indices[i]:stroke_indices[i + 1]] for i in range(len(stroke_indices) - 1)]
        for j, stroke in enumerate(strokes):
            stroke.to_csv(f'Strokes Dataset/{i.split(".")[0]}_{j + 1}.txt', sep=' ', header=None, index=False)
    c+=1
    print(f'{subfolder} done, total completion {(c / 71) * 100}%')