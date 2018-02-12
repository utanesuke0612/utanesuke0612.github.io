---
layout: post
title: Uda-DataAnalysis-43-机器学习-主成分分析（PCA）
date: 2018-01-16 13:00:01
categories: 数据分析
tags: R Udacity DataAnalysis 
---
* content
{:toc}


# 1. 练习1-5: 关于数据维度

- 下面的图三和图四，将坐标轴进行平移和旋转后，能将数据维度变为1(即数据只在x方向或是只在y方向发生变化)

![image](https://user-images.githubusercontent.com/18595935/36058993-a7d071f2-0e71-11e8-86b5-6e8a0287bf44.png)

- 但是下面的数据，无论坐标轴怎么移位和旋转，其数据在x和y轴都会发生变化，所以数据是`二维`

![image](https://user-images.githubusercontent.com/18595935/36059010-069ff46e-0e72-11e8-9fa9-cb4626305f7e.png)

# 6. 用于数据转换的PCA

PCA就是要为这些数据找到新的坐标轴，并确定这些坐标轴的重要性。

![image](https://user-images.githubusercontent.com/18595935/36059034-a6d4239c-0e72-11e8-9a16-7229200d2fba.png)

# 8. 练习8-11: 查找新轴

![image](https://user-images.githubusercontent.com/18595935/36059431-3b131924-0e7c-11e8-83c7-3348a1c144bd.png)

图1和图2中的△x与△y分别表示，新x轴与新y轴，在原始X轴与Y轴方向上的位移，比如图2中y'上的△x和△y，y'在原始X轴上前移1个单位，则在Y轴方向上上移2个单位。

# 16. 在保留信息的时候进行压缩

![image](https://user-images.githubusercontent.com/18595935/36060641-e054ffb0-0e90-11e8-856d-92137aeb9d4b.png)

- 下面的示例，将两个原始特征，处理成新的特征size

![image](https://user-images.githubusercontent.com/18595935/36060677-592536da-0e91-11e8-846d-64ca5fead097.png)

# 19. 最大方差

将数据映射到粗红色的线条上，能最大程度上保留信息

![image](https://user-images.githubusercontent.com/18595935/36060702-0a35532e-0e92-11e8-821a-3cc03b550c2b.png)

# 20. 最大方差与信息损失

下面是另一个示例，也是将两个特征用PCA的方式，压缩成一个特征：

![image](https://user-images.githubusercontent.com/18595935/36060728-a098cf62-0e92-11e8-98ef-27c7abe853e4.png)

# 23. 用于特征转换的PCA

下面是一个预测流程，先用PCA将四个特征转换为2个，再用回归出模型，通过模型进行预测。

![image](https://user-images.githubusercontent.com/18595935/36060834-5e2d5ede-0e94-11e8-8d1d-1a4bfa406b5b.png)

# 28. sklearn 中的 PCA

参考 [sklearn.decomposition.PCA](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)

```python
>>> import numpy as np
>>> from sklearn.decomposition import PCA
>>> X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
>>> pca = PCA(n_components=2)
>>> pca.fit(X)
PCA(copy=True, iterated_power='auto', n_components=2, random_state=None,
  svd_solver='auto', tol=0.0, whiten=False)
>>> print　pca.explained_variance_ratio_  
[ 0.99244...  0.00755...]

>>> print pca.components_[0]
[-0.83849224 -0.54491354]
>>> print pca.components_[1]
[ 0.54491354 -0.83849224]

```

- `explained_variance_ratio_`：方差，Percentage of variance explained by each of the selected components.

- 视频中的示例代码：

![image](https://user-images.githubusercontent.com/18595935/36062082-7049983a-0ea8-11e8-9ed3-54a4b1761cf4.png)

最后绘制的图形如下：

![image](https://user-images.githubusercontent.com/18595935/36062119-28389de2-0ea9-11e8-9287-4f6c61f476f9.png)



# 29. 何时使用PCA

1. latent features driving the patterns in data(big shots@Enron), 驱动数据模式中的隐藏特征
2. dimensionality reduction , visualize high-dimensional data ,reduce noise，make other algorithms(regression,classification)

# 30. 用于人脸识别的PCA

What makes facial recognition in pictures good for PCA?

[⭕]1. pictures of faces generally have high input dimensionality - many pixels

[⭕]2. faces have general patterns that could be captured in smaller number of dimensions -  two eyes on top,mouth/chin on buttom

[☓]3. facial recognition is simple using machine learning - humans do it easily


# 31. 特征脸方法代码

参考[sklearn.decomposition.RandomizedPCA](http://ogrisel.github.io/scikit-learn.org/sklearn-tutorial/modules/generated/sklearn.decomposition.RandomizedPCA.html)

## 31.1 原始的示例代码

根据示例代码[Faces recognition example using eigenfaces and SVMs](http://scikit-learn.org/0.16/auto_examples/applications/face_recognition.html)改编而来：

```python
"""
===================================================
Faces recognition example using eigenfaces and SVMs
===================================================

The dataset used in this example is a preprocessed excerpt of the
"Labeled Faces in the Wild", aka LFW_:

  http://vis-www.cs.umass.edu/lfw/lfw-funneled.tgz (233MB)

  .. _LFW: http://vis-www.cs.umass.edu/lfw/

  original source: http://scikit-learn.org/stable/auto_examples/applications/face_recognition.html

"""

print __doc__

from time import time
import logging
import pylab as pl
import numpy as np

from sklearn.cross_validation import train_test_split
from sklearn.datasets import fetch_lfw_people
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import RandomizedPCA
from sklearn.svm import SVC

# Display progress logs on stdout
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

# 1. 下载需要的数据
###############################################################################
# Download the data, if not already on disk and load it as numpy arrays
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

# introspect the images arrays to find the shapes (for plotting)
n_samples, h, w = lfw_people.images.shape
np.random.seed(42)

# for machine learning we use the data directly (as relative pixel
# position info is ignored by this model)
X = lfw_people.data
n_features = X.shape[1]

# the label to predict is the id of the person
y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]

print "Total dataset size:"
print "n_samples: %d" % n_samples
print "n_features: %d" % n_features
print "n_classes: %d" % n_classes

# 2. 将数据区分为训练集和测试集
###############################################################################
# Split into a training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)


# 3. 应用PCA
###############################################################################
# Compute a PCA (eigenfaces) on the face dataset (treated as unlabeled
# dataset): unsupervised feature extraction / dimensionality reduction
n_components = 150

print "Extracting the top %d eigenfaces from %d faces" % (n_components, X_train.shape[0])
t0 = time()
pca = RandomizedPCA(n_components=n_components, whiten=True).fit(X_train)
print "done in %0.3fs" % (time() - t0)

eigenfaces = pca.components_.reshape((n_components, h, w))

print "Projecting the input data on the eigenfaces orthonormal basis"
t0 = time()
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
print "done in %0.3fs" % (time() - t0)

# 4. 训练一个SVM分类模型
###############################################################################
# Train a SVM classification model

print "Fitting the classifier to the training set"
t0 = time()
param_grid = {
         'C': [1e3, 5e3, 1e4, 5e4, 1e5],
          'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1],
          }
# for sklearn version 0.16 or prior, the class_weight parameter value is 'auto'
clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), param_grid)
clf = clf.fit(X_train_pca, y_train)
print "done in %0.3fs" % (time() - t0)
print "Best estimator found by grid search:"
print clf.best_estimator_


###############################################################################
# Quantitative evaluation of the model quality on the test set

print "Predicting the people names on the testing set"
t0 = time()
y_pred = clf.predict(X_test_pca)
print "done in %0.3fs" % (time() - t0)

print classification_report(y_test, y_pred, target_names=target_names)
print confusion_matrix(y_test, y_pred, labels=range(n_classes))


###############################################################################
# Qualitative evaluation of the predictions using matplotlib

def plot_gallery(images, titles, h, w, n_row=3, n_col=4):
    """Helper function to plot a gallery of portraits"""
    pl.figure(figsize=(1.8 * n_col, 2.4 * n_row))
    pl.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.35)
    for i in range(n_row * n_col):
        pl.subplot(n_row, n_col, i + 1)
        pl.imshow(images[i].reshape((h, w)), cmap=pl.cm.gray)
        pl.title(titles[i], size=12)
        pl.xticks(())
        pl.yticks(())


# plot the result of the prediction on a portion of the test set

def title(y_pred, y_test, target_names, i):
    pred_name = target_names[y_pred[i]].rsplit(' ', 1)[-1]
    true_name = target_names[y_test[i]].rsplit(' ', 1)[-1]
    return 'predicted: %s\ntrue:      %s' % (pred_name, true_name)

prediction_titles = [title(y_pred, y_test, target_names, i)
                         for i in range(y_pred.shape[0])]

plot_gallery(X_test, prediction_titles, h, w)

# plot the gallery of the most significative eigenfaces

eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenface_titles, h, w)

pl.show()

```

## 31.2 上述代码执行后结果如下：

```
===================================================
Faces recognition example using eigenfaces and SVMs
===================================================

The dataset used in this example is a preprocessed excerpt of the
"Labeled Faces in the Wild", aka LFW_:

  http://vis-www.cs.umass.edu/lfw/lfw-funneled.tgz (233MB)

  .. _LFW: http://vis-www.cs.umass.edu/lfw/

  original source: http://scikit-learn.org/stable/auto_examples/applications/face_recognition.html

2018-02-11 10:54:12,556 Downloading LFW metadata: http://vis-www.cs.umass.edu/lfw/pairsDevTrain.txt
2018-02-11 10:54:14,078 Downloading LFW metadata: http://vis-www.cs.umass.edu/lfw/pairsDevTest.txt
2018-02-11 10:54:15,191 Downloading LFW metadata: http://vis-www.cs.umass.edu/lfw/pairs.txt
2018-02-11 10:54:17,059 Downloading LFW data (~200MB): http://vis-www.cs.umass.edu/lfw/lfw-funneled.tgz
2018-02-11 11:12:11,134 Decompressing the data archive to C:\Users\utane\scikit_learn_data\lfw_home\lfw_funneled
2018-02-11 11:12:37,053 Loading LFW people faces from C:\Users\utane\scikit_learn_data\lfw_home
2018-02-11 11:12:37,585 Loading face #00001 / 01288
2018-02-11 11:12:39,467 Loading face #01001 / 01288
Total dataset size:
n_samples: 1288
n_features: 1850
n_classes: 7
Extracting the top 150 eigenfaces from 966 faces

C:\python2.7\lib\site-packages\sklearn\utils\deprecation.py:52: DeprecationWarning: Class RandomizedPCA is deprecated; RandomizedPCA was deprecated in 0.18 and will be removed in 0.20. Use PCA(svd_solver='randomized') instead. The new implementation DOES NOT store whiten ``components_``. Apply transform to get them.
  warnings.warn(msg, category=DeprecationWarning)
done in 0.150s
Projecting the input data on the eigenfaces orthonormal basis
done in 0.023s
Fitting the classifier to the training set
done in 17.542s
Best estimator found by grid search:
SVC(C=1000.0, cache_size=200, class_weight='balanced', coef0=0.0,
  decision_function_shape=None, degree=3, gamma=0.005, kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)
Predicting the people names on the testing set
done in 0.056s
                   precision    recall  f1-score   support

     Ariel Sharon       0.62      0.38      0.48        13
     Colin Powell       0.83      0.87      0.85        60
  Donald Rumsfeld       0.94      0.63      0.76        27
    George W Bush       0.82      0.98      0.89       146
Gerhard Schroeder       0.95      0.76      0.84        25
      Hugo Chavez       1.00      0.47      0.64        15
       Tony Blair       0.94      0.81      0.87        36

      avg / total       0.85      0.84      0.84       322

[[  5   1   0   7   0   0   0]
 [  1  52   0   7   0   0   0]
 [  1   2  17   6   0   0   1]
 [  0   3   0 143   0   0   0]
 [  0   1   0   4  19   0   1]
 [  0   3   0   4   1   7   0]
 [  1   1   1   4   0   0  29]]
```

输出图形如下：

![image](https://user-images.githubusercontent.com/18595935/36071850-a12db444-0f58-11e8-8ae4-7f72a140aa40.png)

# 34. 每个主成分的可释方差

添加如下的代码：

```python
print "################## 34: ",len(pca.explained_variance_ratio_)
print "################## 34: ",pca.explained_variance_ratio_[0]
print "################## 34: ",pca.explained_variance_ratio_[1]
```

输出结果如下，即前两位的可释方差：

```
################## 34:  150
################## 34:  0.19346527332
################## 34:  0.15116845544
```

# 35. 要使用多少个主成分？

As you add more printcipal components as features for training your classifier, do you expect it to get better or worse performance?
→ could go either way

- 修改代码：

```python
# 修改为150,200,500
n_components = 500

# ....

### 添加代码
from sklearn.metrics import f1_score
f1 = f1_score(y_test, y_pred, average='macro') 
print "############# 35 - 500:",f1

```

- 输出结果，可以看到一味增加特征数量，不一定使f1分数变高：

```python
############# 35 - 150: 0.75924570596
############# 35 - 200: 0.780214834211
############# 35 - 500: 0.675017062571
```

While ideally, adding components should provide us additional signal to improve our performance, it is possible that we end up at a complexity where we overfit.