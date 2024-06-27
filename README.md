# Report for Assignment 1
## IOPaint

Name: <Group 20>

URL: <https://github.com/Sanster/IOPaint>

Number of lines of code and the tool used to count it: <32,775 using Lizard>

Programming language: Python

## Coverage measurement
### Existing tool
<Inform the name of the existing tool that was executed and how it was executed>
Coverage.py was used to test coverage using unittest. Here is the command we run: 
coverage run --source=iopaint -m unittest discover -s iopaint/tests

Coverage results from coverage.py using unittest before our instrumentation and testing:

openaimodel.py:

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture1.png)

common.py:

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture2.png)

util.py:

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture3.png)

<Show the coverage results provided by the existing tool with a screenshot>

### Your own coverage tool
<The following is supposed to be repeated for each group member>
<Group member name> Isabella Reyes

Function 1: forward() from TimestepEmbedSequential class in openaimodel.py 
https://github.com/Sanster/IOPaint/compare/main...nova-jiang:SEG-IOPaint:main#diff-d8e87eab477587cf443be3dbdc456613121ee5ec2b65492de89475e34c519af3 

Coverage results output by instrumentation: 

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture4.png)

<Provide a screenshot of the coverage results output by the instrumentation>


Function 2: forward() from Upsample class in openaimodel.py 
https://github.com/Sanster/IOPaint/compare/main...nova-jiang:SEG-IOPaint:main#diff-d8e87eab477587cf443be3dbdc456613121ee5ec2b65492de89475e34c519af3 

Coverage results output by instrumentation: 
 
![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture5.png)

<Group member name> Saskia Ufenast Smolders

Function 1: forward() from the Swish class in common.py
https://github.com/nova-jiang/SEG-IOPaint/commit/3825110289a2c1597edf375d8d17506ddfe84cf3

Coverage results output by instrumentation:

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture6.png)

<Provide a screenshot of the coverage results output by the instrumentation>


Function 2: initiation function from the Activation class in common.py
https://github.com/nova-jiang/SEG-IOPaint/commit/3825110289a2c1597edf375d8d17506ddfe84cf3

Coverage results output by instrumentation:

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture7.png)

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture8.png)

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture9.png)



<Group member name> Nova Jiang

Function 1: save_imges() from iopaint.model.anytext.utils.py
https://github.com/nova-jiang/SEG-IOPaint/commit/0a6fff64083b51c965c44326fc9451e78c2fd5e8

Coverage results output by instrumentation:

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture10.png)

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture11.png)

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture12.png)


Function 2: resize_image() from iopaint.model.anytext.utils.py
https://github.com/nova-jiang/SEG-IOPaint/commit/0a6fff64083b51c965c44326fc9451e78c2fd5e8

Coverage results output by instrumentation:

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture13.png)

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture14.png)

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture15.png)


## Coverage improvement

### Individual tests
<The following is supposed to be repeated for each group member>

<Group member name> Isabella
 
<Test 1> TestTimestepEmbedSequentual

Commit link to test file: 
https://github.com/Sanster/IOPaint/compare/main...nova-jiang:SEG-IOPaint:main#diff-212a42d68b03ef20ef24af3e9f5749dcd2cd9088d5e1a150bcf6b9888cd7aeaa 

Please note that the following coverage reports only show the coverage of my instrumented functions. All other functions in this file were commented out when creating the report. 

Screenshot of old coverage results: 

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture16.png)

Screenshot of new coverage results: 

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture17.png)

Coverage improvement: 
The coverage increased from 0% to 100%. This is because there were no previous tests run on the TimestepEmbedSequential class and its forward() function. I created a test containing three functions, where each function consisted of a test case for one of the branches in the forward method. This allowed each branch to be properly entered, and therefore improved its coverage. 


<Test 2> TestUpsample

Commit link to test file: 
https://github.com/Sanster/IOPaint/compare/main...nova-jiang:SEG-IOPaint:main#diff-212a42d68b03ef20ef24af3e9f5749dcd2cd9088d5e1a150bcf6b9888cd7aeaa 

Please note that the following coverage reports only show the coverage of my instrumented functions. All other functions in this file were commented out when creating the report. 

Screenshot of old coverage results: 

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture18.png)

Screenshot of new coverage results: 

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture19.png)

Coverage improvement: 
The coverage increased from 0% to 100%. This is because there were no previous tests run on the Upsample class and its forward() function. I created a test containing two functions, each with different test cases. One tested for 3D inputs without convolution, and the other tested for 2D inputs with convolution. The latter was designed to enter two different branches in Upsample, one for not being 3D and another for using convolution. This allowed each branch to be properly entered, and therefore improved the coverage. 


<Group member name> Saskia Ufenast Smolders

<Test 1> test_swish.py
https://github.com/nova-jiang/SEG-IOPaint/commit/66d9510910022c7a90841ab2fae86b8bbaa60f36

Screenshot of old coverage results: 

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture20.png)

Screenshot of new coverage results: 

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture21.png)

<Provide a screenshot of the new coverage results>
The coverage of the common.py file improved by 42% with the newly added tests for the Swish function. This is mainly due to the fact that there was no test file prior to this one. Both branches of the function are tested, namely when it is in place and when it isn’t. 

<State the coverage improvement with a number and elaborate on why the coverage is improved>


<Test 2> test_activation.py

https://github.com/nova-jiang/SEG-IOPaint/commit/07fd5383094e9ef192832f447d9512dabb0cf33d

The old coverage result excluding the newly added test_swish function is 0%.
The added test of the activation function increases the coverage of the common.py file by 97%. Combined with the test for the swish function showed above, this percentage increases all the way up to 100%. Each individual activation function and branch has a test case. The expected value when applying one of these functions is compared to the obtained value to assert its correctness. 

Screenshot of old coverage results:

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture22.png)

Screenshot of new coverage results: 

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture23.png)

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture24.png)


<Group member name> Nova Jiang

<Test 1> save_images()
https://github.com/nova-jiang/SEG-IOPaint/commit/0a6fff64083b51c965c44326fc9451e78c2fd5e8

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture25.png)

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture26.png)

Screenshot of old coverage results: 

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture27.png)

Screenshot of old coverage results: 

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture28.png)

<Provide a screenshot of the new coverage results>
The coverage increased from 0% to 100% for this function. Initially, none of the instrumented branches were being tested in the tests files, resulting in 0% coverage. I created tests for the function that cover scenarios like saving images to folders that don't exist, saving images with empty image lists, or saving correct images to existing folders, which are very common accidents we may encounter in reality. Also, the printing statements in the test cases help to debug and show the current status of testing. 

<State the coverage improvement with a number and elaborate on why the coverage is improved>

<Test 2> resize_image
https://github.com/nova-jiang/SEG-IOPaint/commit/0a6fff64083b51c965c44326fc9451e78c2fd5e8
The coverage increased from 0% to 100% for this function, which shows that the function went from not being tested to fully tested. I developed tests for calling this function with valid inputs, inputs not requiring resizing, invalid input types, and empty inputs. In this case, special attention were paid to edge cases, such as empty inputs and invalid data types, which helped cover branches that might be easily overlooked in typical usage scenarios. Each of these branches was hit and tested after improvement, so it efficiently improved the coverage.

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture29.png)

Screenshot of old coverage results: 

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture30.png)

Screenshot of new coverage results: 

![Image text](https://github.com/nova-jiang/SEG-IOPaint/blob/main/assets/Picture31.png)

### Overall

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions
Isabella:  
- Instrumented the forward methods in the TimestepEmbedSequential and Upsample classes in openaimodel.py. 
- Created a test file containing test cases to run on these functions, in order to test their coverage. 

Saskia:
- Instrumented the forward function in the Swish class and the init function in the Activation class of the common.py file.
- Created test cases for all branches of the functions and increased the coverage.

Nova: 
- Instrumented the save_images and resize_image methods in the utils.py under anytext folder.
- Created test cases to run the chosen functions and test and improve each branches’ coverage.

<Write what each group member did>

