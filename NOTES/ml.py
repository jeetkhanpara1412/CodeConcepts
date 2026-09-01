import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================================
# MACHINE LEARNING - FULL NOTES
# ==========================================================


# ----------------------------------------------------------
# Machine Learning - Getting Started
# ----------------------------------------------------------
# - Machine Learning (ML) is a program that analyzes data and
#   learns to predict outcomes, without being explicitly programmed.
# - Main types: Supervised Learning, Unsupervised Learning,
#   Reinforcement Learning.
# - Common libraries: NumPy, Pandas, Matplotlib, SciPy, scikit-learn.
# - Typical workflow: collect data -> clean/prepare -> train model
#   -> evaluate -> predict.
print("ML Getting Started - see comments above")


# ----------------------------------------------------------
# Mean Median Mode
# ----------------------------------------------------------
# - Mean = average of all values.
# - Median = middle value when data is sorted.
# - Mode = most frequently occurring value.

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x_mean = np.mean(speed)     # sub-point: mean
print(x_mean)

x_median = np.median(speed)  # sub-point: median
print(x_median)

from scipy import stats
x_mode = stats.mode(speed, keepdims=True)  # sub-point: mode
print(x_mode)


# ----------------------------------------------------------
# Standard Deviation
# ----------------------------------------------------------
# - Standard deviation measures how spread out values are.
# - Low std = values are close to the mean.
# - High std = values are spread over a wider range.
# - Variance is the average of squared differences from the mean.
# - std = sqrt(variance)

speed2 = [86, 87, 88, 86, 87, 85, 86]
x_std = np.std(speed2)     # sub-point: low variation example
print(x_std)

speed3 = [32, 111, 138, 28, 59, 77, 97]
x_std2 = np.std(speed3)     # sub-point: high variation example
print(x_std2)

x_var = np.var(speed3)       # sub-point: variance
print(x_var)
print(np.sqrt(x_var))         # sub-point: sqrt(variance) == std


# ----------------------------------------------------------
# Percentile
# ----------------------------------------------------------
# - Percentiles describe the value below which a percentage of
#   data falls, e.g. the 75th percentile means 75% of values are
#   lower than that value.

ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

x_p90 = np.percentile(ages, 90)   # sub-point: 90th percentile
print(x_p90)

x_p75 = np.percentile(ages, 75)    # sub-point: 75th percentile
print(x_p75)

x_p50 = np.percentile(ages, 50)     # sub-point: 50th percentile == median
print(x_p50)


# ----------------------------------------------------------
# Data Distribution
# ----------------------------------------------------------
# - Real-world data sets are often large; NumPy can create big
#   random data sets to simulate and study distributions.

np.random.seed(0)
x_dist = np.random.uniform(0.0, 5.0, 250)   # sub-point: 250 random floats between 0 and 5
print(x_dist[:10])

plt.hist(x_dist, 5)   # sub-point: histogram of the distribution (5 bins)
plt.title("Data Distribution Example")
plt.show()


# ----------------------------------------------------------
# Normal Data Distribution
# ----------------------------------------------------------
# - A normal (Gaussian) distribution is symmetric and bell-shaped,
#   centered around the mean.
# - np.random.normal(loc, scale, size) generates it.
# - loc = mean, scale = standard deviation.

x_norm = np.random.normal(5.0, 1.0, 100000)   # sub-point: normal distribution
plt.hist(x_norm, 100)
plt.title("Normal Data Distribution")
plt.show()


# ----------------------------------------------------------
# Scatter Plot
# ----------------------------------------------------------
# - A scatter plot shows the relationship between two variables
#   using dots for each observation.

age_sc = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
speed_sc = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
plt.scatter(age_sc, speed_sc)    # sub-point: basic scatter plot
plt.title("Scatter Plot Example")
plt.show()

# sub-point: scatter plot of a random normal distribution (2 variables)
x_sc2 = np.random.normal(5.0, 1.0, 1000)
y_sc2 = np.random.normal(10.0, 2.0, 1000)
plt.scatter(x_sc2, y_sc2)
plt.title("Scatter Plot of Random Normal Data")
plt.show()


# ----------------------------------------------------------
# Linear Regression
# ----------------------------------------------------------
# - Linear regression finds the relationship between variables
#   and fits a straight line (y = slope*x + intercept) to predict values.
# - scipy.stats.linregress() computes slope, intercept, r-value, etc.

x_lr = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y_lr = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(x_lr, y_lr)

def myfunc(x):    # sub-point: function to compute predicted y for each x
    return slope * x + intercept

mymodel = list(map(myfunc, x_lr))

plt.scatter(x_lr, y_lr)
plt.plot(x_lr, mymodel)    # sub-point: draw the regression line
plt.title("Linear Regression Example")
plt.show()

print(r)   # sub-point: r value shows relationship strength (-1 to 1)

speed_pred = myfunc(10)   # sub-point: predict speed for a 10 year old car
print(speed_pred)


# ----------------------------------------------------------
# Polynomial Regression
# ----------------------------------------------------------
# - Used when data points don't fit a straight line well.
# - np.polyfit() fits a polynomial; np.poly1d() creates the function.

x_pr = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y_pr = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

mymodel_pr = np.poly1d(np.polyfit(x_pr, y_pr, 3))   # sub-point: fit degree-3 polynomial
myline = np.linspace(1, 22, 100)

plt.scatter(x_pr, y_pr)
plt.plot(myline, mymodel_pr(myline))   # sub-point: draw the polynomial curve
plt.title("Polynomial Regression Example")
plt.show()

from sklearn.metrics import r2_score
print(r2_score(y_pr, mymodel_pr(x_pr)))   # sub-point: R-squared (goodness of fit)

speed_pred2 = mymodel_pr(17)   # sub-point: predict value at x=17
print(speed_pred2)


# ----------------------------------------------------------
# Multiple Regression
# ----------------------------------------------------------
# - Multiple regression predicts a value based on two or more
#   independent variables (features).

from sklearn import linear_model

mr_data = pd.DataFrame({
    'Weight': [790, 1160, 929, 865, 1140, 929, 1109, 1365, 1112, 1150],
    'Volume': [1000, 1200, 1000, 900, 1500, 1000, 1400, 1500, 1500, 1600],
    'CO2': [99, 95, 95, 90, 105, 105, 90, 92, 98, 99]
})
X_mr = mr_data[['Weight', 'Volume']]   # sub-point: features (independent variables)
y_mr = mr_data['CO2']                    # sub-point: target (dependent variable)

regr = linear_model.LinearRegression()
regr.fit(X_mr, y_mr)   # sub-point: train the model

predictedCO2 = regr.predict([[2300, 1300]])   # sub-point: predict CO2 for new values
print(predictedCO2)

print(regr.coef_)   # sub-point: coefficients (how much each feature affects the result)


# ----------------------------------------------------------
# Scale
# ----------------------------------------------------------
# - Feature scaling standardizes values to a comparable range
#   so features with different units don't unfairly dominate.
# - StandardScaler: z = (x - mean) / std

from sklearn.preprocessing import StandardScaler

scale = StandardScaler()
scaled_X = scale.fit_transform(X_mr)   # sub-point: scale the features
print(scaled_X)

regr2 = linear_model.LinearRegression()
regr2.fit(scaled_X, y_mr)
scaled_new = scale.transform([[2300, 1.3]])   # sub-point: scale new data before predicting
predictedCO2_2 = regr2.predict(scaled_new)
print(predictedCO2_2)


# ----------------------------------------------------------
# Train/Test
# ----------------------------------------------------------
# - Splitting data into a training set and a testing set measures
#   how well the model performs on unseen data (avoids overfitting).
# - Common split: 80% train, 20% test.

np.random.seed(2)
x_tt = np.random.normal(3, 1, 100)
y_tt = np.random.normal(150, 40, 100) / x_tt

train_x = x_tt[:80]    # sub-point: 80% for training
train_y = y_tt[:80]
test_x = x_tt[80:]      # sub-point: 20% for testing
test_y = y_tt[80:]

mymodel_tt = np.poly1d(np.polyfit(train_x, train_y, 4))
myline_tt = np.linspace(0, 6, 100)
plt.scatter(train_x, train_y)
plt.plot(myline_tt, mymodel_tt(myline_tt))
plt.title("Train Data Fit")
plt.show()

r2_train = r2_score(train_y, mymodel_tt(train_x))   # sub-point: R2 on training data
print(r2_train)

r2_test = r2_score(test_y, mymodel_tt(test_x))        # sub-point: R2 on test data
print(r2_test)

print(mymodel_tt(5))   # sub-point: predict a new value with the trained model


# ----------------------------------------------------------
# Decision Tree
# ----------------------------------------------------------
# - A Decision Tree is a flowchart-like structure used for
#   classification decisions based on feature values.

from sklearn.tree import DecisionTreeClassifier

dt_data = pd.DataFrame({
    'Age': [36, 42, 23, 52, 43, 44, 66, 35, 52, 35],
    'Experience': [10, 12, 4, 4, 21, 14, 3, 14, 13, 5],
    'Rank': [9, 4, 6, 4, 8, 5, 7, 9, 7, 9],
    'Nationality': [0, 1, 0, 0, 1, 0, 1, 1, 0, 1],
    'Go': [0, 0, 1, 0, 1, 0, 1, 1, 0, 1]
})

features = ['Age', 'Experience', 'Rank', 'Nationality']
X_dt = dt_data[features]
y_dt = dt_data['Go']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X_dt, y_dt)   # sub-point: train the decision tree

print(dtree.predict([[40, 10, 7, 1]]))   # sub-point: predict for a new person

from sklearn.tree import plot_tree
plot_tree(dtree, feature_names=features)   # sub-point: visualize the tree
plt.title("Decision Tree Example")
plt.show()


# ----------------------------------------------------------
# Confusion Matrix
# ----------------------------------------------------------
# - A confusion matrix summarizes classification results:
#   True Positives, True Negatives, False Positives, False Negatives.
# - Used to derive Accuracy, Precision, Recall (Sensitivity), Specificity.

from sklearn import metrics

actual = np.random.binomial(1, 0.9, size=1000)
predicted = np.random.binomial(1, 0.9, size=1000)

confusion_matrix = metrics.confusion_matrix(actual, predicted)   # sub-point: build matrix

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix,
                                             display_labels=[False, True])
cm_display.plot()   # sub-point: visualize the matrix
plt.title("Confusion Matrix Example")
plt.show()

print(metrics.accuracy_score(actual, predicted))    # sub-point: accuracy
print(metrics.precision_score(actual, predicted))     # sub-point: precision
print(metrics.recall_score(actual, predicted))          # sub-point: recall/sensitivity


# ----------------------------------------------------------
# Hierarchical Clustering
# ----------------------------------------------------------
# - Unsupervised method that groups similar data points into
#   nested clusters, visualized with a dendrogram.

from scipy.cluster.hierarchy import dendrogram, linkage

x_hc = [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]
y_hc = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
data_hc = list(zip(x_hc, y_hc))

linkage_data = linkage(data_hc, method='ward')   # sub-point: compute linkage
dendrogram(linkage_data)   # sub-point: plot dendrogram
plt.title("Hierarchical Clustering Dendrogram")
plt.show()

from sklearn.cluster import AgglomerativeClustering
hc_model = AgglomerativeClustering(n_clusters=2, metric='euclidean', linkage='ward')
labels_hc = hc_model.fit_predict(data_hc)   # sub-point: assign cluster labels
plt.scatter(x_hc, y_hc, c=labels_hc)
plt.title("Hierarchical Clustering Result")
plt.show()


# ----------------------------------------------------------
# Logistic Regression
# ----------------------------------------------------------
# - Used for classification problems (predicting discrete categories,
#   e.g. yes/no) instead of continuous values like linear regression.

from sklearn.linear_model import LogisticRegression

X_lg = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37,
                  4.96, 4.52, 3.69, 5.88]).reshape(-1, 1)
y_lg = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = LogisticRegression()
logr.fit(X_lg, y_lg)   # sub-point: train logistic regression model

predicted_lg = logr.predict(np.array([3.46]).reshape(-1, 1))  # sub-point: predict class
print(predicted_lg)

log_odds = logr.coef_       # sub-point: coefficient (log-odds)
odds = np.exp(log_odds)      # sub-point: convert log-odds to odds
print(odds)


# ----------------------------------------------------------
# Grid Search
# ----------------------------------------------------------
# - Grid Search systematically tests different hyperparameter
#   values to find the combination that gives the best model performance.

from sklearn.linear_model import LogisticRegression as LR2
from sklearn.model_selection import GridSearchCV
from sklearn import datasets

iris = datasets.load_iris()
X_gs = iris['data']
y_gs = iris['target']

logit = LR2(max_iter=10000)
print(logit.fit(X_gs, y_gs).score(X_gs, y_gs))   # sub-point: baseline score (C=1 default)

C_values = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]  # sub-point: values to test
scores = []
for c in C_values:
    logit.set_params(C=c)
    logit.fit(X_gs, y_gs)
    scores.append(logit.score(X_gs, y_gs))
print(scores)   # sub-point: scores for each C value

gs = GridSearchCV(LR2(max_iter=10000), {'C': C_values})   # sub-point: automated grid search
gs.fit(X_gs, y_gs)
print(gs.best_params_)   # sub-point: best hyperparameter found


# ----------------------------------------------------------
# Categorical Data
# ----------------------------------------------------------
# - ML models need numbers, so categorical (text) data must be
#   converted using techniques like One-Hot Encoding or dummy variables.

cat_df = pd.DataFrame({
    'Car': ['Toyota', 'Mitsubishi', 'Skoda', 'Toyota'],
    'Volume': [1000, 1200, 1000, 900]
})

ohe = pd.get_dummies(cat_df[['Car']])   # sub-point: one-hot encoding
print(ohe)

cat_df_final = pd.concat([cat_df, ohe], axis=1)   # sub-point: merge encoded columns back
print(cat_df_final)

dummies_dropfirst = pd.get_dummies(cat_df[['Car']], drop_first=True)  # sub-point: avoid dummy trap
print(dummies_dropfirst)


# ----------------------------------------------------------
# K-means
# ----------------------------------------------------------
# - K-means is an unsupervised algorithm that groups data into
#   K clusters based on similarity (distance to cluster centers).

from sklearn.cluster import KMeans

np.random.seed(1)
x_km = np.random.uniform(1, 100, 100)
y_km = np.random.uniform(1, 100, 100)
data_km = list(zip(x_km, y_km))

# sub-point: elbow method to find optimal K
inertias = []
for i in range(1, 11):
    kmeans_i = KMeans(n_clusters=i, n_init=10)
    kmeans_i.fit(data_km)
    inertias.append(kmeans_i.inertia_)

plt.plot(range(1, 11), inertias, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

kmeans = KMeans(n_clusters=3, n_init=10)   # sub-point: fit with chosen K
kmeans.fit(data_km)
plt.scatter(x_km, y_km, c=kmeans.labels_)   # sub-point: visualize clusters
plt.title("K-means Clustering Result")
plt.show()


# ----------------------------------------------------------
# Bootstrap Aggregation (Bagging)
# ----------------------------------------------------------
# - Bagging trains multiple models on random subsets (with
#   replacement) of the data and combines their predictions to
#   reduce variance and overfitting.

from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier as DTC

data_bag = datasets.load_wine(as_frame=True)
X_bag = data_bag.data
y_bag = data_bag.target
X_train, X_test, y_train, y_test = train_test_split(X_bag, y_bag, random_state=22, test_size=0.25)

dtree_bag = DTC(random_state=22)
dtree_bag.fit(X_train, y_train)
print("Base tree train/test:", dtree_bag.score(X_train, y_train), dtree_bag.score(X_test, y_test))

bagging_model = BaggingClassifier(estimator=DTC(), n_estimators=50,
                                   max_samples=0.8, random_state=22)  # sub-point: bagging model
bagging_model.fit(X_train, y_train)
print("Bagging train/test:", bagging_model.score(X_train, y_train), bagging_model.score(X_test, y_test))


# ----------------------------------------------------------
# Cross Validation
# ----------------------------------------------------------
# - Cross validation evaluates model performance more reliably
#   by splitting data into multiple folds and testing on each.

from sklearn import datasets as ds
from sklearn.tree import DecisionTreeClassifier as DTC2
from sklearn.model_selection import KFold, cross_val_score, LeaveOneOut, LeavePOut, ShuffleSplit, StratifiedKFold

X_cv, y_cv = ds.load_iris(return_X_y=True)
clf_cv = DTC2(random_state=42)

k_folds = KFold(n_splits=5)                       # sub-point: standard K-Fold
scores_cv = cross_val_score(clf_cv, X_cv, y_cv, cv=k_folds)
print(scores_cv, scores_cv.mean())

sk_folds = StratifiedKFold(n_splits=5)              # sub-point: stratified K-Fold (preserves class ratio)
scores_sk = cross_val_score(clf_cv, X_cv, y_cv, cv=sk_folds)
print(scores_sk, scores_sk.mean())

loo = LeaveOneOut()                                   # sub-point: Leave-One-Out CV
scores_loo = cross_val_score(clf_cv, X_cv, y_cv, cv=loo)
print(scores_loo.mean())

ss = ShuffleSplit(train_size=0.6, test_size=0.3, n_splits=5)  # sub-point: Shuffle Split
scores_ss = cross_val_score(clf_cv, X_cv, y_cv, cv=ss)
print(scores_ss.mean())


# ----------------------------------------------------------
# AUC - ROC Curve
# ----------------------------------------------------------
# - ROC (Receiver Operating Characteristic) curve plots True
#   Positive Rate vs False Positive Rate at different thresholds.
# - AUC (Area Under Curve) summarizes performance: closer to 1 is better.

from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LogisticRegression as LR3

X_roc, y_roc = make_classification(n_samples=1000, n_classes=2, random_state=1)
X_tr, X_te, y_tr, y_te = tts(X_roc, y_roc, test_size=0.5, random_state=1)

model_roc = LR3()
model_roc.fit(X_tr, y_tr)
probs = model_roc.predict_proba(X_te)[:, 1]   # sub-point: predicted probabilities

fpr, tpr, thresholds = roc_curve(y_te, probs)   # sub-point: compute ROC curve points
plt.plot(fpr, tpr)
plt.plot([0, 1], [0, 1], linestyle='--')   # sub-point: baseline (random guess) line
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title("ROC Curve Example")
plt.show()

auc_score = roc_auc_score(y_te, probs)   # sub-point: AUC score
print(auc_score)


# ----------------------------------------------------------
# K-nearest neighbors (KNN)
# ----------------------------------------------------------
# - KNN classifies a new point based on the majority class among
#   its K closest neighbors in the training data.

from sklearn.neighbors import KNeighborsClassifier

x_knn = [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]
y_knn = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
classes_knn = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]
data_knn = list(zip(x_knn, y_knn))

knn = KNeighborsClassifier(n_neighbors=1)   # sub-point: K=1
knn.fit(data_knn, classes_knn)

new_point = [(8, 21)]
prediction = knn.predict(new_point)   # sub-point: predict class of a new point
print(prediction)

plt.scatter(x_knn, y_knn, c=classes_knn)
plt.scatter(8, 21, c='red', marker='x', s=100)  # sub-point: mark the new point
plt.title("K-nearest Neighbors Example")
plt.show()


# ==========================================================
# EXTRA TOPICS (BONUS - beyond the official W3Schools tutorial)
# ==========================================================

# ----------------------------------------------------------
# ML Data Types (Numerical, Categorical, Ordinal)
# ----------------------------------------------------------
# - Knowing the data type tells you which technique to use.
# - NUMERICAL data = numbers.
#     - Discrete: counted, limited to integers (e.g. number of cars).
#     - Continuous: measured, can be any number (e.g. price, weight).
# - CATEGORICAL data = values that cannot be ranked/measured against
#   each other (e.g. colors, yes/no).
# - ORDINAL data = like categorical, but CAN be ranked
#   (e.g. school grades A > B > C).

data_types_example = pd.DataFrame({
    'Discrete_CarsPassing': [3, 5, 2, 8],      # numerical - discrete
    'Continuous_Price': [19.99, 45.50, 12.25, 99.00],  # numerical - continuous
    'Categorical_Color': ['red', 'blue', 'red', 'green'],  # categorical
    'Ordinal_Grade': ['A', 'C', 'B', 'A']       # ordinal
})
print(data_types_example)


# ----------------------------------------------------------
# ML Correlation & Covariance (deeper look)
# ----------------------------------------------------------
# - Correlation measures the strength & direction of the linear
#   relationship between two variables, ranging from -1 to 1.
# - +1 = perfect positive relationship, -1 = perfect negative,
#   0 = no linear relationship.
# - Covariance shows the direction of the relationship, but is
#   not standardized (harder to interpret magnitude).

corr_df = pd.DataFrame({
    'Hours_Studied': [1, 2, 3, 4, 5, 6],
    'Exam_Score': [50, 55, 65, 70, 85, 90]
})
print(corr_df.corr())    # correlation matrix
print(corr_df.cov())      # covariance matrix


# ----------------------------------------------------------
# ML Probability Basics (Bayes' Theorem)
# ----------------------------------------------------------
# - Bayes' Theorem updates the probability of an event based on
#   new evidence: P(A|B) = P(B|A) * P(A) / P(B)
# - Core idea behind the Naive Bayes classifier (below).

# Example: probability a patient has a disease given a positive test
p_disease = 0.01          # prior probability of disease
p_pos_given_disease = 0.9  # test sensitivity (true positive rate)
p_pos_given_healthy = 0.05  # false positive rate

p_pos = (p_pos_given_disease * p_disease) + (p_pos_given_healthy * (1 - p_disease))
p_disease_given_pos = (p_pos_given_disease * p_disease) / p_pos   # Bayes' Theorem
print(p_disease_given_pos)   # probability patient actually has disease given positive test


# ----------------------------------------------------------
# ML Handling Missing Data
# ----------------------------------------------------------
# - Real data often has gaps. Options: drop rows/columns, or
#   impute (fill in) missing values using mean/median/mode or
#   a model-based approach.

from sklearn.impute import SimpleImputer

missing_df = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [np.nan, 2, 3, 4]})
print(missing_df.dropna())    # sub-point: drop rows with missing values

imputer = SimpleImputer(strategy='mean')   # sub-point: fill with column mean
imputed = imputer.fit_transform(missing_df)
print(imputed)

imputer_median = SimpleImputer(strategy='median')   # sub-point: fill with median
print(imputer_median.fit_transform(missing_df))

imputer_const = SimpleImputer(strategy='constant', fill_value=0)  # sub-point: fill with a constant
print(imputer_const.fit_transform(missing_df))


# ----------------------------------------------------------
# ML Outlier Detection & Removal
# ----------------------------------------------------------
# - Outliers are extreme values that can distort model training.
# - Common method: Z-score (how many std devs a point is from mean).
# - Another method: IQR (Interquartile Range) rule.

outlier_data = np.array([12, 14, 13, 15, 16, 14, 100, 13, 15, 14])  # 100 is an outlier

# sub-point: Z-score method
mean_o = np.mean(outlier_data)
std_o = np.std(outlier_data)
z_scores = (outlier_data - mean_o) / std_o
print(z_scores)
outliers_z = outlier_data[np.abs(z_scores) > 2]   # points more than 2 std devs away
print("Outliers (Z-score):", outliers_z)

# sub-point: IQR method
Q1 = np.percentile(outlier_data, 25)
Q3 = np.percentile(outlier_data, 75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers_iqr = outlier_data[(outlier_data < lower_bound) | (outlier_data > upper_bound)]
print("Outliers (IQR):", outliers_iqr)


# ----------------------------------------------------------
# ML Feature Engineering
# ----------------------------------------------------------
# - Creating new features from existing data to help the model
#   learn better patterns.

fe_df = pd.DataFrame({
    'Length': [2, 3, 4],
    'Width': [3, 4, 5],
    'Date': pd.to_datetime(['2024-01-15', '2024-06-20', '2024-12-01'])
})
fe_df['Area'] = fe_df['Length'] * fe_df['Width']   # sub-point: combine existing features
fe_df['Month'] = fe_df['Date'].dt.month              # sub-point: extract date part
fe_df['Is_Weekend'] = fe_df['Date'].dt.dayofweek >= 5  # sub-point: derived boolean feature
print(fe_df)


# ----------------------------------------------------------
# ML Feature Selection
# ----------------------------------------------------------
# - Selecting the most relevant features improves accuracy and
#   reduces overfitting/training time.

from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.datasets import load_iris

iris_fs = load_iris()
X_fs, y_fs = iris_fs.data, iris_fs.target

selector = SelectKBest(score_func=f_classif, k=2)   # sub-point: select best 2 features
X_selected = selector.fit_transform(X_fs, y_fs)
print(X_selected[:5])
print(selector.get_support())   # sub-point: which features were selected (boolean mask)


# ----------------------------------------------------------
# ML Ridge Regression (L2 Regularization)
# ----------------------------------------------------------
# - Adds a penalty proportional to the SQUARE of coefficients,
#   shrinking them to reduce overfitting (but rarely to exactly 0).
# - 'alpha' controls how strong the penalty is.

from sklearn.linear_model import Ridge

X_ridge = np.array([[1], [2], [3], [4], [5]])
y_ridge = np.array([2, 4, 5, 4, 5])

ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X_ridge, y_ridge)
print(ridge_model.coef_, ridge_model.intercept_)
print(ridge_model.predict([[6]]))   # predict a new value


# ----------------------------------------------------------
# ML Lasso Regression (L1 Regularization)
# ----------------------------------------------------------
# - Adds a penalty proportional to the ABSOLUTE VALUE of
#   coefficients, which can shrink some coefficients to exactly 0
#   (effectively performing feature selection).

from sklearn.linear_model import Lasso

lasso_model = Lasso(alpha=0.5)
lasso_model.fit(X_ridge, y_ridge)
print(lasso_model.coef_, lasso_model.intercept_)
print(lasso_model.predict([[6]]))


# ----------------------------------------------------------
# ML Elastic Net
# ----------------------------------------------------------
# - Combines Ridge (L2) and Lasso (L1) penalties together.
# - 'l1_ratio' controls the mix: 0 = pure Ridge, 1 = pure Lasso.

from sklearn.linear_model import ElasticNet

elastic_model = ElasticNet(alpha=0.5, l1_ratio=0.5)
elastic_model.fit(X_ridge, y_ridge)
print(elastic_model.coef_, elastic_model.intercept_)


# ----------------------------------------------------------
# ML Support Vector Machines (SVM)
# ----------------------------------------------------------
# - SVM finds the best boundary (hyperplane) that separates
#   classes with the maximum margin.
# - The 'kernel' parameter lets it handle non-linear boundaries
#   (e.g. 'linear', 'rbf', 'poly').

from sklearn.svm import SVC
from sklearn.datasets import make_blobs

X_svm, y_svm = make_blobs(n_samples=100, centers=2, random_state=6)

svm_model = SVC(kernel='linear')   # sub-point: linear kernel
svm_model.fit(X_svm, y_svm)
print(svm_model.predict([[0, 0]]))

svm_model_rbf = SVC(kernel='rbf')   # sub-point: non-linear (RBF) kernel
svm_model_rbf.fit(X_svm, y_svm)
print(svm_model_rbf.predict([[0, 0]]))

plt.scatter(X_svm[:, 0], X_svm[:, 1], c=y_svm)
plt.title("SVM Training Data")
plt.show()


# ----------------------------------------------------------
# ML Naive Bayes
# ----------------------------------------------------------
# - A classification algorithm based on Bayes' Theorem, assuming
#   features are independent of each other ("naive" assumption).
# - Fast, works well for text classification (e.g. spam detection).

from sklearn.naive_bayes import GaussianNB

X_nb = np.array([[1, 2], [2, 3], [3, 3], [6, 7], [7, 8], [8, 8]])
y_nb = np.array([0, 0, 0, 1, 1, 1])

nb_model = GaussianNB()
nb_model.fit(X_nb, y_nb)   # sub-point: train Naive Bayes model
print(nb_model.predict([[2, 2]]))   # sub-point: predict class for a new point
print(nb_model.predict_proba([[2, 2]]))  # sub-point: predicted class probabilities


# ----------------------------------------------------------
# ML Random Forest
# ----------------------------------------------------------
# - An ensemble of many Decision Trees, each trained on a random
#   subset of data/features. Final prediction = majority vote
#   (classification) or average (regression).
# - Reduces overfitting compared to a single Decision Tree.

from sklearn.ensemble import RandomForestClassifier

iris_rf = load_iris()
X_rf, y_rf = iris_rf.data, iris_rf.target

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)  # sub-point: 100 trees
rf_model.fit(X_rf, y_rf)
print(rf_model.predict([X_rf[0]]))
print(rf_model.feature_importances_)   # sub-point: which features matter most


# ----------------------------------------------------------
# ML Precision-Recall Curve
# ----------------------------------------------------------
# - Plots Precision vs Recall at different classification thresholds.
# - More informative than ROC when classes are imbalanced.

from sklearn.metrics import precision_recall_curve

X_pr, y_pr = make_classification(n_samples=1000, weights=[0.9, 0.1], random_state=1)
X_tr_pr, X_te_pr, y_tr_pr, y_te_pr = tts(X_pr, y_pr, test_size=0.5, random_state=1)
model_pr = LR3()
model_pr.fit(X_tr_pr, y_tr_pr)
probs_pr = model_pr.predict_proba(X_te_pr)[:, 1]

precision, recall, thresholds_pr = precision_recall_curve(y_te_pr, probs_pr)
plt.plot(recall, precision)
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision-Recall Curve")
plt.show()


# ----------------------------------------------------------
# ML Bias-Variance Tradeoff
# ----------------------------------------------------------
# - Bias = error from overly simplistic assumptions (underfitting).
# - Variance = error from too much sensitivity to training data
#   (overfitting).
# - Goal: find the sweet spot that minimizes total error.
# - Demonstrated below by comparing polynomial degrees.

np.random.seed(0)
x_bv = np.linspace(0, 1, 30)
y_bv = np.sin(2 * np.pi * x_bv) + np.random.normal(0, 0.2, 30)

for degree in [1, 4, 15]:   # sub-point: low degree=high bias, high degree=high variance
    coeffs = np.polyfit(x_bv, y_bv, degree)
    p = np.poly1d(coeffs)
    xs_bv = np.linspace(0, 1, 100)
    plt.plot(xs_bv, p(xs_bv), label=f'degree={degree}')

plt.scatter(x_bv, y_bv, color='black', s=10)
plt.legend()
plt.title("Bias-Variance Tradeoff (degree 1 vs 4 vs 15)")
plt.show()


# ----------------------------------------------------------
# ML Overfitting & Underfitting
# ----------------------------------------------------------
# - Underfitting: model is too simple, performs poorly on both
#   training and test data (high bias).
# - Overfitting: model is too complex, performs great on training
#   data but poorly on test data (high variance, memorized noise).
# - Good fit: performs well on both training and test data.

train_scores, test_scores = [], []
degrees = range(1, 15)
x_of_train, x_of_test = x_bv[:20], x_bv[20:]
y_of_train, y_of_test = y_bv[:20], y_bv[20:]

for d in degrees:
    coeffs_of = np.polyfit(x_of_train, y_of_train, d)
    p_of = np.poly1d(coeffs_of)
    train_scores.append(r2_score(y_of_train, p_of(x_of_train)))
    test_scores.append(r2_score(y_of_test, p_of(x_of_test)))

plt.plot(degrees, train_scores, label='Train R2')
plt.plot(degrees, test_scores, label='Test R2')
plt.xlabel('Polynomial Degree (model complexity)')
plt.ylabel('R2 Score')
plt.legend()
plt.title("Overfitting vs Underfitting")
plt.show()


# ----------------------------------------------------------
# ML Boosting (AdaBoost & Gradient Boosting)
# ----------------------------------------------------------
# - Boosting trains models SEQUENTIALLY, where each new model
#   focuses on correcting the errors of the previous ones.
# - Different from Bagging, which trains models independently in parallel.

from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier

iris_boost = load_iris()
X_boost, y_boost = iris_boost.data, iris_boost.target
X_tr_b, X_te_b, y_tr_b, y_te_b = tts(X_boost, y_boost, test_size=0.3, random_state=42)

ada_model = AdaBoostClassifier(n_estimators=50, random_state=42)   # sub-point: AdaBoost
ada_model.fit(X_tr_b, y_tr_b)
print("AdaBoost accuracy:", ada_model.score(X_te_b, y_te_b))

gb_model = GradientBoostingClassifier(n_estimators=50, learning_rate=0.1, random_state=42)  # sub-point: Gradient Boosting
gb_model.fit(X_tr_b, y_tr_b)
print("Gradient Boosting accuracy:", gb_model.score(X_te_b, y_te_b))


# ----------------------------------------------------------
# ML Stacking
# ----------------------------------------------------------
# - Stacking combines predictions from multiple different models
#   (base learners) using another model (meta-learner) that learns
#   how to best combine them.

from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression as LR4
from sklearn.neighbors import KNeighborsClassifier as KNN2

base_learners = [
    ('dt', DecisionTreeClassifier(random_state=42)),
    ('knn', KNN2(n_neighbors=3))
]
stack_model = StackingClassifier(estimators=base_learners, final_estimator=LR4())
stack_model.fit(X_tr_b, y_tr_b)
print("Stacking accuracy:", stack_model.score(X_te_b, y_te_b))


# ----------------------------------------------------------
# ML DBSCAN (Density-Based Clustering)
# ----------------------------------------------------------
# - Groups points that are closely packed (dense regions), marking
#   isolated points as noise/outliers.
# - Unlike K-means, it does NOT require specifying the number of
#   clusters in advance, and can find irregularly shaped clusters.

from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons

X_db, _ = make_moons(n_samples=300, noise=0.05, random_state=0)
dbscan_model = DBSCAN(eps=0.2, min_samples=5)   # sub-point: eps = neighborhood radius
labels_db = dbscan_model.fit_predict(X_db)
plt.scatter(X_db[:, 0], X_db[:, 1], c=labels_db, cmap='viridis')
plt.title("DBSCAN Clustering Example")
plt.show()
print("Number of clusters found:", len(set(labels_db)) - (1 if -1 in labels_db else 0))


# ----------------------------------------------------------
# ML Principal Component Analysis (PCA)
# ----------------------------------------------------------
# - PCA reduces the number of features (dimensionality) while
#   preserving as much variance (information) as possible.
# - Useful for visualization and speeding up training on
#   high-dimensional data.

from sklearn.decomposition import PCA

iris_pca = load_iris()
X_pca_data = iris_pca.data
y_pca_data = iris_pca.target

pca = PCA(n_components=2)   # sub-point: reduce from 4 features to 2
X_reduced = pca.fit_transform(X_pca_data)
print(pca.explained_variance_ratio_)   # sub-point: how much variance each component captures

plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y_pca_data)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title("PCA - Iris Dataset Reduced to 2D")
plt.show()


# ----------------------------------------------------------
# ML t-SNE (t-Distributed Stochastic Neighbor Embedding)
# ----------------------------------------------------------
# - Another dimensionality reduction technique, mainly used for
#   VISUALIZING high-dimensional data in 2D/3D.
# - Preserves local structure (similar points stay close together)
#   better than PCA, but is slower and mainly for visualization
#   (not for feeding into further models).

from sklearn.manifold import TSNE

tsne = TSNE(n_components=2, random_state=42, perplexity=30)
X_tsne = tsne.fit_transform(X_pca_data)
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y_pca_data)
plt.title("t-SNE - Iris Dataset Visualization")
plt.show()


# ----------------------------------------------------------
# ML Anomaly / Outlier Detection (model-based)
# ----------------------------------------------------------
# - Beyond simple Z-score/IQR rules, models like Isolation Forest
#   detect anomalies in multi-dimensional data by isolating points
#   that are "few and different" - they take fewer steps to isolate.

from sklearn.ensemble import IsolationForest

X_anom = np.concatenate([np.random.normal(0, 1, (100, 2)),
                          np.random.uniform(-6, 6, (10, 2))])  # normal + injected anomalies

iso_model = IsolationForest(contamination=0.1, random_state=42)
preds_anom = iso_model.fit_predict(X_anom)   # sub-point: -1 = anomaly, 1 = normal
plt.scatter(X_anom[:, 0], X_anom[:, 1], c=preds_anom, cmap='coolwarm')
plt.title("Isolation Forest - Anomaly Detection")
plt.show()


# ----------------------------------------------------------
# ML Neural Network Basics (Perceptron / MLP)
# ----------------------------------------------------------
# - A Neural Network is made of layers of connected "neurons".
# - Each neuron computes a weighted sum of inputs, then applies an
#   activation function (e.g. ReLU, sigmoid) to introduce non-linearity.
# - Trained via backpropagation: errors are propagated backward to
#   adjust weights and reduce the loss.
# - MLPClassifier is a simple fully-connected neural network in sklearn.

from sklearn.neural_network import MLPClassifier

iris_nn = load_iris()
X_nn, y_nn = iris_nn.data, iris_nn.target
X_tr_nn, X_te_nn, y_tr_nn, y_te_nn = tts(X_nn, y_nn, test_size=0.3, random_state=1)

nn_model = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000, random_state=1)
# sub-point: hidden_layer_sizes=(10,10) means 2 hidden layers of 10 neurons each
nn_model.fit(X_tr_nn, y_tr_nn)
print("Neural Network accuracy:", nn_model.score(X_te_nn, y_te_nn))


# ----------------------------------------------------------
# ML Time Series Forecasting
# ----------------------------------------------------------
# - Predicting future values based on historical, time-ordered data.
# - Moving Average smooths out short-term fluctuations.

ts_data = pd.Series([112, 118, 132, 129, 121, 135, 148, 148, 136, 119],
                     index=pd.date_range('2024-01-01', periods=10, freq='M'))

moving_avg = ts_data.rolling(window=3).mean()   # sub-point: simple moving average
print(moving_avg)

plt.plot(ts_data, label='Original')
plt.plot(moving_avg, label='3-Month Moving Average')
plt.legend()
plt.title("Time Series - Moving Average")
plt.show()

# sub-point: simple naive forecast (predict next = last observed value)
next_forecast = ts_data.iloc[-1]
print("Naive forecast for next period:", next_forecast)


# ----------------------------------------------------------
# ML Pipelines
# ----------------------------------------------------------
# - Pipelines chain preprocessing steps and a model together into
#   a single object, so transformations are applied consistently
#   to both training and test data (prevents data leakage).

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler as SS2

pipe = Pipeline([
    ('scaler', SS2()),                       # sub-point: step 1 - scale features
    ('classifier', RandomForestClassifier(random_state=42))  # sub-point: step 2 - train model
])

X_pipe, y_pipe = load_iris(return_X_y=True)
X_tr_p, X_te_p, y_tr_p, y_te_p = tts(X_pipe, y_pipe, test_size=0.3, random_state=1)

pipe.fit(X_tr_p, y_tr_p)   # sub-point: fits scaler AND model in one call
print("Pipeline accuracy:", pipe.score(X_te_p, y_te_p))


# ==========================================================
# CAMPUSX "100 DAYS OF ML" - ADDITIONAL TOPICS
# (topics from the playlist not already covered above)
# ==========================================================

# ----------------------------------------------------------
# Working with CSV Files (advanced options)
# ----------------------------------------------------------
# - pd.read_csv() has many useful parameters beyond the basics.

csv_text = "a,b,c\n1,2,3\n4,5,6\n7,8,9\n"
with open('sample.csv', 'w') as f:
    f.write(csv_text)

print(pd.read_csv('sample.csv', usecols=['a', 'b']))    # sub-point: load only specific columns
print(pd.read_csv('sample.csv', nrows=2))                 # sub-point: load only first N rows
print(pd.read_csv('sample.csv', dtype={'a': float}))        # sub-point: force column dtype
print(pd.read_csv('sample.csv', names=['x', 'y', 'z'], skiprows=1))  # sub-point: rename + skip header
print(pd.read_csv('sample.csv', index_col='a'))               # sub-point: set a column as index

for chunk in pd.read_csv('sample.csv', chunksize=2):   # sub-point: read large files in chunks
    print(chunk)


# ----------------------------------------------------------
# Working with JSON and SQL
# ----------------------------------------------------------
# - Data can also come from JSON APIs or SQL databases directly.

import sqlite3

conn = sqlite3.connect(':memory:')   # sub-point: create an in-memory SQLite database
sql_df = pd.DataFrame({'id': [1, 2, 3], 'name': ['Tom', 'Jack', 'Steve']})
sql_df.to_sql('people', conn, index=False)   # sub-point: write DataFrame to SQL table

result_df = pd.read_sql('SELECT * FROM people WHERE id > 1', conn)  # sub-point: query SQL into DataFrame
print(result_df)


# ----------------------------------------------------------
# Fetching Data via API (API to DataFrame)
# ----------------------------------------------------------
# - Many real-world datasets come from REST APIs returning JSON.
# import requests
# response = requests.get('https://api.example.com/data')
# api_df = pd.DataFrame(response.json())
print("API to DataFrame - requires 'requests' library and a live endpoint (see comments)")


# ----------------------------------------------------------
# Web Scraping to DataFrame
# ----------------------------------------------------------
# - HTML tables on web pages can be scraped directly into DataFrames.
# import pandas as pd
# tables = pd.read_html('https://example.com/table-page.html')  # returns list of DataFrames
# scraped_df = tables[0]
print("Web Scraping to DataFrame - pd.read_html() extracts <table> elements from a URL")


# ----------------------------------------------------------
# Understanding Your Data (Descriptive Statistics)
# ----------------------------------------------------------
# - Before modeling, always explore: shape, info, describe, nulls, duplicates.

eda_df = pd.DataFrame({
    'Age': [22, 25, 47, 52, np.nan, 36],
    'Salary': [25000, 30000, 65000, 72000, 45000, 50000]
})
print(eda_df.shape)          # sub-point: rows, columns
print(eda_df.info())          # sub-point: dtypes and non-null counts
print(eda_df.describe())       # sub-point: statistical summary
print(eda_df.isnull().sum())    # sub-point: count of missing values per column
print(eda_df.duplicated().sum())  # sub-point: count of duplicate rows


# ----------------------------------------------------------
# Univariate Analysis
# ----------------------------------------------------------
# - Analyzing ONE variable at a time to understand its distribution.
# - Categorical: count plots / pie charts. Numerical: histograms / boxplots.

uni_df = pd.DataFrame({
    'Age': np.random.normal(35, 10, 200),
    'Category': np.random.choice(['A', 'B', 'C'], 200)
})
plt.hist(uni_df['Age'], bins=20)     # sub-point: numerical univariate - histogram
plt.title("Univariate Analysis - Age Distribution")
plt.show()

uni_df['Category'].value_counts().plot(kind='bar')   # sub-point: categorical univariate - bar chart
plt.title("Univariate Analysis - Category Counts")
plt.show()


# ----------------------------------------------------------
# Bivariate & Multivariate Analysis
# ----------------------------------------------------------
# - Bivariate: relationship between TWO variables (scatter, boxplot by group).
# - Multivariate: relationships among THREE+ variables (pairplot, heatmap).

bi_df = pd.DataFrame({
    'Age': np.random.normal(35, 10, 200),
    'Salary': np.random.normal(50000, 15000, 200),
    'Department': np.random.choice(['Sales', 'Tech', 'HR'], 200)
})
plt.scatter(bi_df['Age'], bi_df['Salary'])   # sub-point: bivariate - numerical vs numerical
plt.title("Bivariate Analysis - Age vs Salary")
plt.show()

bi_df.boxplot(column='Salary', by='Department')   # sub-point: bivariate - numerical vs categorical
plt.title("Bivariate Analysis - Salary by Department")
plt.show()

print(bi_df.corr(numeric_only=True))   # sub-point: multivariate - correlation matrix


# ----------------------------------------------------------
# Pandas Profiling (Automated EDA)
# ----------------------------------------------------------
# - ydata-profiling (formerly pandas-profiling) auto-generates a
#   full EDA report (distributions, correlations, missing values, etc.)
#   with one line of code.
# pip install ydata-profiling
# from ydata_profiling import ProfileReport
# profile = ProfileReport(eda_df, title="My Data Report")
# profile.to_file("report.html")
print("Pandas Profiling - generates a full automated EDA HTML report (see comments)")


# ----------------------------------------------------------
# Standardization vs Normalization
# ----------------------------------------------------------
# - Standardization (Z-score scaling): mean=0, std=1. Formula: (x-mean)/std.
#   Good when data roughly follows a normal distribution.
# - Normalization (Min-Max scaling): squishes values into a [0,1] range.
#   Formula: (x-min)/(max-min). Good when you need bounded values.

from sklearn.preprocessing import StandardScaler as SS3, MinMaxScaler

scale_df = pd.DataFrame({'Age': [18, 25, 40, 60, 22], 'Salary': [20000, 40000, 80000, 150000, 35000]})

standardized = SS3().fit_transform(scale_df)   # sub-point: standardization
print(standardized)

normalized = MinMaxScaler().fit_transform(scale_df)   # sub-point: normalization (min-max)
print(normalized)


# ----------------------------------------------------------
# Ordinal Encoding
# ----------------------------------------------------------
# - Converts ordered categorical data into numbers that preserve
#   the rank order (e.g. Low < Medium < High).

from sklearn.preprocessing import OrdinalEncoder

ord_df = pd.DataFrame({'Size': ['Small', 'Medium', 'Large', 'Medium', 'Small']})
oe = OrdinalEncoder(categories=[['Small', 'Medium', 'Large']])   # sub-point: define the order explicitly
ord_df['Size_encoded'] = oe.fit_transform(ord_df[['Size']])
print(ord_df)


# ----------------------------------------------------------
# One Hot Encoding (formal sklearn approach)
# ----------------------------------------------------------
# - Converts unordered categorical data into binary columns
#   (one column per category, 1 if present, 0 otherwise).

from sklearn.preprocessing import OneHotEncoder

ohe_df = pd.DataFrame({'Color': ['Red', 'Blue', 'Green', 'Blue']})
ohe_sk = OneHotEncoder(sparse_output=False)
encoded_cols = ohe_sk.fit_transform(ohe_df[['Color']])
print(encoded_cols)
print(ohe_sk.get_feature_names_out())   # sub-point: names of the new binary columns


# ----------------------------------------------------------
# Column Transformer
# ----------------------------------------------------------
# - Applies DIFFERENT preprocessing to different columns in one step
#   (e.g. scale numeric columns, one-hot encode categorical columns).

from sklearn.compose import ColumnTransformer

ct_df = pd.DataFrame({
    'Age': [25, 32, 47, 51],
    'Salary': [30000, 45000, 60000, 80000],
    'City': ['NY', 'LA', 'NY', 'SF']
})

ct = ColumnTransformer(transformers=[
    ('num', SS3(), ['Age', 'Salary']),                 # sub-point: scale numeric columns
    ('cat', OneHotEncoder(sparse_output=False), ['City'])  # sub-point: encode categorical column
])
transformed = ct.fit_transform(ct_df)
print(transformed)


# ----------------------------------------------------------
# Function Transformer
# ----------------------------------------------------------
# - Wraps a custom Python function (e.g. log transform) so it can
#   be used inside an sklearn Pipeline like any other transformer.

from sklearn.preprocessing import FunctionTransformer

ft_data = np.array([[1], [10], [100], [1000]])
log_transformer = FunctionTransformer(np.log1p)   # sub-point: log(1+x) transform
print(log_transformer.transform(ft_data))


# ----------------------------------------------------------
# Power Transformer
# ----------------------------------------------------------
# - Transforms skewed data to look more Gaussian (normal), which
#   helps many models perform better.
# - 'yeo-johnson' works with negative values; 'box-cox' needs positive-only data.

from sklearn.preprocessing import PowerTransformer

skewed_data = np.random.exponential(scale=2, size=(100, 1))   # skewed data
pt = PowerTransformer(method='yeo-johnson')
transformed_pt = pt.fit_transform(skewed_data)
print("Skew before:", pd.Series(skewed_data.flatten()).skew())
print("Skew after:", pd.Series(transformed_pt.flatten()).skew())


# ----------------------------------------------------------
# Binning and Binarization
# ----------------------------------------------------------
# - Binning: grouping continuous values into discrete "bins" (like cut/qcut).
# - Binarization: converting values into 0/1 based on a threshold.

from sklearn.preprocessing import KBinsDiscretizer, Binarizer

bin_data = np.array([[5], [15], [25], [35], [45], [55]])

kbd = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')  # sub-point: equal-width bins
print(kbd.fit_transform(bin_data))

binarizer = Binarizer(threshold=25)   # sub-point: 1 if value > threshold, else 0
print(binarizer.fit_transform(bin_data))


# ----------------------------------------------------------
# Handling Mixed Variables
# ----------------------------------------------------------
# - Some columns contain a mix of numbers and text (e.g. "A1", "B2"),
#   which need to be split into separate numeric and categorical parts.

mixed_df = pd.DataFrame({'ID': ['A1', 'B2', 'C3', 'A4']})
mixed_df['Letter'] = mixed_df['ID'].str.extract(r'([A-Za-z]+)')   # sub-point: extract letter part
mixed_df['Number'] = mixed_df['ID'].str.extract(r'(\d+)').astype(int)  # sub-point: extract number part
print(mixed_df)


# ----------------------------------------------------------
# Handling Date and Time
# ----------------------------------------------------------
# - Dates should be converted to datetime, then broken into useful
#   features (year, month, day, weekday) for ML models.

date_df = pd.DataFrame({'Date': ['2024-01-15', '2024-06-20', '2024-12-25']})
date_df['Date'] = pd.to_datetime(date_df['Date'])   # sub-point: convert to datetime
date_df['Year'] = date_df['Date'].dt.year             # sub-point: extract year
date_df['Month'] = date_df['Date'].dt.month            # sub-point: extract month
date_df['Day'] = date_df['Date'].dt.day                  # sub-point: extract day
date_df['Weekday'] = date_df['Date'].dt.day_name()         # sub-point: extract weekday name
date_df['Days_Since'] = (pd.Timestamp.now() - date_df['Date']).dt.days  # sub-point: time difference
print(date_df)


# ----------------------------------------------------------
# Complete Case Analysis (CCA)
# ----------------------------------------------------------
# - The simplest missing-data strategy: drop any row that has
#   missing values in ANY of the selected columns.
# - Only safe when data is missing completely at random and the
#   percentage of missing rows is small.

cca_df = pd.DataFrame({'A': [1, np.nan, 3, 4], 'B': [5, 6, np.nan, 8]})
cca_result = cca_df.dropna()   # sub-point: complete case analysis
print(cca_result)
print(f"Rows kept: {len(cca_result)} out of {len(cca_df)}")


# ----------------------------------------------------------
# Missing Indicator
# ----------------------------------------------------------
# - Instead of (or in addition to) imputing, adds a new binary
#   column that flags WHERE data was originally missing - this
#   preserves the information that a value was missing.

from sklearn.impute import MissingIndicator

mi_df2 = pd.DataFrame({'A': [1, np.nan, 3, np.nan]})
indicator = MissingIndicator()
flags = indicator.fit_transform(mi_df2)
print(flags)   # True where the value was missing


# ----------------------------------------------------------
# KNN Imputer
# ----------------------------------------------------------
# - Fills missing values using the average of the K nearest
#   neighbors (based on the other available features) - smarter
#   than a plain mean/median fill.

from sklearn.impute import KNNImputer

knn_impute_df = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [10, 20, 30, np.nan]})
knn_imputer = KNNImputer(n_neighbors=2)
print(knn_imputer.fit_transform(knn_impute_df))


# ----------------------------------------------------------
# Iterative Imputer (MICE)
# ----------------------------------------------------------
# - Models each feature with missing values as a function of the
#   other features, and iterates until estimates stabilize -
#   more sophisticated than KNN imputation.

from sklearn.experimental import enable_iterative_imputer  # noqa - required to enable
from sklearn.impute import IterativeImputer

iter_df = pd.DataFrame({'A': [1, 2, np.nan, 4, 5], 'B': [2, 4, 6, 8, np.nan]})
iter_imputer = IterativeImputer(random_state=0)
print(iter_imputer.fit_transform(iter_df))


# ----------------------------------------------------------
# Outlier Detection using Percentiles
# ----------------------------------------------------------
# - A simpler alternative to IQR: cap/remove values outside a
#   chosen low and high percentile (e.g. below 1st or above 99th).

pct_data = np.array([12, 14, 13, 15, 16, 14, 100, 13, 15, 14, -50])

lower_pct = np.percentile(pct_data, 1)     # sub-point: 1st percentile as lower cutoff
upper_pct = np.percentile(pct_data, 99)     # sub-point: 99th percentile as upper cutoff
filtered_pct = pct_data[(pct_data >= lower_pct) & (pct_data <= upper_pct)]
print(filtered_pct)

capped = np.clip(pct_data, lower_pct, upper_pct)   # sub-point: cap instead of remove
print(capped)


# ----------------------------------------------------------
# Feature Construction and Feature Splitting
# ----------------------------------------------------------
# - Feature Construction: combine existing features into a new,
#   more informative one (e.g. Family_Size = SibSp + Parch + 1).
# - Feature Splitting: break one column into multiple useful parts
#   (e.g. splitting a "Name" column into Title/First/Last name).

fam_df = pd.DataFrame({'SibSp': [1, 0, 2], 'Parch': [0, 1, 1]})
fam_df['Family_Size'] = fam_df['SibSp'] + fam_df['Parch'] + 1   # sub-point: feature construction
print(fam_df)

name_df = pd.DataFrame({'Name': ['Smith, Mr. John', 'Doe, Mrs. Jane', 'Brown, Miss. Amy']})
name_df['Title'] = name_df['Name'].str.extract(r',\s*(\w+)\.')   # sub-point: feature splitting
print(name_df)


# ----------------------------------------------------------
# Curse of Dimensionality
# ----------------------------------------------------------
# - As the number of features (dimensions) grows, data becomes
#   increasingly sparse, distances between points become less
#   meaningful, and models need exponentially more data to
#   generalize well. This is why dimensionality reduction
#   (PCA, t-SNE, feature selection) matters.

for dims in [2, 10, 50, 100]:
    points = np.random.uniform(0, 1, (100, dims))
    dists = []
    for i in range(10):
        d = np.linalg.norm(points[i] - points[i + 1])
        dists.append(d)
    print(f"Dimensions={dims}, avg distance between points={np.mean(dists):.4f}")
    # sub-point: notice how average distance changes / points become more "spread out"
    # as dimensions increase, making nearest-neighbor style methods less effective


# ----------------------------------------------------------
# Regression Metrics (deeper)
# ----------------------------------------------------------
# - MAE: Mean Absolute Error - average of absolute differences.
# - MSE: Mean Squared Error - average of squared differences (penalizes big errors more).
# - RMSE: Root Mean Squared Error - same units as target variable.
# - R2 Score: proportion of variance explained by the model (higher is better, max 1).
# - Adjusted R2: R2 adjusted for the number of predictors (penalizes unnecessary features).

from sklearn.metrics import mean_absolute_error, mean_squared_error

y_true_reg = np.array([100, 150, 200, 250, 300])
y_pred_reg = np.array([110, 140, 210, 230, 310])

mae = mean_absolute_error(y_true_reg, y_pred_reg)
mse = mean_squared_error(y_true_reg, y_pred_reg)
rmse = np.sqrt(mse)
r2 = r2_score(y_true_reg, y_pred_reg)

n = len(y_true_reg)   # sub-point: adjusted R2 calculation
p = 1                   # number of predictors
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2:", r2)
print("Adjusted R2:", adj_r2)


# ----------------------------------------------------------
# Types of Gradient Descent
# ----------------------------------------------------------
# - Batch GD: uses the ENTIRE dataset to compute gradient each step
#   (stable but slow for large data).
# - Stochastic GD (SGD): uses ONE random sample per step (fast,
#   noisy convergence).
# - Mini-batch GD: uses a small random BATCH per step (a practical
#   middle ground - most commonly used in practice).

def batch_gradient_descent(X, y, lr=0.01, epochs=100):
    m, b = 0, 0
    n = len(X)
    for _ in range(epochs):
        y_pred = m * X + b
        dm = (-2 / n) * np.sum(X * (y - y_pred))
        db = (-2 / n) * np.sum(y - y_pred)
        m -= lr * dm
        b -= lr * db
    return m, b

X_gd = np.array([1, 2, 3, 4, 5], dtype=float)
y_gd = np.array([2, 4, 6, 8, 10], dtype=float)
m_final, b_final = batch_gradient_descent(X_gd, y_gd)
print(f"Batch GD result: m={m_final:.3f}, b={b_final:.3f}")   # sub-point: batch GD demo

from sklearn.linear_model import SGDRegressor
sgd_model = SGDRegressor(max_iter=1000, learning_rate='constant', eta0=0.01)  # sub-point: SGD via sklearn
sgd_model.fit(X_gd.reshape(-1, 1), y_gd)
print(sgd_model.coef_, sgd_model.intercept_)


# ----------------------------------------------------------
# Softmax Regression (Multiclass Logistic Regression)
# ----------------------------------------------------------
# - Extends logistic regression to handle MORE THAN 2 classes by
#   using the softmax function to output a probability for each class.

from sklearn.linear_model import LogisticRegression as LR5

iris_soft = load_iris()
X_soft, y_soft = iris_soft.data, iris_soft.target   # 3 classes

softmax_model = LR5(multi_class='multinomial', max_iter=200)  # sub-point: multinomial = softmax
softmax_model.fit(X_soft, y_soft)
print(softmax_model.predict_proba([X_soft[0]]))   # sub-point: probability for each of the 3 classes


# ----------------------------------------------------------
# Voting Ensemble
# ----------------------------------------------------------
# - Combines predictions from several DIFFERENT models by voting
#   (classification) or averaging (regression).
# - 'hard' voting = majority class wins; 'soft' voting = average
#   predicted probabilities.

from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression as LR6
from sklearn.svm import SVC as SVC2

X_vote, y_vote = load_iris(return_X_y=True)

voting_model = VotingClassifier(estimators=[
    ('lr', LR6(max_iter=200)),
    ('dt', DecisionTreeClassifier()),
    ('svc', SVC2(probability=True))
], voting='soft')   # sub-point: soft voting combines predicted probabilities

voting_model.fit(X_vote, y_vote)
print(voting_model.predict([X_vote[0]]))


# ----------------------------------------------------------
# XGBoost
# ----------------------------------------------------------
# - An optimized, faster, regularized implementation of Gradient
#   Boosting - one of the most popular algorithms for tabular data
#   competitions (e.g. on Kaggle).
# pip install xgboost
# from xgboost import XGBClassifier
# xgb_model = XGBClassifier(n_estimators=100, learning_rate=0.1)
# xgb_model.fit(X_train, y_train)
# print(xgb_model.score(X_test, y_test))
print("XGBoost - requires 'pip install xgboost' (see comments for usage)")


# ----------------------------------------------------------
# Blending
# ----------------------------------------------------------
# - Similar to Stacking, but the meta-model is trained on a
#   HOLD-OUT validation set (not via cross-validation), making it
#   simpler and faster than stacking, at a slight cost to robustness.

X_blend, y_blend = load_iris(return_X_y=True)
X_train_b, X_holdout, y_train_b, y_holdout = tts(X_blend, y_blend, test_size=0.3, random_state=1)
X_holdout_train, X_test_b, y_holdout_train, y_test_b = tts(X_holdout, y_holdout, test_size=0.5, random_state=1)

base1 = DecisionTreeClassifier().fit(X_train_b, y_train_b)   # sub-point: train base models on train set
base2 = KNN2(n_neighbors=3).fit(X_train_b, y_train_b)

holdout_preds = np.column_stack([   # sub-point: get base model predictions on holdout set
    base1.predict(X_holdout_train),
    base2.predict(X_holdout_train)
])
meta_model = LR6(max_iter=200).fit(holdout_preds, y_holdout_train)  # sub-point: train meta-model on those predictions

test_preds = np.column_stack([base1.predict(X_test_b), base2.predict(X_test_b)])
print("Blending accuracy:", meta_model.score(test_preds, y_test_b))


# ----------------------------------------------------------
# K-Means++ , Elbow Method & Silhouette Score
# ----------------------------------------------------------
# - K-Means++ is the default smart initialization for KMeans, which
#   picks better starting centroids than pure random (faster, more
#   stable convergence).
# - Elbow Method: plot inertia vs K, pick K at the "elbow" bend.
# - Silhouette Score: measures how well-separated clusters are
#   (ranges -1 to 1, higher is better).

from sklearn.metrics import silhouette_score

X_km2, _ = make_blobs(n_samples=300, centers=4, random_state=42)

km_pp = KMeans(n_clusters=4, init='k-means++', n_init=10, random_state=42)  # sub-point: k-means++ init
km_pp.fit(X_km2)

sil_scores = []
for k in range(2, 8):
    km_test = KMeans(n_clusters=k, init='k-means++', n_init=10, random_state=42)
    labels_test = km_test.fit_predict(X_km2)
    sil_scores.append(silhouette_score(X_km2, labels_test))   # sub-point: silhouette score per K

plt.plot(range(2, 8), sil_scores, marker='o')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Silhouette Score')
plt.title("Silhouette Score vs K")
plt.show()


# ----------------------------------------------------------
# Association Rule Learning (Apriori Algorithm)
# ----------------------------------------------------------
# - Finds relationships between items in transactional data
#   (e.g. "customers who buy bread also buy butter") - "Market
#   Basket Analysis".
# - Key metrics: Support, Confidence, Lift.
# pip install mlxtend
# from mlxtend.frequent_patterns import apriori, association_rules
# from mlxtend.preprocessing import TransactionEncoder
#
# transactions = [['bread', 'milk'], ['bread', 'diaper', 'beer'], ['milk', 'diaper', 'beer', 'coke']]
# te = TransactionEncoder()
# te_data = te.fit(transactions).transform(transactions)
# trans_df = pd.DataFrame(te_data, columns=te.columns_)
# frequent_itemsets = apriori(trans_df, min_support=0.3, use_colnames=True)
# rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
# print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
print("Apriori / Association Rules - requires 'pip install mlxtend' (see comments)")


# ----------------------------------------------------------
# Model Deployment Basics
# ----------------------------------------------------------
# - Once trained, a model needs to be saved and served so it can
#   be used in a real application.
# - pickle/joblib saves the trained model to disk.
# - Flask/Streamlit/FastAPI serve the model via a web app or API.

import pickle

deploy_model = LogisticRegression()
X_dep, y_dep = load_iris(return_X_y=True)
deploy_model.fit(X_dep, y_dep)

with open('model.pkl', 'wb') as f:
    pickle.dump(deploy_model, f)   # sub-point: save trained model to disk

with open('model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)   # sub-point: load model back for use in an app
print(loaded_model.predict([X_dep[0]]))

# Example Flask snippet for serving predictions (conceptual, not run here):
# from flask import Flask, request, jsonify
# app = Flask(__name__)
# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json['features']
#     prediction = loaded_model.predict([data])
#     return jsonify({'prediction': int(prediction[0])})


# ==========================================================
# ALL TYPES OF ML MODELS - REGRESSION, CLASSIFICATION, CLUSTERING
# ==========================================================

# ==========================================================
# PART A: ALL REGRESSION MODELS
# (predicting a CONTINUOUS numeric value)
# ==========================================================

from sklearn.model_selection import train_test_split as tts2
from sklearn.datasets import make_regression, load_diabetes

X_reg, y_reg = make_regression(n_samples=200, n_features=1, noise=15, random_state=42)
X_reg_tr, X_reg_te, y_reg_tr, y_reg_te = tts2(X_reg, y_reg, test_size=0.2, random_state=42)

# ----------------------------------------------------------
# 1. Linear Regression
# ----------------------------------------------------------
# - Fits a straight line: y = mx + b. Best for simple linear relationships.
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_reg_tr, y_reg_tr)
print("Linear Regression R2:", lin_reg.score(X_reg_te, y_reg_te))

# ----------------------------------------------------------
# 2. Polynomial Regression
# ----------------------------------------------------------
# - Linear Regression applied to polynomial-transformed features,
#   fits curves instead of straight lines.
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=3)
X_poly_tr = poly.fit_transform(X_reg_tr)
X_poly_te = poly.transform(X_reg_te)
poly_reg = LinearRegression()
poly_reg.fit(X_poly_tr, y_reg_tr)
print("Polynomial Regression R2:", poly_reg.score(X_poly_te, y_reg_te))

# ----------------------------------------------------------
# 3. Ridge Regression (L2)
# ----------------------------------------------------------
# - Linear Regression + penalty on the SQUARE of coefficients (shrinks them).
from sklearn.linear_model import Ridge
ridge_reg = Ridge(alpha=1.0)
ridge_reg.fit(X_reg_tr, y_reg_tr)
print("Ridge R2:", ridge_reg.score(X_reg_te, y_reg_te))

# ----------------------------------------------------------
# 4. Lasso Regression (L1)
# ----------------------------------------------------------
# - Linear Regression + penalty on ABSOLUTE coefficients (can zero some out).
from sklearn.linear_model import Lasso
lasso_reg = Lasso(alpha=0.1)
lasso_reg.fit(X_reg_tr, y_reg_tr)
print("Lasso R2:", lasso_reg.score(X_reg_te, y_reg_te))

# ----------------------------------------------------------
# 5. Elastic Net Regression
# ----------------------------------------------------------
# - Combines Ridge (L2) and Lasso (L1) penalties together.
from sklearn.linear_model import ElasticNet
elastic_reg = ElasticNet(alpha=0.1, l1_ratio=0.5)
elastic_reg.fit(X_reg_tr, y_reg_tr)
print("ElasticNet R2:", elastic_reg.score(X_reg_te, y_reg_te))

# ----------------------------------------------------------
# 6. Support Vector Regression (SVR)
# ----------------------------------------------------------
# - SVM adapted for regression: fits a line/curve within a margin
#   of tolerance ('epsilon'), ignoring small errors within that margin.
from sklearn.svm import SVR
svr_model = SVR(kernel='rbf', C=100, epsilon=0.1)
svr_model.fit(X_reg_tr, y_reg_tr)
print("SVR R2:", svr_model.score(X_reg_te, y_reg_te))

# ----------------------------------------------------------
# 7. Decision Tree Regressor
# ----------------------------------------------------------
# - Splits data into regions based on feature thresholds, predicts
#   the average value of the region a new point falls into.
from sklearn.tree import DecisionTreeRegressor
dt_reg = DecisionTreeRegressor(max_depth=5, random_state=42)
dt_reg.fit(X_reg_tr, y_reg_tr)
print("Decision Tree Regressor R2:", dt_reg.score(X_reg_te, y_reg_te))

# ----------------------------------------------------------
# 8. K-Nearest Neighbors (KNN) Regressor
# ----------------------------------------------------------
# - Predicts a value as the average of the K nearest neighbors' values.
from sklearn.neighbors import KNeighborsRegressor
knn_reg = KNeighborsRegressor(n_neighbors=5)
knn_reg.fit(X_reg_tr, y_reg_tr)
print("KNN Regressor R2:", knn_reg.score(X_reg_te, y_reg_te))

# ----------------------------------------------------------
# 9. Random Forest Regressor
# ----------------------------------------------------------
# - Ensemble of many Decision Tree Regressors, predictions averaged
#   together for a more stable, less overfit result.
from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(n_estimators=100, random_state=42)
rf_reg.fit(X_reg_tr, y_reg_tr)
print("Random Forest Regressor R2:", rf_reg.score(X_reg_te, y_reg_te))

# ----------------------------------------------------------
# 10. AdaBoost Regressor
# ----------------------------------------------------------
# - Boosting: sequentially trains weak learners, each focusing more
#   on the previous model's errors.
from sklearn.ensemble import AdaBoostRegressor
ada_reg = AdaBoostRegressor(n_estimators=50, random_state=42)
ada_reg.fit(X_reg_tr, y_reg_tr)
print("AdaBoost Regressor R2:", ada_reg.score(X_reg_te, y_reg_te))

# ----------------------------------------------------------
# 11. Gradient Boosting Regressor
# ----------------------------------------------------------
# - Boosting using gradient descent to minimize the loss function
#   at each step - usually stronger than AdaBoost.
from sklearn.ensemble import GradientBoostingRegressor
gb_reg = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
gb_reg.fit(X_reg_tr, y_reg_tr)
print("Gradient Boosting Regressor R2:", gb_reg.score(X_reg_te, y_reg_te))

# ----------------------------------------------------------
# 12. XGBoost Regressor
# ----------------------------------------------------------
# - Optimized, regularized gradient boosting - very popular for
#   tabular data competitions.
# from xgboost import XGBRegressor
# xgb_reg = XGBRegressor(n_estimators=100, learning_rate=0.1)
# xgb_reg.fit(X_reg_tr, y_reg_tr)
# print("XGBoost Regressor R2:", xgb_reg.score(X_reg_te, y_reg_te))
print("XGBoost Regressor - requires 'pip install xgboost' (see comments)")

# ----------------------------------------------------------
# 13. Bayesian Ridge Regression
# ----------------------------------------------------------
# - A probabilistic version of Ridge Regression; estimates coefficients
#   as probability distributions rather than fixed values, naturally
#   regularizing and providing uncertainty estimates.
from sklearn.linear_model import BayesianRidge
bayes_reg = BayesianRidge()
bayes_reg.fit(X_reg_tr, y_reg_tr)
print("Bayesian Ridge R2:", bayes_reg.score(X_reg_te, y_reg_te))

# ----------------------------------------------------------
# 14. Huber Regressor (Robust Regression)
# ----------------------------------------------------------
# - Combines squared loss (for small errors) and absolute loss (for
#   large errors), making it less sensitive to outliers than plain
#   Linear Regression.
from sklearn.linear_model import HuberRegressor
huber_reg = HuberRegressor()
huber_reg.fit(X_reg_tr, y_reg_tr.ravel())
print("Huber Regressor score:", huber_reg.score(X_reg_te, y_reg_te))


# ==========================================================
# PART B: ALL CLASSIFICATION MODELS
# (predicting a DISCRETE category/class)
# ==========================================================

from sklearn.datasets import load_wine
X_clf, y_clf = load_wine(return_X_y=True)
X_clf_tr, X_clf_te, y_clf_tr, y_clf_te = tts2(X_clf, y_clf, test_size=0.2, random_state=42)

# ----------------------------------------------------------
# 1. Logistic Regression
# ----------------------------------------------------------
# - Predicts class probabilities using the sigmoid/softmax function;
#   despite the name, it's a classification algorithm.
from sklearn.linear_model import LogisticRegression
log_clf = LogisticRegression(max_iter=5000)
log_clf.fit(X_clf_tr, y_clf_tr)
print("Logistic Regression accuracy:", log_clf.score(X_clf_te, y_clf_te))

# ----------------------------------------------------------
# 2. K-Nearest Neighbors (KNN) Classifier
# ----------------------------------------------------------
# - Classifies a point based on the majority class among its K
#   nearest neighbors.
from sklearn.neighbors import KNeighborsClassifier
knn_clf = KNeighborsClassifier(n_neighbors=5)
knn_clf.fit(X_clf_tr, y_clf_tr)
print("KNN Classifier accuracy:", knn_clf.score(X_clf_te, y_clf_te))

# ----------------------------------------------------------
# 3. Decision Tree Classifier
# ----------------------------------------------------------
# - Splits data using a flowchart of if/else feature-based decisions.
from sklearn.tree import DecisionTreeClassifier
dt_clf = DecisionTreeClassifier(max_depth=5, random_state=42)
dt_clf.fit(X_clf_tr, y_clf_tr)
print("Decision Tree Classifier accuracy:", dt_clf.score(X_clf_te, y_clf_te))

# ----------------------------------------------------------
# 4. Random Forest Classifier
# ----------------------------------------------------------
# - Ensemble of many Decision Trees, prediction by majority vote.
from sklearn.ensemble import RandomForestClassifier
rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)
rf_clf.fit(X_clf_tr, y_clf_tr)
print("Random Forest Classifier accuracy:", rf_clf.score(X_clf_te, y_clf_te))

# ----------------------------------------------------------
# 5. Support Vector Machine (SVM) Classifier
# ----------------------------------------------------------
# - Finds the best boundary (hyperplane) that separates classes
#   with maximum margin; kernel trick handles non-linear boundaries.
from sklearn.svm import SVC
svm_clf = SVC(kernel='rbf', random_state=42)
svm_clf.fit(X_clf_tr, y_clf_tr)
print("SVM Classifier accuracy:", svm_clf.score(X_clf_te, y_clf_te))

# ----------------------------------------------------------
# 6. Gaussian Naive Bayes
# ----------------------------------------------------------
# - Assumes features follow a normal distribution within each class;
#   fast, works well for continuous features.
from sklearn.naive_bayes import GaussianNB
gnb_clf = GaussianNB()
gnb_clf.fit(X_clf_tr, y_clf_tr)
print("Gaussian Naive Bayes accuracy:", gnb_clf.score(X_clf_te, y_clf_te))

# ----------------------------------------------------------
# 7. Multinomial Naive Bayes
# ----------------------------------------------------------
# - Best for discrete count data (e.g. word counts in text
#   classification / spam detection).
from sklearn.naive_bayes import MultinomialNB
X_counts = np.abs(X_clf).astype(int)   # sub-point: needs non-negative count-like data
mnb_clf = MultinomialNB()
mnb_clf.fit(X_counts[:len(X_clf_tr)], y_clf_tr)
print("Multinomial Naive Bayes accuracy:", mnb_clf.score(X_counts[len(X_clf_tr):], y_clf_te))

# ----------------------------------------------------------
# 8. Bernoulli Naive Bayes
# ----------------------------------------------------------
# - Best for binary/boolean features (e.g. word present/absent in text).
from sklearn.naive_bayes import BernoulliNB
X_binary = (X_clf > np.median(X_clf)).astype(int)   # sub-point: convert to binary features
bnb_clf = BernoulliNB()
bnb_clf.fit(X_binary[:len(X_clf_tr)], y_clf_tr)
print("Bernoulli Naive Bayes accuracy:", bnb_clf.score(X_binary[len(X_clf_tr):], y_clf_te))

# ----------------------------------------------------------
# 9. AdaBoost Classifier
# ----------------------------------------------------------
# - Sequentially trains weak learners, each correcting previous errors.
from sklearn.ensemble import AdaBoostClassifier
ada_clf = AdaBoostClassifier(n_estimators=50, random_state=42)
ada_clf.fit(X_clf_tr, y_clf_tr)
print("AdaBoost Classifier accuracy:", ada_clf.score(X_clf_te, y_clf_te))

# ----------------------------------------------------------
# 10. Gradient Boosting Classifier
# ----------------------------------------------------------
# - Boosting via gradient descent on the loss function.
from sklearn.ensemble import GradientBoostingClassifier
gb_clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
gb_clf.fit(X_clf_tr, y_clf_tr)
print("Gradient Boosting Classifier accuracy:", gb_clf.score(X_clf_te, y_clf_te))

# ----------------------------------------------------------
# 11. XGBoost Classifier
# ----------------------------------------------------------
# - Optimized, regularized gradient boosting implementation.
# from xgboost import XGBClassifier
# xgb_clf = XGBClassifier(n_estimators=100, learning_rate=0.1)
# xgb_clf.fit(X_clf_tr, y_clf_tr)
# print("XGBoost Classifier accuracy:", xgb_clf.score(X_clf_te, y_clf_te))
print("XGBoost Classifier - requires 'pip install xgboost' (see comments)")

# ----------------------------------------------------------
# 12. Linear Discriminant Analysis (LDA)
# ----------------------------------------------------------
# - Finds a linear combination of features that best SEPARATES
#   classes; also usable for dimensionality reduction.
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
lda_clf = LinearDiscriminantAnalysis()
lda_clf.fit(X_clf_tr, y_clf_tr)
print("LDA accuracy:", lda_clf.score(X_clf_te, y_clf_te))

# ----------------------------------------------------------
# 13. Quadratic Discriminant Analysis (QDA)
# ----------------------------------------------------------
# - Like LDA, but allows a different (curved/quadratic) boundary
#   per class instead of a single shared linear boundary.
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
qda_clf = QuadraticDiscriminantAnalysis()
qda_clf.fit(X_clf_tr, y_clf_tr)
print("QDA accuracy:", qda_clf.score(X_clf_te, y_clf_te))

# ----------------------------------------------------------
# 14. Perceptron
# ----------------------------------------------------------
# - The simplest neural network: a single neuron/linear classifier,
#   the foundational building block of modern neural networks.
from sklearn.linear_model import Perceptron
perc_clf = Perceptron(max_iter=1000, random_state=42)
perc_clf.fit(X_clf_tr, y_clf_tr)
print("Perceptron accuracy:", perc_clf.score(X_clf_te, y_clf_te))

# ----------------------------------------------------------
# 15. Multi-Layer Perceptron (Neural Network) Classifier
# ----------------------------------------------------------
# - A fully-connected feedforward neural network with one or more
#   hidden layers, trained via backpropagation.
from sklearn.neural_network import MLPClassifier
mlp_clf = MLPClassifier(hidden_layer_sizes=(20, 10), max_iter=2000, random_state=42)
mlp_clf.fit(X_clf_tr, y_clf_tr)
print("MLP Classifier accuracy:", mlp_clf.score(X_clf_te, y_clf_te))


# ==========================================================
# PART C: ALL CLUSTERING MODELS (Unsupervised)
# (grouping similar data points without labels)
# ==========================================================

from sklearn.datasets import make_blobs, make_moons
X_clust, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.8, random_state=42)

# ----------------------------------------------------------
# 1. K-Means Clustering
# ----------------------------------------------------------
# - Partitions data into K clusters by minimizing distance to
#   cluster centroids. Requires specifying K in advance.
from sklearn.cluster import KMeans
kmeans_c = KMeans(n_clusters=4, init='k-means++', n_init=10, random_state=42)
labels_km = kmeans_c.fit_predict(X_clust)
plt.scatter(X_clust[:, 0], X_clust[:, 1], c=labels_km, cmap='viridis')
plt.title("K-Means Clustering")
plt.show()

# ----------------------------------------------------------
# 2. Hierarchical (Agglomerative) Clustering
# ----------------------------------------------------------
# - Builds a tree (dendrogram) of nested clusters by repeatedly
#   merging the closest pairs of clusters/points.
from sklearn.cluster import AgglomerativeClustering
agg_c = AgglomerativeClustering(n_clusters=4)
labels_agg = agg_c.fit_predict(X_clust)
plt.scatter(X_clust[:, 0], X_clust[:, 1], c=labels_agg, cmap='viridis')
plt.title("Hierarchical Clustering")
plt.show()

# ----------------------------------------------------------
# 3. DBSCAN (Density-Based)
# ----------------------------------------------------------
# - Groups closely-packed points, marks sparse points as noise.
# - Does not need K specified; finds irregularly shaped clusters.
from sklearn.cluster import DBSCAN
X_moons, _ = make_moons(n_samples=300, noise=0.05, random_state=42)
dbscan_c = DBSCAN(eps=0.2, min_samples=5)
labels_db = dbscan_c.fit_predict(X_moons)
plt.scatter(X_moons[:, 0], X_moons[:, 1], c=labels_db, cmap='viridis')
plt.title("DBSCAN Clustering")
plt.show()

# ----------------------------------------------------------
# 4. Mean Shift Clustering
# ----------------------------------------------------------
# - Finds clusters by shifting points toward areas of higher
#   density until convergence - automatically determines the
#   number of clusters (no K needed).
from sklearn.cluster import MeanShift
ms_c = MeanShift()
labels_ms = ms_c.fit_predict(X_clust)
plt.scatter(X_clust[:, 0], X_clust[:, 1], c=labels_ms, cmap='viridis')
plt.title("Mean Shift Clustering")
plt.show()
print("Mean Shift found clusters:", len(set(labels_ms)))

# ----------------------------------------------------------
# 5. Gaussian Mixture Models (GMM)
# ----------------------------------------------------------
# - Assumes data is generated from a mixture of several Gaussian
#   (normal) distributions; unlike K-means, gives "soft" cluster
#   assignments (probability of belonging to each cluster).
from sklearn.mixture import GaussianMixture
gmm_c = GaussianMixture(n_components=4, random_state=42)
labels_gmm = gmm_c.fit_predict(X_clust)
plt.scatter(X_clust[:, 0], X_clust[:, 1], c=labels_gmm, cmap='viridis')
plt.title("Gaussian Mixture Model Clustering")
plt.show()
print(gmm_c.predict_proba(X_clust[:3]))   # sub-point: soft probabilities per cluster

# ----------------------------------------------------------
# 6. Spectral Clustering
# ----------------------------------------------------------
# - Uses the eigenvalues of a similarity graph to reduce
#   dimensionality before clustering - good at finding clusters
#   with complex, non-convex shapes.
from sklearn.cluster import SpectralClustering
spec_c = SpectralClustering(n_clusters=2, affinity='nearest_neighbors', random_state=42)
labels_spec = spec_c.fit_predict(X_moons)
plt.scatter(X_moons[:, 0], X_moons[:, 1], c=labels_spec, cmap='viridis')
plt.title("Spectral Clustering")
plt.show()

# ----------------------------------------------------------
# 7. Affinity Propagation
# ----------------------------------------------------------
# - Clusters by having data points "vote" for exemplar points that
#   best represent them; automatically determines number of clusters.
from sklearn.cluster import AffinityPropagation
ap_c = AffinityPropagation(random_state=42)
labels_ap = ap_c.fit_predict(X_clust)
plt.scatter(X_clust[:, 0], X_clust[:, 1], c=labels_ap, cmap='viridis')
plt.title("Affinity Propagation Clustering")
plt.show()
print("Affinity Propagation found clusters:", len(set(labels_ap)))

# ----------------------------------------------------------
# 8. OPTICS (Ordering Points To Identify Clustering Structure)
# ----------------------------------------------------------
# - Similar to DBSCAN but handles clusters of VARYING density
#   better, by producing a reachability plot instead of one fixed eps.
from sklearn.cluster import OPTICS
optics_c = OPTICS(min_samples=5)
labels_optics = optics_c.fit_predict(X_moons)
plt.scatter(X_moons[:, 0], X_moons[:, 1], c=labels_optics, cmap='viridis')
plt.title("OPTICS Clustering")
plt.show()

# ----------------------------------------------------------
# 9. BIRCH (Balanced Iterative Reducing and Clustering)
# ----------------------------------------------------------
# - Builds a compact tree summary of the data first, making it
#   efficient for VERY LARGE datasets that don't fit in memory easily.
from sklearn.cluster import Birch
birch_c = Birch(n_clusters=4)
labels_birch = birch_c.fit_predict(X_clust)
plt.scatter(X_clust[:, 0], X_clust[:, 1], c=labels_birch, cmap='viridis')
plt.title("BIRCH Clustering")
plt.show()


# ==========================================================
# END OF NOTES
# ==========================================================