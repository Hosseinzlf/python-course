
# # Explore data with NumPy and Pandas

# In[1]:


# Exploring data arrays with NumPy
data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
print(data)


# In[2]:


import numpy as np

grades = np.array(data)
print(grades)


# In[3]:


print (type(data),'x 2:', data * 2)
print('---')
print (type(grades),'x 2:', grades * 2)


# In[4]:



grades.mean()


# In[5]:



grades[0]


# In[6]:


grades.shape


# In[7]:


# Define an array of study hours
study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]

# Create a 2D array (an array of arrays)
student_data = np.array([study_hours, grades])

# display the array
student_data


# In[8]:


# Show shape of 2D array
student_data.shape


# In[9]:


# Show the first element of the first element
student_data[0][0]


# In[10]:


# Get the mean value of each sub-array
avg_study = student_data[0].mean()
avg_grade = student_data[1].mean()

print('Average study hours: {:.2f}\nAverage grade: {:.2f}'.format(avg_study, avg_grade))


# # Exploring tabular data with Pandas

# In[11]:


import pandas as pd

df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
                            'StudyHours':student_data[0],
                            'Grade':student_data[1]})

df_students 


# In[12]:


# Get the data for index value 5
df_students.loc[5]


# In[13]:


# Get the rows with index values from 0 to 5
df_students.loc[0:5]


# In[14]:


# Get data in the first five rows
df_students.iloc[0:5]


# In[15]:


df_students.iloc[0,[1,2]]


# In[16]:


df_students.loc[0,'Grade']


# In[17]:


df_students.loc[df_students['Name']=='Aisha']


# In[18]:


df_students[df_students.Name == 'Aisha']


# # Loading a DataFrame from a file

# In[22]:


df_students = pd.read_csv('grades.csv',delimiter=',',header='infer')
df_students.head()


# In[23]:


df_students.isnull()


# In[24]:


df_students.isnull().sum()


# In[25]:


df_students[df_students.isnull().any(axis=1)]


# In[27]:


df_students.StudyHours = df_students.days_studied.fillna(df_students.days_studied.mean())
df_students


# In[28]:


# Get the mean study hours using to column name as an index
mean_study = df_students['days_studied'].mean()

# Get the mean grade using the column name as a property (just to make the point!)
mean_grade = df_students.grades.mean()

# Print the mean study hours and mean grade
print('Average weekly study days: {:.2f}\nAverage grade: {:.2f}'.format(mean_study, mean_grade))


# In[29]:


# Get students who studied for the mean or more hours
df_students[df_students.StudyHours > mean_study]


# In[31]:


# What was their mean grade?
df_students[df_students.StudyHours > mean_study].grades.mean()


# In[32]:


passes  = pd.Series(df_students['grades'] >= 4)
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)

df_students


# In[34]:


# Create a DataFrame with the data sorted by Grade (descending)
df_students = df_students.sort_values('grades', ascending=False)

# Show the DataFrame
df_students


# In[ ]:




