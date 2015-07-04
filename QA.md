# Questions & Answers

---
### 1. Decision Process
Considering I have a very Active Community site then I would check whether the Three Vs of Big Data are being fulfilled or not.
 1. **Volume** - If my site data is not fitting on a single machine and is over few TBs then using _Hadoop_ and _MapReduce_ would be optimal decision for processing this type of data, else it would be wise to use to find a solution without _Hadoop_.
 2. **Variety** - Since my community site would have various type of data documents, images, videos, programming files, etc. _Hadoop_ can very efficiently handle this different types of data.
 3. **Velocity** - The rate at which new data is generated is an important factor while taking decision whether to use _Hadoop_ or not. _Hadoop_ alone cannot perform Real Time Analysis instead it is used along with Spark framework. So, if my site has a high traffic throughout then I would definitely use _Hadoop_ to gather statistics about users.  
Moreover, while going for such technology _Hadoop_ & _MapReduce_, one should keep in mind all _MapReduce_ Design Patterns since it'll give you a quick Insight whether your problem can/cannot be solved using this technique and will work as boilerplate solution.

---
### 2. Search Functionality
For improving the Indexes, there are atleast four ways -
 1. Remove all the most common words that occur in each post, like - a, I, you, etc
 2. Make Index of only valid alphanumeric words and not of large numbers
 3. Don't include HTML Tags in the indexes.
 4. Another solution could be use a dictionary that contains all words to be indexed, but this method can be slow.

I have implemented the code using above rules, you can find it below -
- **Lesson 4 - Design Patterns - Problem 3 Solution Optimized**
 - [p3V2mapper.py](http://github.com/np1810/Hadoop_and_MapReduce/blob/master/L4_DesignPatterns/p3V2mapper.py)
 - [p3V2reducer.py](http://github.com/np1810/Hadoop_and_MapReduce/blob/master/L4_DesignPatterns/p3V2reducer.py)

---
### 3. Other Questions
The dataset can be used to find out answers to many questions.  
For Example - I have used the dataset to find out the Quickest Replies Post i.e. it gives a post ID alongwith average difference between successive q&a/comments in seconds.
- **Lesson 5 - Other Questions - Quick Replies**
 - [quick_replies_mapper.py](http://github.com/np1810/Hadoop_and_MapReduce/blob/master/L5_FinalProject/quick_replies/quick_replies_mapper.py)
 - [quick_replies_reducer.py](http://github.com/np1810/Hadoop_and_MapReduce/blob/master/L5_FinalProject/quick_replies/quick_replies_reducer.py)
 
##### Quick Replies Output Graph
![](https://raw.githubusercontent.com/np1810/Hadoop_and_MapReduce/master/L5_FinalProject/quick_replies/quick_replies_output.png)

---
Copyright (c) 2015 [Nitin Pathak](http://nitinpathak.esy.es)
