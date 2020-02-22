#!/usr/bin/python3

import requests

import getpass

from bs4 import BeautifulSoup as bs


#Try to Read EMAIL and PASSWORD 

try:
    file = open('login_info.data', 'r')
    login_info_data= file.readlines()
  
    email = login_info_data[0]
    password = login_info_data[1]
    file.close()


except(FileNotFoundError,IndexError):
    email =  input("email: ")
    password = getpass.getpass("Password: ")

    raw_data = [email,"\n", password]
    file_new = open('login_info.data', 'w')
    file_new.writelines(raw_data)
    file_new.close()



# headers
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}


# login data
login_data = {
    'name': email,
    'pass': password,
    'form_id': 'user_login',
    'op': 'Log+in'  
}



with requests.Session() as s:

    # Get Vocab answers function
    def GetVocab():
        # get vocab's source code
        vocab_page= s.get(target_HW + "?step=vocab-academy")
        vocab_page_content = bs(vocab_page.content, "html5lib")

        # get script
        vocab_script = vocab_page_content.find('p', {'class': 'mb-0'})

        # ge answer keys
        vocab_answer = vocab_page_content.find('script', {'type': "text/javascript"})
        
        # print script and answers
        print(vocab_script, '\n' * 3, vocab_answer)
    
    # get Comprehension
    def GetComp():

        # get source code of comp page
        comp_page = s.get(target_HW + "?step=comprehension")
        comp_page_content = bs(comp_page.content, "html5lib")

        #get answers as string
        comp_answers = str(str(comp_page_content.findAll('script')[3]).split(""" is_correct_answer":"1" """))

        #print answers
        list_answer_end = []

        for i in range(70,len(comp_answers)):
            if(comp_answers[i] == "1" and comp_answers[i -10] == "_"):
                list_answer_end.append(i - 24)


        list_answer_end.reverse()
        list_answer_string = []
        str_answer = ""
        for i in list_answer_end:
            for h in range(i,70,-1): 
                if(comp_answers[h] == "\"" and i - h > 3):
                    list_answer_string.append(str_answer[::-1])
                    str_answer = ""
                    break
                else:
                    str_answer = str_answer + comp_answers[h] 



        print(list(set(list_answer_string)))



    # get Listening Lab
    def ListLab():
        #get source code of Listening Lab
        listLab_page = s.get(target_HW + "?step=listening-lab")
        listLab_page_content = bs(listLab_page.content, "html5lib")

        #get answers
        listLab_answers = str(str(listLab_page_content.findAll('script')[3]).split(""" is_correct_answer":"1" """))

        #print answers
        list_answer_start = []
        list_answer_end = []
        list_answer_point = []
        list_answer_end_clean_temp = []
        list_answer_end_clean = []

        for i in range(70,len(listLab_answers)):
            if(listLab_answers[i] == "1" and listLab_answers[i -10] == "_"):
                list_answer_point.append(i)
        

        for g in list_answer_point:
            x = 0
            for h in range(g, g + 100):
                if(listLab_answers[h] == "\""):
                    if(x == 7):
                        list_answer_start.append(h)
                    if(x == 8):
                        list_answer_end.append(h)

                    x += 1


        for i in range(0, len(list_answer_start) -1):
            list_answer_end_clean_temp.append(listLab_answers[list_answer_start[i]: list_answer_end[i]])

        for h in list(set(list_answer_end_clean_temp)):
            list_answer_end_clean.append(h)

        print(list_answer_end_clean)

        
    # get Advanced Comprehension
    def AdvComp():
        # get source AdvComp'scode
        advComp_page = s.get(target_HW + "?step=advanced-comprehension")
        advComp_page_content = bs(advComp_page.content, "html5lib")

        # get answers
        advCom_answers = str(str(advComp_page_content.findAll('script')[3]).split(""" is_correct_answer":"1" """))

        #print answers
        list_answer_end = []


        for i in range(70,len(advCom_answers)):
            if(advCom_answers[i] == "1" and advCom_answers[i -10] == "_"):
                list_answer_end.append(i - 24)


        list_answer_end.reverse()
        list_answer_string = []
        str_answer = ""
        for i in list_answer_end:
            for h in range(i,70,-1): 
                if(advCom_answers[h] == "\""):
                    list_answer_string.append(str_answer[::-1])
                    str_answer = ""
                    break
                else:
                    str_answer = str_answer + advCom_answers[h] 




        print(list(set(list_answer_string)))

    # get Grammar answers
    def Gram():
        #get source code
        gram_page = s.get(target_HW + "?step=grammar")
        gram_page_content = bs(gram_page.content, "html5lib")

        #get answers
        gram_answers = gram_page_content.findAll('script')[4]

        # print answers
        print(gram_answers)


    # set login page
    login_page = s.get("https://lingua-attack.com/en-EA/user/login", headers=headers)

    # get login source code
    login_page_content = bs(login_page.content, "html5lib")
    
    # add form_build_id to login_data
    login_data['form_build_id'] = login_page_content.find('input', attrs={'name': 'form_build_id'})['value']

    # login
    r = s.post("https://lingua-attack.com/en-EA/user/login", login_data, headers=headers)
    
    try:
        r.history[0].status_code
        controlPoint0 = 1
    except(IndexError):
        print('Başarısız login çabası.')
        file_delete = open('login_info.data', 'w+')
        file_delete.close()
        controlPoint0 = 0
        




    # MAIN PART
    while(controlPoint0 == 1):

        try:
            # get vocab link
            target_HW = input("lingua homework link: ")

            islem_no = int(input("Yapmak istediğin işlem ne?\nComprehension cevapları: 1\nListening Lab cevapları: 2\nAdvanced Comprehension cevapları: 3\nVocab Academy cevapları: 4\nGrammar cevapları: 5\nHomework Link Değiştir: 6\nYardımcı Notlar: 7\nÇıkış: 8\nİşlem No: "))
            print("\n" * 3)

            if(islem_no == 1):
                GetComp();print("\n" * 3)
                
            elif(islem_no == 2):
                ListLab();print("\n" * 3)

            elif(islem_no == 3):
                AdvComp();print("\n" * 3)

            elif(islem_no == 4):
                GetVocab();print("\n" * 3)

            elif(islem_no == 5):
                Gram();print("\n" * 3)

            elif(islem_no == 6):
                target_HW = input("lingua homework link: ");print("\n" * 3)

            elif(islem_no == 7):
                print("""Başarılı olan/olamayan giriş bilgileriniz scripti tuttuğunuz uzantıda "login_info.data" dosyasında tutulmaktadır.\n\nBilgileri sıfırlamak için bu dosyayı silin.\n\nBu bilgiler şifrelenmemiştir, bu risk teşkil etmektedir.\n\nÖzellikle bu scripti paylaşırken "login_info.data" dosyasını paylaşmadığınıza emin olun.\n\n"login_info.data" scriptin gerekli bir parçası değildir, script kendi oluşturmaktadır ve giriş bilgilerinizi burada depolar. """, "\n" * 3)

            elif(islem_no == 8):
                break

            else:
                print("Geçerli bir işlem gir! ", "\n" * 3)

        except:
            print("Bir şeyleri yanlış yaptın!", "\n" * 3)
