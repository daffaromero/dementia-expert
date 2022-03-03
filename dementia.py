from experta import *
import ast


class DementiaOrNot(KnowledgeEngine):
    username = "", 

    @DefFacts()
    def InitialRun(self):        
        yield Fact(Diagnose = 'true')
        print("----DEMENTIA DIAGNOSIS SYSTEM----\nThis system will help you diagnose yourself or someone else for early signs of dementia.\n")
        print("Disclaimer: Please note that the diagnosis shown is not an officially licensed medical diagnosis, and may be inaccurate.\nPlease consult a doctor for further information regarding your condition.\n")
        print("We will now ask you a few questions.")
        
    @Rule(Fact(Diagnose = 'true'), NOT(Fact(name = W())), salience = 100)
    def PatientName(self):
        self.username = input("Please type in the patient's name.\n")
        self.declare(Fact(name=self.username)) 
        
    @Rule(Fact(Diagnose = 'true'), NOT(Fact(old = W())), salience = 90)
    def isOld(self):
        self.old = input("\nIs the patient over 65 years of age?\nType 'yes' or 'no'\n")
        self.old = self.old.lower()
        self.declare(Fact(old = self.old.strip().lower()))
    
    @Rule(Fact(Diagnose = 'true'), NOT(Fact(memory = W())), salience = 80)
    def hasMemoryIssues(self):
        self.memory = input("\nDoes the patient have a hard time remembering recent events?\nType 'yes' or 'no'\n")
        self.memory = self.memory.lower()
        self.declare(Fact(memory = self.memory.strip().lower()))

    @Rule(Fact(Diagnose = 'true'), NOT(Fact(difficulty = W())), salience = 70)
    def hasDifficulty(self):
        self.difficulty = input("\nDoes the patient have trouble carrying out some tasks, like cooking?\nType 'yes' or 'no'\n")
        self.difficulty = self.difficulty.lower()
        self.declare(Fact(difficulty = self.difficulty.strip().lower()))
        
    @Rule(Fact(Diagnose = 'true'), NOT(Fact(speaking = W())), salience = 60)
    def hasSpeakingIssues(self):
        self.speaking = input("\nDoes the patient have trouble finding words when speaking?\nType 'yes' or 'no'\n")
        self.speaking = self.speaking.lower()
        self.declare(Fact(speaking = self.speaking.strip().lower()))
        
    @Rule(Fact(Diagnose = 'true'), NOT(Fact(disorient = W())), salience = 50)
    def hasTimePlace(self):
        self.disorient = input("\nHas the patient been confused about where they are, which year they are in, and/or the time of day?\nType 'yes' or 'no'\n")
        self.disorient = self.disorient.lower()
        self.declare(Fact(disorient = self.disorient.strip().lower()))
        
    @Rule(Fact(Diagnose = 'true'), NOT(Fact(movement = W())), salience = 40)
    def hasMovement(self):
        self.movement = input("\nHas the patient had difficulty walking?\nType 'yes' or 'no'\n")
        self.movement = self.movement.lower()
        self.declare(Fact(movement = self.movement.strip().lower()))
        
    @Rule(Fact(Diagnose = 'true'), NOT(Fact(mood = W())), salience = 30)
    def hasMoodChanges(self):
        self.mood = input("\nHas the patient shown changes in mood?\nType 'yes' or 'no'\n")
        self.mood = self.mood.lower()
        self.declare(Fact(mood = self.mood.strip().lower()))
        
    @Rule(Fact(Diagnose = 'true'), NOT(Fact(thinking = W())), salience = 20)
    def hasThinking(self):
        self.thinking = input("\nHas the patient experienced difficulties with attention, planning, and reasoning?\nType 'yes' or 'no'\n")     
        self.thinking = self.thinking.lower()
        self.declare(Fact(thinking = self.thinking.strip().lower()))
        
    @Rule(Fact(Diagnose = 'true'), Fact(old = 'no'), Fact(memory = 'yes'), Fact(difficulty = 'yes'), Fact(speaking = 'yes'), Fact(disorient = 'yes'), Fact(movement = 'yes'), Fact(mood = 'yes'), Fact(thinking = 'yes'))
    def dementia_0(self):
        self.declare(Fact(disease = "Early-onset dementia: mixed dementia"))    
    
    @Rule(Fact(Diagnose = 'true'), Fact(old = 'yes'), Fact(memory = 'yes'), Fact(difficulty = 'yes'), Fact(speaking = 'yes'), Fact(disorient = 'yes'), Fact(movement = 'yes'), Fact(mood = 'yes'), Fact(thinking = 'yes'))
    def dementia_1(self):
        self.declare(Fact(disease = "Mixed dementia"))
        
    @Rule(Fact(Diagnose = 'true'), Fact(old = 'no'), Fact(memory = 'yes'), Fact(difficulty = 'yes'), Fact(speaking = 'yes'), Fact(disorient = 'yes'), Fact(movement = 'no'), Fact(mood = 'no'), Fact(thinking = 'no'))
    def dementia_2(self):
        self.declare(Fact(disease = "Early-onset Alzheimer's disease"))
    
    @Rule(Fact(Diagnose = 'true'), Fact(old = 'yes'), Fact(memory = 'yes'), Fact(difficulty = 'yes'), Fact(speaking = 'yes'), Fact(disorient = 'yes'), Fact(movement = 'no'), Fact(mood = 'no'), Fact(thinking = 'no'))
    def dementia_3(self):
        self.declare(Fact(disease = "Alzheimer's disease"))

    @Rule(Fact(Diagnose = 'true'), Fact(old = 'no'), Fact(memory = 'no'), Fact(difficulty = 'yes'), Fact(speaking = 'no'), Fact(disorient = 'yes'), Fact(movement = 'yes'), Fact(mood = 'yes'), Fact(thinking = 'yes'))
    def dementia_4(self):
        self.declare(Fact(disease = "Early-onset dementia: Vascular dementia"))
    
    @Rule(Fact(Diagnose = 'true'), Fact(old = 'yes'), Fact(memory = 'no'), Fact(difficulty = 'yes'), Fact(speaking = 'no'), Fact(disorient = 'yes'), Fact(movement = 'yes'), Fact(mood = 'yes'), Fact(thinking = 'yes'))
    def dementia_5(self):
        self.declare(Fact(disease = "Vascular dementia"))

    @Rule(Fact(Diagnose = 'true'), NOT (Fact(disease = W())), salience = -1)
    def unmatched(self):
        self.declare(Fact(disease = 'unknown'))
        
    @Rule(Fact(Diagnose = 'true'), Fact(disease = MATCH.disease), salience = 1)
    def getDisease(self, disease):
        
        if(disease == 'unknown'):
            conditionList = []
            conditionList.append('old')
            conditionList.append('memory')
            conditionList.append('difficulty')
            conditionList.append('speaking')
            conditionList.append('disorient')
            conditionList.append('movement')
            conditionList.append('mood')
            conditionList.append('thinking')
            #print('\n\nWe checked the following conditions:', conditionList)
            conditionList_val=[self.old,self.memory,self.difficulty,self.speaking,self.disorient,self.movement,self.mood,self.thinking]
            #print('\nNoted conditions in the patient are:', conditionList_val)
            
            file = open("conditions.txt", "r")
            contents = file.read()
            guide = ast.literal_eval(contents)
            file.close()
            
            yes_cond = []
            for i in range(0,len(conditionList_val)):
                if conditionList_val[i] == 'yes':
                    yes_cond.append(conditionList[i])
                    
            max_val = 0
            print('\nNoticed symptoms:', yes_cond)
            for key in guide.keys():
                val = guide[key].split(",")
                count = 0
                print(key,":",val)
                for x in val:
                    if x in yes_cond:
                        count+=1
                if count > max_val:
                    max_val = count
                    predict = key
            
            if max_val == 0:
                print("\nNo signs of dementia.")
            else:   
                print("\nWe are unable to tell you the exact disease with confidence.")
                print("There is a chance the patient might have:", predict)
                print("Please seek further advice from a doctor.")
        else:    
            print('\nWe have diagnosed the patient with:', disease)
            print("We suggest a visit to the doctor immediately.")

if __name__ == "__main__":
    engine = DementiaOrNot()
    engine.reset()
    engine.run()
    #print('Printing engine facts after 1 run',engine.facts)