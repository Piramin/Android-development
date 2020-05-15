import math
from kivy.app import App

from kivy.uix.pagelayout import PageLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior

def Klick(const_new):
    print(const_new)        
    set_screen('ksi_calculate')
    pass

#Функция, меняющая экран.
def set_screen(name_screen):
    sm.current = name_screen
        
#Класс основного экрана.    
class MainScreen(Screen):
    def __init__(self, **kw):
        super(MainScreen, self).__init__(**kw)

        bl = BoxLayout(orientation = 'vertical')
        with bl.canvas:
            Color(35/255,174/255,190/255,1)
            Rectangle(size=(Window.width, Window.height), pos=(0, 0)) #задний фон
            
        al_top = AnchorLayout(anchor_x = 'center',anchor_y = 'center')    
        al_top.add_widget(Label(text='Thermophysical \n     Calculator'))
        bl.add_widget(al_top)
        al_post = AnchorLayout(anchor_x = 'center',anchor_y = 'center')
        al_post.add_widget(Label(text='Development of MPEI. \nAll rights reserved. \n22.04.2020.'))
        bl.add_widget(al_post)
        bl.add_widget(Widget())
        
        gl = GridLayout(cols = 3,spacing = 3,padding = 5)
        gl.add_widget(Button(text='Miss',
                             size_hint=[.3, .15] ,
                             background_color = [16/255,84/255,91/255,1] ,
                             background_normal = '' ,
                             on_press = lambda x: 0))
        gl.add_widget(Button(text='Nusselt',
                             size_hint=[.3, .15] ,
                             background_color = [16/255,84/255,91/255,1] ,
                             background_normal = ''  ,
                             on_press = lambda x: set_screen('nu')))
        gl.add_widget(Button(text='Ksi',
                             size_hint=[.3, .15] ,
                             background_color = [16/255,84/255,91/255,1] ,
                             background_normal = ''  ,
                             on_press = lambda x: set_screen('ksi')))
        bl.add_widget(gl)
        self.add_widget(bl)        
        
class Val_Screen(Screen):
    const = 0    
    def __init__(self,text_val,**kw):
        super(Val_Screen, self).__init__(**kw)
        Num = 4
        self.const = 0
        with self.canvas:
            Color(35/255,174/255,190/255,1)
            Rectangle(size=(Window.width, Window.height), pos=(0, 0))        
        gl = GridLayout(cols = 1, rows = Num ,spacing = 5,padding = 5)

        formula = text_val+str(0)+'.jpg'
        gl.add_widget(Button(#text='Ksi',
                             #background_color = [16/255,84/255,91/255,1],
                             background_normal = formula,
                             on_press = lambda x: self.Klick(0,text_val) ))

        formula = text_val+str(1)+'.jpg'
        gl.add_widget(Button(#text='Ksi',
                             #background_color = [16/255,84/255,91/255,1],
                             background_normal = formula,
                             on_press = lambda x: self.Klick(1,text_val) ))

        formula = text_val+str(2)+'.jpg'
        gl.add_widget(Button(#text='Ksi',
                             #background_color = [16/255,84/255,91/255,1],
                             background_normal = formula,
                             on_press = lambda x: self.Klick(2,text_val) ))
        
        gl.add_widget(Button(text='Return to main page',
                             background_color = [16/255,84/255,91/255,1],
                             background_normal='',
                             on_press = lambda x: set_screen('main')))
        self.add_widget(gl)
    def Klick(self,const_new,text_val):
        self.const = const_new
        set_screen(text_val.lower()+'_calculate')
        pass
    
class ResultScreen(Screen):
    text = '0'    
    def __init__(self,text_val, **kw):
        super(ResultScreen, self).__init__(**kw)
        with self.canvas:
            Color(35/255,174/255,190/255,1)
            Rectangle(size=(Window.width, Window.height), pos=(0, 0))    
            
        self.lbl = Label(text = self.text)
        #self.update_label(text_val)
        
        bl = BoxLayout(orientation = 'vertical')
        
        gl = GridLayout(cols = 2, rows = 1 ,spacing = 5,padding = 5)
        gl.add_widget(Button(text='Return to'+'\n'+text_val+' page',
                             background_color = [16/255,84/255,91/255,1],
                             background_normal='',
                             on_press = lambda x: set_screen(text_val.lower())))
        gl.add_widget(Button(text='Return to\nmain page',
                             background_color = [16/255,84/255,91/255,1],
                             background_normal='',
                             on_press = lambda x: set_screen('main')))

        
        bl.add_widget(self.lbl)
        bl.add_widget(Button(text='Calculate',
                             background_color = [16/255,84/255,91/255,1],
                             background_normal='',
                             on_press = lambda x: self.update_label(text_val)))
        bl.add_widget(gl)
        self.add_widget(bl)
        
    def update_label(self,text_val):
        if text_val == 'Ksi':
            Num_formule = Val_Ksi_S.const
            Re = Calculate_Ksi.value_text
            if Re == '':
                self.text = '0'
            else:
                Re = float(Calculate_Ksi.value_text)
                if Num_formule == 0:
                    Num_formule = 64.0/Re
                    self.text = str(Num_formule)
                elif Num_formule == 1:
                    Num_formule = 0.3164/(Re)**.25
                    self.text = str(Num_formule)
                elif Num_formule == 2:
                    Num_formule = (1.82*math.log10(Re) - 1.64)**(-2)
                    self.text = str(Num_formule)
                else:
                    self.text = 'Error , please check your code!'
            self.lbl.text = self.text
            self.text = '0'
            Calculate_Ksi.value_text = ''
            Calculate_Ksi.text = 'Введите Re:'

        elif text_val == 'Nu':
            Num_formule = Val_Nu_S.const
            RePrKsi = Calculate_Nu.value_text
            if RePrKsi == '':
                self.text = '0'
            else:
                RePrKsi = RePrKsi.split(",")
                Re = float(RePrKsi[0])
                Pr = float(RePrKsi[1])
                Ksi = float(RePrKsi[2])
                if Num_formule == 0:
                    Num_formule = (Re*Pr*Ksi/8)/(1 + 900/Re + 12.7*(Pr**(2/3) - 1)*(Ksi/8)**.5)
                    self.text = str(Num_formule)
                elif Num_formule == 1:
                    Num_formule = 0.3164/(Re)**.25
                    self.text = str(Num_formule)
                elif Num_formule == 2:
                    Num_formule = (1.82*math.log10(Re) - 1.64)**(-2)
                    self.text = str(Num_formule)
                else:
                    self.text = 'Error , please check your code!'
            self.lbl.text = self.text
            self.text = '0'
            Calculate_Nu.value_text = ''
            Calculate_Nu.text = 'Введите Re,Pr,Ksi:'

class CalculateScreen(Screen):
    text = ''
    value_text = '0'
    def __init__(self,text_val, **kw):
        super(CalculateScreen, self).__init__(**kw)
        with self.canvas:
            Color(35/255,174/255,190/255,1)
            Rectangle(size=(Window.width, Window.height), pos=(0, 0))    

        if text_val == 'Ksi':
            self.text = 'Введите Re:'
            self.value_text = ''
        elif text_val == 'Nu':
            self.text = 'Введите Re,Pr,Ksi:'
            self.value_text = ''
            
        self.lbl = Label(text = self.text)
        #self.lbl = Label(text = self.text + self.value_text)
        
        bl = BoxLayout(orientation = 'vertical')
        
        gl_keyboard = GridLayout(cols = 3, rows = 5 ,spacing = 3,padding = 3)


        gl_keyboard.add_widget(Button(text='1',
                               background_color = [16/255,84/255,91/255,1],
                               background_normal='',
                               on_press = self.add_number))
        gl_keyboard.add_widget(Button(text='2',
                               background_color = [16/255,84/255,91/255,1],
                               background_normal='',
                               on_press =  self.add_number))
        gl_keyboard.add_widget(Button(text='3',
                               background_color = [16/255,84/255,91/255,1],
                               background_normal='',
                               on_press =  self.add_number))
        gl_keyboard.add_widget(Button(text='4',
                               background_color = [16/255,84/255,91/255,1],
                               background_normal='',
                               on_press =  self.add_number))
        gl_keyboard.add_widget(Button(text='5',
                               background_color = [16/255,84/255,91/255,1],
                               background_normal='',
                               on_press =  self.add_number))
        gl_keyboard.add_widget(Button(text='6',
                               background_color = [16/255,84/255,91/255,1],
                               background_normal='',
                               on_press =  self.add_number))
        gl_keyboard.add_widget(Button(text='7',
                               background_color = [16/255,84/255,91/255,1],
                               background_normal='',
                               on_press =  self.add_number))
        gl_keyboard.add_widget(Button(text='8',
                               background_color = [16/255,84/255,91/255,1],
                               background_normal='',
                               on_press =  self.add_number))
        gl_keyboard.add_widget(Button(text='9',
                               background_color = [16/255,84/255,91/255,1],
                               background_normal='',
                               on_press =  self.add_number))
        gl_keyboard.add_widget(Button(text='0',
                               background_color = [16/255,84/255,91/255,1],
                               background_normal='',
                               on_press =  self.add_number))
        gl_keyboard.add_widget(Button(text='.',
                               background_color = [16/255,84/255,91/255,1],
                               background_normal='',
                               on_press =  self.add_number))
        gl_keyboard.add_widget(Button(text=',',
                               background_color = [16/255,84/255,91/255,1],
                               background_normal='',
                               on_press =  self.add_number))
        gl_keyboard.add_widget(Button(text='delete',
                               background_color = [16/255,84/255,91/255,1],
                               background_normal='',
                               on_press = self.add_number))
        
        gl_keyboard.add_widget(Button(text=' Next >',
                                      background_color = [16/255,84/255,91/255,1],
                                      background_normal='',
                                      on_press = lambda x: set_screen(text_val.lower()+'_result')))
        gl_keyboard.add_widget(Button(text='Return to\nmain page',
                                      background_color = [16/255,84/255,91/255,1],
                                      background_normal='',
                                      on_press = lambda x: set_screen('main')))

        
        bl.add_widget(self.lbl)
        bl.add_widget(gl_keyboard)
        self.add_widget(bl)
        

    def add_number(self,instance):
        if instance.text == 'delete':
            if self.text != 'Введите Re:' and self.text != 'Введите Re,Pr,Ksi:':
                self.value_text = self.value_text[0:-1]
                self.text = self.text[0:-1]
        else:
            self.value_text += instance.text
            self.text += instance.text
        self.lbl.text = self.text
    
    #def delete_number(self):
    #    self.value_text = self.value_text[0:-1]
    #    self.text = self.text[0:-1]
    #    self.lbl.text = self.text

#Настройка экранов##################################################
sm = ScreenManager()
Main_S = MainScreen(name='main')

Val_Ksi_S = Val_Screen('Ksi',name='ksi')
Val_Nu_S = Val_Screen('Nu',name='nu')

Calculate_Ksi = CalculateScreen('Ksi',name='ksi_calculate')
Calculate_Nu = CalculateScreen('Nu',name='nu_calculate')

Result_Ksi = ResultScreen('Ksi',name='ksi_result')
Result_Nu = ResultScreen('Nu',name='nu_result')
        
sm.add_widget(Main_S)

sm.add_widget(Val_Ksi_S)
sm.add_widget(Val_Nu_S)

sm.add_widget(Calculate_Ksi)
sm.add_widget(Calculate_Nu)

sm.add_widget(Result_Ksi)
sm.add_widget(Result_Nu)
######################################################################
    
class NusseltApp(App):
    def build(self):
        Num_formule_ksi = Val_Ksi_S.const
        
        Result_Ksi.text = str(Num_formule_ksi)
        return sm

if __name__ == '__main__':
    NusseltApp().run()
