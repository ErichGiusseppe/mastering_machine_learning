Celda de texto <c2d2864e>
# %% [markdown]
# Taller 1 - Universidad de los Andes

**Participantes:**

- Erich Giusseppe Soto Parada
- Diana Valentina Molina Murillo
- Haider Yesid Fonseca Najar


Celda de texto <6d9c6abe>
# %% [markdown]
instalaciones

Celda de código <ce1d1fa4>
# %% [code]
pip install pandas scikit-learn seaborn ydata_profiling imblearn
Resultado de la ejecución
6KB
	Stream
		Collecting pandas
		  Downloading pandas-2.3.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (91 kB)
		Collecting scikit-learn
		  Downloading scikit_learn-1.7.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (17 kB)
		Collecting seaborn
		  Using cached seaborn-0.13.2-py3-none-any.whl.metadata (5.4 kB)
		Requirement already satisfied: numpy>=1.23.2 in /home/erich/dev/mastering_machine_learning/taller_clase_2/.venv/lib/python3.11/site-packages (from pandas) (2.1.2)
		Requirement already satisfied: python-dateutil>=2.8.2 in /home/erich/dev/mastering_machine_learning/taller_clase_2/.venv/lib/python3.11/site-packages (from pandas) (2.9.0.post0)
		Collecting pytz>=2020.1 (from pandas)
		  Using cached pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
		Collecting tzdata>=2022.7 (from pandas)
		  Using cached tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
		Collecting scipy>=1.8.0 (from scikit-learn)
		  Downloading scipy-1.15.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (61 kB)
		Collecting joblib>=1.2.0 (from scikit-learn)
		  Using cached joblib-1.5.1-py3-none-any.whl.metadata (5.6 kB)
		Collecting threadpoolctl>=3.1.0 (from scikit-learn)
		  Using cached threadpoolctl-3.6.0-py3-none-any.whl.metadata (13 kB)
		Collecting matplotlib!=3.6.1,>=3.4 (from seaborn)
		  Downloading matplotlib-3.10.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (11 kB)
		Collecting contourpy>=1.0.1 (from matplotlib!=3.6.1,>=3.4->seaborn)
		  Downloading contourpy-1.3.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.5 kB)
		Collecting cycler>=0.10 (from matplotlib!=3.6.1,>=3.4->seaborn)
		  Using cached cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
		Collecting fonttools>=4.22.0 (from matplotlib!=3.6.1,>=3.4->seaborn)
		  Downloading fonttools-4.58.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (106 kB)
		Collecting kiwisolver>=1.3.1 (from matplotlib!=3.6.1,>=3.4->seaborn)
		  Downloading kiwisolver-1.4.8-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.2 kB)
		Requirement already satisfied: packaging>=20.0 in /home/erich/dev/mastering_machine_learning/taller_clase_2/.venv/lib/python3.11/site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (25.0)
		Requirement already satisfied: pillow>=8 in /home/erich/dev/mastering_machine_learning/taller_clase_2/.venv/lib/python3.11/site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (11.0.0)
		Collecting pyparsing>=2.3.1 (from matplotlib!=3.6.1,>=3.4->seaborn)
		  Using cached pyparsing-3.2.3-py3-none-any.whl.metadata (5.0 kB)
		Requirement already satisfied: six>=1.5 in /home/erich/dev/mastering_machine_learning/taller_clase_2/.venv/lib/python3.11/site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)
		Downloading pandas-2.3.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.4 MB)
		[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m12.4/12.4 MB[0m [31m90.3 MB/s[0m eta [36m0:00:00[0m
		[?25hDownloading scikit_learn-1.7.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.9 MB)
		[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m12.9/12.9 MB[0m [31m82.4 MB/s[0m eta [36m0:00:00[0m
		[?25hUsing cached seaborn-0.13.2-py3-none-any.whl (294 kB)
		Using cached joblib-1.5.1-py3-none-any.whl (307 kB)
		Downloading matplotlib-3.10.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (8.6 MB)
		[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m8.6/8.6 MB[0m [31m92.2 MB/s[0m eta [36m0:00:00[0m
		[?25hDownloading contourpy-1.3.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (326 kB)
		Using cached cycler-0.12.1-py3-none-any.whl (8.3 kB)
		Downloading fonttools-4.58.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (5.0 MB)
		[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m5.0/5.0 MB[0m [31m85.7 MB/s[0m eta [36m0:00:00[0m
		[?25hDownloading kiwisolver-1.4.8-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.4 MB)
		[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m1.4/1.4 MB[0m [31m71.6 MB/s[0m eta [36m0:00:00[0m
		[?25hUsing cached pyparsing-3.2.3-py3-none-any.whl (111 kB)
		Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
		Downloading scipy-1.15.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (37.7 MB)
		[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m37.7/37.7 MB[0m [31m96.3 MB/s[0m eta [36m0:00:00[0mta [36m0:00:01[0m
		[?25hUsing cached threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
		Using cached tzdata-2025.2-py2.py3-none-any.whl (347 kB)
		Installing collected packages: pytz, tzdata, threadpoolctl, scipy, pyparsing, kiwisolver, joblib, fonttools, cycler, contourpy, scikit-learn, pandas, matplotlib, seaborn
		[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m14/14[0m [seaborn]3/14[0m [seaborn]ib]n]
		[1A[2KSuccessfully installed contourpy-1.3.2 cycler-0.12.1 fonttools-4.58.4 joblib-1.5.1 kiwisolver-1.4.8 matplotlib-3.10.3 pandas-2.3.0 pyparsing-3.2.3 pytz-2025.2 scikit-learn-1.7.0 scipy-1.15.3 seaborn-0.13.2 threadpoolctl-3.6.0 tzdata-2025.2
		Note: you may need to restart the kernel to use updated packages.

Celda de código <I-6Ybf4sz8fJ>
# %% [code]
from google.colab import drive
drive.mount('/content/drive')

Celda de texto <71486364>
# %% [markdown]
### imports

Celda de código <2bc1e7f0>
# %% [code]
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import torch
from torch.nn.functional import one_hot
from torch.utils.data import Dataset, TensorDataset, DataLoader
import torch.nn as nn
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport
from sklearn.preprocessing import OneHotEncoder
from imblearn.over_sampling import SMOTE
from sklearn.metrics import (
    f1_score,
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)
%matplotlib inline

Celda de texto <d3bfa3d8>
# %% [markdown]
### Funciones

Celda de código <06a20997>
# %% [code]
def evaluate_model_classification(model, X, y, loss_fn, dataset_name="Test"):
    model.eval()
    with torch.no_grad():
        logits = model(X.float())[:, 0]
        loss = loss_fn(logits, y)
        probs = torch.sigmoid(logits)
        preds = (probs > 0.5).long()
        true = y.long()

        print(f"{dataset_name} Loss (BCEWithLogits): {loss.item():.4f}")

        # f1 = f1_score(true.cpu().numpy(), preds.cpu().numpy())
        # accuracy = accuracy_score(true.cpu().numpy(), preds.cpu().numpy())

        # print(f"{dataset_name} F1-Score: {f1:.4f}")
        # print(f"{dataset_name} Accuracy: {accuracy:.4f}")
        print(f"\n{dataset_name} Classification Report:\n")
        print(
            classification_report(
                true.cpu().numpy(),
                preds.cpu().numpy(),
                target_names=["Class 0", "Class 1"],
            )
        )

        y_true_np = true.cpu().numpy()
        y_pred_np = preds.cpu().numpy()
        cm = confusion_matrix(y_true_np, y_pred_np, labels=[0, 1])
        disp = ConfusionMatrixDisplay(
            confusion_matrix=cm, display_labels=["Class 0", "Class 1"]
        )
        disp.plot(cmap=plt.cm.Blues)
        plt.title(f"{dataset_name} - Matriz de Confusión")
        plt.show()

        # print(f"Matriz de Confusión ({dataset_name}):\n", cm)

Celda de texto <6cfb1063>
# %% [markdown]
### Carga de los datos

Celda de código <56afcdaa>
# %% [code]
data_mpg = (
    "/home/erich/dev/mastering_machine_learning/taller_clase_2/Erich/data/auto-mpg.data"
)

Celda de código <47c84a30>
# %% [code]
df = pd.read_csv(
    data_mpg,
    names=[
        "MPG",
        "Cylinders",
        "Displacement",
        "Horsepower",
        "Weight",
        "Acceleration",
        "Model Year",
        "Origin",
    ],
    sep=" ",
    na_values="?",
    comment="\t",
    skipinitialspace=True,
)

Celda de texto <f76e6efb>
# %% [markdown]
### Exploracion

Celda de código <c4f886d4>
# %% [code]
profile = ProfileReport(
    df,
    title="Reporte de Perfilado",
    explorative=True,
    correlations={
        "auto": {"calculate": False},
        "pearson": {"calculate": True},
        "spearman": {"calculate": True},
        "kendall": {"calculate": True},
        "phi_k": {"calculate": True},
        "cramers": {"calculate": False},
    },
)

Celda de código <7c5c3820>
# %% [code]
profile.to_notebook_iframe()
Resultado de la ejecución
3600KB
	Stream
		100%|██████████| 8/8 [00:00<00:00, 94254.02it/s]00:00, 108.39it/s, Describe variable: Origin]
		Summarize dataset: 100%|██████████| 56/56 [00:11<00:00,  4.76it/s, Completed]                         
		Generate report structure: 100%|██████████| 1/1 [00:02<00:00,  2.24s/it]
		Render HTML: 100%|██████████| 1/1 [00:00<00:00,  1.21it/s]

Celda de texto <c2f343ef>
# %% [markdown]
Podemos ver en el reporte que muchas de las variables estan altamente coorelacionadas pero dado que solo vamos a usar una no nos genera mayor problema.

Tambien centrandonos en por ejemplo los cilinders, estos tienen una clases con 3 y 5 que son muy inferiores en representatividad a nivel de clases comparados con el resto, por ende el modelo realmente no va a aprender de estas clases se recomienda o aniadirlas a otras de las clases cercanas o eliminar estos datos, aunque al ser ordinal no presenta un problema tan grabe.

Ademas como esta no va a ser la variable que se va a utilizar pues no se haran los cambios respectivos.

Celda de código <7a697105>
# %% [code]
df.head()
Resultado de la ejecución
3KB
	text/plain
		MPG  Cylinders  Displacement  Horsepower  Weight  Acceleration  \
		0  18.0          8         307.0       130.0  3504.0          12.0   
		1  15.0          8         350.0       165.0  3693.0          11.5   
		2  18.0          8         318.0       150.0  3436.0          11.0   
		3  16.0          8         304.0       150.0  3433.0          12.0   
		4  17.0          8         302.0       140.0  3449.0          10.5   
		
		   Model Year  Origin  
		0          70       1  
		1          70       1  
		2          70       1  
		3          70       1  
		4          70       1

Celda de código <58a43330>
# %% [code]
print(f"Shape:  \n{df.shape}\n")
print(f"Numero de nulos: \n{df.isna().sum()}")
Resultado de la ejecución
0KB
	Stream
		Shape:  
		(398, 8)
		
		Numero de nulos: 
		MPG             0
		Cylinders       0
		Displacement    0
		Horsepower      6
		Weight          0
		Acceleration    0
		Model Year      0
		Origin          0
		dtype: int64

Celda de código <285ec047>
# %% [code]
df = df.dropna()
df = df.reset_index(drop=True)
print(f"Shape:  \n{df.shape}\n")
print(f"Numero de nulos: \n{df.isna().sum()}")
Resultado de la ejecución
0KB
	Stream
		Shape:  
		(392, 8)
		
		Numero de nulos: 
		MPG             0
		Cylinders       0
		Displacement    0
		Horsepower      0
		Weight          0
		Acceleration    0
		Model Year      0
		Origin          0
		dtype: int64

Celda de texto <4dfe8e59>
# %% [markdown]
### Exploracion de los datos

Celda de código <4100f425>
# %% [code]
df.describe()
Resultado de la ejecución
4KB
	text/plain
		MPG   Cylinders  Displacement  Horsepower       Weight  \
		count  392.000000  392.000000    392.000000  392.000000   392.000000   
		mean    23.445918    5.471939    194.411990  104.469388  2977.584184   
		std      7.805007    1.705783    104.644004   38.491160   849.402560   
		min      9.000000    3.000000     68.000000   46.000000  1613.000000   
		25%     17.000000    4.000000    105.000000   75.000000  2225.250000   
		50%     22.750000    4.000000    151.000000   93.500000  2803.500000   
		75%     29.000000    8.000000    275.750000  126.000000  3614.750000   
		max     46.600000    8.000000    455.000000  230.000000  5140.000000   
		
		       Acceleration  Model Year      Origin  
		count    392.000000  392.000000  392.000000  
		mean      15.541327   75.979592    1.576531  
		std        2.758864    3.683737    0.805518  
		min        8.000000   70.000000    1.000000  
		25%       13.775000   73.000000    1.000000  
		50%       15.500000   76.000000    1.000000  
		75%       17.025000   79.000000    2.000000  
		max       24.800000   82.000000    3.000000

Celda de código <67820b5e>
# %% [code]
sns.pairplot(df)
Resultado de la ejecución
764KB
	text/plain
		<seaborn.axisgrid.PairGrid at 0x74199a3ea150>
		<Figure size 2000x2000 with 72 Axes>

Celda de texto <e784a297>
# %% [markdown]
Pareciera que muchas de las relaciones por ejemplo tiene mpg aunque pueden ser aproximadas mediante una funcion mas parecida a una exponencial negativa, esto teniendo en cuenta que solo se pueden usar capas lineales tendremos que intentar linealizar los datos del modelos lo mas posible para que el modelo dadas sus capacidades pueda hacer correctamente las predicciones, esto dado que nuestro modelo solo puede aprender relaciones lineales y el modelo de redes neuronales en este caso al no tener funcion de activacion son combinaciones lineales.

Celda de código <b6fb8b9c>
# %% [code]
df.columns
Resultado de la ejecución
0KB
	text/plain
		Index(['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight',
		       'Acceleration', 'Model Year', 'Origin'],
		      dtype='object')

Celda de código <76d4752a>
# %% [code]
# Se hace la prueba para visualizar si los cambios son los correctos se puede intentar usar boxcox
# para algo digamos automatizado pero dado el comportamiento se propone utilizar logaritmica dado que el comportamiento que se ve es exponencial.
columnas_transformacion = ["Displacement", "Horsepower", "Weight"]
df_try = df.copy()

for columna in columnas_transformacion:
    new_column = f"log_{columna}"
    df_try[new_column] = np.log(df_try[columna])
    df_try = df_try.drop(columns=columna)

Celda de código <06d77dd8>
# %% [code]
sns.pairplot(df_try)
Resultado de la ejecución
790KB
	text/plain
		<seaborn.axisgrid.PairGrid at 0x7419e7c77710>
		<Figure size 2000x2000 with 72 Axes>

Celda de texto <5e729e69>
# %% [markdown]
Ahora para comprobar que las transformaciones funcionaron o son mejores se pueden ver los resultados al implementar modelos o en su defecto podemos ver las correlaciones lineales que nos da pearson para ver que tanto mejoramos o no estas relaciones.

Celda de código <524dba35>
# %% [code]
sns.heatmap(df.corr(), annot=True)
Resultado de la ejecución
88KB
	text/plain
		<Axes: >
		<Figure size 640x480 with 2 Axes>

Celda de código <e211dce6>
# %% [code]
sns.heatmap(df_try.corr(), annot=True)
Resultado de la ejecución
91KB
	text/plain
		<Axes: >
		<Figure size 640x480 with 2 Axes>

Celda de texto <2668f3eb>
# %% [markdown]
vemos que si mejora un poco las coorelaciones lineales, por ende dejaremos las variables transformadas con logaritmos

Celda de texto <ab4146aa>
# %% [markdown]
# Parte 1

Celda de texto <fe4ee22e>
# %% [markdown]
Dadas las correlaciones la que tiene mayor coorelacion es la de log_weight por ende va a ser la que se va a utilizar, por ende partiremos los datos en X y Y.

Celda de código <65e3a523>
# %% [code]
df_try.columns
Resultado de la ejecución
0KB
	text/plain
		Index(['MPG', 'Cylinders', 'Acceleration', 'Model Year', 'Origin',
		       'log_Displacement', 'log_Horsepower', 'log_Weight'],
		      dtype='object')

Celda de código <63da025a>
# %% [code]
# X = df[["Weight"]]
# Y = df[["MPG"]]

Celda de código <9f65ba7d>
# %% [code]
X = df_try[["log_Weight"]]
Y = df_try[["MPG"]]

Celda de texto <151d8865>
# %% [markdown]
particion de los datos en train y test

Celda de código <2d6fc7f3>
# %% [code]
from sklearn.preprocessing import StandardScaler

Celda de código <240dd311>
# %% [code]
x_train, x_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=100
)  # 77
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
# x_train_scaled = pd.DataFrame(x_train_scaled, columns=x_train.columns, index=x_train.index)
x_train_scaled = torch.tensor(x_train_scaled).float()  # ['log_Weight'].values

x_test_scaled = scaler.transform(x_test)
# x_test_scaled = pd.DataFrame(x_test_scaled, columns=x_test.columns, index=x_test.index)
x_test_scaled = torch.tensor(x_test_scaled).float()  # ['log_Weight'].values

y_train_tensor = torch.tensor(y_train["MPG"].values).float()
y_test_tensor = torch.tensor(y_test["MPG"].values).float()

Celda de texto <231d217a>
# %% [markdown]
## Punto 1 y Punto 2

Celda de código <4e5cd1b0>
# %% [code]
from torch.utils.data import Dataset, TensorDataset, DataLoader

train_ds = TensorDataset(x_train_scaled, y_train_tensor)
batch_size = 16
torch.manual_seed(77)

train_dl = DataLoader(train_ds, batch_size, shuffle=True)

Celda de código <a82b6674>
# %% [code]
import torch.nn as nn

hidden_units = [1]
input_size = x_train.shape[1]

all_layers = []
for hidden_units_layer in hidden_units:
    layer = nn.Linear(input_size, hidden_units_layer)
    all_layers.append(layer)
    # all_layers.append(nn.ReLU())
    input_size = hidden_units_layer

# all_layers.append(nn.Linear(hidden_units[-1], 1))
model = nn.Sequential(*all_layers)

model
Resultado de la ejecución
0KB
	text/plain
		Sequential(
		  (0): Linear(in_features=1, out_features=1, bias=True)
		)

Celda de código <38c74606>
# %% [code]
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

torch.manual_seed(1)
num_epochs = 200
log_epochs = 20
loss_history = []

for epoch in range(num_epochs):
    loss_hist_train = 0
    for x_batch, y_batch in train_dl:
        pred = model(x_batch)[:, 0]
        loss = loss_fn(pred, y_batch)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        loss_hist_train += loss.item()

    avg_loss = loss_hist_train / len(train_dl)
    loss_history.append(avg_loss)
    if epoch % log_epochs == 0:
        print(f"Epoch {epoch} Loss {avg_loss:.4f}")
Resultado de la ejecución
0KB
	Stream
		Epoch 0 Loss 455.3168
		Epoch 20 Loss 18.6469
		Epoch 40 Loss 19.0664
		Epoch 60 Loss 18.8610
		Epoch 80 Loss 18.9167
		Epoch 100 Loss 18.7154
		Epoch 120 Loss 18.4465
		Epoch 140 Loss 19.0040
		Epoch 160 Loss 18.5777
		Epoch 180 Loss 18.4661

Celda de código <107a84e6>
# %% [code]
plt.figure(figsize=(8, 4))
plt.plot(loss_history)
plt.title("Historial de pérdida (MSE) durante el entrenamiento")
plt.xlabel("Época")
plt.ylabel("Pérdida")
plt.grid(True)
plt.show()
Resultado de la ejecución
31KB
	text/plain
		<Figure size 800x400 with 1 Axes>

Celda de código <ad899421>
# %% [code]
with torch.no_grad():

    pred = model(x_train_scaled.float())[:, 0]
    loss = loss_fn(pred, y_train_tensor)
    print(f"Train MSE: {loss.item():.4f}")
    print(f"Train MAE: {nn.L1Loss()(pred,y_train_tensor).item():.4f}")

    pred = model(x_test_scaled.float())[:, 0]
    loss = loss_fn(pred, y_test_tensor)
    print(f"Test MSE: {loss.item():.4f}")
    print(f"Test MAE: {nn.L1Loss()(pred,y_test_tensor).item():.4f}")
Resultado de la ejecución
0KB
	Stream
		Train MSE: 18.7309
		Train MAE: 3.2334
		Test MSE: 12.6695
		Test MAE: 2.7204

Celda de código <0c9fdd2f>
# %% [code]
x_plot = x_test_scaled[:, 0].numpy()
y_true = y_test_tensor.numpy()
y_pred = pred.numpy()

Celda de código <0562fc3b>
# %% [code]
plt.figure(figsize=(8, 5))
plt.scatter(x_plot, y_true, color="blue", label="Valores reales")
plt.scatter(x_plot, y_pred, color="red", alpha=0.6, label="Predicciones")
plt.plot(x_plot, y_pred, color="black", linewidth=1, label="Línea del modelo")
plt.title("Predicción del modelo vs valores reales")
plt.xlabel("Variable predictora")
plt.ylabel("Variable objetivo")
plt.legend()
plt.grid(True)
plt.show()
Resultado de la ejecución
61KB
	text/plain
		<Figure size 800x500 with 1 Axes>

Celda de texto <yplA4uQQvYJv>
# %% [markdown]
### Conclusión

Celda de texto <okQG3rqRvkJ0>
# %% [markdown]
En el primer modelo, abordamos el problema de manera simple, utilizando una regresión lineal, tal como lo especifica el enunciado. Este modelo se configuró con una sola capa y una única variable predictora: el peso, dado que presentaba la mayor correlación con la variable dependiente (MPG). Sin embargo, al analizar la relación en los gráficos, observamos que la relación no era lineal, por lo que decidimos aplicar una transformación logarítmica a la variable Peso.

Al evaluar el desempeño del modelo, encontramos que el MSE sin la transformación logarítmica fue de 13.8, mientras que con la transformación se redujo a 12.6, lo que representó una mejora significativa en el ajuste del modelo. Para optimizar aún más los resultados, se utilizaron las variables escaladas, lo que facilitó el proceso de aprendizaje y contribuyó a una mejor generalización del modelo.

Se utilizaron 200 épocas de entrenamiento, ya que, según las gráficas de evolución de la pérdida, este fue el punto en el que el modelo empezó a converger, alcanzando un equilibrio entre precisión y eficiencia en el proceso de optimización.

En resumen, este modelo inicial, aunque básico, muestra una mejora notable en el rendimiento gracias a la transformación logarítmica de los datos y el uso de escalado. Sin embargo, es importante señalar que aún hay espacio para mejorar, especialmente en modelos más complejos.


Celda de texto <cf9c9d95>
# %% [markdown]
### Punto 3

Celda de código <0ab7fe76>
# %% [code]
X = df[["Weight"]]
Y = df[["MPG"]]

Celda de código <565e155c>
# %% [code]
x_train, x_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=100
)  # 77
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
# x_train_scaled = pd.DataFrame(x_train_scaled, columns=x_train.columns, index=x_train.index)
x_train_scaled = torch.tensor(x_train_scaled).float()  # ['log_Weight'].values

x_test_scaled = scaler.transform(x_test)
# x_test_scaled = pd.DataFrame(x_test_scaled, columns=x_test.columns, index=x_test.index)
x_test_scaled = torch.tensor(x_test_scaled).float()  # ['log_Weight'].values

y_train_tensor = torch.tensor(y_train["MPG"].values).float()
y_test_tensor = torch.tensor(y_test["MPG"].values).float()

Celda de código <5da66840>
# %% [code]
from torch.utils.data import Dataset, TensorDataset, DataLoader
import torch.nn as nnx_test_scaled

input_size = x_train.shape[1]
y_train_tensor = torch.tensor(y_train["MPG"].values).float()
y_test_tensor = torch.tensor(y_test["MPG"].values).float()

train_ds = TensorDataset(x_train_scaled, y_train_tensor)
batch_size = 16
torch.manual_seed(77)

train_dl = DataLoader(train_ds, batch_size, shuffle=True)


hidden_units = []
input_size = x_train.shape[1]

all_layers = []

all_layers.append(nn.Linear(input_size, 1))
all_layers.append(nn.ReLU())
model = nn.Sequential(*all_layers)

model
Resultado de la ejecución
0KB
	text/plain
		Sequential(
		  (0): Linear(in_features=1, out_features=1, bias=True)
		  (1): ReLU()
		)

Celda de código <3f60590b>
# %% [code]
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

torch.manual_seed(1)
num_epochs = 200
log_epochs = 20
loss_history = []

for epoch in range(num_epochs):
    loss_hist_train = 0
    for x_batch, y_batch in train_dl:
        pred = model(x_batch)[:, 0]
        loss = loss_fn(pred, y_batch)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        loss_hist_train += loss.item()

    avg_loss = loss_hist_train / len(train_dl)
    loss_history.append(avg_loss)
    if epoch % log_epochs == 0:
        print(f"Epoch {epoch} Loss {avg_loss:.4f}")

plt.figure(figsize=(8, 4))
plt.plot(loss_history)
plt.title("Historial de pérdida (MSE) durante el entrenamiento")
plt.xlabel("Época")
plt.ylabel("Pérdida")
plt.grid(True)
plt.show()
with torch.no_grad():

    pred = model(x_train_scaled.float())[:, 0]
    loss = loss_fn(pred, y_train_tensor)
    print(f"Train MSE: {loss.item():.4f}")
    print(f"Train MAE: {nn.L1Loss()(pred,y_train_tensor).item():.4f}")

    pred = model(x_test_scaled.float())[:, 0]
    loss = loss_fn(pred, y_test_tensor)
    print(f"Test MSE: {loss.item():.4f}")
    print(f"Test MAE: {nn.L1Loss()(pred,y_test_tensor).item():.4f}")
x_plot = x_test_scaled[:, 0].numpy()
y_true = y_test_tensor.numpy()
y_pred = pred.numpy()
sorted_indices = np.argsort(x_plot)
x_plot_sorted = x_plot[sorted_indices]
y_pred_sorted = y_pred[sorted_indices]
plt.figure(figsize=(8, 5))
plt.scatter(x_plot, y_true, color="blue", label="Valores reales")
plt.scatter(x_plot, y_pred, color="red", alpha=0.6, label="Predicciones")
plt.plot(
    x_plot_sorted, y_pred_sorted, color="black", linewidth=1, label="Línea del modelo"
)
plt.title("Predicción del modelo vs valores reales")
plt.xlabel("Variable predictora")
plt.ylabel("Variable objetivo")
plt.legend()
plt.grid(True)
plt.show()
Resultado de la ejecución
100KB
	Stream
		Epoch 0 Loss 620.2462
		Epoch 20 Loss 155.6380
		Epoch 40 Loss 48.1410
		Epoch 60 Loss 25.6918
		Epoch 80 Loss 21.4649
		Epoch 100 Loss 20.1824
		Epoch 120 Loss 19.8168
		Epoch 140 Loss 20.2936
		Epoch 160 Loss 19.8907
		Epoch 180 Loss 19.7751
		Train MSE: 20.0787
		Train MAE: 3.4215
		Test MSE: 13.2642
		Test MAE: 2.8188
	text/plain
		<Figure size 800x400 with 1 Axes>
		<Figure size 800x500 with 1 Axes>

Celda de texto <2adfeab7>
# %% [markdown]
### Punto 4

Celda de código <32a1d8bf>
# %% [code]
from torch.utils.data import Dataset, TensorDataset, DataLoader
import torch.nn as nn

train_ds = TensorDataset(x_train_scaled, y_train_tensor)
batch_size = 16
torch.manual_seed(77)

train_dl = DataLoader(train_ds, batch_size, shuffle=True)


hidden_units = [3, 1]
input_size = x_train.shape[1]

all_layers = []
for hidden_units_layer in hidden_units:
    layer = nn.Linear(input_size, hidden_units_layer)
    all_layers.append(layer)
    all_layers.append(nn.ReLU())
    input_size = hidden_units_layer

all_layers.append(nn.Linear(hidden_units[-1], 1))
model = nn.Sequential(*all_layers)

model
Resultado de la ejecución
0KB
	text/plain
		Sequential(
		  (0): Linear(in_features=1, out_features=3, bias=True)
		  (1): ReLU()
		  (2): Linear(in_features=3, out_features=1, bias=True)
		  (3): ReLU()
		  (4): Linear(in_features=1, out_features=1, bias=True)
		)

Celda de código <6192e3f1>
# %% [code]
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

torch.manual_seed(1)
num_epochs = 200
log_epochs = 20
loss_history = []

for epoch in range(num_epochs):
    loss_hist_train = 0
    for x_batch, y_batch in train_dl:
        pred = model(x_batch)[:, 0]
        loss = loss_fn(pred, y_batch)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        loss_hist_train += loss.item()

    avg_loss = loss_hist_train / len(train_dl)
    loss_history.append(avg_loss)
    if epoch % log_epochs == 0:
        print(f"Epoch {epoch} Loss {avg_loss:.4f}")
Resultado de la ejecución
0KB
	Stream
		Epoch 0 Loss 561.1659
		Epoch 20 Loss 19.5885
		Epoch 40 Loss 19.3517
		Epoch 60 Loss 19.5545
		Epoch 80 Loss 19.1213
		Epoch 100 Loss 18.9642
		Epoch 120 Loss 18.6052
		Epoch 140 Loss 19.1235
		Epoch 160 Loss 19.2055
		Epoch 180 Loss 18.8484

Celda de código <b9650e70>
# %% [code]
plt.figure(figsize=(8, 4))
plt.plot(loss_history)
plt.title("Historial de pérdida (MSE) durante el entrenamiento")
plt.xlabel("Época")
plt.ylabel("Pérdida")
plt.grid(True)
plt.show()
Resultado de la ejecución
32KB
	text/plain
		<Figure size 800x400 with 1 Axes>

Celda de código <cfc42b82>
# %% [code]
with torch.no_grad():

    pred = model(x_train_scaled.float())[:, 0]
    loss = loss_fn(pred, y_train_tensor)
    print(f"Train MSE: {loss.item():.4f}")
    print(f"Train MAE: {nn.L1Loss()(pred,y_train_tensor).item():.4f}")

    pred = model(x_test_scaled.float())[:, 0]
    loss = loss_fn(pred, y_test_tensor)
    print(f"Test MSE: {loss.item():.4f}")
    print(f"Test MAE: {nn.L1Loss()(pred,y_test_tensor).item():.4f}")
Resultado de la ejecución
0KB
	Stream
		Train MSE: 18.8163
		Train MAE: 3.1548
		Test MSE: 12.2124
		Test MAE: 2.5750

Celda de código <6ba5a3a6>
# %% [code]
x_plot = x_test_scaled[:, 0].numpy()
y_true = y_test_tensor.numpy()
y_pred = pred.numpy()

Celda de código <33f5a237>
# %% [code]
sorted_indices = np.argsort(x_plot)
x_plot_sorted = x_plot[sorted_indices]
y_pred_sorted = y_pred[sorted_indices]

Celda de código <74a29238>
# %% [code]
plt.figure(figsize=(8, 5))
plt.scatter(x_plot, y_true, color="blue", label="Valores reales")
plt.scatter(x_plot, y_pred, color="red", alpha=0.6, label="Predicciones")
plt.plot(
    x_plot_sorted, y_pred_sorted, color="black", linewidth=1, label="Línea del modelo"
)
plt.title("Predicción del modelo vs valores reales")
plt.xlabel("Variable predictora")
plt.ylabel("Variable objetivo")
plt.legend()
plt.grid(True)
plt.show()
Resultado de la ejecución
65KB
	text/plain
		<Figure size 800x500 with 1 Axes>

Celda de código <4ebea13b>
# %% [code]
from torch.utils.data import Dataset, TensorDataset, DataLoader
import torch.nn as nn

train_ds = TensorDataset(x_train_scaled, y_train_tensor)
batch_size = 16
torch.manual_seed(77)

train_dl = DataLoader(train_ds, batch_size, shuffle=True)


hidden_units = [64, 32]
input_size = x_train.shape[1]

all_layers = []
for hidden_units_layer in hidden_units:
    layer = nn.Linear(input_size, hidden_units_layer)
    all_layers.append(layer)
    all_layers.append(nn.ReLU())
    input_size = hidden_units_layer

all_layers.append(nn.Linear(hidden_units[-1], 1))
model = nn.Sequential(*all_layers)

model
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

torch.manual_seed(1)
num_epochs = 200
log_epochs = 20
loss_history = []

for epoch in range(num_epochs):
    loss_hist_train = 0
    for x_batch, y_batch in train_dl:
        pred = model(x_batch)[:, 0]
        loss = loss_fn(pred, y_batch)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        loss_hist_train += loss.item()

    avg_loss = loss_hist_train / len(train_dl)
    loss_history.append(avg_loss)
    if epoch % log_epochs == 0:
        print(f"Epoch {epoch} Loss {avg_loss:.4f}")
plt.figure(figsize=(8, 4))
plt.plot(loss_history)
plt.title("Historial de pérdida (MSE) durante el entrenamiento")
plt.xlabel("Época")
plt.ylabel("Pérdida")
plt.grid(True)
plt.show()
with torch.no_grad():

    pred = model(x_train_scaled.float())[:, 0]
    loss = loss_fn(pred, y_train_tensor)
    print(f"Train MSE: {loss.item():.4f}")
    print(f"Train MAE: {nn.L1Loss()(pred,y_train_tensor).item():.4f}")

    pred = model(x_test_scaled.float())[:, 0]
    loss = loss_fn(pred, y_test_tensor)
    print(f"Test MSE: {loss.item():.4f}")
    print(f"Test MAE: {nn.L1Loss()(pred,y_test_tensor).item():.4f}")

x_plot = x_test_scaled[:, 0].numpy()
y_true = y_test_tensor.numpy()
y_pred = pred.numpy()
sorted_indices = np.argsort(x_plot)
x_plot_sorted = x_plot[sorted_indices]
y_pred_sorted = y_pred[sorted_indices]
plt.figure(figsize=(8, 5))
plt.scatter(x_plot, y_true, color="blue", label="Valores reales")
plt.scatter(x_plot, y_pred, color="red", alpha=0.6, label="Predicciones")
plt.plot(
    x_plot_sorted, y_pred_sorted, color="black", linewidth=1, label="Línea del modelo"
)
plt.title("Predicción del modelo vs valores reales")
plt.xlabel("Variable predictora")
plt.ylabel("Variable objetivo")
plt.legend()
plt.grid(True)
plt.show()
Resultado de la ejecución
101KB
	Stream
		Epoch 0 Loss 410.0155
		Epoch 20 Loss 19.3040
		Epoch 40 Loss 19.2217
		Epoch 60 Loss 19.6662
		Epoch 80 Loss 19.0624
		Epoch 100 Loss 18.9877
		Epoch 120 Loss 18.5123
		Epoch 140 Loss 18.9646
		Epoch 160 Loss 19.1508
		Epoch 180 Loss 18.7672
		Train MSE: 18.6389
		Train MAE: 3.1384
		Test MSE: 12.3655
		Test MAE: 2.6199
	text/plain
		<Figure size 800x400 with 1 Axes>
		<Figure size 800x500 with 1 Axes>

Celda de texto <y22MiXJy7QfT>
# %% [markdown]
### Conclusión

Celda de texto <d9d5a6c2>
# %% [markdown]
# Parte 2

Celda de código <aa8e2f2e>
# %% [code]
path_hearth = (
    "/home/erich/dev/mastering_machine_learning/taller_clase_2/Erich/data/heart.csv"
)
df_hearth = pd.read_csv(path_hearth)

Celda de texto <92e9c7b0>
# %% [markdown]
### Exploracion y limpieza

Celda de código <bc7e88fe>
# %% [code]
profile = ProfileReport(
    df_hearth,
    explorative=True,
    correlations={
        "auto": {"calculate": False},
        "pearson": {"calculate": True},
        "spearman": {"calculate": True},
        "kendall": {"calculate": True},
        "phi_k": {"calculate": True},
        "cramers": {"calculate": False},
    },
)

Celda de código <9018ca10>
# %% [code]
profile.to_notebook_iframe()
Resultado de la ejecución
2761KB
	Stream
		100%|██████████| 14/14 [00:00<00:00, 102478.63it/s]:00, 63.27it/s, Describe variable: target]
		Summarize dataset: 100%|██████████| 51/51 [00:03<00:00, 15.92it/s, Completed]                     
		Generate report structure: 100%|██████████| 1/1 [00:03<00:00,  3.66s/it]
		Render HTML: 100%|██████████| 1/1 [00:00<00:00,  1.17it/s]

Celda de texto <92646332>
# %% [markdown]
#### Dividimos en train y test

Celda de código <6f17ba49>
# %% [code]
path_hearth = (
    "/home/erich/dev/mastering_machine_learning/taller_clase_2/Erich/data/heart.csv"
)
df_hearth = pd.read_csv(path_hearth)

Celda de código <69f02bc6>
# %% [code]
df_train, df_test = train_test_split(
    df_hearth, test_size=0.2, random_state=100, stratify=df_hearth["target"]
)

Celda de texto <51dd9d3f>
# %% [markdown]
#### age

Celda de código <8b0f6501>
# %% [code]
sns.boxplot(df_train["age"])
Resultado de la ejecución
8KB
	text/plain
		<Axes: ylabel='age'>
		<Figure size 640x480 with 1 Axes>

Celda de texto <50341533>
# %% [markdown]
En general se observa una buena distribucion. Dado lo anterior, se decide no realizar cambios, al menos en esta fase.


Celda de texto <dd380245>
# %% [markdown]
#### Sex

Celda de código <b5df4e90>
# %% [code]
df_train["sex"].value_counts()
Resultado de la ejecución
0KB
	text/plain
		sex
		1    165
		0     77
		Name: count, dtype: int64

Celda de texto <3b1b9774>
# %% [markdown]
Se observan dos categorias y además existe un desbalance notable. Sin embargo, dado que este no es la variable objetivo no se realiza un cambio significativo.

Celda de texto <4f0c9a92>
# %% [markdown]
#### cp

Celda de código <e7203c53>
# %% [code]
df_train["cp"].value_counts()
Resultado de la ejecución
0KB
	text/plain
		cp
		4    112
		3     68
		2     37
		1     21
		0      4
		Name: count, dtype: int64

Celda de texto <29e97c19>
# %% [markdown]
Dado que la clase 0 tiene unicamente 4 representantes, se espera que al modelo le cueste entender mas las caracteristicas. En casos generales juntariamos el caso 0 con el 1 pero en este caso cp en https://archive.ics.uci.edu/dataset/45/heart+disease esta definido como:

cp: chest pain type
- Value 1: typical angina
- Value 2: atypical angina
- Value 3: non-anginal pain
- Value 4: asymptomatic

Por ende, se considera como un error y se elimina.

Celda de código <c5196aa6>
# %% [code]
df_train = df_train[df_train["cp"] != 0]

Celda de código <040a3867>
# %% [code]
df_train["cp"].value_counts()
Resultado de la ejecución
0KB
	text/plain
		cp
		4    112
		3     68
		2     37
		1     21
		Name: count, dtype: int64

Celda de texto <3b8f1b4f>
# %% [markdown]
#### trestbps

Celda de código <67252622>
# %% [code]
sns.boxplot(df_train["trestbps"])
Resultado de la ejecución
13KB
	text/plain
		<Axes: ylabel='trestbps'>
		<Figure size 640x480 with 1 Axes>

Celda de código <d859150d>
# %% [code]
df_train["trestbps"].describe()
Resultado de la ejecución
0KB
	text/plain
		count    238.000000
		mean     131.050420
		std       17.945463
		min       94.000000
		25%      120.000000
		50%      130.000000
		75%      140.000000
		max      200.000000
		Name: trestbps, dtype: float64

Celda de texto <aaf5d89e>
# %% [markdown]
Teniendo en cuenta los resultados vamos a eliminar los datos que se pasen del limite. Entonces, por ende, se eliminan los datos que se pasen de Q3 + 1.5 * IQR

Celda de código <9492aa5e>
# %% [code]
IQR = df_train["trestbps"].quantile(0.75) - df_train["trestbps"].quantile(0.25)

Celda de código <74268ca5>
# %% [code]
df_train["trestbps"].quantile(0.75) + 1.5 * IQR
Resultado de la ejecución
0KB
	text/plain
		np.float64(170.0)

Celda de código <d4881b82>
# %% [code]
df_train = df_train[df_train["trestbps"] <= 170]

Celda de código <3c2a34dc>
# %% [code]
sns.boxplot(df_train["trestbps"])
Resultado de la ejecución
12KB
	text/plain
		<Axes: ylabel='trestbps'>
		<Figure size 640x480 with 1 Axes>

Celda de texto <83244271>
# %% [markdown]
#### chol

Celda de código <199bf136>
# %% [code]
sns.boxplot(df_train["chol"])
Resultado de la ejecución
10KB
	text/plain
		<Axes: ylabel='chol'>
		<Figure size 640x480 with 1 Axes>

Celda de código <a627a0b9>
# %% [code]
IQR = df_train["chol"].quantile(0.75) - df_train["chol"].quantile(0.25)
threashold = df_train["chol"].quantile(0.75) + 1.5 * IQR


df_train = df_train[df_train["chol"] <= threashold]

Celda de código <65222cb3>
# %% [code]
sns.boxplot(df_train["chol"])
Resultado de la ejecución
10KB
	text/plain
		<Axes: ylabel='chol'>
		<Figure size 640x480 with 1 Axes>

Celda de texto <ef530780>
# %% [markdown]
#### restecg

Celda de código <1695a341>
# %% [code]
df_train["restecg"].value_counts()
Resultado de la ejecución
0KB
	text/plain
		restecg
		0    116
		2    108
		1      4
		Name: count, dtype: int64

Celda de texto <79fcb764>
# %% [markdown]
Teniendo en cuenta que solo hay 4 de la categoria 1 y este es having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV),se estima que el modelo no va a tener un aprendizaje real de esta categoria. Dado lo anterior, se toma como ruido y se eliminan los registros.

Celda de código <db6a19c3>
# %% [code]
df_train = df_train[df_train["restecg"] != 1]

Celda de código <fede783a>
# %% [code]
df_train["restecg"].value_counts()
Resultado de la ejecución
0KB
	text/plain
		restecg
		0    116
		2    108
		Name: count, dtype: int64

Celda de texto <49f0187d>
# %% [markdown]
#### thalach

Celda de código <d3f8c5e7>
# %% [code]
sns.boxplot(df_train["thalach"])
Resultado de la ejecución
10KB
	text/plain
		<Axes: ylabel='thalach'>
		<Figure size 640x480 with 1 Axes>

Celda de código <7a370c0a>
# %% [code]
IQR = df_train["thalach"].quantile(0.75) - df_train["thalach"].quantile(0.25)
threashold = df_train["thalach"].quantile(0.25) - 1.5 * IQR


df_train = df_train[df_train["thalach"] >= threashold]

Celda de código <93806863>
# %% [code]
sns.boxplot(df_train["thalach"])
Resultado de la ejecución
10KB
	text/plain
		<Axes: ylabel='thalach'>
		<Figure size 640x480 with 1 Axes>

Celda de texto <0c8200c4>
# %% [markdown]
#### exang

Celda de código <d53935cf>
# %% [code]
df_train["exang"].value_counts()
Resultado de la ejecución
0KB
	text/plain
		exang
		0    159
		1     65
		Name: count, dtype: int64

Celda de texto <ce15b63b>
# %% [markdown]
Existe desbalance, si embargo no se considera pertinente una intervención significativa.

Celda de texto <ccccf4f6>
# %% [markdown]
#### oldpeak

Celda de código <614a15eb>
# %% [code]
sns.boxplot(df_train["oldpeak"])
Resultado de la ejecución
10KB
	text/plain
		<Axes: ylabel='oldpeak'>
		<Figure size 640x480 with 1 Axes>

Celda de código <a9974491>
# %% [code]
IQR = df_train["oldpeak"].quantile(0.75) - df_train["oldpeak"].quantile(0.25)
upper_threashold = df_train["oldpeak"].quantile(0.75) + 1.5 * IQR
down_threashold = df_train["oldpeak"].quantile(0.25) - 1.5 * IQR

df_train = df_train[
    (df_train["oldpeak"] <= upper_threashold) & (df_train["oldpeak"] >= down_threashold)
]

Celda de código <0f791e6a>
# %% [code]
sns.boxplot(df_train["oldpeak"])
Resultado de la ejecución
12KB
	text/plain
		<Axes: ylabel='oldpeak'>
		<Figure size 640x480 with 1 Axes>

Celda de texto <7c393586>
# %% [markdown]
#### slope and ca

Celda de código <4e464e77>
# %% [code]
df_train[
    "slope"
].value_counts()  # Aunque sea pequenio se va a dejar el 3, pero es perfectamente eliminable.
Resultado de la ejecución
0KB
	text/plain
		slope
		1    109
		2     99
		3     13
		Name: count, dtype: int64

Celda de código <15eb1da1>
# %% [code]
df_train["ca"].value_counts()
Resultado de la ejecución
0KB
	text/plain
		ca
		0    128
		1     51
		2     32
		3     10
		Name: count, dtype: int64

Celda de texto <9d0fc889>
# %% [markdown]
#### thal

Celda de código <003f5d31>
# %% [code]
df_train["thal"].value_counts()  # se elimina la clase que tiene un solo elemento
Resultado de la ejecución
0KB
	text/plain
		thal
		normal        122
		reversible     84
		fixed          14
		2               1
		Name: count, dtype: int64

Celda de código <b83d1d0f>
# %% [code]
df_train = df_train[df_train["thal"] != "2"]

Celda de código <45a82ffc>
# %% [code]
df_train["thal"].value_counts()
Resultado de la ejecución
0KB
	text/plain
		thal
		normal        122
		reversible     84
		fixed          14
		Name: count, dtype: int64

Celda de código <0b6b4550>
# %% [code]
thal_col = df_train[["thal"]]

encoder = OneHotEncoder(
    drop="first", sparse_output=False, dtype=int, handle_unknown="ignore"
)

thal_encoded = encoder.fit_transform(thal_col)

thal_encoded_cols = encoder.get_feature_names_out(["thal"])

thal_encoded_df = pd.DataFrame(
    thal_encoded, columns=thal_encoded_cols, index=df_train.index
)

df_train = pd.concat([df_train.drop(columns="thal"), thal_encoded_df], axis=1)

Celda de código <b5da34c5>
# %% [code]
# Si hacemos One Hot encoding a train tambien lo tenemos que hacer a test y eso es lo que se va a hacer aca

thal_test_col = df_test[["thal"]]
thal_test_encoded = encoder.transform(thal_test_col)

thal_encoded_cols = encoder.get_feature_names_out(["thal"])

thal_test_encoded_df = pd.DataFrame(
    thal_test_encoded, columns=thal_encoded_cols, index=df_test.index
)

df_test = pd.concat([df_test.drop(columns="thal"), thal_test_encoded_df], axis=1)

Celda de texto <54677103>
# %% [markdown]
#### target (variable a predecir)

Celda de código <a9c676f4>
# %% [code]
df_train["target"].value_counts()
Resultado de la ejecución
0KB
	text/plain
		target
		0    163
		1     57
		Name: count, dtype: int64

Celda de texto <9b8849da>
# %% [markdown]
Como se puede ver se tiene un desbalance importante.Por ende, se procede a balancerlas


Celda de código <a74105bd>
# %% [code]
X = df_train.drop("target", axis=1)
y = df_train["target"]

smote = SMOTE(random_state=100)
X_resampled, y_resampled = smote.fit_resample(X, y)

df_resampled = pd.DataFrame(X_resampled, columns=X.columns)
df_resampled["target"] = y_resampled

Celda de código <8f736d2c>
# %% [code]
df_resampled["target"].value_counts()
Resultado de la ejecución
0KB
	text/plain
		target
		0    163
		1    163
		Name: count, dtype: int64

Celda de código <2b2702d5>
# %% [code]
df_resampled.head()
Resultado de la ejecución
4KB
	text/plain
		age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang  oldpeak  slope  \
		0   37    0   3       120   215    0        0      170      0      0.0      1   
		1   68    1   4       144   193    1        0      141      0      3.4      2   
		2   57    1   4       110   201    0        0      126      1      1.5      2   
		3   50    0   4       110   254    0        2      159      0      0.0      1   
		4   52    1   2       120   325    0        0      172      0      0.2      1   
		
		   ca  thal_normal  thal_reversible  target  
		0   0            1                0       0  
		1   2            0                1       1  
		2   0            0                0       0  
		3   0            1                0       0  
		4   0            1                0       0

Celda de texto <cec2e577>
# %% [markdown]
y asi tenemos las clases balanceadas y en general el dataset limpio

Celda de código <8221e778>
# %% [code]
df_hearth = df_resampled

Celda de código <ac0ec092>
# %% [code]
df_hearth
Resultado de la ejecución
7KB
	text/plain
		age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang   oldpeak  \
		0     37    0   3       120   215    0        0      170      0  0.000000   
		1     68    1   4       144   193    1        0      141      0  3.400000   
		2     57    1   4       110   201    0        0      126      1  1.500000   
		3     50    0   4       110   254    0        2      159      0  0.000000   
		4     52    1   2       120   325    0        0      172      0  0.200000   
		..   ...  ...  ..       ...   ...  ...      ...      ...    ...       ...   
		321   56    0   4       130   283    1        1      103      0  1.622257   
		322   52    1   4       118   185    0        0      113      0  1.460067   
		323   62    0   4       141   216    0        2      121      0  1.608364   
		324   64    1   3       134   253    0        1      127      0  2.795731   
		325   57    1   3       130   255    0        2      143      0  0.771919   
		
		     slope  ca  thal_normal  thal_reversible  target  
		0        1   0            1                0       0  
		1        2   2            0                1       1  
		2        2   0            0                0       0  
		3        1   0            1                0       0  
		4        1   0            1                0       0  
		..     ...  ..          ...              ...     ...  
		321      2   0            0                0       1  
		322      2   0            0                1       1  
		323      2   2            0                1       1  
		324      2   1            0                0       1  
		325      2   1            0                0       1  
		
		[326 rows x 15 columns]

Celda de texto <PAm_nAEBySr8>
# %% [markdown]


Celda de texto <3959ce74>
# %% [markdown]
### Mayor información

Celda de código <099ead41>
# %% [code]
from sklearn.preprocessing import StandardScaler, MinMaxScaler

numerical = ["age", "trestbps", "chol", "thalach", "oldpeak"]
binary = ["sex", "fbs", "restecg", "exang", "thal_normal", "thal_reversible"]
ordinal = ["slope", "ca", "cp"]


X_train, X_test, y_train, y_test = (
    df_train.drop("target", axis=1),
    df_test.drop("target", axis=1),
    df_train["target"],
    df_test["target"],
)

df_train, df_test = train_test_split(
    df_hearth, test_size=0.2, random_state=100, stratify=df_hearth["target"]
)

scaler_num = StandardScaler()
scaler_ord = MinMaxScaler()


X_train_num = pd.DataFrame(
    scaler_num.fit_transform(X_train[numerical]), columns=numerical, index=X_train.index
)
X_test_num = pd.DataFrame(
    scaler_num.transform(X_test[numerical]), columns=numerical, index=X_test.index
)

X_train_ord = pd.DataFrame(
    scaler_ord.fit_transform(X_train[ordinal]), columns=ordinal, index=X_train.index
)
X_test_ord = pd.DataFrame(
    scaler_ord.transform(X_test[ordinal]), columns=ordinal, index=X_test.index
)

X_train_bin = X_train[binary]
X_test_bin = X_test[binary]

X_train_processed = pd.concat([X_train_num, X_train_ord, X_train_bin], axis=1)


X_test_processed = pd.concat([X_test_num, X_test_ord, X_test_bin], axis=1)

X_train_processed = torch.tensor(X_train_processed.values).float()
X_test_processed = torch.tensor(X_test_processed.values).float()
y_train = torch.tensor(y_train.values).float()
y_test = torch.tensor(y_test.values).float()

Celda de código <e1d2eaa7>
# %% [code]
X_train_processed.shape
Resultado de la ejecución
0KB
	text/plain
		torch.Size([220, 14])

Celda de texto <fbe50186>
# %% [markdown]
### Punto 1 y 2

Celda de código <82a032d0>
# %% [code]
train_ds = TensorDataset(X_train_processed, y_train)
batch_size = 16
torch.manual_seed(77)

train_dl = DataLoader(train_ds, batch_size, shuffle=True)


hidden_units = [32, 16, 2]
input_size = X_train_processed.shape[1]

all_layers = []
for hidden_units_layer in hidden_units:
    layer = nn.Linear(input_size, hidden_units_layer)
    all_layers.append(layer)
    all_layers.append(nn.ReLU())
    input_size = hidden_units_layer

all_layers.append(nn.Linear(hidden_units[-1], 1))
model = nn.Sequential(*all_layers)

model
Resultado de la ejecución
0KB
	text/plain
		Sequential(
		  (0): Linear(in_features=14, out_features=32, bias=True)
		  (1): ReLU()
		  (2): Linear(in_features=32, out_features=16, bias=True)
		  (3): ReLU()
		  (4): Linear(in_features=16, out_features=2, bias=True)
		  (5): ReLU()
		  (6): Linear(in_features=2, out_features=1, bias=True)
		)

Celda de código <83e853cf>
# %% [code]
loss_fn = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

torch.manual_seed(1)
num_epochs = 200
log_epochs = 20
loss_history = []

for epoch in range(num_epochs):
    loss_hist_train = 0
    for x_batch, y_batch in train_dl:
        pred = model(x_batch)[:, 0]
        loss = loss_fn(pred, y_batch)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        loss_hist_train += loss.item()

    avg_loss = loss_hist_train / len(train_dl)
    loss_history.append(avg_loss)
    if epoch % log_epochs == 0:
        print(f"Epoch {epoch} Loss {avg_loss:.4f}")
Resultado de la ejecución
0KB
	Stream
		Epoch 0 Loss 0.7661
		Epoch 20 Loss 0.3349
		Epoch 40 Loss 0.2304
		Epoch 60 Loss 0.1816
		Epoch 80 Loss 0.1316
		Epoch 100 Loss 0.0849
		Epoch 120 Loss 0.0546
		Epoch 140 Loss 0.0334
		Epoch 160 Loss 0.0226
		Epoch 180 Loss 0.0177

Celda de código <3796d426>
# %% [code]
plt.figure(figsize=(8, 4))
plt.plot(loss_history)
plt.title("Historial de pérdida (MSE) durante el entrenamiento")
plt.xlabel("Época")
plt.ylabel("Pérdida")
plt.grid(True)
plt.show()
Resultado de la ejecución
40KB
	text/plain
		<Figure size 800x400 with 1 Axes>

Celda de código <84f3a2e6>
# %% [code]
evaluate_model_classification(
    model, X_train_processed, y_train, loss_fn, dataset_name="Train"
)
evaluate_model_classification(
    model, X_test_processed, y_test, loss_fn, dataset_name="Test"
)
Resultado de la ejecución
52KB
	Stream
		Train Loss (BCEWithLogits): 0.0108
		
		Train Classification Report:
		
		              precision    recall  f1-score   support
		
		     Class 0       1.00      1.00      1.00       163
		     Class 1       1.00      1.00      1.00        57
		
		    accuracy                           1.00       220
		   macro avg       1.00      1.00      1.00       220
		weighted avg       1.00      1.00      1.00       220
		Test Loss (BCEWithLogits): 2.0264
		
		Test Classification Report:
		
		              precision    recall  f1-score   support
		
		     Class 0       0.81      0.86      0.84        44
		     Class 1       0.57      0.47      0.52        17
		
		    accuracy                           0.75        61
		   macro avg       0.69      0.67      0.68        61
		weighted avg       0.74      0.75      0.75        61
	text/plain
		<Figure size 640x480 with 2 Axes>
		<Figure size 640x480 with 2 Axes>

Celda de texto <CypyMPT30HEu>
# %% [markdown]
## Análisis punto 1 y punto 2
El modelo base realizado, entrenado y con activación ReLU mostró un comportamiento usual en sobreajuste.

En principio, en la fase de entrenamiento tuvo una perdida muy baja de 0.0108 y las métricas resultantes obtuvieron 100% de precisión y recall en ambas clases. Además, vale la pena resaltar que al observar la matriz de confusión se evidencia que el modelo logró clasificar correctamente todos los elementos asociados al conjunto de entrenamiento. El f1-score fue de 1.

Por otro lado, el modelo en prueba demostró que la perdida aumento hasta tomar el valor de 2.0264 y el desempeño disminuyó: Accuracy: 75%, Precision class 1: 0.57 y recall class: 0.47. Además, en la matriz de confusión de la prueba se observa que el modelo clasificó mal 9 de los 17 casos positivos. Además, dados los resultados del F1-score se puede observar que el modelo comete errores en predecir la enfermedad y no detecta varios casos positivos al tener un bajo recall.

Al analizar la curva de perdida se concluye que el modelo aprendió de forma rápida y continuó mejorando en el entrenamiento. Sin embargo, no se generaliza bien el conjunto de prueba.

Celda de texto <f6801919>
# %% [markdown]
### Punto 3

Celda de texto <a9d6bb89>
# %% [markdown]
##### Caso 1

Celda de código <cc8af4ea>
# %% [code]
train_ds = TensorDataset(X_train_processed, y_train)
batch_size = 16
torch.manual_seed(77)

train_dl = DataLoader(train_ds, batch_size, shuffle=True)
hidden_units = [8, 5, 2]
input_size = X_train_processed.shape[1]

all_layers = []
for hidden_units_layer in hidden_units:
    layer = nn.Linear(input_size, hidden_units_layer)
    all_layers.append(layer)
    all_layers.append(nn.ReLU())
    input_size = hidden_units_layer

all_layers.append(nn.Linear(hidden_units[-1], 1))
model = nn.Sequential(*all_layers)

model

loss_fn = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

torch.manual_seed(1)
num_epochs = 200
log_epochs = 20
loss_history = []

for epoch in range(num_epochs):
    loss_hist_train = 0
    for x_batch, y_batch in train_dl:
        pred = model(x_batch)[:, 0]
        loss = loss_fn(pred, y_batch)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        loss_hist_train += loss.item()

    avg_loss = loss_hist_train / len(train_dl)
    loss_history.append(avg_loss)
    if epoch % log_epochs == 0:
        print(f"Epoch {epoch} Loss {avg_loss:.4f}")
plt.figure(figsize=(8, 4))
plt.plot(loss_history)
plt.title("Historial de pérdida (MSE) durante el entrenamiento")
plt.xlabel("Época")
plt.ylabel("Pérdida")
plt.grid(True)
plt.show()

evaluate_model_classification(
    model, X_train_processed, y_train, loss_fn, dataset_name="Train"
)
evaluate_model_classification(
    model, X_test_processed, y_test, loss_fn, dataset_name="Test"
)
Resultado de la ejecución
91KB
	Stream
		Epoch 0 Loss 0.6961
		Epoch 20 Loss 0.4154
		Epoch 40 Loss 0.3460
		Epoch 60 Loss 0.3172
		Epoch 80 Loss 0.3009
		Epoch 100 Loss 0.2728
		Epoch 120 Loss 0.2594
		Epoch 140 Loss 0.2445
		Epoch 160 Loss 0.2323
		Epoch 180 Loss 0.2248
		Train Loss (BCEWithLogits): 0.2054
		
		Train Classification Report:
		
		              precision    recall  f1-score   support
		
		     Class 0       0.99      0.92      0.95       163
		     Class 1       0.81      0.96      0.88        57
		
		    accuracy                           0.93       220
		   macro avg       0.90      0.94      0.92       220
		weighted avg       0.94      0.93      0.93       220
		Test Loss (BCEWithLogits): 0.5688
		
		Test Classification Report:
		
		              precision    recall  f1-score   support
		
		     Class 0       0.83      0.86      0.84        44
		     Class 1       0.60      0.53      0.56        17
		
		    accuracy                           0.77        61
		   macro avg       0.71      0.70      0.70        61
		weighted avg       0.76      0.77      0.77        61
	text/plain
		<Figure size 800x400 with 1 Axes>
		<Figure size 640x480 with 2 Axes>
		<Figure size 640x480 with 2 Axes>

Celda de texto <8eaddae7>
# %% [markdown]
##### Caso 2

Celda de código <30e7c0de>
# %% [code]
train_ds = TensorDataset(X_train_processed, y_train)
batch_size = 16
torch.manual_seed(77)

train_dl = DataLoader(train_ds, batch_size, shuffle=True)

hidden_units = [12, 4, 2]
input_size = X_train_processed.shape[1]

all_layers = []
for hidden_units_layer in hidden_units:
    layer = nn.Linear(input_size, hidden_units_layer)
    all_layers.append(layer)
    all_layers.append(nn.ReLU())
    input_size = hidden_units_layer

all_layers.append(nn.Linear(hidden_units[-1], 1))
model = nn.Sequential(*all_layers)

model

loss_fn = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

torch.manual_seed(1)
num_epochs = 200
log_epochs = 20
loss_history = []

for epoch in range(num_epochs):
    loss_hist_train = 0
    for x_batch, y_batch in train_dl:
        pred = model(x_batch)[:, 0]
        loss = loss_fn(pred, y_batch)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        loss_hist_train += loss.item()

    avg_loss = loss_hist_train / len(train_dl)
    loss_history.append(avg_loss)
    if epoch % log_epochs == 0:
        print(f"Epoch {epoch} Loss {avg_loss:.4f}")
plt.figure(figsize=(8, 4))
plt.plot(loss_history)
plt.title("Historial de pérdida (MSE) durante el entrenamiento")
plt.xlabel("Época")
plt.ylabel("Pérdida")
plt.grid(True)
plt.show()

evaluate_model_classification(
    model, X_train_processed, y_train, loss_fn, dataset_name="Train"
)
evaluate_model_classification(
    model, X_test_processed, y_test, loss_fn, dataset_name="Test"
)
Resultado de la ejecución
96KB
	Stream
		Epoch 0 Loss 0.6072
		Epoch 20 Loss 0.3967
		Epoch 40 Loss 0.3409
		Epoch 60 Loss 0.3135
		Epoch 80 Loss 0.2997
		Epoch 100 Loss 0.2742
		Epoch 120 Loss 0.2627
		Epoch 140 Loss 0.2499
		Epoch 160 Loss 0.2407
		Epoch 180 Loss 0.2372
		Train Loss (BCEWithLogits): 0.2197
		
		Train Classification Report:
		
		              precision    recall  f1-score   support
		
		     Class 0       0.97      0.93      0.95       163
		     Class 1       0.82      0.93      0.87        57
		
		    accuracy                           0.93       220
		   macro avg       0.89      0.93      0.91       220
		weighted avg       0.93      0.93      0.93       220
		Test Loss (BCEWithLogits): 0.5816
		
		Test Classification Report:
		
		              precision    recall  f1-score   support
		
		     Class 0       0.86      0.86      0.86        44
		     Class 1       0.65      0.65      0.65        17
		
		    accuracy                           0.80        61
		   macro avg       0.76      0.76      0.76        61
		weighted avg       0.80      0.80      0.80        61
	text/plain
		<Figure size 800x400 with 1 Axes>
		<Figure size 640x480 with 2 Axes>
		<Figure size 640x480 with 2 Axes>

Celda de texto <329f3767>
# %% [markdown]
## Punto 4

Celda de texto <d8c6626c>
# %% [markdown]
### Caso 1

Celda de código <283b09a7>
# %% [code]
train_ds = TensorDataset(X_train_processed, y_train)
batch_size = 16
torch.manual_seed(77)

train_dl = DataLoader(train_ds, batch_size, shuffle=True)

hidden_units = [10, 5]
input_size = X_train_processed.shape[1]

all_layers = []
for hidden_units_layer in hidden_units:
    layer = nn.Linear(input_size, hidden_units_layer)
    all_layers.append(layer)
    all_layers.append(nn.ReLU())
    input_size = hidden_units_layer

all_layers.append(nn.Linear(hidden_units[-1], 1))
model = nn.Sequential(*all_layers)

model

loss_fn = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

torch.manual_seed(1)
num_epochs = 200
log_epochs = 20
loss_history = []

for epoch in range(num_epochs):
    loss_hist_train = 0
    for x_batch, y_batch in train_dl:
        pred = model(x_batch)[:, 0]
        loss = loss_fn(pred, y_batch)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        loss_hist_train += loss.item()

    avg_loss = loss_hist_train / len(train_dl)
    loss_history.append(avg_loss)
    if epoch % log_epochs == 0:
        print(f"Epoch {epoch} Loss {avg_loss:.4f}")
plt.figure(figsize=(8, 4))
plt.plot(loss_history)
plt.title("Historial de pérdida (MSE) durante el entrenamiento")
plt.xlabel("Época")
plt.ylabel("Pérdida")
plt.grid(True)
plt.show()

evaluate_model_classification(
    model, X_train_processed, y_train, loss_fn, dataset_name="Train"
)
evaluate_model_classification(
    model, X_test_processed, y_test, loss_fn, dataset_name="Test"
)
Resultado de la ejecución
91KB
	Stream
		Epoch 0 Loss 0.6972
		Epoch 20 Loss 0.3446
		Epoch 40 Loss 0.2950
		Epoch 60 Loss 0.2790
		Epoch 80 Loss 0.2665
		Epoch 100 Loss 0.2485
		Epoch 120 Loss 0.2383
		Epoch 140 Loss 0.2268
		Epoch 160 Loss 0.2193
		Epoch 180 Loss 0.2134
		Train Loss (BCEWithLogits): 0.1992
		
		Train Classification Report:
		
		              precision    recall  f1-score   support
		
		     Class 0       0.97      0.91      0.94       163
		     Class 1       0.79      0.93      0.85        57
		
		    accuracy                           0.92       220
		   macro avg       0.88      0.92      0.90       220
		weighted avg       0.93      0.92      0.92       220
		Test Loss (BCEWithLogits): 0.5400
		
		Test Classification Report:
		
		              precision    recall  f1-score   support
		
		     Class 0       0.86      0.84      0.85        44
		     Class 1       0.61      0.65      0.63        17
		
		    accuracy                           0.79        61
		   macro avg       0.74      0.74      0.74        61
		weighted avg       0.79      0.79      0.79        61
	text/plain
		<Figure size 800x400 with 1 Axes>
		<Figure size 640x480 with 2 Axes>
		<Figure size 640x480 with 2 Axes>

Celda de texto <b5363d3b>
# %% [markdown]
### Caso 2

Celda de código <7cc89dab>
# %% [code]
train_ds = TensorDataset(X_train_processed, y_train)
batch_size = 16
torch.manual_seed(77)

train_dl = DataLoader(train_ds, batch_size, shuffle=True)

hidden_units = [10]
input_size = X_train_processed.shape[1]

all_layers = []
for hidden_units_layer in hidden_units:
    layer = nn.Linear(input_size, hidden_units_layer)
    all_layers.append(layer)
    all_layers.append(nn.ReLU())
    input_size = hidden_units_layer

all_layers.append(nn.Linear(hidden_units[-1], 1))
model = nn.Sequential(*all_layers)

model

loss_fn = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

torch.manual_seed(1)
num_epochs = 200
log_epochs = 20
loss_history = []

for epoch in range(num_epochs):
    loss_hist_train = 0
    for x_batch, y_batch in train_dl:
        pred = model(x_batch)[:, 0]
        loss = loss_fn(pred, y_batch)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        loss_hist_train += loss.item()

    avg_loss = loss_hist_train / len(train_dl)
    loss_history.append(avg_loss)
    if epoch % log_epochs == 0:
        print(f"Epoch {epoch} Loss {avg_loss:.4f}")
plt.figure(figsize=(8, 4))
plt.plot(loss_history)
plt.title("Historial de pérdida (MSE) durante el entrenamiento")
plt.xlabel("Época")
plt.ylabel("Pérdida")
plt.grid(True)
plt.show()
evaluate_model_classification(
    model, X_train_processed, y_train, loss_fn, dataset_name="Train"
)
evaluate_model_classification(
    model, X_test_processed, y_test, loss_fn, dataset_name="Test"
)
Resultado de la ejecución
91KB
	Stream
		Epoch 0 Loss 0.7451
		Epoch 20 Loss 0.4502
		Epoch 40 Loss 0.3486
		Epoch 60 Loss 0.3220
		Epoch 80 Loss 0.3123
		Epoch 100 Loss 0.2985
		Epoch 120 Loss 0.2899
		Epoch 140 Loss 0.2817
		Epoch 160 Loss 0.2776
		Epoch 180 Loss 0.2693
		Train Loss (BCEWithLogits): 0.2563
		
		Train Classification Report:
		
		              precision    recall  f1-score   support
		
		     Class 0       0.92      0.93      0.93       163
		     Class 1       0.80      0.77      0.79        57
		
		    accuracy                           0.89       220
		   macro avg       0.86      0.85      0.86       220
		weighted avg       0.89      0.89      0.89       220
		Test Loss (BCEWithLogits): 0.4453
		
		Test Classification Report:
		
		              precision    recall  f1-score   support
		
		     Class 0       0.82      0.93      0.87        44
		     Class 1       0.73      0.47      0.57        17
		
		    accuracy                           0.80        61
		   macro avg       0.77      0.70      0.72        61
		weighted avg       0.79      0.80      0.79        61
	text/plain
		<Figure size 800x400 with 1 Axes>
		<Figure size 640x480 with 2 Axes>
		<Figure size 640x480 with 2 Axes>

Celda de texto <PkU8SnLL336w>
# %% [markdown]
### Conclusión

Celda de texto <0eAT0GhG36f_>
# %% [markdown]


Celda de texto <d946c0df>
# %% [markdown]
#### Punto 5

Celda de texto <ea521b24>
# %% [markdown]
##### Caso 1

Celda de código <a59eacce>
# %% [code]
train_ds = TensorDataset(X_train_processed, y_train)
batch_size = 16
torch.manual_seed(77)

train_dl = DataLoader(train_ds, batch_size, shuffle=True)

hidden_units = [10, 5, 2]
input_size = X_train_processed.shape[1]

all_layers = []
for hidden_units_layer in hidden_units:
    layer = nn.Linear(input_size, hidden_units_layer)
    all_layers.append(layer)
    all_layers.append(nn.LeakyReLU())
    input_size = hidden_units_layer

all_layers.append(nn.Linear(hidden_units[-1], 1))
model = nn.Sequential(*all_layers)

model

loss_fn = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

torch.manual_seed(1)
num_epochs = 200
log_epochs = 20
loss_history = []

for epoch in range(num_epochs):
    loss_hist_train = 0
    for x_batch, y_batch in train_dl:
        pred = model(x_batch)[:, 0]
        loss = loss_fn(pred, y_batch)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        loss_hist_train += loss.item()

    avg_loss = loss_hist_train / len(train_dl)
    loss_history.append(avg_loss)
    if epoch % log_epochs == 0:
        print(f"Epoch {epoch} Loss {avg_loss:.4f}")
plt.figure(figsize=(8, 4))
plt.plot(loss_history)
plt.title("Historial de pérdida (MSE) durante el entrenamiento")
plt.xlabel("Época")
plt.ylabel("Pérdida")
plt.grid(True)
plt.show()

evaluate_model_classification(
    model, X_train_processed, y_train, loss_fn, dataset_name="Train"
)
evaluate_model_classification(
    model, X_test_processed, y_test, loss_fn, dataset_name="Test"
)
Resultado de la ejecución
97KB
	Stream
		Epoch 0 Loss 0.6126
		Epoch 20 Loss 0.4578
		Epoch 40 Loss 0.2977
		Epoch 60 Loss 0.2743
		Epoch 80 Loss 0.2610
		Epoch 100 Loss 0.2440
		Epoch 120 Loss 0.2368
		Epoch 140 Loss 0.2264
		Epoch 160 Loss 0.2204
		Epoch 180 Loss 0.2165
		Train Loss (BCEWithLogits): 0.2049
		
		Train Classification Report:
		
		              precision    recall  f1-score   support
		
		     Class 0       0.95      0.91      0.93       163
		     Class 1       0.77      0.88      0.82        57
		
		    accuracy                           0.90       220
		   macro avg       0.86      0.89      0.88       220
		weighted avg       0.91      0.90      0.90       220
		Test Loss (BCEWithLogits): 0.5742
		
		Test Classification Report:
		
		              precision    recall  f1-score   support
		
		     Class 0       0.85      0.89      0.87        44
		     Class 1       0.67      0.59      0.62        17
		
		    accuracy                           0.80        61
		   macro avg       0.76      0.74      0.75        61
		weighted avg       0.80      0.80      0.80        61
	text/plain
		<Figure size 800x400 with 1 Axes>
		<Figure size 640x480 with 2 Axes>
		<Figure size 640x480 with 2 Axes>

Celda de texto <868a1495>
# %% [markdown]
##### Caso 2

Celda de código <2bd3b4b3>
# %% [code]
train_ds = TensorDataset(X_train_processed, y_train)
batch_size = 16
torch.manual_seed(77)

train_dl = DataLoader(train_ds, batch_size, shuffle=True)

hidden_units = [10, 5, 2]
input_size = X_train_processed.shape[1]

all_layers = []
for hidden_units_layer in hidden_units:
    layer = nn.Linear(input_size, hidden_units_layer)
    all_layers.append(layer)
    all_layers.append(nn.Tanh())
    input_size = hidden_units_layer

all_layers.append(nn.Linear(hidden_units[-1], 1))
model = nn.Sequential(*all_layers)

model

loss_fn = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

torch.manual_seed(1)
num_epochs = 200
log_epochs = 20
loss_history = []

for epoch in range(num_epochs):
    loss_hist_train = 0
    for x_batch, y_batch in train_dl:
        pred = model(x_batch)[:, 0]
        loss = loss_fn(pred, y_batch)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        loss_hist_train += loss.item()

    avg_loss = loss_hist_train / len(train_dl)
    loss_history.append(avg_loss)
    if epoch % log_epochs == 0:
        print(f"Epoch {epoch} Loss {avg_loss:.4f}")
plt.figure(figsize=(8, 4))
plt.plot(loss_history)
plt.title("Historial de pérdida (MSE) durante el entrenamiento")
plt.xlabel("Época")
plt.ylabel("Pérdida")
plt.grid(True)
plt.show()
evaluate_model_classification(
    model, X_train_processed, y_train, loss_fn, dataset_name="Train"
)
evaluate_model_classification(
    model, X_test_processed, y_test, loss_fn, dataset_name="Test"
)
Resultado de la ejecución
91KB
	Stream
		Epoch 0 Loss 0.6518
		Epoch 20 Loss 0.3758
		Epoch 40 Loss 0.3178
		Epoch 60 Loss 0.2933
		Epoch 80 Loss 0.2787
		Epoch 100 Loss 0.2591
		Epoch 120 Loss 0.2494
		Epoch 140 Loss 0.2376
		Epoch 160 Loss 0.2311
		Epoch 180 Loss 0.2256
		Train Loss (BCEWithLogits): 0.2086
		
		Train Classification Report:
		
		              precision    recall  f1-score   support
		
		     Class 0       0.99      0.91      0.95       163
		     Class 1       0.80      0.96      0.87        57
		
		    accuracy                           0.93       220
		   macro avg       0.89      0.94      0.91       220
		weighted avg       0.94      0.93      0.93       220
		Test Loss (BCEWithLogits): 0.6110
		
		Test Classification Report:
		
		              precision    recall  f1-score   support
		
		     Class 0       0.82      0.82      0.82        44
		     Class 1       0.53      0.53      0.53        17
		
		    accuracy                           0.74        61
		   macro avg       0.67      0.67      0.67        61
		weighted avg       0.74      0.74      0.74        61
	text/plain
		<Figure size 800x400 with 1 Axes>
		<Figure size 640x480 with 2 Axes>
		<Figure size 640x480 with 2 Axes>


