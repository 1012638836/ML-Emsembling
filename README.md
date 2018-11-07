# ML-Emsembling
* 相关链接

1.集成算法总结：https://www.cnblogs.com/sddai/p/7647731.html   这个链接主要讲集成算法的两个大类：Boosting和Bagging的基本原理。<br>
2.有放回抽样详解：https://blog.csdn.net/chenyukuai6625/article/details/73692347   这个链接讲了bagging的有放回采样的原理，并且有一个小例子，通过这个例子我明白了随机森林中“随机”二字的含义。<br>
3.决策树原理讲解：https://blog.csdn.net/akadiao/article/details/77800909   这个链接讲解了如何利用csv的工具包对数据进行离散化赋值的用法(注意：这里没有使用pandas工具包)<br>
4.决策树DecisionTreeClassifier的具体参数讲解：https://blog.csdn.net/y0929/article/details/82686177   这个链接讲解了决策树的默认参数。实验证明：当决策树不设置最深层数时，predict_proba()的结果一般是[ 0,1 ]或者[ 1 , 0 ](二分类)。放决策树设置最深层数时，predict_proba()的结果是[ 0.38,0.62 ](打个比方和)，这是我做实验时的观察。<br>
5.关于sklearn的predict和predict_proba的区别：https://blog.csdn.net/m0_37870649/article/details/79549142   <br>

* 关于程序

main.ipynb介绍了集成算法如何将若干个基本分类器进行集合的，将每种分类器的结果进行平均，之后我们发现AUC的值得到了提高，说明集成算法能提高分类器的分类性能。




   
