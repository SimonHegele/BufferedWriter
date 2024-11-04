# BufferedWriter
Simple buffered file writer for dealing with large amount of data and files efficiently

For each file out of an arbitrary large amount of files the BufferedWriter stores a
list of lines. Only when they exceed a predefined limit their contents are 
collectively written to the filesystem. As each file is opened and close less times 
the BufferedWriter operates much faster. Also, accessing the same file twice in very
short period of time can cause Errors. This can also be prevented by using the 
BufferedWriter.

## Speed test 

I generated a list of 100,000 random integer numbers. Each of these numbers should be
written to one of 1,000 files according to its residual class. Regular writing,
where for each integer number the file is opened and closed, shows to be much slower.

<p float="left">
  <img src="test.png" width="500" /> 
</p>
