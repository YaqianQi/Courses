import re
import pandas as pd
class PdfDefinitionExtractor:

    def __init__(self, token_list):
        self.token_list = token_list

    def match_term_with_explanation(self, terms):
        test_t = self.token_list
        res = terms
        adjust_content = ["invalid"]
        adjust_content = test_t + adjust_content
        adjust_content = adjust_content[1:]
        res['content'] = adjust_content
        return res

    def catch_term(self):
        terms = []
        for i in range(len(self.token_list)):
            s_list = self.token_list[i]
            try:
                term1 = self.find_glossary_term_back(s_list)
            except:
                term1 = "-1"
            try:
                term2 = self.find_last_string_with_comma_started(s_list)
            except:
                term2 = self.search_no_parenthesis_pattern(s_list)
            try:
                term3 = self.find_the_last_string(s_list.split())
            except:
                term3 = "-1"
            term = [term1, term2, term3]
            terms.append(term)
        terms = pd.DataFrame(terms)
        res = pd.concat([terms], axis=1)
        res.columns = ['TERM1', 'TERM2', 'TERM3']
        output = self.match_term_with_explanation(res)
        return output

    @staticmethod
    def find_glossary_term_back(s_list):
        start = len(s_list) - 1
        end = start
        res = ''
        for i in range(len(s_list) - 1, 0, -1):
            if s_list[i] == '"':
                start = i
                end = start+1
                while (end > 0 and s_list[end] != '"'):
                    end -= 1
            if s_list[i] == ".":
                res = s_list[end:len(s_list) - 1]
                break
        return res
    @staticmethod
    def find_last_string_with_comma_started(s_list):
        start_pos = [m.start() for m in re.finditer('. "', s_list)]
        res = s_list[start_pos[0]+2:]
        return res
    @staticmethod
    def search_no_parenthesis_pattern(s_list):
        term = ""
        if '. ' in s_list:
            term = s_list.split('. ')[1].strip()
        else:
            if len(s_list.split()) < 4:
                term = s_list.strip()
        return term
        
    def find_the_last_string(self, list_text):
        temp = ""
        idx = len(list_text)-1
        start = '"'
        end = '"'

        while idx >= 0:
            if list_text[idx].endswith(end):
                temp += list_text[idx]
                while(idx - 1 >= 0  and list_text[idx].startswith(start) is not True):
                    idx -= 1
                    temp = temp + " "+  list_text[idx]
            if temp != "":
                return self.reverse(temp)
            idx -= 1
        return str(-1)

    @staticmethod
    def reverse(input_string):
        out_str = ""
        for i in input_string.split():
            out_str = i + " " + out_str
        return out_str