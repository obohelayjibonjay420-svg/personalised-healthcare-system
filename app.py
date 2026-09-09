Gender
Alcohol_Missing    0    1
Gender                   
Female           727  236
Male             803  234
Chi-square = 0.942, p = 0.3318

Smoking_Status
Alcohol_Missing    0    1
Smoking_Status           
Current smoker   322   87
Former smoker    337  113
Non-smoker       871  270
Chi-square = 1.797, p = 0.4073

Physical_Activity_Level
Alcohol_Missing            0    1
Physical_Activity_Level          
Highly Active            219   58
Lightly Active           451  148
Moderately Active        467  131
Sedentary                393  133
Chi-square = 3.274, p = 0.3512

Diet_Type
Alcohol_Missing    0   1
Diet_Type               
Balanced         291  74
High Protein     250  73
Keto             223  82
Mediterranean    245  76
Vegan            268  78
Vegetarian       253  87
Chi-square = 5.209, p = 0.3909

Sleep_Quality
Alcohol_Missing    0    1
Sleep_Quality            
Excellent        193   68
Fair             750  223
Good             278   70
Poor             309  109
Chi-square = 4.891, p = 0.1799

Age                       t =   -1.113, p = 0.2662
BMI                       t =   -0.581, p = 0.5616
Cholesterol               t =    0.562, p = 0.5741
Glucose_Level             t =   -0.014, p = 0.9887
HbA1c                     t =   -0.616, p = 0.5382
Stress_Level              t =   -0.084, p = 0.9332
Depression_Score          t =   -0.713, p = 0.4759
Anxiety_Score             t =    0.182, p = 0.8554
Sleep_Hours               t =    1.165, p = 0.2443
Systolic_BP               t =   -0.569, p = 0.5692
Diastolic_BP              t =    0.525, p = 0.5998
LDL                       t =    0.574, p = 0.5659
HDL                       t =    0.827, p = 0.4087
Triglycerides             t =   -0.709, p = 0.4785
CRP                       t =   -0.056, p = 0.9551
eGFR                      t =   -0.176, p = 0.8602
Waist_Circumference       t =   -0.721, p = 0.4714

Alcohol_Consumption_Clean
Moderate    664
Low         551
Unknown     470
High        315
Name: count, dtype: int64

0        Unknown
1            Low
2            Low
3           High
4            Low
          ...   
1995        High
1996         Low
1997    Moderate
1998         Low
1999    Moderate
Name: Alcohol_Consumption_Clean, Length: 2000, dtype: str

Variable	Q1	Q3	IQR	Lower_Bound	Upper_Bound	Min	Max	Outliers_n	Outliers_%
11	Social_Isolation_Index	4.00000	6.00000	2.00000	1.000000	9.000000	0.000	10.000	32	1.60
3	Glucose_Level	83.10000	99.80000	16.70000	58.050000	124.850000	50.000	134.200	23	1.15
2	Cholesterol	174.87500	219.20000	44.32500	108.387500	285.687500	83.600	328.400	21	1.05
16	Diastolic_BP	65.00000	77.00000	12.00000	47.000000	95.000000	40.000	109.000	15	0.75
15	Systolic_BP	102.00000	120.00000	18.00000	75.000000	147.000000	80.000	153.000	13	0.65
7	PRS_Type2Diabetes	-0.67675	0.71025	1.38700	-2.757250	2.790750	-3.000	3.000	13	0.65
20	CRP	0.83000	2.09000	1.26000	-1.060000	3.980000	0.000	4.710	13	0.65
19	Triglycerides	107.10000	186.52500	79.42500	-12.037500	305.662500	20.000	335.200	11	0.55
1	BMI	23.80000	30.50000	6.70000	13.750000	40.550000	16.000	50.300	10	0.50
10	Anxiety_Score	3.00000	7.00000	4.00000	-3.000000	13.000000	0.000	16.000	10	0.50
17	LDL	96.20000	137.02500	40.82500	34.962500	198.262500	40.000	244.600	10	0.50
14	HRV	40.00000	59.00000	19.00000	11.500000	87.500000	10.000	96.000	9	0.45
18	HDL	42.20000	59.30000	17.10000	16.550000	84.950000	10.000	91.800	9	0.45
22	Waist_Circumference	55.87500	73.82500	17.95000	28.950000	100.750000	50.000	127.100	8	0.40
6	PRS_Cardiometabolic	-0.68800	0.66325	1.35125	-2.714875	2.690125	-2.909	2.939	6	0.30
21	eGFR	92.20000	113.70000	21.50000	59.950000	145.950000	55.300	140.000	6	0.30
4	HbA1c	4.60000	5.50000	0.90000	3.250000	6.850000	3.500	7.100	5	0.25
9	Depression_Score	3.00000	9.00000	6.00000	-6.000000	18.000000	0.000	19.000	1	0.05
13	Resting_Heart_Rate	66.00000	77.00000	11.00000	49.500000	93.500000	47.000	93.000	1	0.05
5	Predicted_Insurance_Cost	598.19000	2018.10250	1419.91250	-1531.678750	4147.971250	331.800	3684.190	0	0.00
0	Age	38.00000	60.00000	22.00000	5.000000	93.000000	18.000	85.000	0	0.00
12	Sleep_Hours	6.00000	7.70000	1.70000	3.450000	10.250000	3.500	10.000	0	0.00
8	Stress_Level	4.20000	7.10000	2.90000	-0.150000	11.450000	1.000	10.000	0	0.00
skewness = df[numeric_vars].skew().sort_values(ascending=False)

print(skewness)
Waist_Circumference         0.603293
Predicted_Insurance_Cost    0.434751
Anxiety_Score               0.375843
CRP                         0.333699
Depression_Score            0.287178
BMI                         0.223132
Triglycerides               0.143008
Systolic_BP                 0.099280
HbA1c                       0.089874
HDL                         0.064598
LDL                         0.059205
Diastolic_BP                0.047058
Sleep_Hours                 0.030920
Age                         0.025432
Cholesterol                 0.022176
Social_Isolation_Index      0.020629
PRS_Cardiometabolic         0.014431
Resting_Heart_Rate          0.009821
HRV                        -0.001511
Glucose_Level              -0.021651
PRS_Type2Diabetes          -0.045078
Stress_Level               -0.045127
eGFR                       -0.090299
dtype: float64
import matplotlib.pyplot as plt

plot_vars = [
    'Age',
    'BMI',
    'Glucose_Level',
    'HbA1c',
    'Systolic_BP',
    'LDL',
    'HDL',
    'Triglycerides',
    'CRP',
    'eGFR',
    'Waist_Circumference'
]

for col in plot_vars:
    plt.figure(figsize=(7, 4))
    plt.hist(df[col].dropna(), bins=30)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()













Pasted markdown(20260909-125435).md
File
machine learning approch a jaor jnno data set ready koro

Supervised or jeta applicable hoy ta step by step dao(keno dile tar too short explain korbe)
my idea: jehetu eta Personalised Healthcare Recommendation System dataset
Ami unique and effective proto type or jet banale most impactful hbe ta korte cai
Next... 
X shape: (2000, 32)

Categorical variables:
['Gender', 'Smoking_Status', 'Alcohol_Consumption', 'Physical_Activity_Level', 'Diet_Type', 'Sleep_Quality']

Numerical variables:
['Age', 'BMI', 'Cholesterol', 'Glucose_Level', 'HbA1c', 'PRS_Cardiometabolic', 'PRS_Type2Diabetes', 'APOE_e4_Carrier', 'BRCA_Pathogenic_Variant', 'Family_History_CVD', 'Family_History_T2D', 'Stress_Level', 'Depression_Score', 'Anxiety_Score', 'Social_Isolation_Index', 'Sleep_Hours', 'Resting_Heart_Rate', 'HRV', 'Systolic_BP', 'Diastolic_BP', 'LDL', 'HDL', 'Triglycerides', 'CRP', 'eGFR', 'Waist_Circumference']

Total features: 32


svg

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(

X,

y,

test\_size**=**0.20,

random\_state**=**42,

stratify**=**y

)

print("Training set:", X_train.shape)

print("Testing set :", X_test.shape)

print("\nTraining target:")

print(y_train.value_counts())

print("\nTesting target:")

print(y_test.value_counts())

Training set: (1600, 32)
Testing set : (400, 32)

Training target:
Health_Risk
Low         647
High        498
Moderate    455
Name: count, dtype: int64

Testing target:
Health_Risk
Low         162
High        125
Moderate    113
Name: count, dtype: int64


svg

from sklearn.compose import ColumnTransformer

from sklearn.pipeline import Pipeline

from sklearn.preprocessing import OneHotEncoder, StandardScaler

from sklearn.impute import SimpleImputer

numeric_transformer = Pipeline([

('imputer', SimpleImputer(strategy**=**'median')),

('scaler', StandardScaler())

])

categorical_transformer = Pipeline([

('imputer', SimpleImputer(strategy**=**'most_frequent')),

('onehot', OneHotEncoder(

    handle\_unknown**=**'ignore',

    sparse\_output**=False**

))

])

preprocessor = ColumnTransformer([

('num', numeric_transformer, numeric_cols),

('cat', categorical_transformer, categorical_cols)

])

print("Preprocessor ready.")

Preprocessor ready.


from sklearn.linear_model import LogisticRegression

logistic_model = Pipeline([

('preprocessor', preprocessor),

('classifier', LogisticRegression(

    max\_iter**=**2000,

    class\_weight**=**'balanced',

    random\_state**=**42

))

])

logistic_model.fit(X_train, y_train)

print("Logistic Regression trained successfully.")

Logistic Regression trained successfully.


from sklearn.ensemble import RandomForestClassifier

rf_model = Pipeline([

('preprocessor', preprocessor),

('classifier', RandomForestClassifier(

    n\_estimators**=**500,

    random\_state**=**42,

    class\_weight**=**'balanced',

    n\_jobs**=-**1

))

])

rf_model.fit(X_train, y_train)

print("Random Forest trained successfully.")

Random Forest trained successfully.


from sklearn.ensemble import ExtraTreesClassifier

extra_model = Pipeline([

('preprocessor', preprocessor),

('classifier', ExtraTreesClassifier(

    n\_estimators**=**500,

    random\_state**=**42,

    class\_weight**=**'balanced',

    n\_jobs**=-**1

))

])

extra_model.fit(X_train, y_train)

print("Extra Trees trained successfully.")

Extra Trees trained successfully.


from sklearn.metrics import (

accuracy\_score,

balanced\_accuracy\_score,

f1\_score,

precision\_score,

recall\_score,

classification\_report

)

models = {

'Logistic Regression': logistic_model,

'Random Forest': rf_model,

'Extra Trees': extra_model

}

results = []

for name, model in models.items():

y\_pred **=** model.predict(X\_test)

results.append({

'Model': name,

'Accuracy': accuracy_score(y_test, y_pred),

'Balanced_Accuracy': balanced_accuracy_score(y_test, y_pred),

'Macro_Precision': precision_score(

        y\_test, y\_pred, average**=**'macro'

),

'Macro_Recall': recall_score(

        y\_test, y\_pred, average**=**'macro'

),

'Macro_F1': f1_score(

        y\_test, y\_pred, average**=**'macro'

),

'Weighted_F1': f1_score(

        y\_test, y\_pred, average**=**'weighted'

)

})

results_df = pd.DataFrame(results)

results_df = results_df.sort_values(

'Macro_F1',

ascending**=False**

)

display(results_df.round(4))

ModelAccuracyBalanced_AccuracyMacro_PrecisionMacro_RecallMacro_F1Weighted_F1							
0	Logistic Regression	0.9150	0.9127	0.9125	0.9127	0.9124	0.9156
1	Random Forest	0.7925	0.7745	0.7766	0.7745	0.7741	0.7877
2	Extra Trees	0.7625	0.7318	0.7462	0.7318	0.7175	0.7379

svg

for name, model in models.items():

y\_pred **=** model.predict(X\_test)

print("\n" + "="*70)

print(name)

print("="*70)

print(

    classification\_report(

        y\_test,

        y\_pred,

        digits**=**4

)

)

======================================================================
Logistic Regression
======================================================================
              precision    recall  f1-score   support

        High     0.9669    0.9360    0.9512       125
         Low     0.9317    0.9259    0.9288       162
    Moderate     0.8390    0.8761    0.8571       113

    accuracy                         0.9150       400
   macro avg     0.9125    0.9127    0.9124       400
weighted avg     0.9165    0.9150    0.9156       400


======================================================================
Random Forest
======================================================================
              precision    recall  f1-score   support

        High     0.8425    0.8560    0.8492       125
         Low     0.8343    0.9012    0.8665       162
    Moderate     0.6531    0.5664    0.6066       113

    accuracy                         0.7925       400
   macro avg     0.7766    0.7745    0.7741       400
weighted avg     0.7857    0.7925    0.7877       400


======================================================================
Extra Trees
======================================================================
              precision    recall  f1-score   support

        High     0.7551    0.8880    0.8162       125
         Low     0.7887    0.9444    0.8596       162
    Moderate     0.6949    0.3628    0.4767       113

    accuracy                         0.7625       400
   macro avg     0.7462    0.7318    0.7175       400
weighted avg     0.7517    0.7625    0.7379       400

Pasted markdown(20260909-130650).md
File
here the output of step 13-15

Pasted markdown(20260909-130956).md
File
next
Pasted markdown(20260909-131235).md
File
Next...
HighLowModerate			
0	0.0000	1.0000	0.0000
1	0.3311	0.0005	0.6684
2	0.9985	0.0000	0.0015
3	0.0000	0.9996	0.0004
4	0.3595	0.0134	0.6271
5	1.0000	0.0000	0.0000
6	0.0000	0.9923	0.0077
7	0.0000	0.9978	0.0022
8	0.0000	1.0000	0.0000
9	0.0000	0.9771	0.0229
<br>ClassBrier_Score		
0	High	0.0269
1	Low	0.0446
2	Moderate	0.0672
Macro ROC-AUC: 0.9782
Weighted ROC-AUC: 0.9794

=====================================================================
Top predictors — High
======================================================================
Feature	Coefficient	Odds_Ratio	Abs_Coefficient
0	num__Age	3.7130	40.9782	3.7130
20	num__LDL	3.0183	20.4574	3.0183
5	num__PRS_Cardiometabolic	2.7689	15.9411	2.7689
21	num__HDL	-2.6269	0.0723	2.6269
9	num__Family_History_CVD	2.1487	8.5733	2.1487
30	cat__Smoking_Status_Non-smoker	-1.6041	0.2011	1.6041
2	num__Cholesterol	1.5092	4.5231	1.5092
28	cat__Smoking_Status_Current smoker	1.4671	4.3365	1.4671
18	num__Systolic_BP	1.3580	3.8883	1.3580
22	num__Triglycerides	-0.5615	0.5704	0.5615
3	num__Glucose_Level	0.4850	1.6242	0.4850
6	num__PRS_Type2Diabetes	0.4786	1.6138	0.4786
45	cat__Sleep_Quality_Excellent	-0.3427	0.7099	0.3427
37	cat__Physical_Activity_Level_Moderately Active	-0.3193	0.7267	0.3193
40	cat__Diet_Type_High Protein	0.2649	1.3034	0.2649

======================================================================
Top predictors — Low
======================================================================
Feature	Coefficient	Odds_Ratio	Abs_Coefficient
0	num__Age	-3.4704	0.0311	3.4704
20	num__LDL	-2.5848	0.0754	2.5848
5	num__PRS_Cardiometabolic	-2.4607	0.0854	2.4607
21	num__HDL	2.3070	10.0438	2.3070
9	num__Family_History_CVD	-1.9356	0.1443	1.9356
30	cat__Smoking_Status_Non-smoker	1.4744	4.3683	1.4744
28	cat__Smoking_Status_Current smoker	-1.4028	0.2459	1.4028
2	num__Cholesterol	-1.2862	0.2763	1.2862
18	num__Systolic_BP	-1.2663	0.2819	1.2663
6	num__PRS_Type2Diabetes	-0.5513	0.5762	0.5513
45	cat__Sleep_Quality_Excellent	0.5424	1.7202	0.5424
22	num__Triglycerides	0.4748	1.6078	0.4748
3	num__Glucose_Level	-0.4508	0.6371	0.4508
1	num__BMI	-0.3940	0.6743	0.3940
37	cat__Physical_Activity_Level_Moderately Active	0.3691	1.4464	0.3691

======================================================================
Top predictors — Moderate
======================================================================
Feature	Coefficient	Odds_Ratio	Abs_Coefficient
20	num__LDL	-0.4335	0.6482	0.4335
21	num__HDL	0.3200	1.3771	0.3200
5	num__PRS_Cardiometabolic	-0.3083	0.7347	0.3083
0	num__Age	-0.2427	0.7845	0.2427
2	num__Cholesterol	-0.2230	0.8002	0.2230
9	num__Family_History_CVD	-0.2130	0.8081	0.2130
45	cat__Sleep_Quality_Excellent	-0.1998	0.8189	0.1998
1	num__BMI	0.1901	1.2094	0.1901
4	num__HbA1c	0.1403	1.1506	0.1403
35	cat__Physical_Activity_Level_Highly Active	0.1393	1.1495	0.1393
30	cat__Smoking_Status_Non-smoker	0.1297	1.1385	0.1297
31	cat__Alcohol_Consumption_High	0.1161	1.1231	0.1161
32	cat__Alcohol_Consumption_Low	-0.1043	0.9010	0.1043
18	num__Systolic_BP	-0.0917	0.9124	0.0917
48	cat__Sleep_Quality_Poor	0.0902	1.0944	0.0902

SHAP version: 0.52.0
Background dataset has 400 samples but max_samples=100. Subsampling to 100 samples for SHAP value computation. To use all samples, set max_samples=400 when initializing the masker.
SHAP calculated successfully.

Step 32 theke shuru koro... by analyzing all these perfectly

Pasted markdown(20260909-132543).md
File
next
Pasted markdown(20260909-133425).md
File
Next
Pasted markdown(20260909-140420).md
File
ScenarioPredictionHigh_ProbabilityHigh_Probability_ChangeHigh_Decision_ScoreHigh_Decision_ChangeLow_ProbabilityLow_Probability_ChangeLow_Decision_ScoreLow_Decision_ChangeModerate_ProbabilityModerate_Probability_ChangeModerate_Decision_ScoreModerate_Decision_Change														
0	Baseline	High	1.000000	0.000000	17.823816	0.000000	0.0	0.0	-18.007227	0.000000	0.000000	0.000000	0.183411	0.000000
1	LDL improvement	High	0.999998	-0.000002	14.012729	-3.811087	0.0	0.0	-14.743530	3.263697	0.000002	0.000002	0.730801	0.547390
2	LDL + TG improvement	High	0.999999	-0.000001	14.793826	-3.029991	0.0	0.0	-15.404088	2.603140	0.000001	0.000001	0.610262	0.426851
3	Lipid + BMI improvement	High	0.999999	-0.000001	14.553889	-3.269927	0.0	0.0	-14.940366	3.066862	0.000001	0.000001	0.386476	0.203065
4	Comprehensive lifestyle scenario	High	0.999989	-0.000011	12.135225	-5.688591	0.0	0.0	-12.814091	5.193136	0.000011	0.000011	0.678866	0.495455<br><br><br>
solve this 
Pasted markdown(20260909-143621).md
File
analysis the whole data... what next
Pasted markdown(20260909-144532).md
File
next
Pasted markdown(20260909-145350).md
File
Okk.. next
Pasted markdown(20260909-145717).md
File
Okk.. next...
Yesterday 10:07 PM
Pasted markdown(20260909-160736).md
File
Next...
Pasted markdown(20260909-170315).md
File
Next....
Today 12:56 AM
Pasted markdown(20260909-185643).md
File
Next
Pasted markdown(20260909-190015).md
File
okk now final phase
Calibrated final model trained successfully.


# ============================================================

# STEP 119B: Calibrated Predictions on Untouched Test Set

# ============================================================

calibrated_test_pred = calibrated_model.predict(

X\_test\_final

)

calibrated_test_prob = calibrated_model.predict_proba(

X\_test\_final

)

print("Calibrated predictions generated.")

print("Probability matrix shape:", calibrated_test_prob.shape)

Calibrated predictions generated.
Probability matrix shape: (400, 3)


svg

# ============================================================

# STEP 119C: Calibrated Model Performance

# ============================================================

cal_accuracy = accuracy_score(

y\_test,

calibrated\_test\_pred

)

cal_balanced = balanced_accuracy_score(

y\_test,

calibrated\_test\_pred

)

cal_macro_f1 = f1_score(

y\_test,

calibrated\_test\_pred,

average**=**'macro'

)

cal_weighted_f1 = f1_score(

y\_test,

calibrated\_test\_pred,

average**=**'weighted'

)

cal_auc = roc_auc_score(

y\_test,

calibrated\_test\_prob,

multi\_class**=**'ovr',

average**=**'macro'

)

cal_logloss = log_loss(

y\_test,

calibrated\_test\_prob

)

print("=" * 65)

print("CALIBRATED FINAL MODEL — TEST SET")

print("=" * 65)

print(f"Accuracy : {cal_accuracy:.4f}")

print(f"Balanced Accuracy : {cal_balanced:.4f}")

print(f"Macro-F1 : {cal_macro_f1:.4f}")

print(f"Weighted-F1 : {cal_weighted_f1:.4f}")

print(f"Macro ROC-AUC : {cal_auc:.4f}")

print(f"Log Loss : {cal_logloss:.4f}")

print("\nClassification Report:\n")

print(

classification\_report(

    y\_test,

    calibrated\_test\_pred,

    digits**=**4

)

)

=================================================================
CALIBRATED FINAL MODEL — TEST SET
=================================================================
Accuracy          : 0.9050
Balanced Accuracy : 0.8888
Macro-F1          : 0.8934
Weighted-F1       : 0.8998
Macro ROC-AUC     : 0.9815
Log Loss          : 0.4366

Classification Report:

              precision    recall  f1-score   support

        High     0.8905    0.9760    0.9313       125
         Low     0.8804    1.0000    0.9364       162
    Moderate     0.9873    0.6903    0.8125       113

    accuracy                         0.9050       400
   macro avg     0.9194    0.8888    0.8934       400
weighted avg     0.9138    0.9050    0.8998       400



svg

# ============================================================

# STEP 119D: Class-wise Brier Scores

# ============================================================

classes = calibrated_model.classes_

brier_results = []

for i, class_name in enumerate(classes):

y\_binary **=** (

    y\_test **==** class\_name

).astype(int)

brier **=** brier\_score\_loss(

    y\_binary,

    calibrated\_test\_prob[:, i]

)

brier\_results.append({

'Class': class_name,

'Brier_Score': brier

})

brier_df = pd.DataFrame(

brier\_results

)

display(

brier\_df.round(4)

)

ClassBrier_Score		
0	High	0.0489
1	Low	0.0634
2	Moderate	0.1120

svg

next

Confusion Matrix:
[[122   2   1]
 [  0 162   0]
 [ 15  20  78]]



<Figure size 700x600 with 0 Axes>


image

*# ============================================================*

*# STEP 121B: Normalized Confusion Matrix*

*# ============================================================*

cm\_normalized **=** confusion\_matrix(

    y\_test,

    calibrated\_test\_pred,

    labels**=**classes,

    normalize**=**'true'

)

plt.figure(figsize**=**(7, 6))

disp **=** ConfusionMatrixDisplay(

    confusion\_matrix**=**cm\_normalized,

    display\_labels**=**classes

)

disp.plot(

    values\_format**=**'.2f'

)

plt.title(

'Normalized Confusion Matrix — Calibrated Final Model'

)

plt.tight\_layout()

plt.show()


<Figure size 700x600 with 0 Axes>


image

*# ============================================================*

*# STEP 122: Multiclass ROC Curves*

*# ============================================================*

**from** sklearn.preprocessing **import** label\_binarize

**from** sklearn.metrics **import** roc\_curve, auc

*# ------------------------------------------------------------*

*# Binarize the outcome*

*# ------------------------------------------------------------*

y\_test\_binary **=** label\_binarize(

    y\_test,

    classes**=**classes

)

plt.figure(figsize**=**(8, 7))

**for** i, class\_name **in** enumerate(classes):

    fpr, tpr, \_ **=** roc\_curve(

        y\_test\_binary[:, i],

        calibrated\_test\_prob[:, i]

)

    roc\_auc\_class **=** auc(

        fpr,

        tpr

)

    plt.plot(

        fpr,

        tpr,

        marker**=None**,

        label**=**f'{class\_name} (AUC = {roc\_auc\_class:**.3f**})'

)

*# ------------------------------------------------------------*

*# Random classifier reference*

*# ------------------------------------------------------------*

plt.plot(

[0, 1],

[0, 1],

    linestyle**=**'--',

    label**=**'Random classifier'

)

plt.xlabel('False Positive Rate')

plt.ylabel('True Positive Rate')

plt.title(

'One-vs-Rest ROC Curves — Calibrated Final Model'

)

plt.legend()

plt.tight\_layout()

plt.show()

image

*# ============================================================*

*# STEP 123: Precision-Recall Curves*

*# ============================================================*

**from** sklearn.metrics **import** precision\_recall\_curve, average\_precision\_score

plt.figure(figsize**=**(8, 7))

**for** i, class\_name **in** enumerate(classes):

    precision, recall, \_ **=** precision\_recall\_curve(

        y\_test\_binary[:, i],

        calibrated\_test\_prob[:, i]

)

    ap **=** average\_precision\_score(

        y\_test\_binary[:, i],

        calibrated\_test\_prob[:, i]

)

    plt.plot(

        recall,

        precision,

        label**=**f'{class\_name} (AP = {ap:**.3f**})'

)

plt.xlabel('Recall')

plt.ylabel('Precision')

plt.title(

'One-vs-Rest Precision–Recall Curves — Calibrated Final Model'

)

plt.legend()

plt.tight\_layout()

plt.show()

image

*# ============================================================*

*# STEP 124: Class-specific ROC-AUC and Average Precision*

*# ============================================================*

roc\_results **=** []

**for** i, class\_name **in** enumerate(classes):

*# ROC-AUC*

    class\_auc **=** roc\_auc\_score(

        y\_test\_binary[:, i],

        calibrated\_test\_prob[:, i]

)

*# Average Precision*

    class\_ap **=** average\_precision\_score(

        y\_test\_binary[:, i],

        calibrated\_test\_prob[:, i]

)

    roc\_results.append({

'Class': class\_name,

'ROC\_AUC': class\_auc,

'Average\_Precision': class\_ap

})

roc\_pr\_df **=** pd.DataFrame(

    roc\_results

)

display(

    roc\_pr\_df.round(4)

)

| **ClassROC\_AUCAverage\_Precision** |          |        |        |
| ----------------------------------- | -------- | ------ | ------ |
| **0**                               | High     | 0.9872 | 0.9841 |
| **1**                               | Low      | 0.9883 | 0.9810 |
| **2**                               | Moderate | 0.9690 | 0.9202 |

svg

*# ============================================================*

*# STEP 125: Misclassification Analysis*

*# ============================================================*

error\_df **=** X\_test\_final.copy()

error\_df['Actual\_Risk'] **=** y\_test.values

error\_df['Predicted\_Risk'] **=** calibrated\_test\_pred

error\_df['Prediction\_Correct'] **=** (

    error\_df['Actual\_Risk']

**==**

    error\_df['Predicted\_Risk']

)

*# ------------------------------------------------------------*

*# Only incorrect predictions*

*# ------------------------------------------------------------*

errors\_only **=** error\_df[

**\~**error\_df['Prediction\_Correct']

].copy()

print(

"Total test observations:",

len(error\_df)

)

print(

"Incorrect predictions:",

len(errors\_only)

)

print(

"Error rate:",

round(

len(errors\_only) **/** len(error\_df) **\*** 100,

2

),

"%"

)

display(

    errors\_only[

[

'Actual\_Risk',

'Predicted\_Risk'

]

].head(20)

)


Total test observations: 400
Incorrect predictions: 38
Error rate: 9.5 %


| **Actual\_RiskPredicted\_Risk** |          |          |
| ------------------------------- | -------- | -------- |
| **1799**                        | Moderate | Low      |
| **1155**                        | Moderate | High     |
| **1986**                        | Moderate | High     |
| **1270**                        | Moderate | High     |
| **1807**                        | Moderate | Low      |
| **1371**                        | Moderate | High     |
| **1045**                        | Moderate | Low      |
| **371**                         | High     | Moderate |
| **973**                         | Moderate | Low      |
| **1099**                        | Moderate | Low      |
| **1632**                        | Moderate | Low      |
| **1669**                        | Moderate | Low      |
| **914**                         | Moderate | High     |
| **1156**                        | Moderate | Low      |
| **64**                          | High     | Low      |
| **1739**                        | Moderate | High     |
| **299**                         | Moderate | Low      |
| **954**                         | Moderate | Low      |
| **1602**                        | Moderate | Low      |
| **1267**                        | Moderate | High     |

svg

*# ============================================================*

*# STEP 125B: Misclassification Pattern*

*# ============================================================*

error\_pattern **=** pd.crosstab(

    error\_df['Actual\_Risk'],

    error\_df['Predicted\_Risk']

)

print("Actual vs Predicted:")

display(error\_pattern)


Actual vs Predicted:


| **Predicted\_RiskHighLowModerate** |     |     |    |
| ---------------------------------- | --- | --- | -- |
| **Actual\_Risk**                   |     |     |    |
| **High**                           | 122 | 2   | 1  |
| **Low**                            | 0   | 162 | 0  |
| **Moderate**                       | 15  | 20  | 78 |

svg

Pasted markdown(20260909-192150).md
File
okk final next
FeaturePatient_ValueModel_ContributionClinical_SignalActionablePriority_ScoreRecommendation_PriorityRecommendation								
0	LDL	170.4	5.2144	HIGH	True	15.6431	HIGH	Consider clinical assessment of LDL cholestero...
1	Smoking_Status	Current smoker	1.4577	HIGH	True	4.3732	HIGH	Smoking cessation support should be prioritize...
2	Cholesterol	229.7	1.3904	MODERATE	True	2.7807	MODERATE	Consider reviewing the complete lipid profile ...
3	Alcohol_Consumption	Moderate	-0.2138	MODERATE	True	0.4276	MODERATE	Review alcohol intake and consider reducing co...
4	Sleep_Quality	Fair	0.1019	MODERATE	True	0.2038	MODERATE	Review sleep quality and identify modifiable f...
5	Age	60	2.5980	UNKNOWN	False	NaN	CONTEXT	Age is non-modifiable and should be used for r...
6	HDL	38.5	2.5674	UNKNOWN	False	NaN	CONTEXT	HDL should be interpreted as part of the compl...
7	Family_History_CVD	1	2.3795	UNKNOWN	False	NaN	CONTEXT	Family history is non-modifiable but should be...
8	PRS_Cardiometabolic	0.8	2.1762	UNKNOWN	False	NaN	CONTEXT	Genetic risk is non-modifiable and should be i...
9	Family_History_T2D	0	-0.1663	UNKNOWN	False	NaN	CONTEXT	Family history is non-modifiable but can infor...

svg

# ============================================================

# STEP 129F: Patient Recommendation Report

# ============================================================

print("=" * 75)

print("PERSONALISED HEALTHCARE RECOMMENDATION REPORT")

print("=" * 75)

print(

f"\nPredicted Risk: {patient_prediction}"

)

print("\nRisk Probabilities:")

for _, row in patient_probability_df.iterrows():

print(

f" {row['Risk_Class']}: "

f"{row['Probability'] * 100:.1f}%"

)

print("\nTop Model Contributors:")

for rank, (_, row) in enumerate(

patient\_explanation\_df.head(5).iterrows(),

start**=**1

):

print(

f" {rank}. {row['Feature']} "

f"({row['Signed_Contribution']:.3f})"

)

print("\n" + "-" * 75)

print("PRIORITIZED ACTIONABLE AREAS")

print("-" * 75)

for rank, (_, row) in enumerate(

recommendations\_patient84.iterrows(),

start**=**1

):

print(

f"\n{rank}. {row['Feature']}"

)

print(

f" Patient value: "

f"{row['Patient_Value']}"

)

print(

f" Clinical signal: "

f"{row['Clinical_Signal']}"

)

print(

f" Priority: "

f"{row['Recommendation_Priority']}"

)

print(

f" Recommendation: "

f"{row['Recommendation']}"

)

print("\n" + "=" * 75)

print(

"Research prototype — not a diagnostic or treatment system."

)

print("=" * 75)

===========================================================================
PERSONALISED HEALTHCARE RECOMMENDATION REPORT
===========================================================================

Predicted Risk: High

Risk Probabilities:
  High: 79.5%
  Low: 0.0%
  Moderate: 20.5%

Top Model Contributors:
  1. LDL (5.214)
  2. Age (2.598)
  3. HDL (2.567)
  4. Family_History_CVD (2.379)
  5. PRS_Cardiometabolic (2.176)

---------------------------------------------------------------------------
PRIORITIZED ACTIONABLE AREAS
---------------------------------------------------------------------------

1. LDL
   Patient value: 170.4
   Clinical signal: HIGH
   Priority: HIGH
   Recommendation: Consider clinical assessment of LDL cholesterol and review of overall cardiovascular risk. Dietary pattern and other lipid-management strategies should be discussed with an appropriate healthcare professional.

2. Smoking_Status
   Patient value: Current smoker
   Clinical signal: HIGH
   Priority: HIGH
   Recommendation: Smoking cessation support should be prioritized. Consider behavioural support and evidence-based cessation options with a healthcare professional.

3. Cholesterol
   Patient value: 229.7
   Clinical signal: MODERATE
   Priority: MODERATE
   Recommendation: Consider reviewing the complete lipid profile and overall cardiovascular risk with a healthcare professional.

4. Alcohol_Consumption
   Patient value: Moderate
   Clinical signal: MODERATE
   Priority: MODERATE
   Recommendation: Review alcohol intake and consider reducing consumption if intake is excessive.

5. Sleep_Quality
   Patient value: Fair
   Clinical signal: MODERATE
   Priority: MODERATE
   Recommendation: Review sleep quality and identify modifiable factors that may be interfering with restorative sleep.

6. Age
   Patient value: 60
   Clinical signal: UNKNOWN
   Priority: CONTEXT
   Recommendation: Age is non-modifiable and should be used for risk context only.

7. HDL
   Patient value: 38.5
   Clinical signal: UNKNOWN
   Priority: CONTEXT
   Recommendation: HDL should be interpreted as part of the complete lipid profile rather than treated as an isolated target.

8. Family_History_CVD
   Patient value: 1
   Clinical signal: UNKNOWN
   Priority: CONTEXT
   Recommendation: Family history is non-modifiable but should be considered when interpreting overall cardiovascular risk.

9. PRS_Cardiometabolic
   Patient value: 0.8
   Clinical signal: UNKNOWN
   Priority: CONTEXT
   Recommendation: Genetic risk is non-modifiable and should be interpreted as part of the overall risk profile rather than as a treatment target.

10. Family_History_T2D
   Patient value: 0
   Clinical signal: UNKNOWN
   Priority: CONTEXT
   Recommendation: Family history is non-modifiable but can inform metabolic risk assessment.

===========================================================================
Research prototype — not a diagnostic or treatment system.
===========================================================================


Pasted markdown(20260909-193246).md
File
Ok... final kopro
Pasted markdown(20260909-194949).md
File
Next final ...
This type or more interactive.. dynamic so attractive

Exactly. আপনার দেখানো design-এর মতো card-based, modern, dynamic dashboard করা উচিত—basic 27-field form না।

আমি আপনার জন্য আরও advanced version তৈরি করেছি:

Download Advanced Interactive app.py

নতুন UI-তে থাকবে
Dashboard / Patient Input / Risk Results / Reference Guide navigation
Bangla + English terminology
প্রতিটি variable-এর:
Meaning / অর্থ
Unit
Reference range
Contextual explanation
Profile / Clinical / Lifestyle / Genetics আলাদা interactive tabs
Automatic BMI interpretation
Automatic BP interpretation
Automatic LDL interpretation
Automatic Triglyceride interpretation
Large High / Moderate / Low risk cards
Interactive probability chart
Clinical snapshot
Full parameter/reference table
Genetic/PRS-এর জন্য আলাদা explanation
Mobile/desktop-friendly layout
Research-only safety messaging

আপনার dataset-এর final predictors-এ 6 categorical এবং 26 numerical variables ছিল, তাই interface-এ categorical inputs-গুলো dropdown এবং numerical inputs-গুলো numeric control হিসেবে রাখা হয়েছে।

এখন শুধু এটা করুন

পুরনো GitHub-এর:

app.py

delete/replace করে এই downloaded file-টির নাম app.py দিন।

তারপর GitHub → Commit changes।

Streamlit Cloud automatic redeploy করলে আপনার public link-এই নতুন UI দেখা যাবে:

Your live app

তারপর screenshot দিন। আমরা live UI দেখে final polish করব—বিশেষ করে risk visualization, contributor cards, recommendations এবং What-if simulator যোগ করলে এটা আরও professional হবে। 

app_advanced_interactive.py
Code
Color font and all are perfect and best most fancy looking

হ্যাঁ। আপনার screenshot-এর মতো premium SaaS/medical-AI dashboard aesthetic ধরে UI-টা আরও polished করেছি।

Download the Premium UI app.py

এতে আমি বিশেষভাবে উন্নত করেছি:

Premium Inter + Noto Sans Bengali typography
Clean medical-AI color system
Soft blue/violet gradient hero
Rounded modern cards
Better shadows, borders ও spacing
Premium risk-result cards
Modern tabs
Improved sidebar
Better buttons and metric cards
Responsive mobile layout
Bangla + English readability
পুরো interface-এ consistent visual hierarchy

আপনার model/input logic পরিবর্তন করিনি—শুধু UI/UX upgrade করেছি।

GitHub-এ এটাকে পুরনো app.py দিয়ে replace → Commit করুন। তারপর live link refresh করুন।

Open your live application 

app_premium_ui.py
Code
Color font and all are perfect and best most fancy looking

হ্যাঁ। Screenshot-এ মূল সমস্যা হলো Streamlit dark theme-এর কারণে hero title এবং cards-এর contrast নষ্ট হয়েছে। আমি সেটা ঠিক করে একটি premium light medical-AI UI বানিয়েছি।

Download Final Fancy UI app.py

এই version-এ visual style
Premium white + navy + blue/violet palette
High-contrast professional typography
Inter + Noto Sans Bengali
Glass/soft-gradient hero
Modern rounded cards
Clean shadows
Professional medical dashboard appearance
Better tab styling
Better input controls
Premium risk cards
Clean sidebar
Responsive mobile layout
Dark-mode conflict fix

আপনার screenshot-এর মতো grey/washed-out card আর white-on-white title থাকবে না।

এখন GitHub-এ শুধু:

পুরনো app.py → Delete/Replace → এই file-টি app.py নামে upload → Commit changes

তারপর Streamlit redeploy হবে।

Open live application

এরপর চাইলে আমরা এটাকে আরও এক ধাপ এগিয়ে Apple/Linear/Notion-level polished dashboard করতে পারি—animated risk gauge, contributor visualization, recommendation cards এবং interactive What-if simulator সহ। 

app_final_fancy_ui.py
Code

Library
/
app_final_fancy_ui.py
999
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
import streamlit as st
                "Reference / সাধারণ রেঞ্জ": ref
            })
        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)


        st.warning(
            "Research prototype only / শুধুমাত্র গবেষণার প্রোটোটাইপ। "
            "Model probabilities are statistical outputs and are not causal treatment effects."
        )


elif page == "Reference Guide":
    st.subheader("Reference Guide / রেফারেন্স গাইড")
    st.caption("General educational reference information. Individual clinical targets may differ.")


    ref_rows = []
    for f in features:
        bn, meaning, unit, ref = meta_text(f)
        ref_rows.append({
            "Term": f,
            "বাংলা": bn,
            "Meaning / অর্থ": meaning,
            "Unit": unit,
            "Reference": ref
        })


    st.dataframe(
        pd.DataFrame(ref_rows),
        use_container_width=True,
        hide_index=True,
        height=650
    )


    st.info(
        "Reference ranges are educational and context-dependent. "
        "Genetic/PRS variables do not have universal clinical reference intervals."
    )


# ============================================================
# FOOTER
# ============================================================
st.divider()
st.markdown(
    '<div class="footer-note">Personalised Healthcare Risk Assessment • '
    'Bilingual AI Research Prototype • Not a diagnostic or treatment system</div>',
    unsafe_allow_html=True
)

