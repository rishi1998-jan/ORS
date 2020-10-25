

from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render
from ORS.utility.DataValidator import DataValidator
from service.models import TimeTable
from service.forms import TimeTableForm
from service.service.TimeTableService import TimeTableService
from service.service.CollegeService import CollegeService

class TimeTableCtl(BaseCtl):
    def preload(self,request):
        self.page_list = CollegeService().search(self.form)
        self.preload_data=self.page_list

        #Populate Form from HTTP Request 
    def request_to_form(self,requestForm):
        self.form["id"]  = requestForm["id"]
        self.form["examTime"] = requestForm["examTime"]
        self.form["examDate"] = requestForm["examDate"]
        self.form["subject_ID"] = requestForm["subject_ID"]
        self.form["subjectName"] = requestForm["subjectName"]
        self.form["course_ID"] = requestForm["course_ID"]
        self.form["courseName"] = requestForm["courseName"]
        self.form["semester"] = requestForm["semester"]

    #Populate Form from Model 
    def model_to_form(self,obj):
        if (obj == None):
            return
        self.form["id"]  = obj.id
        self.form["examTime"] =obj.examTime
        self.form["examDate"] = obj.examDate
        self.form["subject_ID"] =obj.subject_ID
        self.form["subjectName"] =obj.subjectName
        self.form["course_ID"] =obj.course_ID
        self.form["courseName"] = obj.courseName
        self.form["semester"] = obj.semester

    #Convert form into module
    def form_to_model(self,obj):
        pk = int(self.form["id"])
        if(pk>0):
            obj.id = pk
        obj.examTime=self.form["examTime"]
        obj.examDate=self.form["examDate"] 
        obj.subject_ID=self.form["subject_ID"] 
        obj.subjectName=self.form["subjectName"] 
        obj.course_ID=self.form["course_ID"] 
        obj.courseName=self.form["courseName"] 
        obj.semester=self.form["semester"] 
        return obj

    #Validate form 
    def input_validation(self):
        super().input_validation()
        inputError =  self.form["inputError"]
        if(DataValidator.isNull(self.form["examTime"])):
            inputError["examTime"] = " examTime can not be null"
            self.form["error"] = True

        if(DataValidator.isNull(self.form["examDate"])):
            inputError["examDate"] = "examDate can not be null"
            self.form["error"] = True

        if(DataValidator.isNull(self.form["subject_ID"])):
            inputError["subject_ID"] = "subject_ID can not be null"
            self.form["error"] = True

        if(DataValidator.isNull(self.form["subjectName"])):
            inputError["subjectName"] = "subjectName can not be null"
            self.form["error"] = True

        if(DataValidator.isNull(self.form["course_ID"])):
            inputError["course_ID"] = "course_ID can not be null"
            self.form["error"] = True

        if(DataValidator.isNull(self.form["courseName"])):
            inputError["courseName"] = "courseName can not be null"
            self.form["error"] = True

        if(DataValidator.isNull(self.form["semester"])):
            inputError["semester"] = "semester can not be null"
            self.form["error"] = True

        return self.form["error"]        

    #Display Marksheet page 
    def display(self,request,params={}):
        if( params["id"] > 0):
            r = self.get_service().get(params["id"])
            self.model_to_form(r)
        res = render(request,self.get_template(), {"form":self.form,"collegeList":self.preload_data})
        return res

    #Submit Marksheet page
    def submit(self,request,params={}):
        r = self.form_to_model(TimeTable())
        self.get_service().save(r)
        self.form["id"] = r.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        res = render(request,self.get_template(),{"form":self.form})
        return res
        
    # Template html of Student page    
    def get_template(self):
        return "ors/TimeTable.html"          

    # Service of Student     
    def get_service(self):
        return TimeTableService()        



