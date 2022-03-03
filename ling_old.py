#!/bin/python3


from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
from time import sleep
from bs4 import BeautifulSoup as bs

"""TODO
[ ]  video page     | Needed after last update
[X]  Comprehension
[X]  listening lab
[X]  adv comp
[X]  vocab
[X]  gramn
[X]  games_par1
[X]  games_par2     | Needs to be edit because of answers which includes two words
"""


class LinBot():
    """
    Class of Lingua Bot
    """

    def __init__(self,mail,password,url,seperated_mod=0):

        self.mail = mail
        self.password = password
        self.url = url
        self.seperated_mod = seperated_mod

        ff_profile = webdriver.FirefoxProfile()
        ff_profile.set_preference("layout.css.devPixelsPerPx","0.6")
        self.driver = webdriver.Firefox(ff_profile)
        #self.driver.execute_script('document.body.style.MozTransform = scale(0.70)')

        #self.driver.execute_script('document.body.style.MozTransform = "scale(0.7)"')

    def Login(self):
        self.driver.get("https://lingua-attack.com/en-EA/user/login")
        
        name = self.driver.find_element_by_xpath("""//*[@id="edit-name"]""")
        password = self.driver.find_element_by_xpath("""//*[@id="edit-pass"]""")
        
        name.send_keys(self.mail)
        password.send_keys(self.password)
        
        self.driver.find_element_by_xpath("""//*[@id="edit-submit"]""").click() # login button
    #"""
    #url="https://english.lingua-attack.com/en-EA/videobooster/france-24-english/boris-johnson-slams-theresa-mays-brexit-plan?step=comprehension"
    #
    #url="https://english.lingua-attack.com/en-EA/videobooster/man-high-castle/julianas-interrogation"
    #"""

    
    def Video_Page(self):
        self.driver.get(self.url + "?step=video")
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="translation-language-modal-select-language"]"""))).click()

            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[2]/main/div/div[4]/div/div/div[2]/div/div/select/option[14]"))).click()

            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="translation-language-modal-save-button"]"""))).click()

            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[2]/main/div/div[3]/div/div[3]/a"))).click()
        except:
            pass

        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[2]/main/div/div[3]/div/div[2]/div[1]/div/div[1]/button"))).click()

        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="js-next-step-button"]"""))).click()

        if(self.seperated_mod == 0):
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[2]/main/div/div[3]/div/div/div/div/a"))).click()

    def Comprehension(self):
        self.driver.get(self.url + "?step=comprehension")
        # GETTING ANSWERS
        # question_amount = len(answer_list) type -list
        # question x = list[x] type -dict

        answer_list = self.driver.execute_script('return vb_survival_test')
        #print("answe_list", answer_list)
        for quest in range(len(answer_list)): # answer_list = question amount
            answer_id = answer_list[quest]['correct_answers'][0]['id']
            print("answer_id",answer_id)
            # get value driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div[3]/div/div[1]/div/div[1]/div/div[1]/label/input").get_attribute('outerHTML') -- gives all string
        
            for ans in range(1, len(answer_list[quest]['all_answers']) +1): # answer_list = question amount
                #ans_id = WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div[3]/div/div[1]/div/div[1]/div/div[{ans}]/label/input"))).get_attribute('outerHTML').replace("value=",'\n').replace('class','\n').split('\n')[1][1:-2] # Get all answers id

                #sleep
            
                while(1):
                    if(self.driver.find_element_by_xpath(f"/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div[3]/div/div[1]/div/div[1]/div/div[{ans}]").get_attribute("class") == "checkbox video-booster__checkbox"):
                        sleep(1.2)
                        break
                    #else:
                    #print(class_name)

                #WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div[3]/div/div[1]/div/div[1]/div/div[{ans}]/label")))
                # Wait until answers span is cickable

                #sleep(2)
                ans_id = self.driver.find_element_by_xpath(f"/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div[3]/div/div[1]/div/div[1]/div/div[{ans}]/label/input").get_attribute('value') # Get all answers id
                print("ans_id",ans_id)

                if(int(answer_id) == int(ans_id)):
                    WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div[3]/div/div[1]/div/div[1]/div/div[{ans}]/label"))).click() # Answer

                    print("equal")

                    WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="next_comprehension"]"""))).click()

                    break

        if(self.seperated_mod == 0):

            # End of section
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="btn-listening-step"]"""))).click()
                    #self.driver.find_element_by_xpath(f"/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div[3]/div/div[1]/div/div[1]/div/div[{ans}]/label").click() # Answer
                    #print("equal")
                    #self.driver.find_element_by_xpath("""//*[@id="next_comprehension"]""").click() # Next button
                    #break

    def Listening_Lab(self):

        self.driver.get(self.url + "?step=listening-lab")

        # GETTING ANSWERS
        # question_amount = len(answer_list) type -list
        # question x = list[x] type -dict

        answer_list = self.driver.execute_script('return listening_lab')
        #print("answe_list", answer_list)
        for quest in range(len(answer_list)): # answer_list = question amount
            answer_id = answer_list[quest]['correct_answers'][0]['id']
            print("answer_id",answer_id)

            for ans in range(1, len(answer_list[quest]['all_answers']) +1): # answer_list = question amount 
                while(1):
                    if(self.driver.find_element_by_xpath(f"/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div[3]/div/div[1]/div/article[1]/div/div/div[{ans}]/label/span").get_attribute("class") == "video-booster__checkbox-icon"):
                        sleep(1.2)
                        break

                ans_id = self.driver.find_element_by_xpath(f"/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div[3]/div/div[1]/div/article[1]/div/div/div[{ans}]/label/input").get_attribute("value") # Get all answers id
                print("ans_id",ans_id)

                if(int(answer_id) == int(ans_id)):
                    WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div[3]/div/div[1]/div/article[1]/div/div/div[{ans}]/label/span"))).click() # Answer

                    print("equal")
                    break

        if(self.seperated_mod == 0):
            # End Section
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="next"]"""))).click()
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH,"""//*[@id="btn-advanced-comprehension-step"]"""))).click()


    def Advanced_Comprehension(self):

        self.driver.get(self.url + "?step=advanced-comprehension")

        # GETTING ANSWERS
        # question_amount = len(answer_list) type -list
        # question x = list[x] type -dict

        answer_list = self.driver.execute_script('return vb_quiz_challenge')
        #print("answe_list", answer_list)
        for quest in range(len(answer_list)): # answer_list = question amount
            answer_id = answer_list[quest]['correct_answers'][0]['id'] 
            print("answer_id",answer_id)

            for ans in range(1, len(answer_list[quest]['all_answers']) +1): # answer_list = question amount 
                while(1):
                    if(self.driver.find_element_by_xpath(f"/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div[3]/div/div[1]/div/div[2]/div[{ans}]/label/span").get_attribute("class") == "video-booster__checkbox-icon"):
                        
                        sleep(1.2)
                        break

                ans_id = self.driver.find_element_by_xpath(f"/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div[3]/div/div[1]/div/div[2]/div[{ans}]/label/input").get_attribute("value") # Get all answers id
                print("ans_id",ans_id)

                if(int(answer_id) == int(ans_id)):
                    WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div[3]/div/div[1]/div/div[2]/div[{ans}]/label/span"))).click() # Answer

                    print("equal")

                    WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="next_advanced_comprehension"]"""))).click()
                    break
        if(self.seperated_mod == 0):
            # End of Seciton
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="btn-vocab-academy-step"]"""))).click()


    def Vocab_Academy(self):
        # Our drag and point thing
        # webdriver.ActionChains(a).drag_and_drop(drag drop ).perform()

        self.driver.get(self.url + "?step=vocab-academy")


        answer_list = self.driver.execute_script('return missingWords')
        vocab_text_len = int(self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div[3]/div/div[1]/div/article[1]/p").get_attribute('innerHTML').count('span') / 2)

        for span_ in range(1, vocab_text_len +1):
            span = self.driver.find_element_by_xpath(f"/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div[3]/div/div[1]/div/article[1]/p/span[{span_}]")

            data_number = span.get_attribute('data-number')

            if(data_number == None):
                pass
            else:
                #sleep(0.75)
                print('data_number:',data_number)
                webdriver.ActionChains(self.driver).drag_and_drop(self.driver.find_element_by_xpath(f"""//*[@id="card{data_number}"]"""), span).perform()
        # End of Seciton
        for i in range(2):
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div[3]/div/div[1]/p"))).click()

        if(self.seperated_mod == 0):
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="btn-grammar-step"]"""))).click()


    def Grammar(self):

        self.driver.get(self.url + "?step=grammar")
        # pick the best answer
        #ans[question]['correct_answers'][0]['id']
        #type_grammar = None

        try:
            print('TRY')
            answer_list = self.driver.execute_script('return vbGrammarGaps')
            #type_grammar = "quiz_fill_gap"

        #drop = self.driver.find_element_by_xpath("""//*[@id="the-gap"]""")
            for question in range(len(answer_list)):
                answer_list = self.driver.execute_script('return vbGrammarGaps')
                sleep(1.25)
                #actions = webdriver.ActionChains(self.driver)
                #//*[@id="item-1"]
                #len(ans[0]['all_answers']) amount of selections [answer]
                for answer in range(len(answer_list[question]['all_answers'])):
                    print(f"Question: {question}, answer:  {answer}")
                    sleep(0.75)
                    if(answer_list[question]['all_answers'][answer]['is_correct_answer'] == '1'):
                        print('Selecting',answer_list[question]['all_answers'][answer]['answer_text'])

                        correct_answer = self.driver.find_element_by_xpath(f"""//*[@id="item-{answer}"]""")
                        gap_drop = self.driver.find_element_by_xpath("""//*[@id="the-gap"]""")
                        webdriver.ActionChains(self.driver).drag_and_drop(correct_answer, gap_drop).perform()
                        sleep(0.50)
                        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="validate"]"""))).click()
                        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="next"]"""))).click()
                        #del actions
                        break


        except:
            print("EXCEPT")
            answer_list = self.driver.execute_script('return grammar_content')
            # type of grammar
            grammar_content = answer_list[0]['section']
            print('GRAMMAR CONTENT',grammar_content)
            # Yes or no
            if(grammar_content == "grammar_lab_correct_incorrect"):
                #ans[0]['correct_answers']
                correct_span_xpath = "/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div[3]/div/div[2]/div[2]/a[1]/span"
                false_span_xpath = "/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div[3]/div/div[2]/div[2]/a[2]/span"
                for question in range(len(answer_list)):
                    try:
                        answer_list[question]['correct_answers']
                        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, correct_span_xpath))).click()
                    except:
                        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, false_span_xpath))).click()
                    WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="next"]"""))).click()

            
            elif(grammar_content == 'grammar_lab_mcq'):
                for question in range(len(answer_list)):
                    #answer_list = self.driver.execute_script('return grammar_content')
                    sleep(1.25)
                    for answer in range(len(answer_list[question]['all_answers'])):
                        print(f"Question: {question}, answer:  {answer}")
                        sleep(0.75)
                        if(answer_list[question]['all_answers'][answer]['is_correct_answer'] == '1'):
                            print('Selecting',answer_list[question]['all_answers'][answer]['answer_text'])
                            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div[3]/div[1]/div/label[{answer+1}]/span"))).click()
                            sleep(0.50)
    
                            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="validate"]"""))).click()
                            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="next"]"""))).click()
                            break
                

            elif(grammar_content == 'make_connection'):
                
                answer_list = self.driver.execute_script('return grammar_content')
                
                question_xpath = "/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div[3]/div[1]/div/div[1]/div[1]/div[{question}]/p"
                answer_xpath = "/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div[3]/div[1]/div/div[1]/div[2]/div[{answer}]/div/p"

                for quest in range(len(answer_list)):
                    #sleep(0.25)
                    question = self.driver.find_element_by_xpath(question_xpath.format(question=quest+1))
                    answer_text = answer_list[quest]['answer_text']

                    for ans in range(len(answer_list)):
                        #sleep(0.25)
                        answer = self.driver.find_element_by_xpath(answer_xpath.format(answer=ans+1))
                        if(answer_text == answer.get_attribute('innerHTML')):
                            webdriver.ActionChains(self.driver).drag_and_drop(answer,self.driver.find_element_by_xpath(answer_xpath.format(answer=quest+1))).perform()
                            break

                sleep(0.75)

                for i in range(2):
                    WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div[3]/p[2]"))).click()


        
        if(self.seperated_mod == 0):
                WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="btn-games"]"""))).click()



    def Game_Zone_1(self):

        self.driver.get(self.url + "?step=games&content=vb&part=letters-box")
        #?step=games&part=letters-drop

        #WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div/a"))).click()

        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/section/div[2]/div[1]/a"))).click()


        #webdriver.ActionChains(d).click_and_hold(dr).move_to_element(mov1).move_to_element(mv2).click().release(dr).perform()

        answer_list = self.driver.execute_script("return dataForGame")

        for question in range(len(answer_list)-2):

            actions = webdriver.ActionChains(self.driver)
            sleep(1.25)
            word_pos_list = answer_list[str(question)]['wordsPositions'][0]['pos']
            print(word_pos_list)

            raw_xpath = "/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/section/div[6]/div/div[3]/div[{y}]/div[{x}]"


            first_word = self.driver.find_element_by_xpath(raw_xpath.format(x=word_pos_list[0]['x']+1,y=word_pos_list[0]['y']+1))
            print("first X:{x} -Y:{y}".format(x=word_pos_list[0]['x'],y=word_pos_list[0]['y']))
            actions.click_and_hold(first_word)

            for word in range(1,len(word_pos_list)):
                actions.move_to_element(self.driver.find_element_by_xpath(raw_xpath.format(x=word_pos_list[word]['x']+1,y=word_pos_list[word]['y']+1)))

            actions.click().release(first_word)
            actions.perform()
            del actions
            sleep(1.25)

    def Game_Zone_2(self):

        self.driver.get(self.url + "?step=games&content=vb&part=letters-drop")
        #?step=games&part=letters-drop

        #WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/div/a"))).click()

        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/section/div[2]/div[1]/a"))).click()


        #webdriver.ActionChains(d).click_and_hold(dr).move_to_element(mov1).move_to_element(mv2).click().release(dr).perform()

        answer_list = self.driver.execute_script("return dataForGame")

        for question in range(len(answer_list)-2):
            actions = webdriver.ActionChains(self.driver)
            sleep(1.25)
            word_pos_list = answer_list[str(question)]['gameStateLettersDrop']['wordsPositions'][0]['pos']
            print(word_pos_list)
            """a['0']['gameStateLettersDrop']['wordsPositions'][0]['pos']



/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/section/div[6]/div/div[1]/div[3]/div[1]/div[7]
/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/section/div[6]/div/div[1]/div[3]/div[2]/div[7]
/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/section/div[6]/div/div[1]/div[2]/p/p --> definiton
            """
            raw_xpath = "/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/section/div[6]/div/div[1]/div[3]/div[{x}]/div[{y}]"

            #first_word = self.driver.find_element_by_xpath(raw_xpath.format(x=word_pos_list[0]['x']+1,y=word_pos_list[0]['y']+1))


            print("first X:{x} -Y:{y}".format(x=word_pos_list[0]['x'],y=word_pos_list[0]['y'])) 
            first_word = WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH,raw_xpath.format(x=word_pos_list[0]['x']+1,y=(7-word_pos_list[0]['y'])))))

            definiton = WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[2]/main/div/div/section/div[2]/div/section/div[6]/div/div[1]/div[2]/p/p"))).get_attribute('innerHTML')
            print('DEFİNİTON',definiton)
            #print("first X:{x} -Y:{y}".format(x=word_pos_list[0]['x'],y=word_pos_list[0]['y']))
            print('Tutmaya başlıyo')
            actions.click_and_hold(first_word)

            for word in range(1,len(word_pos_list)):
                #sleep(0.75)
                print(word,'Tuttu')

                actions.move_to_element(WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH,raw_xpath.format(x=word_pos_list[word]['x']+1,y=(7-word_pos_list[word]['y']))))))
                #actions.move_to_element(self.driver.find_element_by_xpath(raw_xpath.format(x=word_pos_list[word]['x']+1,y=word_pos_list[word]['y']+1)))


            actions.click().release(first_word)
            print('perform')
            actions.perform()
            del actions
            sleep(1.25)
            




if(__name__ == "__main__"):
    a = LinBot('dincer.alperenarda@student.atilim.edu.tr','4bc5cd3','https://english.lingua-attack.com/en-EA/skillbooster/communicating-email')
    #sleep(1)
    a.Login()
    sleep(1)
    a.Video_Page()
    a.Comprehension()
    a.Listening_Lab()
    a.Game_Zone_1()
    a.Game_Zone_2()
    a.Grammar()

