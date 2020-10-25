

from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render,redirect
from ORS.utility.DataValidator import DataValidator
from service.models import Subject
from service.forms import SubjectForm
from service.service.SubjectService import SubjectService
from service.service.CollegeService import CollegeService


class SubjectCtl(BaseCtl):
 
    def preload(self,request):
        self.page_list = CollegeService().search(self.form)
        self.preload_data=self.page_list

    #     #Populate Form from HTTP Request 
    def request_to_form(self,requestForm):
        self.form["id"]  = requestForm["id"]
        self.form["subjectName"] = requestForm["subjectName"]
        self.form["subjectDescription"] = requestForm["subjectDescription"]
        self.form["dob"] = requestForm["dob"]
        self.form["course_ID"] = requestForm["course_ID"]
        self.form["courseName"] = requestForm["courseName"]
        # self.form["college_ID"] = requestForm["college_ID"]
        # self.form["collegeName"] = requestForm["collegeName"]

    #Populate Form from Model 
    def model_to_form(self,obj):
        if (obj == None):
            return
        self.form["id"]  = obj.id
        self.form["subjectName"] =obj.subjectName
        self.form["subjectDescription"] = obj.subjectDescription
        self.form["dob"] =obj.dob
        self.form["course_ID"] =obj.course_ID
        self.form["courseName"] =obj.courseName
        # self.form["college_ID"] = obj.college_ID
        # self.form["collegeName"] = obj.collegeName

    #Convert form into module
    def form_to_model(self,obj):
        pk = int(self.form["id"])
        if(pk>0):
            obj.id = pk
        obj.firstName=self.form["subjectName"]
        obj.subjectDescription=self.form["subjectDescription"] 
        obj.dob=self.form["dob"] 
        obj.course_ID=self.form["course_ID"] 
        obj.courseName=self.form["courseName"] 
        # obj.college_ID=self.form["college_ID"] 
        # obj.collegeName=self.form["collegeName"] 
        return obj

    #Validate form 
    def input_validation(self):
        super().input_validation()
        inputError =  self.form["inputError"]
        if(DataValidator.isNull(self.form["subjectName"])):
            inputError["subjectName"] = " subjectName can not be null"
            self.form["error"] = True

        if(DataValidator.isNull(self.form["subjectDescription"])):
            inputError["subjectDescription"] = "subjectDescription can not be null"
            self.form["error"] = True

        if(DataValidator.isNull(self.form["dob"])):
            inputError["dob"] = "dob can not be null"
            self.form["error"] = True

        if(DataValidator.isNull(self.form["course_ID"])):
            inputError["course_ID"] = "course_ID can not be null"
            self.form["error"] = True

        if(DataValidator.isNull(self.form["courseName"])):
            inputError["courseName"] = "courseName can not be null"
            self.form["error"] = True

        # if(DataValidator.isNull(self.form["college_ID"])):
        #     inputError["college_ID"] = "college_ID can not be null"
        #     self.form["error"] = True

        # if(DataValidator.isNull(self.form["collegeName"])):
        #     inputError["collegeName"] = "college_Name can not be null"
        #     self.form["error"] = True

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
        r = self.form_to_model(Subject())
        self.get_service().save(r)
        self.form["id"] = r.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        res = render(request,self.get_template(),{"form":self.form})
        return res
        
    # Template html of Student page    
    def get_template(self):
        return "ORS/Subject.html"          

    # Service of Student     
    def get_service(self):
        return SubjectService()        
