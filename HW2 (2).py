# HW2
#Due Date: 06/13/2021, 11:59PM

import random

class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
    def __init__(self, cid, cname, credits):
        self.cid=cid
        self.cname=cname
        self.credits=credits
        pass


    def __str__(self):
        cid=self.cid
        credits=self.credits
        cname=self.cname
        return ('{}({}): {}'.format(cid,credits,cname))
        pass

    __repr__ = __str__

    def __eq__(self, other):
        if isinstance(other,Course):
            if self.cid==other.cid:
                return True
            else:
                return False
        else:
            return False
        pass



class Catalog:
    ''' 
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.courseOfferings
        {'CMPSC132': CMPSC132(3): Programming in Python II, 'CMPSC360': CMPSC360(3): Discrete Mathematics}
        >>> C.removeCourse('CMPSC360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC132': CMPSC132(3): Programming in Python II}
        >>> isinstance(C.courseOfferings['CMPSC132'], Course)
        True
    '''
    def __init__(self):
        self.courseOfferings={}
        pass

    def addCourse(self, cid, cname, credits):
        self.cid=cid
        self.cname=cname
        self.credits=credits
        self.course=Course(self.cid,self.cname,self.credits)
        if self.cid in self.courseOfferings.keys():
            return 'Course already added'
        else:
            
            self.courseOfferings[self.cid]=self.course
            return 'Course added successfully'
        pass

    def removeCourse(self, cid):
        if self.cid in self.courseOfferings.keys():
            self.courseOfferings.pop(self.cid)
            return 'Course removed successfully'
        else:
            return 'Course not found'
        pass


class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> semester = Semester(1)
        >>> semester
        No courses
        >>> semester.addCourse(cmpsc132)
        >>> isinstance(semester.courses['CMPSC132'], Course)
        True
        >>> semester.addCourse(math230)
        >>> semester
        CMPSC132, MATH 230
        >>> semester.isFullTime
        False
        >>> semester.totalCredits
        7
        >>> semester.addCourse(phys213)
        >>> semester.addCourse(econ102)
        >>> semester.addCourse(econ102)
        'Course already added'
        >>> semester.addCourse(phil119)
        >>> semester.isFullTime
        True
        >>> semester.dropCourse(phil119)
        >>> semester.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> semester.totalCredits
        16
        >>> semester.dropCourse(cmpsc131)
        'No such course'
        >>> semester.courses
        {'CMPSC132': CMPSC132(3): Programming in Python II, 'MATH 230': MATH 230(4): Calculus, 'PHYS 213': PHYS 213(2): General Physics, 'ECON 102': ECON 102(3): Intro to Economics, 'JAPNS 001': JAPNS 001(4): Japanese I}
    '''

    def __init__(self, sem_num):
        self.sem_num=sem_num
        self.courses={}
        pass



    def __str__(self):
        if len(self.courses)==0:
            return 'No courses'
        else:
            blankstr=''
            for course in self.courses:
                blankstr+=course
                blankstr+=', '
            if blankstr[-2]==',':
                return blankstr[:(len(blankstr))-2]
            else:
                return blankstr
        pass

    __repr__ = __str__

    def addCourse(self, course):
        if isinstance(course,Course):
            if course.cid in self.courses.keys():
                return 'Course already added'
            else:
                self.courses[course.cid]=course
        pass

    def dropCourse(self, course):
        if isinstance(course,Course):
            if course.cid in self.courses.keys():
                self.courses.pop(course.cid)
            else:
                return 'No such course'
        pass

    @property
    def totalCredits(self):
        self.count=0
        for course in self.courses.values():
            self.count+=course.credits
        return self.count
        pass

    @property
    def isFullTime(self):
        if self.totalCredits>=12:
            return True
        else:
            return False
        pass

    
class Loan:
    '''
        >>> import random
        >>> random.seed(2)  # Setting seed to a fixed value, so you can predict what numbers the random module will generate
        >>> first_loan = Loan(4000)
        >>> first_loan
        Balance: $4000
        >>> first_loan.loan_id
        17412
        >>> second_loan = Loan(6000)
        >>> second_loan.amount
        6000
        >>> second_loan.loan_id
        22004
        >>> third_loan = Loan(1000)
        >>> third_loan.loan_id
        21124
    '''
    

    def __init__(self, amount):
        self.amount=amount
        
        self.loan_id=self.__getloanID
        pass


    def __str__(self):
        return ('Balance: ${}'.format(self.amount))
        pass

    __repr__ = __str__


    @property
    def __getloanID(self):
        return (random.randint(10000,99999))
        pass


class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

    def __init__(self, name, ssn):
        self.name=name
        self.ssn=ssn
        pass

    def __str__(self):
        return ('Person({}, ***-**-{})'.format(self.name,self.ssn[7:11]))
        pass

    __repr__ = __str__

    def get_ssn(self):
        return self.ssn
        pass

    def __eq__(self, other):
        if isinstance(other,Person):
            if self.ssn== other.ssn:
                return True
            else:
                return False
        pass

class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> st1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC360', C, 1)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC132}
    '''
    def __init__(self, name, ssn, supervisor=None):
        super().__init__(name,ssn)
        self.supervisor=supervisor
        pass


    def __str__(self):
        return ('Staff({}, {})'.format(self.name,self.id))
        pass

    __repr__ = __str__


    @property
    def id(self):
        self.supervisorid='905'
        namelst=self.name.split()
        
        for word in namelst:
            self.supervisorid+=word[0]
            
        self.supervisorid+=self.ssn[7:11]
        
        return self.supervisorid.lower()
        pass

    @property   
    def getSupervisor(self):
        return self.supervisor
        pass

    def setSupervisor(self, new_supervisor):
        if isinstance(new_supervisor,Staff):
            self.supervisor=new_supervisor
            
            return 'Completed!'
        pass


    def applyHold(self, student):
        if isinstance(student,Student):
            student.hold=True
            return 'Completed!'
        pass

    def removeHold(self, student):
        if isinstance(student,Student):
            student.hold=False
            return 'Completed!'
        pass

    def unenrollStudent(self, student):
        if isinstance(student,Student):
            student.active=False
            return 'Completed!'
        pass




class Student(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC311', C, 1)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132, CMPSC360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC132', C, 1)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC360')
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC360')
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: No courses}
        >>> s1.enrollCourse('CMPSC360', C, 2)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
    '''
    def __init__(self, name, ssn, year):
        random.seed(1)
        self.year=year
        super().__init__(name,ssn)
        self.semesters={}
        self.active=True
        self.hold=False
        self.account=self.__createStudentAccount()


    def __str__(self):
        return ('Student({}, {}, {})'.format(self.name,self.id,self.year))
        pass

    __repr__ = __str__

    def __createStudentAccount(self):
        if self.active==True:
            StudentAccount(self)
        else:
            return None
                
        pass


    @property
    def id(self):
        self.studentid=''
        namelst=self.name.split()
        for word in namelst:
            self.studentid+=word[0]
        self.studentid+=self.ssn[7:11]
        return self.studentid.lower()
        pass

    def registerSemester(self):
        if self.year=='Freshman':
            self.currentsem=1
        if self.hold==False or self.active==True:
            self.semesters[self.currentsem]+=Semester(self.currentsem)
        else:
            return 'Unsuccessful operation'
        self.currentsem+=1

        if len(self.semesters.keys())>2:
            self.year='Sophomore'
        if len(self.semesters.keys())>4:
            self.year='Junior'
        if len(self.semesters.keys())>6:
            self.year='Senior'
        
        pass



    def enrollCourse(self, cid, catalog, semester):
        if self.hold==False or self.active==True:
            if cid in catalog.courseOfferings.keys():
                if catalog.courseOfferings not in self.semesters.values():
                    self.semesters[semester].addCourse(catalog.courseOfferings[cid])
                    self.account.balance+=(self.account.ppc*catalog.courseOfferings[cid].credits)
                else:
                    return 'Course already enrolled'
            else:
                return 'Course not found'
        else:
            return 'Unsuccessful operation'
            
        pass

    def dropCourse(self, cid):
        if self.hold==False or self.active==True:
            if cid in self.semesters.values():
                self.semesters.dropCourse(catalog.courseOfferings[cid])
                self.account.balance-=(self.account.ppc/2)*catalog.courseOfferings[cid].credits
            else:
                return 'Course not found'
        else:
            return 'Unsuccessful operation'
        pass

    def getLoan(self, amount):
        if self.active is not True or self.hold is True:
            return 'Unsuccessful operation'
        if self.semesters.isFullTime is not True:
            return 'Not full-time'
        else:
            self.Loan(amount)
        pass




class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2)
        'Course added successfully'
        >>> C.addCourse('CMPEN270', 'Digital Design', 4)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN270', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.dropCourse('CMPEN270')
        'Course dropped successfully'
        >>> s1.account.balance
        1900.0
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
        >>> StudentAccount.CREDIT_PRICE = 1500
        >>> s2 = Student('Thomas Wang', '123-45-6789', 'Freshman')
        >>> s2.registerSemester()
        >>> s2.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s2.account.balance
        4500
        >>> s1.enrollCourse('CMPEN270', C,1)
        'Course added successfully'
        >>> s1.account.balance
        7900.0
    '''
    
    def __init__(self, student):
        self.student=student
        self.balance=0
        ppc=1000
        self.loans={}
        pass


    def __str__(self):
        return ('Name: {}\nID: {}\nBalance: ${}'.format(self.student.name,self.student.id,self.balance))
        pass

    __repr__ = __str__


    def makePayment(self, amount):
        self.balance=-amount
        return self.balance
        pass


    def chargeAccount(self, amount):
        self.balance+=amount
        return self.balance
        pass





####################### STAND ALONE FUNCTION ###############################################

def createStudent(person):
    """
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> s1 = createStudent(p)
        >>> s1
        Student(Jason Smith, js2629, Freshman)
        >>> isinstance(s1, Student)
        True
        >>> s1.getLoan(4000)
        'Not full-time'
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2)
        'Course added successfully'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC360', C,1)
        'Course added successfully'
        >>> s1.getLoan(4000)
        'Not full-time'
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> s1.getLoan(4000)
        >>> s1.account.loans
        {27611: Balance: $4000}
        >>> s1.getLoan(6000)
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $6000}
    """
    if isinstance(person,Person):
        return Student(person.name,person.get_ssn(),"Freshman")
    pass


#############################################################################################

if __name__=='__main__':
    import doctest
    doctest.testmod()     # Uncomment this line to run all doctest
    doctest.run_docstring_examples(Course, globals(), name='HW1',verbose=True)   # Replace Course with the name of the class you want to run its doctest
