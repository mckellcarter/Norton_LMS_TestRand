import docx
import random

class LMS_test_vers: 

  questions = []
  test_header = []
  test_footer = []
  answer_key_header = []
  answer_key_footer = [] 
  
  def __init__(self, docx_file): 
    ##create a test object by reading in and parsing a docx generated from Norton's test maker for an LMS 
    #XML tags
    xml_paragraph = '<w:p>'
    ques_tag = '<w:ilvl w:val="0"/>'
    ans_tag = '<w:ilvl w:val="1"/>'
    ans_key_tag = '<w:t>Answer:</w:t>'
    
    #temporary structures
    q_temp = ''
    ans_temp = []
    q_temp_extra = []
    answer_key_count = -1  #assumes zero index to access questions
    in_key_answer = False  #use to flag when the next paragraph will have an answer
    
    d = docx.Document(docxfile) 
    ps = d.split(xml_paragraph)
    for p in ps: 
      ######process questions ###############
      if  ques_tag in p and not(answer_key_header): 
        #if we have a non-indented list item and are outside the answer key, new question
        if q_temp = '':
        #if we haven't started a question
          q_temp = p
        else:
        #already have a question in process, time to push it and start a new one. 
          questions.append(LMS_question(q_temp, ans_temp)) 
          q_temp = ''
          ans_temp = []
      elif ans_tag in p and q_temp != '': 
      #if we are in a question and have an indented list item
          ans_temp.append(p)
      elif q_temp and not(answer_key_header): 
        #processing a question but not an answer option so store to be dumped after answers
        q_temp_exta.append(p)
      ####################process answer key ######################      
      elif '<w:t>Answer Key</w:t>' in p:
      #begin Answer key, reset question gathering
        answer_key_header.append(p)
        q_temp = ''
        ans_temp = []      
      elif answer_key_header and ques_tag in p:
        #if in the answer key and detect an unindented list item 
        answer_key_count += 1 
        in_key_answer = True 
      elif in_key_answer and answer_key_header:
        if '<w:t>A</w:t>' in p: 
          key_answer = 0
        elif '<w:t>B</w:t>' in p: 
          key_answer = 1 
        elif '<w:t>C</w:t>' in p: 
          key_answer = 2
        elif '<w:t>D</w:t>' in p: 
          key_answer = 3 
        elif '<w:t>E</w:t>' in p: 
          key_answer = 4
        questions[answer_key_count].update_answer(key_answer)
        in_key_answer = False  #reset in_key_answer flag
    

class LMS_question: 
  def __init__(q, a, c=None): 
    question = q
    answers = a
    correct = c

  def update_answer(self,c): 
    self.correct = c

  def shuffle_answers(self)
    tmp_ans = answers[self.correct]
    answers = random.shuffle(answers)
    correct = [i for i,v in enumerate(answers) if v==tmp_ans][0] #find the index of the item matching the old correct answer (assumes unique answer entries) 
    
