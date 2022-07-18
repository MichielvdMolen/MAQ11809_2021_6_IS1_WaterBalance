from IPython.display import Image

import os
teacher_dir  = os.getenv('TEACHER_DIR')
imgpath = teacher_dir + '/JHL_data/pictures/'
   
def check_my_answer_ISa1_1(x, y, z):
        if x == 'does not' and y == 'do' and z == 'winter':
            print('Hoera! Your answer is correct! Today, we will play a new game: Guess the famous picture and connect it to our Integration skills!')
            print('\033[1m' + 'Feedback:' + '\033[0m', 'The Veenkampen meteorological station does not really experience wetter and drier seasons. We can see this in the figure if we look at the change of precipitation in time. We cannot definitely state that every summer we have less precipitation and that every winter we have more. Still, we may expect that the forum ponds will be filled better in the winter than in spring. Why do you think so?')
            display(Image(filename= imgpath + "fig_mon1.jpg", width=300, height=300))
            return True
        else:
            print('Your answer is not correct. Please, try again!')
            if x != 'does not'              : print('x  is incorrect')
            if y != 'do'                    : print('y  is incorrect')
            if z != 'winter'                : print('z  is incorrect')    
            return False

def check_my_answer_ISa2_1(x, y1, y2, z, q1, q2):
        if x == 'do not' and y1 == 'constant' and y2 == 'precipitation' and z == ('2014/2015', '2015/2016', '2017/2018', '2019/2020') and q1 == 'August' and q2 == 'a':
            print('Hoera! Your answer is correct! Do you already know which picture this is and who the painter is?')
            print('\033[1m' + 'Feedback:' + '\033[0m', 'The same as the precipitation, here we do not observe a seasonal cycle in the water volume. This is not surprising, since the water volume in this simple setup depends only on the precipitation as we assigned evaporation ond Q-terms to have constant values. The pond will be filled up to the rim during several winters: 2014/2015, 2015/2016, 2017/2018 and 2019/2020. During year 2021 and up to 2022, the pond seems to be filled up to the rim on couple of occasions; first in August and then at the end of the year. However, it is not fully clear what happend at the turn of the year (as it is e.g., during 2015/2016). We can say with certainly that the pond is filled with water during August (starting already in July). This happend due to the accumulated rain (see figure for precipitation). Although the rain is not as high as in some other years (see end of 2017-2018), it is its accumulated amount through all year (starting in March) that maked the water in the pond to be filled up to the rim during August.')
            display(Image(filename= imgpath + "fig_mon2.jpg", width=350, height=350))
            return True
        else:
            print('Your answer is not correct. Please, try again!')
            if x  != 'do not'                : print('x  is incorrect')
            if y1 != 'constant'              : print('y1 is incorrect')
            if y2 != 'precipitation'         : print('y2 is incorrect')    
            if '2014/2015' in z              : print('2014/2015 is correct')  
            if '2015/2016' in z              : print('2015/2016 is correct')
            if '2017/2018' in z              : print('2017/2018 is correct')  
            if '2019/2020' in z              : print('2019/2020 is correct')   
            if q1 != 'August'                : print('q1 is incorrect')  
            if q2 != 'a'                     : print('q2 is incorrect')           
            return False
        
def check_my_answer_ISa3_1(x, y, z, u1, u2):
        if x == 'more' and y == ('a', 'b', 'c') and z == 'less' and u1 == ('2018/2019', '2020/2021') and u2 == 'Makkink':
            print('Hoera! Your answer is correct! Still not?')
            print('\033[1m' + 'Feedback:' + '\033[0m', 'Increasing the complexity of our model (i.e., using more realistic evaporation rate) we obtain more realistic simulation of water volume in the pond. Looking at the equation for the evaporation rate, we can see that it depends on the changes in global radiation, saturation water pressure deficit, and atmospheric temperature. Compared to the simple method, here using Makkink method, we can see that the periodic change in the water volume is much more pronounced, and that apart from two winters (2018/2019 and 2020/2021) all winters show the full pond.')
            display(Image(filename= imgpath + "fig_mon3.jpg", width=400, height=400))
            return True
        else:
            print('Your answer is not correct. Please, try again!')
            if x  != 'more'                    : print('x  is incorrect')
            if 'a' in y                        : print('a  is correct')  
            if 'b' in y                        : print('b  is correct')
            if 'c' in y                        : print('c  is correct')  
            if z  != 'less'                    : print('z  is incorrect')  
            if '2018/2019' in u1               : print('2018/2019 is correct')
            if '2020/2021' in u1               : print('2020/2021 is correct')    
            if u2 != 'Makkink'                 : print('u2 is incorrect')
            return False   
        
def check_my_answer_ISa4_1(x, y1, y2):
        if x == 'last' and y1 == 500 and y2 == 1000:
            print('Hoera! Your answer is correct! Almost there!')
            print('\033[1m' + 'Feedback:' + '\033[0m', 'The figure shows that in the first several years the volume does not change during winter when we use the real method, i.e., using realistic values for Q-terms. After 2016, real volume V_real is on average 500 m3 lower compared to the V_mak, and after 2019 it is more than 1000 m3 lower. Which Q-terms are dominant and influence this result we will investigate in the sensitivity study in the next section.')
            display(Image(filename= imgpath + "fig_mon4.jpg", width=450, height=450))
            return True
        else:
            print('Your answer is not correct. Please, try again!')
            if x  != 'last'                    : print('x  is incorrect')
            if y1 != 500                       : print('y1 is incorrect')
            if y2 != 1000                      : print('y2 is incorrect')
            return False        
        
def check_my_answer_ISa5_1(x1, x2, y, z, u):
        if x1 == 'is' and x2 == 2 and y == 'does not' and z == 3 and u == ('vertical inflow'):
            print('Hoera! Your answer is correct! You probably guessed it right: It is Monets Water lilies! In the integration skills 2 we will look at the water quality and as such we will look at the possible development of algae in the Forum ponds!')
            print('\033[1m' + 'Feedback:' + '\033[0m', 'When we change the initial volume by 10%, we can see that the model is sensitive to its change, but this change happens only in the first 2 years of the integration. After that, the initial volume has no influence on the final water volume of the pond. The model does not show sensitivity to changes in the lateral inflow. We would need to reduce the lateral inflow by 30% to see some small changes after 2019. To analyse which variable has the highest influence on the water volume of the pond we can change the lateral inflow, vertical inflow and outflow, and initial volume. When we change each variable separately by 10%, we can see that vertical inflow is the most sensitive variable in the model.')
            display(Image(filename= imgpath + "fig_mon5.jpg", width=500, height=500))
            return True
        else:
            print('Your answer is not correct. Please, try again!')
            if x1 != 'is'                      : print('x1 is incorrect')
            if x2 != 2                         : print('x2 is incorrect')
            if y  != 'does not'                : print('y  is incorrect')
            if z  != 3                         : print('z  is incorrect') 
            if 'vertical inflow' in u          : print('vertical inflow is correct')   
            return False        
                