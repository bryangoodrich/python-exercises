🐍 Daily Python - Machine Learning 🐍

Pre-Trained Models (MobileNet V2)

Today I wanted to host a FastAPI endpoint to deliver a model results as an REST endpoint. So why not just use a pre-trained model? Turned out getting that to work was a long enough learning experience, that's all I got! But it was fun exploring different images.

The setup is pretty straight-forward once you understand it. We process our image to fit the required 128x128 size accordingly. We also pull in this model and the class labels (1001 line text). 

Then we predict the image that results in a 1001 length vector. We order them to get the top estimates and I print them out in order. In this case, the image resulted in these predictions.

1 - Shih-Tzu
2 - Lhasa
3 - Pekinese
4 - Blenheim spaniel
5 - Japanese spaniel

How did it do? Let me know in the comments!

#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/0051.png" />

