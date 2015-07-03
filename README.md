# HADOOP AND MAPREDUCE

---
Hi, This repo contains some of my work done regarding the BigData, Hadoop and MapReduce. It's also a part of Final Project Submission and it'll also work as a guide to other newcomers as well.

  - All MapReduce programs are written in **Python 2** and uses _Hadoop Streaming_
  - **_Outputs_** are also present in the repo
  - Small **_Input Samples_** are also included

---
## Codes
##### COMPULSORY
- [average_length_mapper.py](http://github.com/np1810/Hadoop_and_MapReduce/blob/master/L5_FinalProject/average_length/average_length_mapper.py) [Post and Answer Length Exercise]
- [average_length_reducer.py](http://github.com/np1810/Hadoop_and_MapReduce/blob/master/L5_FinalProject/average_length/average_length_reducer.py) [Post and Answer Length Exercise]
- [popular_tags_mapper.py](http://github.com/np1810/Hadoop_and_MapReduce/blob/master/L5_FinalProject/popular_tags/popular_tags_mapper.py) [Top Tags Exercise]
- [popular_tags_reducer.py](http://github.com/np1810/Hadoop_and_MapReduce/blob/master/L5_FinalProject/popular_tags/popular_tags_reducer.py) [Top Tags Exercise]
- [student_times_mapper.py](http://github.com/np1810/Hadoop_and_MapReduce/blob/master/L5_FinalProject/student_times/student_times_mapper.py) [Student Times Exercise]
- [student_times_reducer.py](http://github.com/np1810/Hadoop_and_MapReduce/blob/master/L5_FinalProject/student_times/student_times_reducer.py) [Student Times Exercise]
- [study_groups_mapper.py](http://github.com/np1810/Hadoop_and_MapReduce/blob/master/L5_FinalProject/study_groups/study_groups_mapper.py) [Study Groups Exercise]
- [study_groups_reducer.py](http://github.com/np1810/Hadoop_and_MapReduce/blob/master/L5_FinalProject/study_groups/study_groups_reducer.py) [Study Groups Exercise]

##### EXTRA CREDIT
- [quick_replies_mapper.py](http://github.com/np1810/Hadoop_and_MapReduce/blob/master/L5_FinalProject/quick_replies/quick_replies_mapper.py) [Gives Quickest Replied IDs]
- [quick_replies_reducer.py](http://github.com/np1810/Hadoop_and_MapReduce/blob/master/L5_FinalProject/quick_replies/quick_replies_reducer.py) [Gives Quickest Replied IDs]
- [popular_tags_extra_mapper.py](http://github.com/np1810/Hadoop_and_MapReduce/blob/master/L5_FinalProject/popular_tags_extra/popular_tags_extra_mapper.py) [Popular Tags Extra Weighted]
- [popular_tags_extra_reducer.py](http://github.com/np1810/Hadoop_and_MapReduce/blob/master/L5_FinalProject/popular_tags_extra/popular_tags_extra_reducer.py) [Popular Tags Extra Weighted]

---
## Final Project Report
##### COMPULSORY
- [Average Length Output][al]
![](https://raw.githubusercontent.com/np1810/Hadoop_and_MapReduce/master/L5_FinalProject/average_length/average_length_output.png)
- [Popular Tags Output][pt]
![](https://raw.githubusercontent.com/np1810/Hadoop_and_MapReduce/master/L5_FinalProject/popular_tags/popular_tags_output.png)
- [Student Times Output][st]
![](https://raw.githubusercontent.com/np1810/Hadoop_and_MapReduce/master/L5_FinalProject/student_times/student_times_output.png)
- [Study Groups Output][sg]
![](https://raw.githubusercontent.com/np1810/Hadoop_and_MapReduce/master/L5_FinalProject/study_groups/study_groups_output.png)

##### EXTRA CREDIT
- [Popular Tags Extra Output][pte]
![](https://raw.githubusercontent.com/np1810/Hadoop_and_MapReduce/master/L5_FinalProject/popular_tags_extra/popular_tags_extra_output.png)
- [Quick Replies Output][qr]
![](https://raw.githubusercontent.com/np1810/Hadoop_and_MapReduce/master/L5_FinalProject/quick_replies/quick_replies_output.png)

---
> Tag Cloud made on [Wordle](http://wordle.net) and Graphs using Microsoft Excel  
> All Complete Input Datasets are available on [Udacity website](http://content.udacity-data.com/course/hadoop/forum_data.tar.gz).

### Execution
Programs can be quickly executed by using **Input Samples** for _TESTING_ only and command is not actually running any **_HADOOP_** task -
```
$ cat input_sample | ./mapper.py | sort | ./reducer.py
```

### Contributing
Changes and improvements are more than welcome! Feel free to fork and open a pull request.

### License
This Repo is licensed under the [MIT License][license]

### Donations
If you would like to donate then [Donate to UNICEF][donate]

### Feels Intriguing!?
Then do visit [my personal site][mysite] where you can find some more interesting stuff and ways to contact me.

---
[mysite]:http://nitinpathak.esy.es
[donate]:http://supportunicef.org
[license]:http://github.com/np1810/Hadoop_and_MapReduce/blob/master/LICENSE.md
[al]:http://github.com/np1810/Hadoop_and_MapReduce/tree/master/L5_FinalProject/average_length/average_length_output.tsv
[pt]:http://github.com/np1810/Hadoop_and_MapReduce/tree/master/L5_FinalProject/popular_tags/popular_tags_output.tsv
[pte]:http://github.com/np1810/Hadoop_and_MapReduce/tree/master/L5_FinalProject/popular_tags_extra/popular_tags_extra_output.tsv
[qr]:http://github.com/np1810/Hadoop_and_MapReduce/tree/master/L5_FinalProject/quick_replies/quick_replies_output.tsv
[st]:http://github.com/np1810/Hadoop_and_MapReduce/tree/master/L5_FinalProject/student_times/student_times_output.tsv
[sg]:http://github.com/np1810/Hadoop_and_MapReduce/blob/master/L5_FinalProject/study_groups/study_groups_output.tsv