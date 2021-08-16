# proj-fot
#mbarat korat 9dam

# l3nasir ta3 kol grop
# l3nasir ta3 kol grop
# l3nasir ta3 kol grop
# l3nasir ta3 kol grop
import time
class tornwa:

    def __init__(self,name_the_grop, name, proname, age, tool, wazn, spead, mharat):
        self.name_the_grop = name_the_grop
        self.name = name
        self.proname = proname
        self.age = age
        self.tool = tool
        self.wazn = wazn
        self.spead = spead
        self.mharat = mharat




    def printobje(self):


        print(self.name_the_grop,self.name, self.proname, self.age, self.tool, self.wazn, self.spead, self.mharat)


class grop_a(tornwa):
    def __init__(self,name_the_grop, name, proname, age, tool, wazn, spead, mharat):
        super().__init__(name_the_grop,name, proname, age, tool, wazn, spead, mharat)




    def printobje1(self):
        print(self.name_the_grop, self.name, self.proname, self.age, self.tool, self.wazn, self.spead, self.mharat)










class grop_b(tornwa):
    def __init__(self,name_the_grop, name, proname, age, tool, wazn, spead, mharat):
        super().__init__(name_the_grop,name, proname, age, tool, wazn, spead, mharat)



    def printobje2(self):
        print(self.name_the_grop, self.name, self.proname, self.age, self.tool, self.wazn, self.spead, self.mharat)

class grop_c(tornwa):
    def __init__(self,name_the_grop, name, proname, age, tool, wazn, spead, mharat):
        super().__init__(name_the_grop,name, proname, age, tool, wazn, spead, mharat)

    def printobje3(self):
        print(self.name_the_grop, self.name, self.proname, self.age, self.tool, self.wazn, self.spead, self.mharat)

class grop_d(tornwa):
    def __init__(self,name_the_grop, name, proname, age, tool, wazn, spead, mharat):
        super().__init__(name_the_grop,name, proname, age, tool, wazn, spead, mharat)

    def printobje4(self):
        print(self.name_the_grop, self.name, self.proname, self.age, self.tool, self.wazn, self.spead, self.mharat)

class grop_e(tornwa):
    def __init__(self,name_the_grop, name, proname, age, tool, wazn, spead, mharat):
        super().__init__(name_the_grop,name, proname, age, tool, wazn, spead, mharat)

    def printobje5(self):
        print(self.name_the_grop, self.name, self.proname, self.age, self.tool, self.wazn, self.spead, self.mharat)


class grop_f(tornwa):
    def __init__(self,name_the_grop, name, proname, age, tool, wazn, spead, mharat):
        super().__init__(name_the_grop,name, proname, age, tool, wazn, spead, mharat)

    def printobje6(self):
        print(self.name_the_grop, self.name, self.proname, self.age, self.tool, self.wazn, self.spead, self.mharat)



class grop_g(tornwa):
    def __init__(self,name_the_grop, name, proname, age, tool, wazn, spead, mharat):
        super().__init__(name_the_grop,name, proname, age, tool, wazn, spead, mharat)

    def printobje7(self):
        print(self.name_the_grop, self.name, self.proname, self.age, self.tool, self.wazn, self.spead, self.mharat)



class grop_h(tornwa):
    def __init__(self, name_the_grop,name, proname, age, tool, wazn, spead, mharat):
        super().__init__(name_the_grop,name, proname, age, tool, wazn, spead, mharat)

    def printobje8(self):
        print(self.name_the_grop, self.name, self.proname, self.age, self.tool, self.wazn, self.spead, self.mharat)



a_1 = grop_a('group a : ','mouh','kiran','23 ans','1.70','55 kg','30 k/h','gardiyan')
a_2 = grop_a('group a : ','hmani','sino','20 ans','1.65','65 kg','35 k/h','difonsor')
a_3 = grop_a('group a : ','bladn','hdad','22 ans','1.75','70 kg','50 k/h','difonsor')
a_4 = grop_a('group a : ','oussama','ben','25 ans','1.81','65 kg','50 k/h','atac')
a_5 = grop_a('group a : ','foad','asas','23 ans','1.85','70 kg','35 k/h','atac')

time.sleep(1)

a_1.printobje1()
a_2.printobje1()
a_3.printobje1()
a_4.printobje1()
a_5.printobje1()






print('=================================================================================')

b_1 = grop_b('group b : ','jems','mirana','30 ans','1.70','75 kg','30 k/h','gardiyan')
b_2 = grop_b('group b : ','hosin','kino','22 ans','1.65','65 kg','35 k/h','difonsor')
b_3 = grop_b('group b : ','kiran','hdad','22 ans','1.75','70 kg','50 k/h','difonsor')
b_4 = grop_b('group b : ','santa','ben','25 ans','1.81','65 kg','50 k/h','atac')
b_5 = grop_b('group b : ','foad','asas','23 ans','1.85','70 kg','35 k/h','atac')

time.sleep(1)
b_1.printobje2()
b_2.printobje2()
b_3.printobje2()
b_4.printobje2()
b_5.printobje2()



print('=================================================================================')

c_1 = grop_c('group c : ','	Xavi','kino','30 ans','1.70','75 kg','30 k/h','gardiyan')
c_2 = grop_c('group c : ','hosin','kino','22 ans','1.65','65 kg','35 k/h','difonsor')
c_3 = grop_c('group c : ','kiran','hdad','22 ans','1.75','70 kg','50 k/h','difonsor')
c_4 = grop_c('group c : ','santa','ben','25 ans','1.81','65 kg','50 k/h','atac')
c_5 = grop_c('group c : ','foad','asas','23 ans','1.85','70 kg','35 k/h','atac')

time.sleep(1)
c_1.printobje3()
c_2.printobje3()
c_3.printobje3()
c_4.printobje3()
c_5.printobje3()

print('=================================================================================')

d_1 = grop_d('group d : ','jems','mirana','30 ans','1.70','75 kg','30 k/h','gardiyan')
d_2 = grop_d('group d : ','hosin','kino','22 ans','1.65','65 kg','35 k/h','difonsor')
d_3 = grop_d('group d : ','kiran','hdad','22 ans','1.75','70 kg','50 k/h','difonsor')
d_4 = grop_d('group d : ','santa','ben','25 ans','1.81','65 kg','50 k/h','atac')
d_5 = grop_d('group d : ','foad','asas','23 ans','1.85','70 kg','35 k/h','atac')

time.sleep(1)
d_1.printobje4()
d_2.printobje4()
d_3.printobje4()
d_4.printobje4()
d_5.printobje4()


print('===================================== : First round : ============================================')


# hna kol grop ch7al mn bit ymarki

class mjmo3a_1:
    def bit(self):

        grop_a = int(input('grop A - enter yor bit : '))

        time.sleep(1)
        grop_b = int(input('grop B - enter yor bit : '))


        if grop_a > grop_b:

            print(' Team A , Team B Winner ')
        elif grop_b > grop_a:
      
            print(' Team B , Team A Winner ')
            print('goop A = ', grop_a, ' : ', 'grop B = ', grop_b)

        elif grop_a == grop_b:

            while True:
                grop_a = int(input('grop A - enter yor bit : '))

                grop_b = int(input('grop B - enter yor bit : '))

                if grop_a > grop_b:
                    print(' Team A , Team B Winner ')
                elif grop_a < grop_b:
                    print(' Team B , Team A Winner ')
                    break


        grop_c = int(input('grop C - enter yor bit : '))

        time.sleep(1)
        grop_d = int(input('grop D - enter yor bit : '))



        if grop_c > grop_d:
            print(' Team C , Team D Winner ')
        elif grop_d > grop_c:
            print(' Team D , Team C  Winner ')
            print('goop C = ',grop_c,' : ','grop D = ',grop_d)

        elif grop_c == grop_d:
            while True:
                grop_c = int(input('grop C - enter yor bit : '))

                grop_d = int(input('grop D - enter yor bit : '))

                if grop_c > grop_d:
                    print(' Team C , Team D Winner ')
                elif grop_c < grop_d:
                    print(' Team D , Team C Winner ')
                    break






        list = ['grop A ', grop_a, 'grop B ', grop_b, 'grop c ', grop_c, 'grop D ', grop_d]
        print(list)
        print('===================================== : Finale : ============================================')
        if grop_a > grop_b and grop_c > grop_d:
            time.sleep(1)
            a = input('entr bit grop  A : ')
            time.sleep(1)
            c = input(('enter bit grop C : '))
            print('grop A : ',a,'\t','grop C : ',c)
            if a > c:
                time.sleep(1)
                print(' ************* grop A win a finale ************* : ',a)
            else:
                time.sleep(1)
                print(' ************* grop C win a finale ************* : ',c)

        elif grop_b > grop_a and grop_c > grop_d:
            time.sleep(1)
            b = input('entr bit grop  B : ')
            time.sleep(1)
            c = input(('enter bit grop  C : '))
            print('grop B : ',b,'\t','grop C : ',c)
            if b > c:
                time.sleep(1)
                print(' ************* grop B win a finale ************* : ',b)
            else:
                time.sleep(1)
                print(' ************* grop C win a finale ************* : ',c)


        elif grop_a > grop_b and grop_d > grop_c:
            time.sleep(1)
            a = input('entr bit grop A : ')
            time.sleep(1)
            d = input(('enter bit grop  D : '))
            print('grop A : ',a,'\t','grop D : ',d)
            if a > d:
                time.sleep(1)
                print(' ************* grop A win a finale ************* : ',a)
            else:
                time.sleep(1)
                print(' ************* grop D win a finale ************* : ',d)
        elif grop_b > grop_a and grop_d > grop_c:
            time.sleep(1)
            b = input('entr bit grop B : ')
            time.sleep(1)
            d = input(('enter bit grop D : '))
            print('grop B : ',b,'\t','grop D : ',d)
            if b > d:
                time.sleep(1)
                print(' ************* grop B win a finale ************* : ',b)
            else:
                time.sleep(1)
                print(' ************* grop D win a finale ************* : ',d)



pos = mjmo3a_1()
pos.bit()
