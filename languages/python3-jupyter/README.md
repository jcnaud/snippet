# Jupyter

## Machine learning

- Supervised algorithm
  - classification
  - regression
- Not supervised algorithm
  - partitionning
  - anomaly detection
  - dimension reduction
  - ...

## Princinpe

Phase
- learning
- tests
  - cross test : GridSearchCV, RandomizedSearchCV





# Regression

type:
- linear
- Polynomial
- logictic (pour classification) == regressio + decision function



n: number of parameter

m: number of case

GD: Gradient decent

| Agorithm | m big | ram used | n big | Hyper params | Make data normalisation | On Scikit-learn |
|--- |--- |--- |--- |--- |--- |--- |
| normale Equation  (analytique) | speed | low ram | slow | 0 | no | LinearRegression|
| DG ordinaire | slow | low ram | slow | 2 | yes |null|
| DG Equation  | speed | higth ram | slow | >=2 | yes | SGDRegressor|
| DG Equation  | speed | higth ram | slow | >=2 | yes |SGDRegressor |

Regression polynomial:

PolynomialFeature
