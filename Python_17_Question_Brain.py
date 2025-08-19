#!/usr/bin/env python
# coding: utf-8

# In[8]:


class QuizBrain:
    def ask_question(self, question_bank):
        for question in question_bank:
            user_answer=input(question.text).capitalize()
            if user_answer==str(question.answer):
                print("You got it right!")
            else:
                print("Ops, not the right the answer!")
                break
            
        


# In[9]:


get_ipython().system('jupyter nbconvert --to script Python_17_Question_Brain.ipynb')


# In[ ]:




